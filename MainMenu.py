from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtCore import QDir, QFile, QFileInfo, QIODevice
from PyQt5.QtWidgets import QVBoxLayout, QFileDialog
from functions.ColorImageToRGBArray import *


class MainMenu(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainMenu, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('dataSecurity.ui', self)  # Load the .ui file

        # define class variables

        # Organize the title alignment
        self.Title.setAlignment(QtCore.Qt.AlignCenter)

        vbox = QVBoxLayout(self)
        # upload color image
        vbox.addWidget(self.ColorImageBtn)
        self.ColorImageBtn.clicked.connect(lambda:self.load_image('c'))

        # upload color image
        vbox.addWidget(self.BinaryImageBtn)
        self.BinaryImageBtn.clicked.connect(lambda:self.load_image('b'))

        self.show()  # Show the GUI


    def load_image(self, t):
        name = QFileDialog.getOpenFileName(self, 'Select Color Image', QDir.currentPath(),
                                           "Image files (*.jpg, *.gif, *.png)")
        if name:
            path = name[0]
            print(path)
            if t == 'b':
                self.binaryImg = binaryConvert(path)
                print(self.binaryImg)
            else:
                self.colorImg = RGBConvert(path)
                print(self.colorImg)
            return path


