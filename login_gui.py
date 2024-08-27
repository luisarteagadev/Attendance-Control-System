import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, 
     QLineEdit, QPushButton, QCheckBox, QMessageBox)
from PyQt6.QtGui import QFont, QPixmap
from PyQt6.QtCore import Qt,QFile , QTextStream
# from registration import NewUserDialog     
from main import MainWindow
class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setFixedSize(360,300)
        self.setWindowTitle("Sistema Colegio")
        self.setUpWindow()
        self.show()
    
    def setUpWindow(self):
        
        self.login_is_successful=False
        login_label= QLabel("Inicia Sesión",self)
        login_label.setFont(QFont("Arial",20))
        login_label.move(120,10)

        username_label=QLabel("Usuario:",self)
        username_label.move(20,54)

        self.username_edit=QLineEdit(self)
        self.username_edit.resize(250,24)
        self.username_edit.move(90,50)

        password_label=QLabel("Contraseña:", self)
        password_label.move(20,86)

        self.password_edit=QLineEdit(self)
        self.password_edit.setEchoMode(QLineEdit.EchoMode.Password)

        self.password_edit.resize(250,24)
        self.password_edit.move(90,82)

        self.show_password_cb=QCheckBox("Mostrar Contraseña",self)
        self.show_password_cb.move(90,110)
        self.show_password_cb.toggled.connect(self.displayPasswordIfChecked)

        login_button=QPushButton("Ingresar",self)
        login_button.resize(320,34)
        login_button.move(20,140)
        login_button.clicked.connect(self.clickLoginButton)

    def clickLoginButton(self):
        users={}
        file="files/users.txt"

        try:
            with open(file,"r") as f:
                for line in f:
                    user_info=line.split(" ")
                    username_info=user_info[0]
                    password_info=user_info[1].strip("\n")
                    users[username_info]= password_info
            
            username=self.username_edit.text()
            password=self.password_edit.text()

            if (username,password) in users.items(): 
                QMessageBox.information(self,"Mensaje de información",
                                        "¡Inicio de sesión exitoso!",
                                        QMessageBox.StandardButton.Ok,
                                        QMessageBox.StandardButton.Ok)
                
                self.login_is_successful=True
                #el close no cierra la ventana como tal, sino lo oculta a la vista
                self.close()
                self.openApplicationWindow()
            else:
                QMessageBox.warning(self, "Mensaje de error",
                    "El usuario o contraseña es incorrecto.", 
                    QMessageBox.StandardButton.Close, 
                    QMessageBox.StandardButton.Close)
        except FileNotFoundError as error:
            QMessageBox.warning(self, "Error",
                f"""<p>Archivo no encontrado.</p> 
                <p>Error: {error}</p>""", 
                QMessageBox.StandardButton.Ok)
            # Create file if it doesn't exist
            f = open(file, "w")


    def displayPasswordIfChecked(self,checked):
        if checked:
            self.password_edit.setEchoMode(QLineEdit.EchoMode.Normal)
        elif checked==False:
            self.password_edit.setEchoMode(QLineEdit.EchoMode.Password)


    def openApplicationWindow(self):
        self.main_window=MainWindow()
        self.main_window.show()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginWindow()

    style_file = QFile("style.qss")
    # if not style_file.open(QFile.OpenModeFlag.ReadOnly ):
    #     print("No se pudo abrir el archivo de estilo")
    #     exit()
    style_file.open(QFile.OpenModeFlag.ReadOnly | QFile.OpenModeFlag.Text)
    style_stream = QTextStream(style_file)
    app.setStyleSheet(style_stream.readAll())
    sys.exit(app.exec())

