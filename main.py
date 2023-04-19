import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from informacion.pagina_principal import pagina, load_stylesheet
from informacion.registro import Datos, load_stylesheet
from informacion.usuario import led
from informacion.no_reg import F_reg
from informacion.reg_eb import reg_g
from informacion.back import g_back
from informacion.save import saved

def menu():
    if __name__ == '__main__':
        app = QApplication(sys.argv)
        stylesheet = load_stylesheet()
        app.setStyleSheet(stylesheet)

        saved_us= saved()
        registro_guardado= reg_g()
        back = g_back()
        user = led()
        reg = Datos(registro_guardado,back,saved_us)
        main =pagina(user, reg)
        main.show()

        sys.exit(app.exec())
menu()