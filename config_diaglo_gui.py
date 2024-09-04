import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QVBoxLayout, QHBoxLayout, QLabel, QWidget
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import Qt, QSize

class ConfigDialog(QDialog):
    def __init__(self, parent=None):
        super(ConfigDialog, self).__init__(parent)
        self.setWindowTitle("Ajustes del sistema")
        self.setFixedSize(400, 300)

        # Layout principal
        main_layout = QVBoxLayout(self)

        # Layout para los botones (iconos)
        button_layout = QHBoxLayout()
        button_layout.setSpacing(40)  # Espaciado entre los iconos

        # Primer botón: Datos de Colegio
        datos_colegio_btn = QPushButton(self)
        datos_colegio_btn.setFixedSize(100, 100)
        datos_colegio_btn.setIcon(QIcon(QPixmap(":/icon/icon/home_icon.ico")))
        datos_colegio_btn.setIconSize(QSize(48, 48))
        datos_colegio_btn.setText("Datos de Colegio")
        datos_colegio_btn.setStyleSheet("text-align: center;")
        button_layout.addWidget(datos_colegio_btn)

        # Segundo botón: Copias de Seguridad
        copias_seguridad_btn = QPushButton(self)
        copias_seguridad_btn.setFixedSize(100, 100)
        copias_seguridad_btn.setIcon(QIcon(QPixmap(":/icon/icon/backup_icon.ico")))
        copias_seguridad_btn.setIconSize(QSize(48, 48))
        copias_seguridad_btn.setText("Copias de Seguridad")
        copias_seguridad_btn.setStyleSheet("text-align: center;")
        button_layout.addWidget(copias_seguridad_btn)

        # Añadir el layout de botones al layout principal
        main_layout.addLayout(button_layout)
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)