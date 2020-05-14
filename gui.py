import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction


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
        actOpen = QAction(QIcon("icons/ovrir.png"), "&Ovrir", self)
        actOpen.setStatusTip("Ouvrir fichier")

        actSave = QAction(QIcon("icons/sauvegarder.png"), "&Sauvegarder", self)
        actSave.setStatusTip("Save Fichier")

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


if __name__ == "__main__":
    app = QApplication(sys.argv)

    myWindow = MyWindow()
    myWindow.show()

    sys.exit(app.exec_())
