import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, 
     QLineEdit, QPushButton, QCheckBox, QMessageBox)
from PyQt6.QtGui import QFont, QPixmap
from PyQt6.QtCore import Qt,QFile , QTextStream    
import main
import conexion_Dao as dao
class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        # INICIA
        self.setFixedSize(380,250)
        self.setWindowTitle("SISTEMA COLEGIO")
        self.setUpWindow()
        self.show()
    def setUpWindow(self):
        # LABEL TITULO
        self.login_is_successful=False
        login_label= QLabel("INICIA SESION",self)
        login_label.setFont(QFont("Arial",20))
        login_label.move(100,10)##
        # USUARIO LABEL
        username_label=QLabel("Usuario:",self)
        username_label.move(20,60)##
        # USUARIO EDIT
        self.username_edit=QLineEdit(self)
        self.username_edit.resize(250,20)
        self.username_edit.move(90,60)##
        # PASSWORD LABEL
        password_label=QLabel("Contraseña:", self)
        password_label.move(20,90)##
        # PASSWORD EDIT
        self.password_edit=QLineEdit(self)
        self.password_edit.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_edit.resize(250,20)
        self.password_edit.move(90,90)##
        # MOSTRAR CONTRASEÑA
        self.show_password_cb=QCheckBox("Mostrar Contraseña",self)
        self.show_password_cb.move(90,130)##
        self.show_password_cb.toggled.connect(self.displayPasswordIfChecked)
        # BOTON INGRESAR
        login_button=QPushButton("INGRESAR",self)
        login_button.resize(320,30)
        login_button.move(20,170)##
        login_button.clicked.connect(self.clickLoginButton)

    def mensajes(self, tipo, mensaje):
        msg_box = QMessageBox()
        if tipo == "info":
            msg_box.setIcon(QMessageBox.Icon.Information)
            msg_box.setWindowTitle(tipo)
        elif tipo == "error":
            msg_box.setIcon(QMessageBox.Icon.Critical)
            msg_box.setWindowTitle(tipo)
        msg_box.setText(mensaje)
        msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg_box.exec()

    def displayPasswordIfChecked(self,checked):
        if checked:
            self.password_edit.setEchoMode(QLineEdit.EchoMode.Normal)
        elif checked==False:
            self.password_edit.setEchoMode(QLineEdit.EchoMode.Password)

    def clickLoginButton(self):
        if self.username_edit.text()=="" or self.password_edit.text()=="":
            self.mensajes("error", "Faltan datos")
        else:
            evalua, tipo = dao.verifica_usuario(self.username_edit.text(), self.password_edit.text())
            if evalua==False and tipo==True:
                self.mensajes("error", "Error en el sistema.")
            elif evalua==False and tipo==False:
                self.mensajes("error", "No se encontro usuario.")
            elif evalua==True and tipo!="":
                self.mensajes("info", "Bienvenido al sistema.")
                self.close()
                self.main_window = main.MainWindow(evalua, tipo)
                self.main_window.show()
            else: 
                self.mensajes("error", "Error en BD")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginWindow()

    style_file = QFile("style.qss")
    style_file.open(QFile.OpenModeFlag.ReadOnly | QFile.OpenModeFlag.Text)
    style_stream = QTextStream(style_file)
    app.setStyleSheet(style_stream.readAll())
    sys.exit(app.exec())

