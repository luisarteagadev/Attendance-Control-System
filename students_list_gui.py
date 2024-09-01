import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QCheckBox, QPushButton, QGridLayout, QFrame, QSpacerItem, QSizePolicy, QScrollArea
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

class StudentsListWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Layout principal
        main_layout = QVBoxLayout()

        # Layout para el título
        title_label = QLabel("Nombre de Curso")
        title_label.setStyleSheet("font-size: 24px; font-weight: bold;")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(title_label)

        # Layout para los filtros
        filter_layout = QGridLayout()

        # Filtros de nombres
        filter_layout.addWidget(QLabel("Nombres"), 0, 0)
        filter_layout.addWidget(QCheckBox("Todos"), 0, 1)
        filter_layout.addWidget(QCheckBox("A"), 0, 2)
        filter_layout.addWidget(QCheckBox("B"), 0, 3)
        filter_layout.addWidget(QCheckBox("C"), 0, 4)
        filter_layout.addWidget(QCheckBox("D"), 0, 5)
        filter_layout.addWidget(QCheckBox("E"), 0, 6)
        filter_layout.addWidget(QCheckBox("F"), 0, 7)
        filter_layout.addWidget(QCheckBox("G"), 0, 8)
        filter_layout.addWidget(QCheckBox("H"), 0, 9)
        filter_layout.addWidget(QCheckBox("I"), 0, 10)
        filter_layout.addWidget(QCheckBox("J"), 0, 11)
        filter_layout.addWidget(QCheckBox("K"), 0, 12)
        filter_layout.addWidget(QCheckBox("L"), 0, 13)

        filter_layout.addWidget(QCheckBox("M"), 1, 1)
        filter_layout.addWidget(QCheckBox("N"), 1, 2)
        filter_layout.addWidget(QCheckBox("Ñ"), 1, 3)
        filter_layout.addWidget(QCheckBox("O"), 1, 4)
        filter_layout.addWidget(QCheckBox("P"), 1, 5)
        filter_layout.addWidget(QCheckBox("Q"), 1, 6)
        filter_layout.addWidget(QCheckBox("R"), 1, 7)
        filter_layout.addWidget(QCheckBox("S"), 1, 8)
        filter_layout.addWidget(QCheckBox("T"), 1, 9)
        filter_layout.addWidget(QCheckBox("U"), 1, 10)
        filter_layout.addWidget(QCheckBox("V"), 1, 11)
        filter_layout.addWidget(QCheckBox("W"), 1, 12)
        filter_layout.addWidget(QCheckBox("X"), 1, 13)
        filter_layout.addWidget(QCheckBox("Y"), 2, 1)
        filter_layout.addWidget(QCheckBox("Z"), 2, 2)

        # Filtros de apellidos
        filter_layout.addWidget(QLabel("Apellidos"), 3, 0)
        filter_layout.addWidget(QCheckBox("Todos"), 3, 1)
        filter_layout.addWidget(QCheckBox("A"), 3, 2)
        filter_layout.addWidget(QCheckBox("B"), 3, 3)
        filter_layout.addWidget(QCheckBox("C"), 3, 4)
        filter_layout.addWidget(QCheckBox("D"), 3, 5)
        filter_layout.addWidget(QCheckBox("E"), 3, 6)
        filter_layout.addWidget(QCheckBox("F"), 3, 7)
        filter_layout.addWidget(QCheckBox("G"), 3, 8)
        filter_layout.addWidget(QCheckBox("H"), 3, 9)
        filter_layout.addWidget(QCheckBox("I"), 3, 10)
        filter_layout.addWidget(QCheckBox("J"), 3, 11)
        filter_layout.addWidget(QCheckBox("K"), 3, 12)
        filter_layout.addWidget(QCheckBox("L"), 3, 13)

        filter_layout.addWidget(QCheckBox("M"), 4, 1)
        filter_layout.addWidget(QCheckBox("N"), 4, 2)
        filter_layout.addWidget(QCheckBox("Ñ"), 4, 3)
        filter_layout.addWidget(QCheckBox("O"), 4, 4)
        filter_layout.addWidget(QCheckBox("P"), 4, 5)
        filter_layout.addWidget(QCheckBox("Q"), 4, 6)
        filter_layout.addWidget(QCheckBox("R"), 4, 7)
        filter_layout.addWidget(QCheckBox("S"), 4, 8)
        filter_layout.addWidget(QCheckBox("T"), 4, 9)
        filter_layout.addWidget(QCheckBox("U"), 4, 10)
        filter_layout.addWidget(QCheckBox("V"), 4, 11)
        filter_layout.addWidget(QCheckBox("W"), 4, 12)
        filter_layout.addWidget(QCheckBox("X"), 4, 13)
        filter_layout.addWidget(QCheckBox("Y"), 5, 1)
        filter_layout.addWidget(QCheckBox("Z"), 5, 2)

        # Botón de Filtrar
        filter_button = QPushButton("Filtrar")
        filter_button.setFixedHeight(45)
        filter_layout.addWidget(filter_button, 2, 14,2,2)

        main_layout.addLayout(filter_layout)

        # Crear una área de scroll para los estudiantes
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        # Widget contenedor para los estudiantes
        students_container = QWidget()
        students_layout = QVBoxLayout(students_container)

        # Crear las filas de información de estudiantes
        for _ in range(10):  # Aumentado a 10 para demostrar el scroll
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
        self.setWindowTitle("Curso")

    def create_student_info(self):
        # Widget para una fila de información de un estudiante
        student_widget = QWidget()
        layout = QHBoxLayout()

        # Imagen de perfil
        image_label = QLabel()
        pixmap = QPixmap("icon/user-48.ico")  # Ruta a la imagen
        image_label.setPixmap(pixmap)
        image_label.setScaledContents(True)
        image_label.setFixedSize(120, 120)  # Ajustar el tamaño de la imagen

        # Layout para la información de texto
        text_layout = QVBoxLayout()
        spacer = QSpacerItem(150, 0, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

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

        # Añadir widgets al layout principal de la fila
        layout.addWidget(image_label)
        layout.addItem(spacer) 
        layout.addLayout(text_layout)

        student_widget.setLayout(layout)

        return student_widget

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StudentsListWidget()
    window.show()
    sys.exit(app.exec())
