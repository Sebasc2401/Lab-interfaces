import sys 
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPixmap

class led(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Elementos de una interfaz:")
        self.setGeometry(100,100,500,500)

        #insertar imagen
        self.label_image = QLabel(self)
        self.label_image.setGeometry(50,50,225,225)
        pixmap = QPixmap("interfaces\logo.png")
        self.label_image.setPixmap(pixmap)
        
        #Crear un menu de selección (ComboBox)
        self.label_combo = QLabel("día de la semana",self)
        self.label_combo.setGeometry(50,280,100,20)
        self.combo_dias = QComboBox(self)
        self.combo_dias.setGeometry(50,310,100,20)
        self.combo_dias.addItems(["Lunes","Martes","Miercoles","Jueves","Viernes","Sábado","Domingo"])

        #Crear un grupo de botones
        self.label_radio = QLabel("Genero:", self) 
        self.label_radio.setGeometry(50, 360, 100, 20) 
        self.radio_masculino = QRadioButton("Masculino", self) 
        self.radio_masculino.setGeometry(50, 380, 100, 20) 
        self.radio_femenino = QRadioButton("Masculino", self) 
        self.radio_femenino.setGeometry(50, 400, 100, 20) 
         
        #Crear casillas de verificacion para las opciones de salud 
        self.label_checkbox = QLabel("Salud:", self) 
        self.label_checkbox.setGeometry(250, 280, 100, 20) 
        self.checkbox_diabetes = QCheckBox("Diabetes", self) 
        self.checkbox_diabetes.setGeometry(250, 300, 100, 20) 
        self.checkbox_hipertension = QCheckBox("Hipertension", self) 
        self.checkbox_hipertension.setGeometry(250, 320, 100, 20)

if __name__ =='__main__':
    app = QApplication(sys.argv)
    
    main_window= led()
    main_window.show()

    sys.exit(app.exec())