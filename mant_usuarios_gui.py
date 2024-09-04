from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QLabel, QLineEdit, 
    QPushButton, QFrame, QListWidget, QTableWidget, QTableWidgetItem, QHeaderView,
    QRadioButton,QComboBox,
    QTabWidget,QGroupBox,QCheckBox
)
from PyQt6.QtCore import Qt

class MantUsuariosWidget(QWidget):
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

        register_layout.addWidget(QLabel("Nombre"), 2, 0)
        register_layout.addWidget(QLineEdit(), 2, 1)

        register_layout.addWidget(QLabel("Usuario"), 3, 0)
        register_layout.addWidget(QLineEdit(),3, 1)

        register_layout.addWidget(QLabel("Contraseña"), 4, 0)
        register_layout.addWidget(QLineEdit(), 4, 1)


        register_layout.addWidget(QLabel("Sexo"), 5, 0)
        rb_sexo_layout=QHBoxLayout()
        
        rb_sexo_m=QRadioButton('Masculino')
        rb_sexo_f=QRadioButton('Femenino')
        rb_sexo_layout.addWidget(rb_sexo_m)
        rb_sexo_layout.addWidget(rb_sexo_f)
        
        register_layout.addLayout(rb_sexo_layout,5,1)


        # register_layout.addWidget(QLineEdit(), 5, 1)
        # register_layout.addWidget(QPushButton("Buscar"), 5, 2)

        register_layout.addWidget(QLabel("Rol"), 6, 0)
        rol_combo=QComboBox()
        register_layout.addWidget(rol_combo, 6, 1)
        register_layout.addWidget(QLabel("Grado"), 7, 0)
        rol_combo=QComboBox()
        register_layout.addWidget(rol_combo, 7, 1)
        # register_layout.addWidget(QPushButton("Buscar"), 6, 2)

        # Botones al final del marco "Registrar Datos"
        button_layout = QHBoxLayout()
        button_layout.addWidget(QPushButton("Agregar"))
        button_layout.addWidget(QPushButton("Modificar"))
        button_layout.addWidget(QPushButton("Eliminar"))

        register_layout.addLayout(button_layout, 8, 0, 1, 3)

        register_frame.setLayout(register_layout)
        top_layout.addWidget(register_frame)

        # Marco para "Registrar Alumnos"
        student_frame = QFrame()
        student_frame.setFrameShape(QFrame.Shape.Box)
        student_frame.setLineWidth(2)
        student_layout = QGridLayout()

        # Lista de alumnos
        student_list = QListWidget()
        tab_bar_accesos= QTabWidget(self)
        self.admin_tab= AdminTabWidget()
        self.cursos_tab = CursosTabWidget()

        tab_bar_accesos.addTab(self.admin_tab, "Administrador")
        tab_bar_accesos.addTab(self.cursos_tab, "Cursos")

        title=QLabel("Permisos de Usuario")
        student_layout.addWidget(title, 0, 0)
        student_layout.addWidget(tab_bar_accesos, 1, 0, 3, 1)

        student_frame.setLayout(student_layout)
        top_layout.addWidget(student_frame)

        main_layout.addLayout(top_layout)

        # Tabla en la parte inferior
        table = QTableWidget(1, 4)
        table.setHorizontalHeaderLabels(["ID", "Nombre", "Usuario","Rol"])
        table.setItem(0, 0, QTableWidgetItem("Clase S-02"))
        table.setItem(0, 1, QTableWidgetItem("Juan Ortega"))
        table.setItem(0, 2, QTableWidgetItem("Juanortega@ue.edu.pe"))
        table.setItem(0, 3, QTableWidgetItem("Estudiante"))

        # Ajustar el tamaño de las columnas
        table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        main_layout.addWidget(table)

        self.setLayout(main_layout)

class AdminTabWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Layout principal
        main_layout = QVBoxLayout()
        
        group_layout = QVBoxLayout()
        group_layout.setContentsMargins(20,0,0,0)

        self.checkbox_block = QCheckBox("Bloquear acceso a este modulo")
        self.checkbox_allow = QCheckBox("Permitir el acceso a este modulo")
        self.checkbox_clases = QCheckBox("Mant. Clases")
        self.checkbox_usuarios = QCheckBox("Mant. Usuarios")
        group_layout.addWidget(self.checkbox_clases)
        group_layout.addWidget(self.checkbox_usuarios)
        

        main_layout.addWidget(self.checkbox_block)
        main_layout.addWidget(self.checkbox_allow)
        main_layout.addLayout(group_layout)
        self.setLayout(main_layout)
class CursosTabWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Layout principal
        main_layout = QVBoxLayout()
        
        group_layout = QVBoxLayout()
        group_layout.setContentsMargins(20,0,0,0)

        self.checkbox_block = QCheckBox("Bloquear acceso a este modulo")
        self.checkbox_allow = QCheckBox("Permitir el acceso a este modulo")
        self.checkbox_list_cursos = QCheckBox("Lista Cursos")
        group_layout.addWidget(self.checkbox_list_cursos)
        
        main_layout.addWidget(self.checkbox_block)
        main_layout.addWidget(self.checkbox_allow)
        main_layout.addLayout(group_layout)
        self.setLayout(main_layout)

        
