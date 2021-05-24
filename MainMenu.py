from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtCore import QDir, QFile, QFileInfo, QIODevice
from PyQt5.QtWidgets import QVBoxLayout, QFileDialog
from Functions.imageConvertionFuncs import *
from Functions.errorMessages import *
from Functions.algorithms import *
from Functions.resizeImage import *


class MainMenu(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainMenu, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('dataSecurity.ui', self)  # Load the .ui file

        # Class variables definition (Optional but the vars definitions below necessary)
        self.encryptedImg = self.binaryImg = self.decipherImg = None
        self.submitted = False

        improveRuntimeReply = QMessageBox.question(self, "Before we get started!",
                                                   "Do you want to improve runtime? Note that original images will be shrink.",
                                                   QMessageBox.Yes, QMessageBox.No, )

        if improveRuntimeReply == QMessageBox.Yes:
            self.shrinkImages = True
        else:
            self.shrinkImages = False

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
            if self.shrinkImages:
                shrinkImage(name[0])
            if t == 'b':
                self.binImgPath = name[0]
                self.binaryImg, self.binImgObj = binaryConvert(self.binImgPath)
                # print(self.binaryImg)
            else:
                self.colorImgPath = name[0]
                self.encryptedImg, self.colorImgObj = RGBConvert(self.colorImgPath)
                # print(self.colorImg)

        return

    def handleSubmit(self):
        try:
            if self.encryptedImg is None or self.binaryImg is None:
                raise NotImplementedError
            elif not checkImagesSize(self.binImgObj, self.colorImgObj):
                raise ValueError
            else:
                print('Successfully received input, implementing algorithm...')

                # If everything is ok, embed the binary image into the color image
                self.encryptedImg = embeddingAlgorithm(self.encryptedImg, self.binaryImg)

                # show results
                img = arrToImage(self.encryptedImg, 'RGB')
                img.show()
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
            if not self.submitted:
                raise NotImplementedError

        except NotImplementedError:
            errorMessage('Embedding algorithm must be done before reconstructing!')

        #If submitted
        else:
            self.decipherImg = FlipColumnAndRows(reconstructedAlgorithm(self.encryptedImg, self.binaryImg))

            img = arrToImage(self.decipherImg, 'L')
            img.show()
        finally:
            # Break function in any case
            return