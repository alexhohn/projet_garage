import sys
import os
import sqlite3
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem

# Handle high resolution displays:
if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi('Garage.ui', self)
        self.setup_ui()

    def setup_ui(self):
        self.setup_table_widget()
        self.setup_modifier_tab()
        self.setup_connections()
        self.columnNames = [
            "article.id_article", 
            "piece_name", 
            "supplier_name",
            "quantity_stock", 
            "last_purchase_date", 
            "last_sale_date",
            "selling_price", 
            "location",
            "picture_path"
        ]
        self.fill_combobox()
        self.fill_comboboxes()
        self.loaddata()
        self.TabPrincipale.setCurrentIndex(0)

    def setup_table_widget(self):
        column_widths = [100, 150, 150, 150, 150, 150]
        for i, width in enumerate(column_widths):
            self.tableWidget.setColumnWidth(i, width)

    def setup_modifier_tab(self):
        column_widths = [100, 150, 150, 150, 150, 150]
        for i, width in enumerate(column_widths):
            self.tableWidget_3.setColumnWidth(i, width)

    def setup_connections(self):
        self.pushButton_Recherche.clicked.connect(self.loaddata)
        self.tableWidget.itemDoubleClicked.connect(self.handle_double_click)
        self.pushButton_Modifier.clicked.connect(self.modifier_article)
        self.pushButton_Supprimer.clicked.connect(self.supprimer_article)
        self.pushButton_Ajouter.clicked.connect(self.ajouter_article)

    def handle_double_click(self, item):
        if self.TabPrincipale.currentIndex() == 0:
            row = item.row()
            data = [self.tableWidget.item(row, col).text() for col in range(self.tableWidget.columnCount())]
            self.add_data_to_modifier_table(data)

    def add_data_to_modifier_table(self, data):
        self.tableWidget_3.setRowCount(1)
        for col, value in enumerate(data):
            self.tableWidget_3.setItem(0, col, QTableWidgetItem(value))


    def fill_combobox(self):
        self.comboBox_Recherche.addItems(self.columnNames)

    def modifier_article(self):
        selected_row = self.tableWidget_3.currentRow()
        if selected_row == -1:
            self.show_message_box("Aucune ligne sélectionnée", "Veuillez sélectionner une ligne à modifier.")
            return
        id_article = self.tableWidget_3.item(selected_row, 0).text()
        new_quantity_stock = self.tableWidget_3.item(selected_row, 3).text()
        area_name = self.tableWidget_3.item(selected_row, 7).text()  # C'est le nom de l'emplacement, pas l'ID

        # Maintenant, récupérez l'ID correspondant à cet emplacement
        connection = self.get_db_connection()
        cur = connection.cursor()
        cur.execute("SELECT id_area FROM area WHERE name = ?", (area_name,))
        result = cur.fetchone()
        if result:
            new_area_id = result[0]
            self.modifier_enregistrement(id_article, new_quantity_stock, new_area_id)
        else:
            self.show_message_box("Erreur", "Le nom de l'emplacement est invalide ou n'existe pas.")
    def supprimer_article(self):
        selected_row = self.tableWidget_3.currentRow()
        if selected_row == -1:
            self.show_message_box("Aucune ligne sélectionnée", "Veuillez sélectionner une ligne à supprimer.")
            return
        id_article = self.tableWidget_3.item(selected_row, 0).text()
        self.supprimer_enregistrement(id_article)

    def get_db_connection(self):
        connection = sqlite3.connect('ma_base_de_donnees.db')
        connection.execute("PRAGMA foreign_keys = ON")
        return connection

    def modifier_enregistrement(self, id_article, new_quantity_stock, new_area_id):
        connection = self.get_db_connection()
        try:
            connection.execute("BEGIN")
            
            # Convertir new_quantity_stock en entier si nécessaire
            new_quantity_stock = int(new_quantity_stock)
            new_area_id = int(new_area_id)  # Assurez-vous que new_area_id est également un entier

            # Mise à jour de la quantité dans la table 'article'
            sqlstr_article = '''
                UPDATE article
                SET quantity_stock=?
                WHERE id_article=?
            '''
            connection.execute(sqlstr_article, (new_quantity_stock, id_article))

            # Mise à jour de l'emplacement dans la table 'article_area'
            sqlstr_article_area = '''
                UPDATE article_area
                SET area_id=?
                WHERE article_id=?
            '''
            connection.execute(sqlstr_article_area, (new_area_id, id_article))

            connection.commit()
            self.show_message_box("Modification réussie", "La quantité et l'emplacement de l'article ont été modifiés avec succès.")
        except Exception as e:
            connection.rollback()
            self.show_message_box("Erreur", f"Une erreur est survenue lors de la modification: {e}")
        finally:
            connection.close()
            self.loaddata()

    def supprimer_enregistrement(self, id_article):
        connection = self.get_db_connection()
        try:
            connection.execute("BEGIN")
            # Supprimer les liens dans la table article_area
            sqlstr_article_area = "DELETE FROM article_area WHERE article_id = ?"
            connection.execute(sqlstr_article_area, (id_article,))

            # Supprimer les liens dans la table piece_vehicule
            sqlstr_piece_vehicule = "DELETE FROM piece_vehicule WHERE piece_id = (SELECT piece_id FROM article WHERE id_article = ?)"
            connection.execute(sqlstr_piece_vehicule, (id_article,))

            # Enfin, supprimer l'article
            sqlstr_article = "DELETE FROM article WHERE id_article = ?"
            connection.execute(sqlstr_article, (id_article,))

            connection.commit()
            self.show_message_box("Suppression réussie", "L'article a été supprimé avec succès.")
        except Exception as e:
            connection.rollback()
            self.show_message_box("Erreur", f"Une erreur est survenue lors de la suppression: {e}")
        finally:
            connection.close()
            self.loaddata()

    def show_message_box(self, title, message):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec_()

    def ajouter_article(self):
        # Récupérer les valeurs des widgets
        piece_id = self.comboBox_Piece.currentData()  # Obtient l'ID de la pièce sélectionnée
        area_id = self.comboBox_Emplacement.currentData()  # Obtient l'ID de l'emplacement sélectionné
        quantity_stock = self.spinBox_Quantite.value()
        last_purchase_date = self.dateEdit_LastBuy.date().toString("yyyy-MM-dd")
        last_sale_date = self.dateEdit_LastSell.date().toString("yyyy-MM-dd")
        selling_price = self.doubleSpinBox_SellPrice.value()
        
        # Ici, vous pouvez ajouter un widget pour sélectionner le fournisseur ou le définir par programmation
        # Pour cet exemple, je vais utiliser une valeur statique pour 'supplier_id'
        supplier_id = 1  # Remplacez par la méthode appropriée pour obtenir l'ID du fournisseur réel
        
        # De même, pour 'picture_path', vous pouvez utiliser un QFileDialog pour obtenir un chemin de fichier
        # Pour cet exemple, je vais utiliser un chemin statique
        picture_path = "path/to/your/image.png"  # Remplacez par la méthode appropriée pour obtenir le chemin de l'image réel

        # Insertion dans la base de données
        connection = self.get_db_connection()
        try:
            cursor = connection.cursor()
            cursor.execute("BEGIN")
            cursor.execute('''
                INSERT INTO article (piece_id, supplier_id, quantity_stock, last_purchase_date, last_sale_date, selling_price, picture_path)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (piece_id, supplier_id, quantity_stock, last_purchase_date, last_sale_date, selling_price, picture_path))
            
            # Obtient l'ID du dernier article inséré pour l'utiliser dans la table article_area
            article_id = cursor.lastrowid

            cursor.execute('''
                INSERT INTO article_area (article_id, area_id)
                VALUES (?, ?)
            ''', (article_id, area_id))
            connection.commit()
            self.show_message_box("Succès", "Article ajouté avec succès.")
        except sqlite3.IntegrityError as e:
            connection.rollback()
            self.show_message_box("Erreur d'intégrité", f"Une erreur d'intégrité des données est survenue: {e}")
        except Exception as e:
            connection.rollback()
            self.show_message_box("Erreur", f"Une erreur est survenue lors de l'ajout de l'article: {e}")
        finally:
            connection.close()
        self.loaddata()


    def fill_comboboxes(self):
        connection = self.get_db_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT id_piece, name FROM piece")
        for row in cursor.fetchall():
            self.comboBox_Piece.addItem(row[1], row[0])

        cursor.execute("SELECT id_area, name FROM area")
        for row in cursor.fetchall():
            self.comboBox_Emplacement.addItem(row[1], row[0])

        connection.close()


    def loaddata(self):
        self.tableWidget.clearContents()
        connection = self.get_db_connection()
        cur = connection.cursor()
        selected_column = self.comboBox_Recherche.currentText()
        search_text = '%' + self.lineEdit.text() + '%'

        # Vérifiez et ajustez cette requête pour correspondre à la structure de votre base de données
        sqlstr = f'''
            SELECT 
                article.id_article, 
                piece.name AS piece_name, 
                supplier.name AS supplier_name,
                article.quantity_stock, 
                article.last_purchase_date, 
                article.last_sale_date,
                article.selling_price, 
                area.name AS location,
                article.picture_path
            FROM article
            INNER JOIN piece ON article.piece_id = piece.id_piece
            INNER JOIN supplier ON article.supplier_id = supplier.id_supplier
            INNER JOIN article_area ON article.id_article = article_area.article_id
            INNER JOIN area ON article_area.area_id = area.id_area
            WHERE {selected_column} LIKE ?
            LIMIT 40
        '''

        cur.execute(sqlstr, (search_text,))
        for row_idx, row_data in enumerate(cur):
            self.tableWidget.setRowCount(row_idx + 1)
            for col_idx, value in enumerate(row_data):
                self.tableWidget.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))
        connection.close()

# main
app = QtWidgets.QApplication(sys.argv)
mainwindow = MainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.show()
sys.exit(app.exec_())