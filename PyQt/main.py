import sys
import os
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QTableWidgetItem, QTableWidget, QWidget, QTabWidget, QVBoxLayout, QMessageBox
from PyQt5 import QtCore

import sqlite3

script_path = os.path.abspath(__file__)
script_directory = os.path.dirname(script_path)

# Définissez le répertoire de travail sur le répertoire du script
os.chdir(script_directory)
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
        
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 150)
        self.tableWidget.setColumnWidth(2, 150)
        self.tableWidget.setColumnWidth(3, 150)
        self.tableWidget.setColumnWidth(4, 150)
        self.tableWidget.setColumnWidth(5, 150)

        # Les colonnes que vous voulez afficher dans la combobox
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

        # Remplir la QComboBox avec les noms des colonnes
        self.fill_combobox()

        # Initialiser l'onglet Modifier
        self.setup_modifier_tab()

        # Connecter le bouton "Rechercher" à la méthode loaddata
        self.pushButton_Recherche.clicked.connect(self.loaddata)

         # Ajoutez un bouton "Modifier"
        self.pushButton_Modifier.clicked.connect(self.modifier_article)

        # Ajoutez un bouton "Supprimer"
        self.pushButton_Supprimer.clicked.connect(self.supprimer_article)

        # Connecter le double-clic dans le tableau de l'onglet Rechercher à la fonction handle_double_click
        self.tableWidget.itemDoubleClicked.connect(self.handle_double_click)

        # Appeler loaddata pour effectuer une recherche au lancement
        self.loaddata()

        # Définir l'onglet de recherche comme l'onglet actif au lancement
        self.TabPrincipale.setCurrentIndex(0)

    def setup_modifier_tab(self):
        self.tableWidget_3.setColumnWidth(0, 100)
        self.tableWidget_3.setColumnWidth(1, 150)
        self.tableWidget_3.setColumnWidth(2, 150)
        self.tableWidget_3.setColumnWidth(3, 150)
        self.tableWidget_3.setColumnWidth(4, 150)
        self.tableWidget_3.setColumnWidth(5, 150)

    def setup_connections(self):
        # Connectez le double-clic dans le tableau de l'onglet Rechercher à la fonction handle_double_click
        self.tableWidget.itemDoubleClicked.connect(self.handle_double_click)

    def setup_ui(self):
        # ... (autres initialisations)
        # Connectez le bouton "Rechercher" à la méthode loaddata
        self.pushButton_Recherche.clicked.connect(self.loaddata)

        # Connectez le double-clic à la fonction handle_double_click
        self.tableWidget.itemDoubleClicked.connect(self.handle_double_click)

    def handle_double_click(self, item):
        # Vérifiez si l'onglet actif est l'onglet Rechercher
        if self.TabPrincipale.currentIndex() == 0:
            # Obtenez la ligne sélectionnée
            row = item.row()
            data = []
            for col in range(self.tableWidget.columnCount()):
                data.append(self.tableWidget.item(row, col).text())

            # Effacez le contenu actuel de l'onglet Modifier
            self.tableWidget_3.clearContents()
            self.tableWidget_3.setRowCount(0)

            # Ajoutez les données au tableau de l'onglet Modifier
            self.add_data_to_modifier_table(data)
            print("Double-clicked! Data added to Modifier table.")

    def add_data_to_modifier_table(self, data):
        # Effacez le contenu actuel de l'onglet Modifier
        self.tableWidget_3.clearContents()
        self.tableWidget_3.setRowCount(0)

        # Ajoutez une nouvelle ligne au tableau de l'onglet Modifier
        row_position = self.tableWidget_3.rowCount()
        self.tableWidget_3.insertRow(row_position)

        # Remplissez les cellules de la nouvelle ligne avec les données
        for col, value in enumerate(data):
            item = QTableWidgetItem(value)
            self.tableWidget_3.setItem(row_position, col, item)

    def fill_combobox(self):
        # Remplir la QComboBox avec les noms des colonnes
        self.comboBox_Recherche.addItems(self.columnNames)

    def modifier_article(self):
        # Vérifiez si une ligne est sélectionnée dans le tableau Modifier
        selected_row = self.tableWidget_3.currentRow()
        if selected_row == -1:
            self.show_message_box("Aucune ligne sélectionnée", "Veuillez sélectionner une ligne à modifier.")
            return

        # Récupérez les nouvelles valeurs depuis les cellules du tableau
        new_values = []
        for col in range(self.tableWidget_3.columnCount()):
            item = self.tableWidget_3.item(selected_row, col)
            new_values.append(item.text() if item else "")

        # Appelez votre méthode modifier_enregistrement pour effectuer la mise à jour
        self.modifier_enregistrement(*new_values)

    def supprimer_article(self):
        # Vérifiez si une ligne est sélectionnée dans le tableau Modifier
        selected_row = self.tableWidget_3.currentRow()
        if selected_row == -1:
            self.show_message_box("Aucune ligne sélectionnée", "Veuillez sélectionner une ligne à supprimer.")
            return

        # Récupérez l'ID de l'article à partir de la cellule de la première colonne
        id_item = self.tableWidget_3.item(selected_row, 0)
        if id_item is None:
            self.show_message_box("ID manquant", "Impossible de supprimer sans ID.")
            return

        id_article = id_item.text()

        # Appelez votre méthode supprimer_enregistrement pour effectuer la suppression
        self.supprimer_enregistrement(id_article)

    def modifier_enregistrement(self, *args):
        # Ajoutez le code nécessaire pour mettre à jour l'enregistrement dans la base de données
        # Utilisez les nouvelles valeurs passées en tant qu'arguments

        # Exemple de code (à adapter à votre structure de base de données)
        database_path = 'ma_base_de_donnees.db'
        connection = sqlite3.connect(database_path)
        cur = connection.cursor()

        # Assuming the SQL query returns the same columns as SELECT statement in loaddata
        id_article, piece_name, supplier_name, quantity_stock, last_purchase_date, last_sale_date, selling_price, location, picture_path = args

        sqlstr = '''
            UPDATE article
            SET piece_id=?, supplier_id=?, quantity_stock=?, last_purchase_date=?, last_sale_date=?, selling_price=?, picture_path=?
            WHERE id_article=?
        '''
        cur.execute(sqlstr, (piece_name, supplier_name, quantity_stock, last_purchase_date, last_sale_date, selling_price, picture_path, id_article))

        connection.commit()
        connection.close()

        # Rafraîchissez le tableau après la modification
        self.loaddata()
        self.show_message_box("Modification réussie", "L'article a été modifié avec succès.")

    def supprimer_enregistrement(self, id_article):
        # Ajoutez le code nécessaire pour supprimer l'enregistrement de la base de données
        # Utilisez l'ID de l'article pour identifier l'enregistrement à supprimer

        # Exemple de code (à adapter à votre structure de base de données)
        database_path = 'ma_base_de_donnees.db'
        connection = sqlite3.connect(database_path)
        cur = connection.cursor()

        sqlstr = "DELETE FROM article WHERE id_article = ?"
        cur.execute(sqlstr, (id_article,))

        connection.commit()
        connection.close()

        # Rafraîchissez le tableau après la suppression
        self.loaddata()
        self.show_message_box("Suppression réussie", "L'article a été supprimé avec succès.")

    def show_message_box(self, title, message):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec_()

    def loaddata(self):
        # Effacer le contenu actuel de la table
        self.tableWidget.clearContents()

        # Initialiser la variable tablerow
        tablerow = 0

        # Chemin relatif de la base de données
        database_path = 'ma_base_de_donnees.db'
        # Connectez-vous à la base de données
        connection = sqlite3.connect(database_path)
        cur = connection.cursor()

        # Obtenir la colonne sélectionnée dans la combobox
        selected_column = self.comboBox_Recherche.currentText()

        # Requête SQL dynamique en fonction de la colonne sélectionnée
        if not self.lineEdit.text():
            # Si le champ de recherche est vide, récupérer tous les enregistrements
            sqlstr = f'''
                SELECT 
                    article.id_article, 
                    piece.name AS piece_name, 
                    supplier.name AS supplier_name,
                    article.quantity_stock, 
                    article.last_purchase_date, 
                    article.last_sale_date,
                    article.selling_price, 
                    area.name AS location,  -- Nouvelle colonne pour l'emplacement
                    article.picture_path
                FROM article
                INNER JOIN piece ON article.piece_id = piece.id_piece
                INNER JOIN supplier ON article.supplier_id = supplier.id_supplier
                INNER JOIN article_area ON article.id_article = article_area.article_id
                INNER JOIN area ON article_area.area_id = area.id_area
                LIMIT 40
            '''
            results = cur.execute(sqlstr)
        else:
            # Sinon, effectuer une recherche basée sur le champ de recherche
            sqlstr = f'''
                SELECT 
                    article.id_article, 
                    piece.name AS piece_name, 
                    supplier.name AS supplier_name,
                    article.quantity_stock, 
                    article.last_purchase_date, 
                    article.last_sale_date,
                    article.selling_price, 
                    area.name AS location,  -- Nouvelle colonne pour l'emplacement
                    article.picture_path
                FROM article
                INNER JOIN piece ON article.piece_id = piece.id_piece
                INNER JOIN supplier ON article.supplier_id = supplier.id_supplier
                INNER JOIN article_area ON article.id_article = article_area.article_id
                INNER JOIN area ON article_area.area_id = area.id_area
                WHERE {selected_column} LIKE ?
                LIMIT 40
            '''
            search_text = self.lineEdit.text()
            # Modifiez ici pour inclure le pourcentage avant et après le texte de recherche
            results = cur.execute(sqlstr, ('%' + search_text + '%',))

        tablerow = 0
        self.tableWidget.setRowCount(40)
        
        for row in results:
            for col, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                self.tableWidget.setItem(tablerow, col, item)
            tablerow += 1

        # Fermez la connexion à la base de données après avoir terminé
        connection.close()



# main
app = QtWidgets.QApplication(sys.argv)
mainwindow = MainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.show()
sys.exit(app.exec_())