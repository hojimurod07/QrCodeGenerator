
from PyQt5.QtWidgets import  *
from PyQt5.Qt import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *



class QRCode(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QrCode generator")
        self.setFixedSize(600,700)

        self.asosiy = QVBoxLayout()

        self.create_image_board()


        self.asosiy.addLayout(self.image_board)
        self.w = QWidget()
        self.w.setLayout(self.asosiy)
        self.setCentralWidget(self.w)

    def create_image_board(self):

        self.image_board = QVBoxLayout()
        self.image_btn  = QPushButton("")
        self.image_btn.setStyleSheet("background-image: url('dr.jpg'); border: none;")
        self.image_board.addWidget(self.image_btn)
        self.image_btn.setFixedSize(600,450)




app  = QApplication([])

oyna= QRCode()
oyna.show()


app.exec_()
