"""Listing 6-8 to Listing 6-11
Written by Joshua Willman
Featured in "Beginning PyQt - A Hands-on Approach to GUI Programming, 2nd Ed."
"""

# Import necessary modules
import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, 
    QRadioButton, QGroupBox, QLineEdit, QTabWidget, 
    QHBoxLayout, QVBoxLayout)
from students_list_gui import StudentsListWidget
from attendance_gui import AttendanceWidget
from dashboard_gui import DashboardWidget
class MenuTabsWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.initializeUI() 

    def initializeUI(self):
        """Set up the application's GUI."""
        self.setMinimumSize(600, 600)
        self.setWindowTitle("Containers Example")

        self.setUpMainWindow()
        

    def setUpMainWindow(self):
        """Create and arrange widgets in the main window.
        Set up tab bar and different tab widgets."""
        # Create tab bar and different page containers
        tab_bar = QTabWidget(self)
        #self.students_list_tab = QWidget()
        self.students_list_tab=StudentsListWidget()
        self.attendance_tab = AttendanceWidget()
        self.dashboard_tab=DashboardWidget()

        tab_bar.addTab(self.students_list_tab, "Alumnos")
        tab_bar.addTab(self.attendance_tab, "Asistencia")
        tab_bar.addTab(self.dashboard_tab,"Dashboard")
       

        # Create the layout for main window
        main_h_box = QHBoxLayout()
        main_h_box.addWidget(tab_bar)
        self.setLayout(main_h_box)

       

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MenuTabsWidget()
    sys.exit(app.exec())