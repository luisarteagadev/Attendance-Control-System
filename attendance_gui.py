from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QDateEdit,
    QPushButton, QRadioButton, QTextEdit, QGridLayout, QSpacerItem, QSizePolicy,
    QFrame,QScrollArea
)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt, QDate

class AttendanceWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        # Título del curso
        course_name = QLabel("Nombre de Curso")
        course_name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(course_name)

        # Fecha de selección
        date_layout = QHBoxLayout()
        select_date_label = QLabel("Seleccionar Fecha")
        date_picker = QDateEdit(calendarPopup=True)
        date_picker.setDate(QDate.currentDate())
        date_picker.setFixedWidth(100)
        
        date_layout.addWidget(select_date_label)
        date_layout.addWidget(date_picker)
        date_layout.addStretch()
        main_layout.addLayout(date_layout)

        #Crear una área de scroll para los estudiantes
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        # Widget contenedor para los estudiantes
        students_container = QWidget()
        students_layout = QVBoxLayout(students_container)
        for _ in range(10):
            students_layout.addWidget(self.create_student_info())
            # Separador horizontal
            separator = QFrame()
            separator.setFrameShape(QFrame.Shape.HLine)
            separator.setFrameShadow(QFrame.Shadow.Sunken)
            students_layout.addWidget(separator)
        scroll_area.setWidget(students_container)
        # Agregar el scroll_area al layout principal
        main_layout.addWidget(scroll_area)
        self.setLayout(main_layout)
    def create_student_info(self):
        # Widget para una fila de información de un estudiante
        student_widget = QWidget()
        layout = QHBoxLayout()
        spacer=QSpacerItem(20, 0, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)
        # Imagen de perfil
        image_label = QLabel()
        pixmap = QPixmap("icon/user-48.ico")  # Ruta a la imagen
        image_label.setPixmap(pixmap)
        image_label.setScaledContents(True)
        image_label.setFixedSize(120, 120)  # Ajustar el tamaño de la imagen

        # Layout para la información de texto
        text_layout = QVBoxLayout()
        # spacer = QSpacerItem(150, 0, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        #text_layout.setContentsMargins(20, 0, 0, 0)
        # Código
        codigo_label = QLabel("Código: ********")
        # Nombre
        nombre_label = QLabel("Nombre: ********")
        # Correo
        correo_label = QLabel("Correo: ********")

        # Añadir etiquetas al layout de texto
        text_layout.addWidget(codigo_label)
        text_layout.addWidget(nombre_label)
        text_layout.addWidget(correo_label)

        attendance_layout=QVBoxLayout()
        attendance_layout.addWidget(QLabel("Estado de asistencia"))
        presente_rb = QRadioButton("Presente")
        tarde_rb = QRadioButton("Tardío")
        ausente_rb = QRadioButton("Ausente")
    
        attendance_layout.addWidget(presente_rb)
        attendance_layout.addWidget(tarde_rb)
        attendance_layout.addWidget(ausente_rb)
        
        observation_layout = QVBoxLayout()
        observation_layout.addWidget(QLabel("Registrar Observación"))
        observation_text = QTextEdit()
        observation_text.setFixedHeight(70)
        observation_layout.addWidget(observation_text)
        # Botón Guardar
        save_button = QPushButton("Guardar")
        save_button.setFixedWidth(80)

        # Añadir widgets al layout principal de la fila
        layout.addWidget(image_label)
        layout.addItem(spacer) 
        layout.addLayout(text_layout)
        layout.addItem(spacer) 
        layout.addLayout(attendance_layout)
        layout.addItem(spacer) 
        layout.addLayout(observation_layout)
        layout.addWidget(save_button)

      
        student_widget.setLayout(layout)

        return student_widget
        
    
