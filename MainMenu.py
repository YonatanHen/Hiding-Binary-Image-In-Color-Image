from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtCore import QDir, QFile, QFileInfo, QIODevice
from PyQt5.QtWidgets import QVBoxLayout, QFileDialog
from functions.imageConvertionFuncs import *
from functions.errorMessages import *


class MainMenu(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainMenu, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('dataSecurity.ui', self)  # Load the .ui file

        # Class variables definition (Optional but the vars definitions below necessary)
        self.colorImg = self.binaryImg = None

        # Widgets definitions
        vbox = QVBoxLayout(self)
        self.errDialog = QtWidgets.QErrorMessage()  # self because it called in another function

        # Organize the title alignment
        self.Title.setAlignment(QtCore.Qt.AlignCenter)

        # upload color image
        vbox.addWidget(self.ColorImageBtn)
        self.ColorImageBtn.clicked.connect(lambda: self.loadImage('c'))

        # upload color image
        vbox.addWidget(self.BinaryImageBtn)
        self.BinaryImageBtn.clicked.connect(lambda: self.loadImage('b'))

        # Submit button
        vbox.addWidget(self.SubmitBtn)
        self.SubmitBtn.clicked.connect(lambda: self.handleSubmit())

        # Show the GUI
        self.show()

    def loadImage(self, t):
        name = QFileDialog.getOpenFileName(self, 'Select Color Image', QDir.currentPath(),
                                           "Image files (*.jpg, *.gif, *.png)")
        if name:
            path = name[0]
            print(path)
            if t == 'b':
                self.binaryImg, self.binImgObj = binaryConvert(path)
                print(self.binaryImg)
            else:
                self.colorImg, self.colorImgObj = RGBConvert(path)
                print(self.colorImg)
            return path

    def handleSubmit(self):
        try:
            if self.colorImg is None or self.binaryImg is None:
                raise NotImplementedError
            elif not checkImagesSize(self.binImgObj, self.colorImgObj):
                raise ValueError
        except NotImplementedError:
            errorMessage('Binary & Color images must uploaded!')
        except ValueError:
            errorMessage('Binary image must be smaller than color image')
        else:
            #If everything is ok, continue here
            return
        finally:
            #Break function in any case
            return

