from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QGridLayout, QFrame
)
from PyQt6.QtCore import Qt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np

class DashboardWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Layout principal
        main_layout = QGridLayout()

        # Sección de Asistencia Mensual
        monthly_attendance_frame = self.create_frame("Asistencia Mensual", "Selecciona Mes", ["Enero", "Febrero", "Marzo"])
        main_layout.addWidget(monthly_attendance_frame, 0, 0)

        # Sección de Group Name (gráfico de pastel)
        group_name_frame = self.create_frame_with_chart("Group Name", "Selecciona Opción", ["Opción 1", "Opción 2"], self.create_pie_chart())
        main_layout.addWidget(group_name_frame, 0, 1)

        # Sección de Tendencia de Ausentismo
        absenteeism_trend_frame = self.create_frame_with_chart("Tendencia de ausentismo", "Selecciona Alumno", ["Apaza Peralta, Manuel"], self.create_line_chart())
        main_layout.addWidget(absenteeism_trend_frame, 1, 0)

        # Sección de Patrones de Tardanza
        tardiness_pattern_frame = self.create_frame_with_chart("Patrones de tardanza", "Selecciona Alumno", ["Apaza Peralta, Manuel"], self.create_bar_chart())
        main_layout.addWidget(tardiness_pattern_frame, 1, 1)

        self.setLayout(main_layout)

    def create_frame(self, title, label_text, combo_options):
        frame = QFrame()
        frame.setFrameShape(QFrame.Shape.Box)
        frame.setLineWidth(2)

        layout = QVBoxLayout()

        title_label = QLabel(title)
        title_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(title_label)

        select_layout = QHBoxLayout()
        select_label = QLabel(label_text)
        combo_box = QComboBox()
        combo_box.addItems(combo_options)
        select_layout.addWidget(select_label)
        select_layout.addWidget(combo_box)
        layout.addLayout(select_layout)

        layout.addStretch()
        frame.setLayout(layout)
        return frame

    def create_frame_with_chart(self, title, label_text, combo_options, chart_widget):
        frame = QFrame()
        frame.setFrameShape(QFrame.Shape.Box)
        frame.setLineWidth(2)

        layout = QVBoxLayout()

        title_label = QLabel(title)
        title_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(title_label)

        select_layout = QHBoxLayout()
        select_label = QLabel(label_text)
        combo_box = QComboBox()
        combo_box.addItems(combo_options)
        select_layout.addWidget(select_label)
        select_layout.addWidget(combo_box)
        layout.addLayout(select_layout)

        layout.addWidget(chart_widget)
        frame.setLayout(layout)
        return frame

    def create_line_chart(self):
        figure = Figure(figsize=(3, 2))
        canvas = FigureCanvas(figure)
        ax = figure.add_subplot(111)
        
        x = np.arange(1, 11)
        y1 = np.random.randint(1, 10, 10)
        y2 = np.random.randint(1, 10, 10)

        ax.plot(x, y1, label="Año anterior", color='gray', linewidth=2, alpha=0.6)
        ax.plot(x, y2, label="Este año", color='black', linewidth=2)
        ax.set_title("Tendencias de Ausentismo")
        ax.legend()

        return canvas

    def create_bar_chart(self):
        figure = Figure(figsize=(3, 2))
        canvas = FigureCanvas(figure)
        ax = figure.add_subplot(111)

        categories = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo']
        values1 = np.random.randint(1, 10, len(categories))
        values2 = np.random.randint(1, 10, len(categories))

        bar_width = 0.35
        index = np.arange(len(categories))
        ax.bar(index, values1, bar_width, label='Año anterior', color='gray', alpha=0.6)
        ax.bar(index + bar_width, values2, bar_width, label='Este año', color='black')
        ax.set_xlabel('Mes')
        ax.set_ylabel('Cantidad')
        ax.set_title('Patrones de Tardanza')
        ax.set_xticks(index + bar_width / 2)
        ax.set_xticklabels(categories)
        ax.legend()

        return canvas

    def create_pie_chart(self):
        figure = Figure(figsize=(3, 2))
        canvas = FigureCanvas(figure)
        ax = figure.add_subplot(111)

        sizes = [20, 30, 50]
        labels = ['Parte A', 'Parte B', 'Parte C']
        ax.pie(sizes, labels=labels, colors=['gray', 'darkgray', 'lightgray'], startangle=90, autopct='%1.1f%%')
        ax.set_title("Distribución de Grupo")

        return canvas

# Ejecución de la aplicación
app = QApplication([])
window = DashboardWidget()
window.show()
app.exec()
