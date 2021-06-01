from PyQt5.QtWidgets import QMessageBox
from PIL import Image


def errorMessage(text):
    '''Handles the GUI error message box'''

    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setText("Error!")
    msg.setInformativeText(text)
    msg.setWindowTitle("Error")
    msg.exec_()


def checkImagesSize(bin, color):
    '''Calculates total pixels in each image, return true of color > bin, else false.
     The binary image will be embedded in the color one so the color image must contain at least
     the number of bits of the binary picture.'''

    b_width, b_height = bin.size
    c_width, c_height = color.size

    # implement the condition
    return b_width <= c_width and b_height <= c_height
