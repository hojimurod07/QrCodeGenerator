
from PyQt5.QtWidgets import  *



class QRCode(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QrCode generator")
        self.setFixedSize(400,500)




app  = QApplication([])

oyna= QRCode()
oyna.show()


app.exec_()
