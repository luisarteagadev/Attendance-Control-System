
import sys
from PyQt6.QtWidgets import (QApplication,QMainWindow,QWidget,
QLabel, QGridLayout,QVBoxLayout , QHBoxLayout, QPushButton,QSpacerItem, QSizePolicy,
QStackedWidget, QMenu, QFrame,QDialog

)

from PyQt6.QtCore import  QFile , QTextStream,QSize, Qt
from PyQt6.QtGui import QPixmap, QIcon, QFont, QAction

from list_cursos_gui import ListCoursesWidget
from mant_clases_gui import MantClasesWidget
from mant_usuarios_gui import MantUsuariosWidget
from config_diaglo_gui import ConfigDialog
class UI_MainWindow(object):
    # def __init__(self):
    #     super().__init__()
    #     self.initializeUI()

    def initializeUI(self, MainWindow: QMainWindow):
       
        # MainWindow.resize(950, 600)
        
        MainWindow.setObjectName("MainWindow")
        self.centralwidget = QWidget(MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)
        

        #---SETUP sideBarIconsMenuWidget
        self.sideBarIconsMenuWidget=QWidget(self.centralwidget)
        self.sideBarIconsMenuWidget.setObjectName("sideBarIconsMenuWidget")

        self.sideBarIconsMenuLayout=QVBoxLayout(self.sideBarIconsMenuWidget)
        self.sideBarIconsMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.sideBarIconsMenuLayout.setSpacing(5)

        self.headerIconsMenuLayout=QHBoxLayout()
        self.logoLabel1=QLabel(self.sideBarIconsMenuWidget)
        self.logoLabel1.setMinimumSize(QSize(35,35))
        self.logoLabel1.setMaximumSize(QSize(35,35))
        self.logoLabel1.setText("")
        self.logoLabel1.setPixmap(QPixmap(":/icon/icon/Logo.png"))
        self.logoLabel1.setScaledContents(True)
        self.headerIconsMenuLayout.addWidget(self.logoLabel1)


        self.bodyIconsMenuLayout=QVBoxLayout()


        self.bodyIconsMenuLayout.setSpacing(0)

        # self.studentsButton1=QPushButton(self.sideBarIconsMenuWidget)
        # self.studentsButton1.setText("")
        # icon = QIcon()
        # icon.addPixmap(QPixmap(":/icon/icon/home-4-32.ico"), QIcon.Mode.Normal, QIcon.State.Off)
        # icon.addPixmap(QPixmap(":/icon/icon/home-4-48.ico"), QIcon.Mode.Normal, QIcon.State.On)
        # self.studentsButton1.setIcon(icon)
        # self.studentsButton1.setIconSize(QSize(20,20))
        # self.studentsButton1.setCheckable(True)
        # self.studentsButton1.setAutoExclusive(True)

        self.studentsButton1= self.studentsUI_1()

        icon = QIcon()
        icon.addPixmap(QPixmap(":/icon/icon/group-32.ico"), QIcon.Mode.Normal, QIcon.State.Off)
        icon.addPixmap(QPixmap(":/icon/icon/group-48.ico"), QIcon.Mode.Normal, QIcon.State.On)
        self.bodyIconsMenuLayout.addWidget(self.studentsButton1)

        self.dashboradButton1 = QPushButton(self.sideBarIconsMenuWidget)
        self.dashboradButton1.setText("")
        icon1 = QIcon()
        icon1.addPixmap(QPixmap(":/icon/icon/group-32.ico"), QIcon.Mode.Normal, QIcon.State.Off)
        icon1.addPixmap(QPixmap(":/icon/icon/group-48.ico"), QIcon.Mode.Normal, QIcon.State.On)
        self.dashboradButton1.setIcon(icon1)
        self.dashboradButton1.setIconSize(QSize(20, 20))
        self.dashboradButton1.setCheckable(True)
        self.dashboradButton1.setAutoExclusive(True)
        self.bodyIconsMenuLayout.addWidget(self.dashboradButton1)
        
        self.ordersButton1 = QPushButton(self.sideBarIconsMenuWidget)
        self.ordersButton1.setText("")
        icon2 = QIcon()
        icon2.addPixmap(QPixmap(":/icon/icon/activity-feed-32.ico"), QIcon.Mode.Normal, QIcon.State.Off)
        icon2.addPixmap(QPixmap(":/icon/icon/activity-feed-48.ico"), QIcon.Mode.Normal, QIcon.State.On)
        self.ordersButton1.setIcon(icon2)
        self.ordersButton1.setIconSize(QSize(20, 20))
        self.ordersButton1.setCheckable(True)
        self.ordersButton1.setAutoExclusive(True)
        self.bodyIconsMenuLayout.addWidget(self.ordersButton1)

        # self.productsButton1 = QPushButton(self.sideBarIconsMenuWidget)
        # self.productsButton1.setText("")
        # icon3 = QIcon()
        # icon3.addPixmap(QPixmap(":/icon/icon/product-32.ico"), QIcon.Mode.Normal, QIcon.State.Off)
        # icon3.addPixmap(QPixmap(":/icon/icon/product-48.ico"), QIcon.Mode.Normal, QIcon.State.On)
        # self.productsButton1.setIcon(icon3)
        # self.productsButton1.setIconSize(QSize(20, 20))
        # self.productsButton1.setCheckable(True)
        # self.productsButton1.setAutoExclusive(True)
        # self.productsButton1.setObjectName("productsButton1")
        # self.bodyIconsMenuLayout.addWidget(self.productsButton1)

        # self.customersButton1 = QPushButton(self.sideBarIconsMenuWidget)
        # self.customersButton1.setText("")
        # icon4 = QIcon()
        # icon4.addPixmap(QPixmap(":/icon/icon/group-32.ico"), QIcon.Mode.Normal, QIcon.State.Off)
        # icon4.addPixmap(QPixmap(":/icon/icon/group-48.ico"), QIcon.Mode.Normal, QIcon.State.On)
        # self.customersButton1.setIcon(icon4)
        # self.customersButton1.setIconSize(QSize(20, 20))
        # self.customersButton1.setCheckable(True)
        # self.customersButton1.setAutoExclusive(True)
        # self.customersButton1.setObjectName("customersButton1")
        # self.bodyIconsMenuLayout.addWidget(self.customersButton1)
        
        spacerItem = QSpacerItem(20, 375, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        
        self.exitButton1 = QPushButton(self.sideBarIconsMenuWidget)
        self.exitButton1.setText("")
        icon5 =QIcon()
        icon5.addPixmap(QPixmap(":/icon/icon/close-window-64.ico"), QIcon.Mode.Normal, QIcon.State.Off)
        self.exitButton1.setIcon(icon5)
        self.exitButton1.setIconSize(QSize(20, 20))

        self.sideBarIconsMenuWidget.setFixedWidth(50)
        self.sideBarIconsMenuLayout.addLayout(self.headerIconsMenuLayout)
        self.sideBarIconsMenuLayout.addLayout(self.bodyIconsMenuLayout)
        self.sideBarIconsMenuLayout.addItem(spacerItem)
        self.sideBarIconsMenuLayout.addWidget(self.exitButton1)

        #---END SETUP sideBarIconsMenuWidget---

        #---SETUP sideBarFullWidget
        self.siderBarFullMenuWidget=QWidget(self.centralwidget)
        self.siderBarFullMenuWidget.setObjectName("siderBarFullMenuWidget")
        
        self.siderBarFullMenuLayout = QVBoxLayout(self.siderBarFullMenuWidget)
        self.headerFullMenuLayout = QHBoxLayout()
        self.headerFullMenuLayout.setSpacing(0)

        self.logoLabel2 = QLabel(self.siderBarFullMenuWidget)
        self.logoLabel2.setMinimumSize(QSize(35, 35))
        self.logoLabel2.setMaximumSize(QSize(35, 35))
        self.logoLabel2.setText("")
        self.logoLabel2.setPixmap(QPixmap(":/icon/icon/Logo.png"))
        self.logoLabel2.setScaledContents(True)
        self.headerFullMenuLayout.addWidget(self.logoLabel2)


        self.logoLabel3 = QLabel(self.siderBarFullMenuWidget)
        font = QFont()
        font.setPointSize(15)
        self.logoLabel3.setFont(font)
        self.logoLabel3.setText("Esan School")
        self.headerFullMenuLayout.addWidget(self.logoLabel3)

        

        self.bodyFullMenuLayout = QVBoxLayout()
        self.bodyFullMenuLayout.setSpacing(0)
        
    #---Intializing UI Elements---
        self.studentsUI_2()
        self.teachersUI_2()
        self.coursesUI_2()
    #---END Intializing UI Elements
        self.bodyFullMenuLayout.addWidget(self.studentsFrame)
        self.bodyFullMenuLayout.addWidget(self.teachers_frame)
        self.bodyFullMenuLayout.addWidget(self.courses_frame)
        # self.dashboradButton2 = QPushButton(self.siderBarFullMenuWidget)
        # self.dashboradButton2.setIcon(icon1)
        # self.dashboradButton2.setIconSize(QSize(14, 14))
        # self.dashboradButton2.setCheckable(True)
        # self.dashboradButton2.setAutoExclusive(True)
        # self.bodyFullMenuLayout.addWidget(self.dashboradButton2)


        # self.ordersButton2 = QPushButton(self.siderBarFullMenuWidget)
        # self.ordersButton2.setIcon(icon2)
        # self.ordersButton2.setIconSize(QSize(14, 14))
        # self.ordersButton2.setCheckable(True)
        # self.ordersButton2.setAutoExclusive(True)
        # self.bodyFullMenuLayout.addWidget(self.ordersButton2)

        # self.productsButton2 = QPushButton(self.siderBarFullMenuWidget)
        # self.productsButton2.setIcon(icon3)
        # self.productsButton2.setIconSize(QSize(14, 14))
        # self.productsButton2.setCheckable(True)
        # self.productsButton2.setAutoExclusive(True)
        # self.bodyFullMenuLayout.addWidget(self.productsButton2)


        # self.customersButton2 = QPushButton(self.siderBarFullMenuWidget)
        # self.customersButton2.setIcon(icon4)
        # self.customersButton2.setIconSize(QSize(14, 14))
        # self.customersButton2.setCheckable(True)
        # self.customersButton2.setAutoExclusive(True)
        # self.bodyFullMenuLayout.addWidget(self.customersButton2)

        
        spacerItem2 = QSpacerItem(20, 373, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        
        self.exitButton2 = QPushButton(self.siderBarFullMenuWidget)
        self.exitButton2.setIcon(icon5)
        self.exitButton2.setIconSize(QSize(14, 14))

        self.siderBarFullMenuWidget.setFixedWidth(200)
        self.siderBarFullMenuLayout.addLayout(self.headerFullMenuLayout)
        self.siderBarFullMenuLayout.addLayout(self.bodyFullMenuLayout)
        self.siderBarFullMenuLayout.addItem(spacerItem2)
        self.siderBarFullMenuLayout.addWidget(self.exitButton2)


        #---END SETUP sideBarFullWidget---

        #---SETUP MainContentArea
        self.mainContentAreaWidget=QWidget(self.centralwidget)
        self.mainContentAreaWidget.setObjectName("mainContentAreaWidget")

        self.mainContentAreaLayout=QVBoxLayout(self.mainContentAreaWidget)
        self.mainContentAreaLayout.setContentsMargins(0, 0, 0, 0)
        self.mainContentAreaLayout.setSpacing(0)

        self.widget = QWidget(self.mainContentAreaWidget)
        self.widget.setMinimumSize(QSize(0, 40))
        self.widget.setObjectName("widget")

        self.headerMainContentLayout=QHBoxLayout(self.widget)
        self.headerMainContentLayout.setContentsMargins(0, 0, 9, 0)
        self.headerMainContentLayout.setSpacing(0)

        self.change_btn = QPushButton(self.widget)
        self.change_btn.setText("")
        icon6 = QIcon()
        icon6.addPixmap(QPixmap(":/icon/icon/menu-4-32.ico"), QIcon.Mode.Normal, QIcon.State.Off)
        self.change_btn.setIcon(icon6)
        self.change_btn.setIconSize(QSize(14, 14))
        self.change_btn.setCheckable(True)
        self.change_btn.setObjectName("change_btn")
        self.headerMainContentLayout.addWidget(self.change_btn)
        
        spacerItem3 = QSpacerItem(236, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.headerMainContentLayout.addItem(spacerItem3)

        self.config_btn=QPushButton(self.mainContentAreaWidget)
        self.config_btn.setText("")
        icon7 = QIcon()
        icon7.addPixmap(QPixmap(":/icon/icon/gear_icon.ico"), QIcon.Mode.Normal, QIcon.State.Off)
        self.config_btn.setIcon(icon7)
        self.config_btn.setObjectName("config_btn")
        self.config_btn.setIconSize(QSize(24, 24))

        self.headerMainContentLayout.addWidget(self.config_btn)


        self.user_btn = QPushButton(self.mainContentAreaWidget)
        self.user_btn.setText("")
        icon8 = QIcon()
        icon8.addPixmap(QPixmap(":/icon/icon/user-48.ico"), QIcon.Mode.Normal, QIcon.State.Off)
        self.user_btn.setIcon(icon8) 
        self.user_btn.setIconSize(QSize(24, 24))
        self.headerMainContentLayout.addWidget(self.user_btn)

        self.stackedWidget=QStackedWidget(self.mainContentAreaWidget)

    #---Initializing WidgetsUI to StackedWidget---
        self.register_students_UI()
        self.mant_clases_UI()
        self.mant_usuarios_UI()
        self.list_courses_UI()
        # self.list_students_UI()
        # self.dashboard_students_UI()
    #---END WidgetsUI to StackedWidget
        self.stackedWidget.addWidget(self.registerStudentWidget)
        self.stackedWidget.addWidget(self.mant_clases_widget)
        self.stackedWidget.addWidget(self.mant_usuarios_widget)
        self.stackedWidget.addWidget(self.list_courses_widget)

        # self.stackedWidget.addWidget(self.listStudentsWidget)
        # self.stackedWidget.addWidget(self.dashboardStudentsWidget)

     

        self.stackedWidget.setCurrentIndex(0)


        self.mainContentAreaLayout.addWidget(self.widget)
        self.mainContentAreaLayout.addWidget(self.stackedWidget)


        self.gridLayout= QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.addWidget(self.sideBarIconsMenuWidget, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.siderBarFullMenuWidget,0,1,1,1)
        self.gridLayout.addWidget(self.mainContentAreaWidget,0,2,1,1)
        
    #---SETUP EVENTS---
        self.change_btn.toggled['bool'].connect(self.sideBarIconsMenuWidget.setVisible)
        self.change_btn.toggled['bool'].connect(self.siderBarFullMenuWidget.setHidden) 
        self.config_btn.clicked.connect(self.show_config_dialog)


        self.menuStudentsButton.clicked.connect(self.toggle_students_menu)
        self.menu_teachers_button.clicked.connect(self.toggle_teachers_menu)
        self.menu_courses_button.clicked.connect(self.toggle_courses_menu)

        self.registerStudentButton.clicked.connect(self.show_page_1)
        self.mant_clases_button.clicked.connect(self.show_page_2)
        self.mant_usuarios_button.clicked.connect(self.show_page_3)
        self.list_courses_button.clicked.connect(self.show_page_4)

    #---END SETUP EVENTS

       
        
    def show_config_dialog(self):
        dialog = ConfigDialog()
        dialog.exec()
        
     

    def studentsUI_1(self):
        studentsButton1=QPushButton(self.sideBarIconsMenuWidget)
        studentsButton1.setText("")
        icon = QIcon()
        icon.addPixmap(QPixmap(":/icon/icon/group-32.ico"), QIcon.Mode.Normal, QIcon.State.Off)
        icon.addPixmap(QPixmap(":/icon/icon/group-48.ico"), QIcon.Mode.Normal, QIcon.State.On)
        studentsButton1.setIcon(icon)
        studentsButton1.setIconSize(QSize(20,20))
        studentsButton1.setCheckable(True)
        studentsButton1.setAutoExclusive(True)

        return studentsButton1
    
   
    def studentsUI_2(self):
        
        self.studentsFrame=QFrame(self.siderBarFullMenuWidget)
        studentsLayout=QVBoxLayout()
        self.studentsFrame.setLayout(studentsLayout)

        self.menuStudentsButton = QPushButton()
        self.menuStudentsButton.setText("Alumnos")
        icon = QIcon()
        icon.addPixmap(QPixmap(":/icon/icon/group-32.ico"), QIcon.Mode.Normal, QIcon.State.Off)
        icon.addPixmap(QPixmap(":/icon/icon/group-48.ico"), QIcon.Mode.Normal, QIcon.State.On)
        self.menuStudentsButton.setIcon(icon)
        self.menuStudentsButton.setIconSize(QSize(14, 14))
        self.menuStudentsButton.setCheckable(True)
        self.menuStudentsButton.setAutoExclusive(True)  
        studentsLayout.addWidget(self.menuStudentsButton)
        
        
        self.studentsMenuFrame=QFrame(self.studentsFrame)
        studentsMenuLayout=QVBoxLayout()
        self.studentsMenuFrame.setLayout(studentsMenuLayout)
        
        self.registerStudentButton = QPushButton()
        self.registerStudentButton.setText("Registrar Alumno")
        # icon = QIcon()
        # icon.addPixmap(QPixmap(":/icon/icon/home-4-32.ico"), QIcon.Mode.Normal, QIcon.State.Off)
        # icon.addPixmap(QPixmap(":/icon/icon/home-4-48.ico"), QIcon.Mode.Normal, QIcon.State.On)
        # self.registerStudentButton.setIcon(icon)
        # self.registerStudentButton.setIconSize(QSize(14, 14))
        self.registerStudentButton.setCheckable(True)
        self.registerStudentButton.setAutoExclusive(True)  
        studentsMenuLayout.addWidget(self.registerStudentButton)

        self.listStudentButton = QPushButton()
        self.listStudentButton.setText("Lista Alumnos")
        # icon = QIcon()
        # icon.addPixmap(QPixmap(":/icon/icon/home-4-32.ico"), QIcon.Mode.Normal, QIcon.State.Off)
        # icon.addPixmap(QPixmap(":/icon/icon/home-4-48.ico"), QIcon.Mode.Normal, QIcon.State.On)
        # self.listStudentButton.setIcon(icon)
        # self.listStudentButton.setIconSize(QSize(14, 14))
        self.listStudentButton.setCheckable(True)
        self.listStudentButton.setAutoExclusive(True)  
        # studentsMenuLayout.addWidget(self.listStudentButton)

        self.dashboardStudentButton = QPushButton()
        self.dashboardStudentButton.setText("Dashboard")
        # icon = QIcon()
        # icon.addPixmap(QPixmap(":/icon/icon/home-4-32.ico"), QIcon.Mode.Normal, QIcon.State.Off)
        # icon.addPixmap(QPixmap(":/icon/icon/home-4-48.ico"), QIcon.Mode.Normal, QIcon.State.On)
        # self.dashboardStudentButton.setIcon(icon)
        self.dashboardStudentButton.setIconSize(QSize(14, 14))
        self.dashboardStudentButton.setCheckable(True)
        self.dashboardStudentButton.setAutoExclusive(True)  
        # studentsMenuLayout.addWidget(self.dashboardStudentButton)

        studentsLayout.addWidget(self.studentsMenuFrame)

    
    def register_students_UI(self):
        self.registerStudentWidget= QWidget()
        # Crear un QLabel para el título
        title_label = QLabel("Registrar Alumno")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Centrar el texto

        # Crear un layout vertical y agregar el título
        layout = QVBoxLayout()
        layout.addWidget(title_label)

        # Asignar el layout al widget
        self.registerStudentWidget.setLayout(layout)

    def list_students_UI(self):
        self.listStudentsWidget= QWidget()
        # Crear un QLabel para el título
        title_label = QLabel("Lista Alumnos")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Centrar el texto

        # Crear un layout vertical y agregar el título
        layout = QVBoxLayout()
        layout.addWidget(title_label)

        # Asignar el layout al widget
        self.listStudentsWidget.setLayout(layout)
    
    def dashboard_students_UI(self):
        self.dashboardStudentsWidget= QWidget()
        # Crear un QLabel para el título
        title_label = QLabel("Dashboard Alumnos")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Centrar el texto

        # Crear un layout vertical y agregar el título
        layout = QVBoxLayout()
        layout.addWidget(title_label)

        # Asignar el layout al widget
        self.dashboardStudentsWidget.setLayout(layout)
        
    def teachersUI_2(self):
        
        self.teachers_frame=QFrame(self.siderBarFullMenuWidget)
        teachersLayout=QVBoxLayout()
        self.teachers_frame.setLayout(teachersLayout)

        self.menu_teachers_button = QPushButton()
        self.menu_teachers_button.setText("Administrador")
        icon = QIcon()
        icon.addPixmap(QPixmap(":/icon/icon/group-32.ico"), QIcon.Mode.Normal, QIcon.State.Off)
        icon.addPixmap(QPixmap(":/icon/icon/group-48.ico"), QIcon.Mode.Normal, QIcon.State.On)
        self.menu_teachers_button.setIcon(icon)
        self.menu_teachers_button.setIconSize(QSize(14, 14))
        self.menu_teachers_button.setCheckable(True)
        self.menu_teachers_button.setAutoExclusive(True)  
        teachersLayout.addWidget(self.menu_teachers_button)
        
        
        self.teachers_menu_frame=QFrame(self.teachers_frame)
        teachersMenuLayout=QVBoxLayout()
        self.teachers_menu_frame.setLayout(teachersMenuLayout)
        
        self.mant_clases_button = QPushButton()
        self.mant_clases_button.setText("Mant. Clases")
        self.mant_clases_button.setCheckable(True)
        self.mant_clases_button.setAutoExclusive(True)  
        teachersMenuLayout.addWidget(self.mant_clases_button)

        self.mant_usuarios_button = QPushButton()
        self.mant_usuarios_button.setText("Mant. Usuarios")
        self.mant_usuarios_button.setCheckable(True)
        self.mant_usuarios_button.setAutoExclusive(True) 
        teachersMenuLayout.addWidget(self.mant_usuarios_button)

        # self.listStudentButton = QPushButton()
        # self.listStudentButton.setText("Lista Alumnos")
        # icon = QIcon()
        # icon.addPixmap(QPixmap(":/icon/icon/home-4-32.ico"), QIcon.Mode.Normal, QIcon.State.Off)
        # icon.addPixmap(QPixmap(":/icon/icon/home-4-48.ico"), QIcon.Mode.Normal, QIcon.State.On)
        # self.listStudentButton.setIcon(icon)
        # self.listStudentButton.setIconSize(QSize(14, 14))
        self.listStudentButton.setCheckable(True)
        self.listStudentButton.setAutoExclusive(True)  
        # studentsMenuLayout.addWidget(self.listStudentButton)

        # self.dashboardStudentButton = QPushButton()
        # self.dashboardStudentButton.setText("Dashboard")
        # icon = QIcon()
        # icon.addPixmap(QPixmap(":/icon/icon/home-4-32.ico"), QIcon.Mode.Normal, QIcon.State.Off)
        # icon.addPixmap(QPixmap(":/icon/icon/home-4-48.ico"), QIcon.Mode.Normal, QIcon.State.On)
        # self.dashboardStudentButton.setIcon(icon)
        # self.dashboardStudentButton.setIconSize(QSize(14, 14))
        # self.dashboardStudentButton.setCheckable(True)
        # self.dashboardStudentButton.setAutoExclusive(True)  
        # studentsMenuLayout.addWidget(self.dashboardStudentButton)

        teachersLayout.addWidget(self.teachers_menu_frame)  
    
    def mant_clases_UI(self):
        self.mant_clases_widget= MantClasesWidget()

    def mant_usuarios_UI(self):
        self.mant_usuarios_widget=MantUsuariosWidget()

    def coursesUI_2(self):
        
        self.courses_frame=QFrame(self.siderBarFullMenuWidget)
        coursesLayout=QVBoxLayout()
        self.courses_frame.setLayout(coursesLayout)

        self.menu_courses_button = QPushButton()
        self.menu_courses_button.setText("Cursos")
        icon = QIcon()
        icon.addPixmap(QPixmap(":/icon/icon/activity-feed-32.ico"), QIcon.Mode.Normal, QIcon.State.Off)
        icon.addPixmap(QPixmap(":/icon/icon/activity-feed-48.ico"), QIcon.Mode.Normal, QIcon.State.On)
        self.menu_courses_button.setIcon(icon)
        self.menu_courses_button.setIconSize(QSize(14, 14))
        self.menu_courses_button.setCheckable(True)
        self.menu_courses_button.setAutoExclusive(True)  
        coursesLayout.addWidget(self.menu_courses_button)
        
        
        self.courses_menu_frame=QFrame(self.courses_frame)
        coursesMenuLayout=QVBoxLayout()
        self.courses_menu_frame.setLayout(coursesMenuLayout)
        
        self.list_courses_button = QPushButton()
        self.list_courses_button.setText("Lista Cursos")
        self.list_courses_button.setCheckable(True)
        self.list_courses_button.setAutoExclusive(True)  
        coursesMenuLayout.addWidget(self.list_courses_button)

        coursesLayout.addWidget(self.courses_menu_frame)


    def list_courses_UI(self):
        self.list_courses_widget=ListCoursesWidget(self.stackedWidget)
       
    

    def toggle_students_menu(self):
        self.studentsMenuFrame.setVisible(not self.studentsMenuFrame.isVisible())
    
    def toggle_teachers_menu(self):
        self.teachers_menu_frame.setVisible(not self.teachers_menu_frame.isVisible())
    def toggle_courses_menu(self):
        self.courses_menu_frame.setVisible(not self.courses_menu_frame.isVisible())

    

    def init_menu_frames(self):
        self.studentsMenuFrame.setVisible(False)
        self.teachers_menu_frame.setVisible(False)
        self.courses_menu_frame.setVisible(False)
    def show_page_1(self):
        self.stackedWidget.setCurrentIndex(0)
    def show_page_2(self):
        self.stackedWidget.setCurrentIndex(1)
    def show_page_3(self):
        self.stackedWidget.setCurrentIndex(2)
    def show_page_4(self):
        self.stackedWidget.setCurrentIndex(3)
import resource_rc