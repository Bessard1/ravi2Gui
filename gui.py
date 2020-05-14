import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QWidget, QVBoxLayout, QTabWidget, QPushButton, QLineEdit


class QInputDIalogue(object):
    pass


class Gui(QMainWindow):

    def __init__(self, parent = None):
        super().__init__()
        self.initUI()
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

    def initUI(self):
        self.statusBar().showMessage('Ready')
        self.setWindowTitle('Test ravi')
        self.show()
        self.setMinimumSize(1280, 720)

        self.__createFileMenu()
        self.__createEditMenu()
        self.__createHelpMenu()

    def __createFileMenu(self):
        actOpen = QAction(QIcon("icons/ouvrir.png"), "&Ouvrir", self)
        actOpen.setShortcut("Ctrl+O")
        actOpen.setStatusTip("Ouvrir fichier")

        actSave = QAction(QIcon("icons/sauvegarder.png"), "&Sauvegarder", self)
        actSave.setShortcut("Ctrl+S")
        actSave.setStatusTip("Sauvegarder Fichier")

        actExit = QAction(QIcon("icons/sortir.png"), "&Sortir", self)
        actExit.setShortcut("Ctrl+Q")
        actExit.setStatusTip("Sortir application")
        actExit.triggered.connect(self.close)

        menuBar = self.menuBar()
        file = menuBar.addMenu("&Fichier")
        file.addAction(actOpen)
        file.addAction(actSave)
        file.addSeparator()
        file.addAction(actExit)

    def __createEditMenu(self):
        actCopy = QAction(QIcon("icons/copier.png"), "&Copier", self)
        actCopy.setStatusTip("Copier")

        actCut = QAction(QIcon("icons/couper.png"), "&Couper", self)
        actCut.setStatusTip("Couper")

        actPaste = QAction(QIcon("icons/coller.png"), "&Coller", self)
        actPaste.setStatusTip("Coller")

        menuBar = self.menuBar()
        edit = menuBar.addMenu("&Edit")
        edit.addAction(actCopy)
        edit.addAction(actCut)
        edit.addSeparator()
        edit.addAction(actPaste)

    def __createHelpMenu(self):
        actAbout = QAction("& A propos", self)
        actAbout.setStatusTip(" A propos...")

        menuBar = self.menuBar()
        helpMenu = menuBar.addMenu("&Aide")
        helpMenu.addAction(actAbout)

    def close(self):
        print("Exit menu item clicked")


        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tabs.resize(300, 200)

        # Add tabs
        self.tabs.addTab(self.tab1, "Onglet 1")
        self.tabs.addTab(self.tab2, "Onglet 2")

        self.tab1.layout = QVBoxLayout(self)
        openButton = QPushButton("nom")

        self.tab1.layout.addtraigger(openButton)
        self.tab1.setLayout(self.tab1)
        openButton.clicked.connect(self.tab1.layout)

        # Create first tab
        self.tab1.layout = QVBoxLayout(self)
        self.pushButton1 = QPushButton("PyQt5 button")
        self.tab1.layout.addWidget(self.pushButton1)
        self.tab1.setLayout(self.tab1.layout)

        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    def openClick(self):
        print("click")
        nom,type = QInputDIalogue.getText(self,"input dialogue", "Votre nom ?",QLineEdit.Normale,"")
        print(nom)
