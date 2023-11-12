# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GarageSndkQO.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1014, 705)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(1000, 500))
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.TabPrincipale = QTabWidget(self.centralwidget)
        self.TabPrincipale.setObjectName(u"TabPrincipale")
        self.TabPrincipale.setMouseTracking(False)
        self.TabPrincipale.setTabPosition(QTabWidget.North)
        self.TabPrincipale.setTabShape(QTabWidget.Rounded)
        self.TabPrincipale.setIconSize(QSize(16, 16))
        self.TabPrincipale.setUsesScrollButtons(False)
        self.TabPrincipale.setTabBarAutoHide(False)
        self.TabRechercher = QWidget()
        self.TabRechercher.setObjectName(u"TabRechercher")
        self.lineEdit = QLineEdit(self.TabRechercher)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(160, 30, 131, 31))
        self.pushButton_Recherche = QPushButton(self.TabRechercher)
        self.pushButton_Recherche.setObjectName(u"pushButton_Recherche")
        self.pushButton_Recherche.setGeometry(QRect(310, 30, 131, 31))
        self.tableWidget = QTableWidget(self.TabRechercher)
        if (self.tableWidget.columnCount() < 9):
            self.tableWidget.setColumnCount(9)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 80, 951, 531))
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.comboBox_Recherche = QComboBox(self.TabRechercher)
        self.comboBox_Recherche.setObjectName(u"comboBox_Recherche")
        self.comboBox_Recherche.setGeometry(QRect(19, 31, 131, 31))
        self.TabPrincipale.addTab(self.TabRechercher, "")
        self.TabModifier = QWidget()
        self.TabModifier.setObjectName(u"TabModifier")
        self.tableWidget_3 = QTableWidget(self.TabModifier)
        if (self.tableWidget_3.columnCount() < 9):
            self.tableWidget_3.setColumnCount(9)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(5, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(6, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(7, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(8, __qtablewidgetitem17)
        if (self.tableWidget_3.rowCount() < 1):
            self.tableWidget_3.setRowCount(1)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(0, __qtablewidgetitem18)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.tableWidget_3.setGeometry(QRect(20, 110, 961, 51))
        self.tableWidget_3.setEditTriggers(QAbstractItemView.DoubleClicked|QAbstractItemView.SelectedClicked)
        self.pushButton = QPushButton(self.TabModifier)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(780, 200, 111, 51))
        self.TabPrincipale.addTab(self.TabModifier, "")
        self.TabAjouter = QWidget()
        self.TabAjouter.setObjectName(u"TabAjouter")
        self.TabPrincipale.addTab(self.TabAjouter, "")

        self.horizontalLayout.addWidget(self.TabPrincipale)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.lineEdit, self.pushButton_Recherche)

        self.retranslateUi(MainWindow)

        self.TabPrincipale.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_Recherche.setText(QCoreApplication.translate("MainWindow", u"Rechercher", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"No. article", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Pi\u00e8ce", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Fournisseur", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Quantit\u00e9 en stock", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Date d'aquisition", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Date derni\u00e8re vente", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Prix de vente", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Emplacement", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Chemin image", None));
        self.TabPrincipale.setTabText(self.TabPrincipale.indexOf(self.TabRechercher), QCoreApplication.translate("MainWindow", u"Rechercher", None))
        ___qtablewidgetitem9 = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"No. article", None));
        ___qtablewidgetitem10 = self.tableWidget_3.horizontalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Pi\u00e8ce", None));
        ___qtablewidgetitem11 = self.tableWidget_3.horizontalHeaderItem(2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Fournisseur", None));
        ___qtablewidgetitem12 = self.tableWidget_3.horizontalHeaderItem(3)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Quantit\u00e9 en stock", None));
        ___qtablewidgetitem13 = self.tableWidget_3.horizontalHeaderItem(4)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Date d'aquisition", None));
        ___qtablewidgetitem14 = self.tableWidget_3.horizontalHeaderItem(5)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Date derni\u00e8re vente", None));
        ___qtablewidgetitem15 = self.tableWidget_3.horizontalHeaderItem(6)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Prix de vente", None));
        ___qtablewidgetitem16 = self.tableWidget_3.horizontalHeaderItem(7)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Emplacement", None));
        ___qtablewidgetitem17 = self.tableWidget_3.horizontalHeaderItem(8)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Chemin image", None));
        ___qtablewidgetitem18 = self.tableWidget_3.verticalHeaderItem(0)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Modifier", None));
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Modifier", None))
        self.TabPrincipale.setTabText(self.TabPrincipale.indexOf(self.TabModifier), QCoreApplication.translate("MainWindow", u"Modifier", None))
        self.TabPrincipale.setTabText(self.TabPrincipale.indexOf(self.TabAjouter), QCoreApplication.translate("MainWindow", u"Ajouter", None))
    # retranslateUi

