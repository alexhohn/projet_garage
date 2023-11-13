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

class NewManufacturerDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Assurez-vous que le chemin vers le fichier UI est correct
        loadUi('Form_NewManufacturer.ui', self)  

        self.pushButton_AjouterManufacturer.clicked.connect(self.accept)


    def accept(self):
        # Récupérez les informations de la nouvelle pièce des widgets
        manufacturer_name = self.lineEdit_NomManufacturer.text()
        manufacturer_adress = self.lineEdit_Adresse.text()
        manufacturer_ZIP = self.lineEdit_ZIP.text()
        manufacturer_Country = self.lineEdit_Country.text()

        # Insérez la nouvelle pièce dans la base de données
        connection = self.get_db_connection()
        try:
            cursor = connection.cursor()
            cursor.execute("BEGIN")
            cursor.execute('''
                INSERT INTO manufacturer (name, adress, zip, country)
                VALUES (?, ?, ?, ?)
            ''', (manufacturer_name, manufacturer_adress, manufacturer_ZIP, manufacturer_Country))
            connection.commit()
            # Affichez un message de succès et fermez le dialogue
            self.show_message_box("Succès", "Nouveau fabricant ajouté avec succès.")
            super().accept()
        except sqlite3.IntegrityError as e:
            connection.rollback()
            self.show_message_box("Erreur d'intégrité", f"Une erreur d'intégrité des données est survenue: {e}")
        except Exception as e:
            connection.rollback()
            self.show_message_box("Erreur", f"Une erreur est survenue lors de l'ajout: {e}")
        finally:
            connection.close()

    def get_db_connection(self):
        # Retournez une nouvelle connexion à votre base de données
        return sqlite3.connect('ma_base_de_donnees.db')

    def show_message_box(self, title, message):
        # Utilisez cette méthode pour afficher des messages à l'utilisateur
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec_()


class NewMVehiculeDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Assurez-vous que le chemin vers le fichier UI est correct
        loadUi('Form_NewVehicule.ui', self)  
        self.populate_manufacturers()
        self.pushButton_AjouterVehicule.clicked.connect(self.accept)

    def populate_manufacturers(self):
        # Récupérez la liste des fabricants de votre base de données et ajoutez-les au comboBox
        connection = self.get_db_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT id_manufacturer, name FROM manufacturer")
        manufacturers = cursor.fetchall()
        self.comboBox_Manufacturer.clear()
        for id_manufacturer, name in manufacturers:
            self.comboBox_Manufacturer.addItem(name, id_manufacturer)
        connection.close()

    def accept(self):
        # Récupérez les informations de la nouvelle pièce des widgets
        manufacturer_id = self.comboBox_Manufacturer.currentData()
        vehicule_model = self.lineEdit_ModelName.text()
        vehicule_year = self.lineEdit_Annee.text()
        vehicule_enginetype = self.lineEdit_EngineType.text()

        # Insérez la nouvelle pièce dans la base de données
        connection = self.get_db_connection()
        try:
            cursor = connection.cursor()
            cursor.execute("BEGIN")
            cursor.execute('''
                INSERT INTO vehicule (manufacturer_id, model, year, engine_type)
                VALUES (?, ?, ?, ?)
            ''', (manufacturer_id, vehicule_model, vehicule_year, vehicule_enginetype))
            connection.commit()
            # Affichez un message de succès et fermez le dialogue
            self.show_message_box("Succès", "Nouveau fabricant ajouté avec succès.")
            super().accept()
        except sqlite3.IntegrityError as e:
            connection.rollback()
            self.show_message_box("Erreur d'intégrité", f"Une erreur d'intégrité des données est survenue: {e}")
        except Exception as e:
            connection.rollback()
            self.show_message_box("Erreur", f"Une erreur est survenue lors de l'ajout: {e}")
        finally:
            connection.close()

    def get_db_connection(self):
        # Retournez une nouvelle connexion à votre base de données
        return sqlite3.connect('ma_base_de_donnees.db')

    def show_message_box(self, title, message):
        # Utilisez cette méthode pour afficher des messages à l'utilisateur
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec_()


class NewPieceDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Assurez-vous que le chemin vers le fichier UI est correct
        loadUi('Form_NewPiece.ui', self)  
        self.populate_manufacturers()
        self.populate_vehicules()
        # Connectez le bouton pour ajouter un nouveau fabricant si nécessaire
        # Si la fonctionnalité n'est pas encore implémentée, vous pouvez commenter la ligne suivante
        self.pushButton_NewManufacturer.clicked.connect(self.open_new_manufacturer_dialog)
        self.pushButton_NewVehicule.clicked.connect(self.open_new_vehicule_dialog)
        self.pushButton_AjouterPiece.clicked.connect(self.accept)

    def populate_manufacturers(self):
        # Récupérez la liste des fabricants de votre base de données et ajoutez-les au comboBox
        connection = self.get_db_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT id_manufacturer, name FROM manufacturer")
        manufacturers = cursor.fetchall()
        self.comboBox_Manufacturer.clear()
        for id_manufacturer, name in manufacturers:
            self.comboBox_Manufacturer.addItem(name, id_manufacturer)
        connection.close()

    def populate_vehicules(self):
        # Récupérez la liste des fabricants de votre base de données et ajoutez-les au comboBox
        connection = self.get_db_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT id_vehicule, model FROM vehicule")
        vehicule = cursor.fetchall()
        self.comboBox_Vehicule.clear()
        for id_vehicule, model in vehicule:
            self.comboBox_Vehicule.addItem(model, id_vehicule)
        connection.close()

    def accept(self):
        # Récupérez les informations de la nouvelle pièce des widgets
        manufacturer_id = self.comboBox_Manufacturer.currentData()
        piece_name = self.lineEdit_PieceName.text()
        ean_number = self.lineEdit_EANPiece.text()
        description = self.plainTextEdit_DescriptionPiece.toPlainText()
        unit_price = self.doubleSpinBox_PrixPiece.value()
        
        # Insérez la nouvelle pièce dans la base de données
        connection = self.get_db_connection()
        try:
            cursor = connection.cursor()
            cursor.execute("BEGIN")
            cursor.execute('''
                INSERT INTO piece (manufacturer_id, name, ean_number, description, unit_price)
                VALUES (?, ?, ?, ?, ?)
            ''', (manufacturer_id, piece_name, ean_number, description, unit_price))
            connection.commit()
            # Affichez un message de succès et fermez le dialogue
            self.show_message_box("Succès", "Nouvelle pièce ajoutée avec succès.")
            super().accept()
        except sqlite3.IntegrityError as e:
            connection.rollback()
            self.show_message_box("Erreur d'intégrité", f"Une erreur d'intégrité des données est survenue: {e}")
        except Exception as e:
            connection.rollback()
            self.show_message_box("Erreur", f"Une erreur est survenue lors de l'ajout de la pièce: {e}")
        finally:
            connection.close()

    def get_db_connection(self):
        # Retournez une nouvelle connexion à votre base de données
        return sqlite3.connect('ma_base_de_donnees.db')

    def show_message_box(self, title, message):
        # Utilisez cette méthode pour afficher des messages à l'utilisateur
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec_()
    
    def open_new_manufacturer_dialog(self):
        # Créez et affichez le dialogue pour une nouvelle pièce
        dialog = NewManufacturerDialog(self)
        dialog.exec_()  # Utilisez exec_() pour rendre le dialogue modal
        self.populate_manufacturers()
        self.populate_vehicules()

    def open_new_vehicule_dialog(self):
        # Créez et affichez le dialogue pour une nouvelle pièce
        dialog = NewMVehiculeDialog(self)
        dialog.exec_()  # Utilisez exec_() pour rendre le dialogue modal
        self.populate_manufacturers()
        self.populate_vehicules() 

class NewSupplierDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Assurez-vous que le chemin vers le fichier UI est correct
        loadUi('Form_NewSupplier.ui', self)  
        self.pushButton_AjouterFournisseur.clicked.connect(self.accept)


    def accept(self):
        # Récupérez les informations du nouveau fournisseur
        supplier_name = self.lineEdit_Nom.text()
        supplier_adress = self.lineEdit_Adresse.text()
        supplier_zip = self.lineEdit_ZIP.text()
        supplier_country = self.lineEdit_Country.text()
        supplier_nameResp =self.lineEdit_RespName.text()
        supplier_telephone = self.lineEdit_telephone.text()
        supplier_email = self.lineEdit_email.text()

        # Insérez la nouvelle pièce dans la base de données
        connection = self.get_db_connection()
        try:
            cursor = connection.cursor()
            cursor.execute("BEGIN")
            cursor.execute('''
                INSERT INTO supplier (name, adress, zip, country, name_resp, telephone, email)
                VALUES (?, ?, ?, ?, ?, ? ,?)
            ''', (supplier_name, supplier_adress, supplier_zip, supplier_country, supplier_nameResp, supplier_telephone, supplier_email))
            connection.commit()
            # Affichez un message de succès et fermez le dialogue
            self.show_message_box("Succès", "Nouveau fournisseur ajouté avec succès.")
            super().accept()
        except sqlite3.IntegrityError as e:
            connection.rollback()
            self.show_message_box("Erreur d'intégrité", f"Une erreur d'intégrité des données est survenue: {e}")
        except Exception as e:
            connection.rollback()
            self.show_message_box("Erreur", f"Une erreur est survenue lors de l'ajout: {e}")
        finally:
            connection.close()

    def get_db_connection(self):
        # Retournez une nouvelle connexion à votre base de données
        return sqlite3.connect('ma_base_de_donnees.db')

    def show_message_box(self, title, message):
        # Utilisez cette méthode pour afficher des messages à l'utilisateur
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec_()

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
        self.pushButton_AjouterArticle.clicked.connect(self.ajouter_article)
        self.pushButton_newPiece.clicked.connect(self.open_new_piece_dialog)
        self.pushButton_NewEmplacement.clicked.connect(self.open_new_location_dialog)
        self.pushButton_NewSupplier.clicked.connect(self.open_new_supplier_dialog)

    def handle_double_click(self, item):
        if self.TabPrincipale.currentIndex() == 0:
            row = item.row()
            data = [self.tableWidget.item(row, col).text() for col in range(self.tableWidget.columnCount())]
            self.add_data_to_modifier_table(data)
        self.TabPrincipale.setCurrentIndex(1)

    def add_data_to_modifier_table(self, data):
        self.tableWidget_3.setRowCount(1)
        for col, value in enumerate(data):
            self.tableWidget_3.setItem(0, col, QTableWidgetItem(value))

    def open_new_piece_dialog(self):
        # Créez et affichez le dialogue pour une nouvelle pièce
        dialog = NewPieceDialog(self)
        dialog.exec_()  # Utilisez exec_() pour rendre le dialogue modal

        # Après la fermeture du dialogue, vous pouvez rafraîchir les combobox ou la table si nécessaire
        self.fill_comboboxes()
        self.loaddata()

    def open_new_location_dialog(self):
        dialog = NewLocationDialog(self)
        if dialog.exec_():
            self.fill_comboboxes()

    def open_new_manufacturer_dialog(self):
        dialog = NewManufacturerDialog(self)
        if dialog.exec_():
            self.fill_comboboxes()

    def open_new_supplier_dialog(self):
        dialog = NewSupplierDialog(self)
        if dialog.exec_():
            self.fill_comboboxes()
            self.loaddata()

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
            self.TabPrincipale.setCurrentIndex(0)

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
        
        # Récupérer l'ID du fournisseur associé à la pièce sélectionnée
        connection = self.get_db_connection()
        try:
            cursor = connection.cursor()
            cursor.execute('SELECT supplier_id FROM piece WHERE id_piece = ?', (piece_id,))
            supplier_row = cursor.fetchone()
            if supplier_row:
                supplier_id = supplier_row[0]
            else:
                self.show_message_box("Erreur", "Aucun fournisseur associé à cette pièce.")
                return
            
            # Insérer l'article dans la base de données
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

        # Vider les combobox existants pour éviter les doublons
        self.comboBox_Piece.clear()
        self.comboBox_Emplacement.clear()
        self.comboBox_Recherche.clear()
        self.comboBox_Supplier.clear()

        cursor.execute("SELECT id_piece, name FROM piece")
        for row in cursor.fetchall():
            self.comboBox_Piece.addItem(row[1], row[0])

        cursor.execute("SELECT id_area, name FROM area")
        for row in cursor.fetchall():
            self.comboBox_Emplacement.addItem(row[1], row[0])
        
        cursor.execute("SELECT id_supplier, name FROM supplier")
        for row in cursor.fetchall():
            self.comboBox_Supplier.addItem(row[1], row[0])

        connection.close()
        self.comboBox_Recherche.addItems(self.columnNames)

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