import sys, csv
from PyQt6.QtWidgets import QApplication, QWidget ,QVBoxLayout , QHBoxLayout ,QLabel, QLineEdit , QPushButton

class pagina(QWidget):
    def __init__(self,ingresar,registrar):
        super().__init__()
        self.registrar = registrar
        self.ingresar = ingresar
        self.init_ui()

    def init_ui(self):    
        self.setWindowTitle('Sistema de información pacientes')
        self.setGeometry(100,100,300,200)

        layout = QVBoxLayout()

        label_username = QLabel('Usuario:')
        layout.addWidget(label_username)

        self.edit_username = QLineEdit()
        layout.addWidget(self.edit_username)

        label_password = QLabel('Contraseña:')
        layout.addWidget(label_password)

        self.edit_password = QLineEdit()
        self.edit_password.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.edit_password)

        btn_ingresar = QPushButton("Ingresar")
        btn_ingresar.clicked.connect(self.auth)
        layout.addWidget(btn_ingresar)

        btn_registro = QPushButton("Registro nuevo paciente")
        btn_registro.clicked.connect(self.reg)
        layout.addWidget(btn_registro)


        self.setLayout(layout)
    
    def auth(self):
        username = self.edit_username.text()
        password = self.edit_password.text()

        if self.validate_credentials(username, password):
            print('Acceso concedido')
            self.ingresar.show()
        else:
            print('Acceso denegado')
    
    def validate_credentials(self,username,password):
        self.user = ""
        self.pas = ""
        with open("datos.csv", "r") as file:
            reader = csv.reader(file, delimiter=';')
            next(reader)
            for row in reader:
                if row[0] == username:
                    self.user= username
                    self.pas = password
                else:
                    self.no_reg.show()
        return username == "usuario" and password == "password"
    
    def reg(self):
        self.registrar.show()
        self.close()
        
def load_stylesheet():
    return   """
        QWidget{
            background-color: #00BFFF;
            box-shadow: 5px 5px 5px #FFFFFF;
        }
        QLabel{
            font-size = 14px;
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
    

if __name__ == '__main__':
    app = QApplication(sys.argv)

    stylesheet = load_stylesheet()
    app.setStyleSheet(stylesheet)

    pag=pagina()
    pag.show()

    sys.exit(app.exec())