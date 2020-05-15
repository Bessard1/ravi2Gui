import sys

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon, QImage, QPalette, QBrush
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QWidget, QVBoxLayout, QTabWidget, QPushButton, \
    QLineEdit, QLabel


class QInputDIalogue(object):
    pass


class Gui(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

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

        class MyTableWidget(QWidget):

            def __init__(self, parent):
                super(QWidget, self).__init__(parent)
                self.layout = QVBoxLayout(self)

        self.myWidget = MyTableWidget(self)

        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()

        # Add tabs
        self.tabs.addTab(self.tab1, "Onglet 1")
        self.tabs.addTab(self.tab2, "Onglet 2")

        self.tab1.layout = QVBoxLayout(self)
        openButton = QPushButton("Nom ?")
        openButton.clicked.connect(self.openClick)

        self.tab1.layout.addWidget(openButton)
        self.tab1.setLayout(self.tab1.layout)

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

"nom etiquette"
class Fenetre(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        # création du champ de texte
        self.champ = QLineEdit()

        # création du bouton
        self.bouton = QPushButton("COPIE")
        # on connecte le signal "clicked" à la méthode "appui_bouton_copie"
        self.bouton.clicked.connect(self.appui_bouton_copie)

        # création de l'étiquette
        self.label = QLabel()

        # mise en place du gestionnaire de mise en forme
        layout = QVBoxLayout()
        layout.addWidget(self.champ)
        layout.addWidget(self.bouton)
        layout.addWidget(self.label)
        self.setLayout(layout)

        self.setWindowTitle("Ma fenetre")

    # on définit une méthode à connecter au signal envoyé
    def appui_bouton_copie(self):
        # la méthode "text" de QLineEdit permet d'obtenir le texte à copier
        texte_a_copier = self.champ.text()
        # la méthode "setText" de QLabel permet de changer
        # le texte de l'étiquette
        self.label.setText(texte_a_copier)


app = QApplication.instance()
if not app:
    app = QApplication(sys.argv)

fen = Fenetre()
fen.show()

app.exec_()

"Couleur"
class MainWindow(QWidget):
    def __init__(self):
       QWidget.__init__(self)
       self.setGeometry(100,100,300,200)

       oImage = QImage("test.png")
       sImage = oImage.scaled(QSize(300,200))                   # resize Image to widgets size
       palette = QPalette()
       palette.setBrush(QPalette.Window, QBrush(sImage))
       self.setPalette(palette)

       self.label = QLabel('Test', self)                        # test, if it's really backgroundimage
       self.label.setGeometry(50,50,200,50)

       self.show()

if __name__ == "__main__":

    app = QApplication(sys.argv)
    oMainwindow = MainWindow()
    sys.exit(app.exec_())