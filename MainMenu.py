from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtCore import QDir, QFile, QFileInfo, QIODevice
from PyQt5.QtWidgets import QVBoxLayout, QFileDialog
from Functions.imageConvertionFuncs import *
from Functions.errorMessages import *
from Functions.algorithms import *


class MainMenu(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainMenu, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('dataSecurity.ui', self)  # Load the .ui file

        # Class variables definition (Optional but the vars definitions below necessary)
        self.encryptedImg = self.binaryImg = self.decipherImg = None
        self.submitted = False

        # Widgets definitions
        vbox = QVBoxLayout(self)
        self.errDialog = QtWidgets.QErrorMessage()  # self because it called in another function

        # Organize the title alignment
        self.Title.setAlignment(QtCore.Qt.AlignCenter)

        # upload color image
        vbox.addWidget(self.ColorImageBtn)
        self.ColorImageBtn.clicked.connect(lambda: self.loadImage('c'))

        # upload back & white image
        vbox.addWidget(self.BinaryImageBtn)
        self.BinaryImageBtn.clicked.connect(lambda: self.loadImage('b'))

        # Submit button
        vbox.addWidget(self.SubmitBtn)
        self.SubmitBtn.clicked.connect(lambda: self.handleSubmit())

        # decipher button
        vbox.addWidget(self.DecipherBtn)
        self.DecipherBtn.clicked.connect(lambda: self.handleDecipher())

        # Show the GUI
        self.show()

    def loadImage(self, t):
        name = QFileDialog.getOpenFileName(self, 'Select Color Image', QDir.currentPath(),
                                           "Image files (*.jpg, *.gif, *.png)")
        if name:
            path = name[0]
            if t == 'b':
                self.binaryImg, self.binImgObj = binaryConvert(path)
                # print(self.binaryImg)
            else:
                self.encryptedImg, self.colorImgObj = RGBConvert(path)
                # print(self.colorImg)
            return path

    def handleSubmit(self):
        try:
            if self.encryptedImg is None or self.binaryImg is None:
                raise NotImplementedError
            elif not checkImagesSize(self.binImgObj, self.colorImgObj):
                raise ValueError
            else:
                print('Successfully received input, implmenting algorithm...')

                # If everything is ok, embed the binary image into the color image
                self.encryptedImg = embeddingAlgorithm(self.encryptedImg, self.binaryImg)

                # show results
                arrToImage(self.encryptedImg, 'RGB')
                reconstructedAlgorithm(self.encryptedImg, self.binaryImg)
                self.submitted = True

        except NotImplementedError:
            errorMessage('Binary & Color images must be uploaded!')
        except ValueError:
            errorMessage('Binary image must be smaller than color image!')

        finally:
            # Break function in any case
            return

    def handleDecipher(self):
        try:
            if self.encryptedImg is None or self.binaryImg is None:
                raise NotImplementedError

        except NotImplementedError:
            errorMessage('Embedding algorithm must be done before reconstructing!')

        #If submitted
        else:
            self.decipherImg = reconstructedAlgorithm(self.encryptedImg)

            # show results
            arrToImage(self.encryptedImg, 'L')

        finally:
            return