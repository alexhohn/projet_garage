import sys
import os
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QTableWidgetItem
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
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 150)
        self.tableWidget.setColumnWidth(2, 150)
        self.tableWidget.setColumnWidth(3, 150)
        self.tableWidget.setColumnWidth(4, 150)
        self.tableWidget.setColumnWidth(5, 150)

        # Mettez à jour cette ligne pour récupérer les noms de colonnes à partir de la base de données
        self.columnNames = self.get_column_names()

        # Remplir la QComboBox avec les noms des colonnes
        self.comboBox_Recherche.addItems(self.columnNames)

        # Connecter le bouton "Rechercher" à la méthode loaddata
        self.pushButton_Recherche.clicked.connect(self.loaddata)

    def get_column_names(self):
        # Fonction pour récupérer dynamiquement les noms de colonnes à partir de la base de données
        connection = sqlite3.connect('ma_base_de_donnees.db')
        cur = connection.cursor()
        cur.execute("PRAGMA table_info(article)")  # Remplacez 'article' par le nom de votre table
        columns = [column[1] for column in cur.fetchall()]
        connection.close()
        return columns

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


print("Répertoire de travail actuel :", os.getcwd())
# main
app = QtWidgets.QApplication(sys.argv)
mainwindow = MainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.show()
sys.exit(app.exec_())