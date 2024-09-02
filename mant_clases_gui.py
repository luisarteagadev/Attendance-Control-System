from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QLabel, QLineEdit, 
    QPushButton, QFrame, QListWidget, QTableWidget, QTableWidgetItem, QHeaderView
)
from PyQt6.QtCore import Qt

class MantClasesWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        # Layout para la parte superior con los dos marcos principales
        top_layout = QHBoxLayout()

        # Marco para "Registrar Datos"
        register_frame = QFrame()

        register_frame.setFrameShape(QFrame.Shape.Box)
        register_frame.setLineWidth(2)
        register_layout = QGridLayout()

        # Elementos dentro del marco "Registrar Datos"
        
        title=QLabel("Registrar Datos")
        register_layout.addWidget(title, 0, 0)
        register_layout.addWidget(QLabel("ID"), 1, 0)
        register_layout.addWidget(QLineEdit(), 1, 1)

        register_layout.addWidget(QLabel("Nombre Clase"), 2, 0)
        register_layout.addWidget(QLineEdit(), 2, 1)

        register_layout.addWidget(QLabel("Hora Inicio"), 3, 0)
        register_layout.addWidget(QLineEdit(),3, 1)

        register_layout.addWidget(QLabel("Hora Fin"), 4, 0)
        register_layout.addWidget(QLineEdit(), 4, 1)

        register_layout.addWidget(QLabel("Curso"), 5, 0)
        register_layout.addWidget(QLineEdit(), 5, 1)
        register_layout.addWidget(QPushButton("Buscar"), 5, 2)

        register_layout.addWidget(QLabel("Profesor"), 6, 0)
        register_layout.addWidget(QLineEdit(), 6, 1)
        register_layout.addWidget(QPushButton("Buscar"), 6, 2)

        # Botones al final del marco "Registrar Datos"
        button_layout = QHBoxLayout()
        button_layout.addWidget(QPushButton("Agregar"))
        button_layout.addWidget(QPushButton("Modificar"))
        button_layout.addWidget(QPushButton("Eliminar"))

        register_layout.addLayout(button_layout, 7, 0, 1, 3)

        register_frame.setLayout(register_layout)
        top_layout.addWidget(register_frame)

        # Marco para "Registrar Alumnos"
        student_frame = QFrame()
        student_frame.setFrameShape(QFrame.Shape.Box)
        student_frame.setLineWidth(2)
        student_layout = QGridLayout()

        # Lista de alumnos
        student_list = QListWidget()
        student_list.addItems(["Juan Ortega", "Carlos Peralta", "Jose Ramírez"])
        title=QLabel("Seleccionar Alumnos")
        student_layout.addWidget(title, 0, 0)
        student_layout.addWidget(student_list, 1, 0, 3, 1)

        # Botones de "Buscar Alumno" y "Eliminar Alumno"
        student_layout.addWidget(QPushButton("Buscar Alumno"), 1, 1)
        student_layout.addWidget(QPushButton("Eliminar Alumno"), 2, 1)
       
        student_frame.setLayout(student_layout)
        top_layout.addWidget(student_frame)

        main_layout.addLayout(top_layout)

        # Tabla en la parte inferior
        table = QTableWidget(1, 3)
        table.setHorizontalHeaderLabels(["Clase", "Profesor", "Curso"])
        table.setItem(0, 0, QTableWidgetItem("Clase S-02"))
        table.setItem(0, 1, QTableWidgetItem("Juan Ortega"))
        table.setItem(0, 2, QTableWidgetItem("Comunicación"))

        # Ajustar el tamaño de las columnas
        table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        main_layout.addWidget(table)

        self.setLayout(main_layout)


