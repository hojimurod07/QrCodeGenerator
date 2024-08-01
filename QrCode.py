
from PyQt5.QtWidgets import  *
from PyQt5.Qt import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import  os

class QRCode(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QrCode generator")
        self.setFixedSize(600,700)

        self.asosiy = QVBoxLayout()

        self.create_image_board()
        self.create_main()

        self.generate.clicked.connect(self.QrCoder)
        self.reset.clicked.connect(self.ResetAll)

        self.asosiy.addLayout(self.image_board)
        self.asosiy.addLayout(self.info)
        self.w = QWidget()
        self.w.setLayout(self.asosiy)
        self.setCentralWidget(self.w)

    def create_image_board(self):

        self.image_board = QVBoxLayout()
        self.image_btn  = QPushButton("")
        self.image_btn.setStyleSheet("background-image: url('dr.jpg'); border: none;")
        self.image_board.addWidget(self.image_btn)
        self.image_btn.setFixedSize(600,450)

    def create_main(self):
        self.info = QVBoxLayout()
        self.btns = QHBoxLayout()
        self.line = QLineEdit()
        self.line.setPlaceholderText("Enter your link")
        self.line.setFixedSize(600,50)
        self.info.addWidget(self.line)
        self.line.setStyleSheet("font-size: 20px")

        self.reset = QPushButton(" ")
        self.reset.setIcon(QIcon("reset.png"))
        self.reset.setFixedSize(120,60)

        self.btns.addWidget(self.reset)

        self.generate = QPushButton("Generate")
        self.generate.setStyleSheet("color:white;background-color: #134898;border-radius:10px;border:none;font-size:22px ")
        self.generate.setStyleSheet("QPushButton::hover"
                             "{"
                             "background-color : #C0C2C4;"
                             "}")

        self.generate.setFixedSize(120, 60)
        self.btns.addWidget(self.generate)
        self.info.addLayout(self.btns)


    def QrCoder(self):
        import qrcode

        img = qrcode.make(self.line.text())
        type(img)

        img.save("images/test.png")
        self.image_btn.setStyleSheet("""
                    QPushButton {
                        background-image: url('images/test.png');
                        background-repeat: no-repeat;
                        background-position: center;
                      
                        border: none;
                    }
                """)

    def ResetAll(self):
        if os.path.exists("images/test.png"):
            os.remove("images/test.png")
            self.image_btn.setStyleSheet("background-image: url('dr.jpg'); border: none;")
            self.line.setText("")
        else:
            pass

app  = QApplication([])

oyna= QRCode()
oyna.show()


app.exec_()
