import sys 
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPixmap

class g_back(QWidget):
    def _init_(self):
        super()._init_()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Precaución')
        self.setGeometry(100,100,300,200)

        layout = QVBoxLayout()

        label_mensaje = QLabel("Cierre la ventana y \n vuelva a abrir la pantalla principal.")
        layout.addWidget(label_mensaje)

        self.setLayout(layout)

def load_stylesheet7():
    return """
        QWidget {
            bbackground-color: #00BFFF;
            box-shadow: 5px 5px 5px #FFFFFF;
        }
        QLabel{
            font-size: 14px;
            color: #000080
        }
        QLineEdit{
            background-color: #FFFFFF;
            border: 1px solir #1E90FF;
            paddin: 3px;
            font-size: 14px;
        }
        QPushButton{
            background-color: #1E90FF;
            color: #FFFFFF;
            border: 1px solid #1E90FF;
            padding: 5px;
            font-size: 14px;
        }
        QPushButton:hover{
            background-color: #6495ED;
            border: 1px solid #6495ED;
        }
    """