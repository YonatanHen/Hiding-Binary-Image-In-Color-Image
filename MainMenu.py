from tkinter import Image

from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtCore import QDir, QFile, QFileInfo, QIODevice
from PyQt5.QtWidgets import QVBoxLayout, QFileDialog


class MainMenu(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainMenu, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('dataSecurity.ui', self)  # Load the .ui file

        #Organize the title alignment
        self.Title.setAlignment(QtCore.Qt.AlignCenter)

        #upload an image
        vbox = QVBoxLayout(self)
        vbox.addWidget(self.ColorImageBtn)
        self.ColorImageBtn.clicked.connect(self.load_image)
        self.show()  # Show the GUI

    def load_image(self):
        name = QFileDialog.getOpenFileName(self, 'Select Color Image', QDir.currentPath(),
                                            "Image files (*.jpg, *.gif, *.png)")
        if name:
            path = name[0]
            print(path)