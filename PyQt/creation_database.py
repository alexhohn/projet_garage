import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)

        layout = QVBoxLayout()

        self.executeButton = QPushButton('Exécuter les requêtes SQL')
        self.executeButton.clicked.connect(self.executeSQLFromFile)
        layout.addWidget(self.executeButton)

        self.centralWidget.setLayout(layout)

    def executeSQLFromFile(self):
        file_path = """C:\\Users\\alexa\\Documents\\DocumentsAHN\\02_Etudes\\01_HEIG-VD\\03_2324\\Branches 2324\\ProjDec1\\projet_garage\\database\\creation_garage.sql"""

        if file_path:
            conn = sqlite3.connect('PyQt\\ma_base_de_donnees.db')
            cur = conn.cursor()

            with open(file_path, 'r') as file:
                requetes = file.read()

            requetes_liste = requetes.split(';')

            i = 0
            for requete in requetes_liste:
                i = i + 1
                try:
                    cur.execute(requete)
                except sqlite3.Error as e:
                    print("Erreur lors de l'exécution de la requête :", e,"Requête numro :", i, "Requête :",requete )
                else:
                    print("Requête exécutée avec succès. Requête numéro :", i, "Requête :",requete )

            conn.commit()
            conn.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())