import sys, csv 
from PyQt6.QtWidgets import QApplication, QWidget ,QVBoxLayout , QHBoxLayout ,QLabel, QLineEdit , QPushButton

class Datos(QWidget):
    def __init__(self,reg, pac_reg,back_g):
        super().__init__()
        self.reg = reg
        self.back_g = back_g
        self.pac_reg = pac_reg
        self.init_ui()

    def init_ui(self): 

        self.setWindowTitle("Registro Usuarios")
        self.setGeometry(100,100,300,200)
        
        layout = QVBoxLayout()

        label_username = QLabel('Usuario:')
        layout.addWidget(label_username)
        self.edit_username = QLineEdit()
        layout.addWidget(self.edit_username)

        label_contrasena = QLabel('Contraseña:')
        layout.addWidget(label_contrasena)
        self.edit_contrasena = QLineEdit()
        layout.addWidget(self.edit_contrasena)

        label_perfil = QLabel('Perfil:')
        layout.addWidget(label_perfil)
        self.edit_perfil = QLineEdit()
        layout.addWidget(self.edit_perfil)

        btn_reg = QPushButton("Crear usuario")
        btn_reg.clicked.connect(self.record_pac)
        layout.addWidget(btn_reg)

        btn_ingreso = QPushButton("Ingresar")
        btn_reg.clicked.connect(self.ingresar)
        layout.addWidget(btn_ingreso)
        self.setLayout(layout)
    
    def record_pac(self):
        #Guardar pacientes 
        self.user = self.edit_username.text()
        self.pas = self.edit_contrasena.text()
        self.perfil = self.edit_perfil.text()
        self.pac_record2=[]
        self.pac_record = [self.user, self.pas, self.perfil]
        self.pac_record2.append(self.pac_record)
        x=0
        with open("Lab interfaz/informacion/datos.csv", "r") as file:
             
            reader = csv.reader(file, delimiter = ",") 
            header = next(reader) 
            #self.username = None 
            for row in reader: 
                if row[0] == self.user: 
                    self.urep.show() 
                    print("Repetido") 
                    x=1
                    return 
        if x == 1:
             self.reg.show()
        elif x== 0:
            with open("Lab interfaz/informacion/datos.csv","a", newline="") as file:
                writer = csv.writer(file, delimiter =";")
                #writer.writerow(["Name","Gender","perfil"])
                writer.writerows(self.pac_record2)
            self.pac_reg.show()
    
    def ingresar (self):
         self.back.show()

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
