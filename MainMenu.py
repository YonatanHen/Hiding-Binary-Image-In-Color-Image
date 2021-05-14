from PyQt5 import QtWidgets, uic, QtCore


class MainMenu(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainMenu, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('dataSecurity.ui', self)  # Load the .ui file
        self.Title.setAlignment(QtCore.Qt.AlignCenter)
        self.show()  # Show the GUI
