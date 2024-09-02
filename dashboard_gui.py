from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QGridLayout, QFrame
)
from PyQt6.QtCore import Qt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np
import pandas as pd
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
        group_name_frame = self.create_frame_with_chart("Porcentaje de Asistencia por alumno", "Selecciona Alumno", ["Opción 1", "Opción 2"], self.create_pie_chart())
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

        layout.addStretch()
        frame.setLayout(layout)
        return frame

    def create_line_chart(self):
        figure = Figure(figsize=(3, 2))
        canvas = FigureCanvas(figure)
        data = {'Fecha': ['Enero-S01', 'Enero-S02', 'Enero-S03', 'Enero-S04', 'Enero-S05'],
        'Ausencias': [1, 1,3, 2, 4 ]}
        df = pd.DataFrame(data)
        ax = figure.add_subplot(111)
        
        x = df['Fecha']
        y=df['Ausencias']
       

        ax.plot(x,y, label="Numero de Ausencias", color='skyblue', linewidth=2, alpha=0.6)
        # ax.plot(x, y2, label="Semana", color='black', linewidth=2)
        ax.set_title("Tendencias de Ausentismo")
        ax.legend()

        return canvas

    def create_bar_chart(self):
        figure = Figure(figsize=(3, 2))
        canvas = FigureCanvas(figure)
        ax = figure.add_subplot(111)

        # Datos de ejemplo
        data = {'Fecha': ['2024-08-01', '2024-08-02', '2024-08-03', '2024-08-04', '2024-08-05',
                        '2024-08-01', '2024-08-07', '2024-08-08', '2024-08-09', '2024-08-10',
                        '2024-08-11', '2024-08-11', '2024-08-12', '2024-08-12']}

        df = pd.DataFrame(data)
        df['Fecha'] = pd.to_datetime(df['Fecha'])

        # Crear la columna 'Día de la Semana' basada en 'Fecha'
        df['Día de la Semana'] = df['Fecha'].dt.day_name()

        # Mapeo de nombres completos a siglas
        day_abbr = {
        'Monday': 'Lun',
        'Tuesday': 'Mar',
        'Wednesday': 'Mié',
        'Thursday': 'Jue',
        'Friday': 'Vie',
        'Saturday': 'Sáb',
        'Sunday': 'Dom'
     }

        # Contar el número de tardanzas por día de la semana
        conteo_tardanzas = df['Día de la Semana'].map(day_abbr).value_counts().reindex(['Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb', 'Dom'], fill_value=0)

        # Crear gráfico de barras
        ax.bar(conteo_tardanzas.index, conteo_tardanzas.values, color='skyblue')
        ax.set_ylabel('Número de Tardanzas')
        ax.set_xlabel('Día de la Semana')
        ax.set_title('Patrón de Tardanza Mensual según Día de la Semana')

        return canvas

    def create_pie_chart(self):
        figure = Figure(figsize=(3, 2))
        canvas = FigureCanvas(figure)
        ax = figure.add_subplot(111)

        sizes = [20, 30, 50]
        labels = ['Parte A', 'Parte B', 'Parte C']
        ax.pie(sizes, labels=labels, colors=['#6699CC', '#336699', '#99CCFF'], startangle=90, autopct='%1.1f%%')
        ax.set_title("Distribución de Grupo")

        return canvas


