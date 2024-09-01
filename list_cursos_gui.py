"""Listing 10-1 to Listing 10-4
Written by Joshua Willman
Featured in "Beginning PyQt - A Hands-on Approach to GUI Programming, 2nd Ed."
"""

# Import necessary modules
import sys
from PyQt6.QtWidgets import (QApplication, QWidget, 
    QPushButton, QListWidget, QListWidgetItem, QInputDialog,QLabel,
    QHBoxLayout, QVBoxLayout,QMessageBox,
    QStackedWidget)
from menu_tabs_gui import MenuTabsWidget
class ListCoursesWidget(QWidget):
    def __init__(self,stackedWidget:QStackedWidget):
        super().__init__()
        self.stackedWidget=stackedWidget
        self.initializeUI()

    def initializeUI(self):
        """Set up the application's GUI."""
        self.setFixedWidth(600)
        self.setWindowTitle("QListWidget Example")

        self.setUpMainWindow()
        # self.show()

    def setUpMainWindow(self):
        """Create and arrange widgets in the main window."""
        
        listCoursesLayout=QVBoxLayout()
        # listCoursesLayout.setContentsMargins(0, 0, 0, 0)
        listCoursesLayout.setSpacing(0)
        # for i in range(2):
        #     list_widget=QListWidget()
        #     list_widget.setAlternatingRowColors(True)
        #     self.list_listwidget.append(list_widget)
        # Initialize the QListWidget with items 
        list_courses_1= ["Nombre curso 1", "Nombre curso 2", "Nombre curso 3", "Nombre curso 4",
                         ]
        list_courses_2= ["Nombre curso 1", "Nombre curso 2", "Nombre curso 3", "Nombre curso 4",
                         ]
        nombre_periodo_list = ["5to Secundaria-2024", "4to Secundaria - 2024" ]

        courses_dict = {}

        # Asignar los cursos de list_courses_1 al primer período
        courses_dict[nombre_periodo_list[0]] = list_courses_1
        courses_dict[nombre_periodo_list[1]] = list_courses_2
            
        self.list_listwidget=[]

        for periodo,cursos in courses_dict.items():
            label=QLabel(periodo)
            listCoursesLayout.addWidget(label)
            list_widget=QListWidget()
            # list_widget.setAlternatingRowColors(True)
            list_widget.itemClicked.connect(self.on_item_clicked)
            self.list_listwidget.append(list_widget)

            
            for curso in cursos:
                list_item=QListWidgetItem(curso)
                list_widget.addItem(list_item)
           
            # total_height = list_widget.sizeHintForRow(0) * list_widget.count() + 2 * list_widget.frameWidth()
            
            listCoursesLayout.addWidget(list_widget)
            
                

        self.setLayout(listCoursesLayout)
        
    
    def on_item_clicked(self, item):
        menu_tabs_widget=MenuTabsWidget()
        self.stackedWidget.addWidget(menu_tabs_widget)
        self.stackedWidget.setCurrentWidget(menu_tabs_widget)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ListCoursesWidget()
    sys.exit(app.exec())