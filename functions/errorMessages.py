from PyQt5.QtWidgets import QMessageBox

def imagesNotLoadedErr():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setText("Error!")
    msg.setInformativeText('Binary & Color images must uploaded!')
    msg.setWindowTitle("Error")
    msg.exec_()