import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt6.QtCore import  QFile , QTextStream
from sidebar_ui import UI_MainWindow

evalua = True
tipo = "administrador"
class MainWindow(QMainWindow):
    def __init__(self, evalua, tipo): # evalua, tipo
        super(MainWindow, self).__init__()
        self.ui = UI_MainWindow()
        self.ui.initializeUI(self)
        self.ui.sideBarIconsMenuWidget.hide()
        self.ui.init_menu_frames()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    style_file = QFile("style.qss")
    style_file.open(QFile.OpenModeFlag.ReadOnly | QFile.OpenModeFlag.Text)
    style_stream = QTextStream(style_file)
    app.setStyleSheet(style_stream.readAll())

    window = MainWindow(evalua, tipo)
    window.show()
    sys.exit(app.exec())
