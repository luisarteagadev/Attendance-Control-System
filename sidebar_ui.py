
import sys
from PyQt6.QtWidgets import (QApplication,QMainWindow,QWidget,
QLabel, QGridLayout,QVBoxLayout , QHBoxLayout, QPushButton,QSpacerItem, QSizePolicy,
QStackedWidget

)

from PyQt6.QtCore import  QFile , QTextStream,QSize, Qt
from PyQt6.QtGui import QPixmap, QIcon, QFont

class UI_MainWindow(object):
    # def __init__(self):
    #     super().__init__()
    #     self.initializeUI()

    def initializeUI(self, MainWindow: QMainWindow):
       
        MainWindow.resize(950, 600)
        MainWindow.setObjectName("MainWindow")
        self.centralwidget = QWidget(MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)
        

        #---SETUP sideBarIconsMenuWidget
        self.sideBarIconsMenuWidget=QWidget(self.centralwidget)
        self.sideBarIconsMenuWidget.setObjectName("sideBarIconsMenuWidget")

        self.sideBarIconsMenuLayout=QVBoxLayout(self.sideBarIconsMenuWidget)
        self.sideBarIconsMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.sideBarIconsMenuLayout.setSpacing(0)

        self.headerIconsMenuLayout=QHBoxLayout()
        self.logoLabel1=QLabel(self.sideBarIconsMenuWidget)
        self.logoLabel1.setMinimumSize(QSize(50,50))
        self.logoLabel1.setMaximumSize(QSize(50,50))
        self.logoLabel1.setText("")
        self.logoLabel1.setPixmap(QPixmap(":/icon/icon/Logo.png"))
        self.logoLabel1.setScaledContents(True)
        self.headerIconsMenuLayout.addWidget(self.logoLabel1)

        self.bodyIconsMenuLayout=QVBoxLayout()
        self.bodyIconsMenuLayout.setSpacing(0)
        self.homeButton1=QPushButton(self.sideBarIconsMenuWidget)
        self.homeButton1.setText("")
        icon = QIcon()
        icon.addPixmap(QPixmap(":/icon/icon/home-4-32.ico"), QIcon.Mode.Normal, QIcon.State.Off)
        icon.addPixmap(QPixmap(":/icon/icon/home-4-48.ico"), QIcon.Mode.Normal, QIcon.State.On)
        self.homeButton1.setIcon(icon)
        self.homeButton1.setIconSize(QSize(20,20))
        self.homeButton1.setCheckable(True)
        self.homeButton1.setAutoExclusive(True)
        self.bodyIconsMenuLayout.addWidget(self.homeButton1)

        self.dashboradButton1 = QPushButton(self.sideBarIconsMenuWidget)
        self.dashboradButton1.setText("")
        icon1 = QIcon()
        icon1.addPixmap(QPixmap(":/icon/icon/dashboard-5-32.ico"), QIcon.Mode.Normal, QIcon.State.Off)
        icon1.addPixmap(QPixmap(":/icon/icon/dashboard-5-48.ico"), QIcon.Mode.Normal, QIcon.State.On)
        self.dashboradButton1.setIcon(icon1)
        self.dashboradButton1.setIconSize(QSize(20, 20))
        self.dashboradButton1.setCheckable(True)
        self.dashboradButton1.setAutoExclusive(True)
        self.bodyIconsMenuLayout.addWidget(self.dashboradButton1)
        
        self.ordersButton1 = QPushButton(self.sideBarIconsMenuWidget)
        self.ordersButton1.setText("")
        icon2 = QIcon()
        icon2.addPixmap(QPixmap(":/icon/icon/activity-feed-32.ico"), QIcon.Mode.Normal, QIcon.State.Off)
        icon2.addPixmap(QPixmap(":/icon/icon/activity-feed-48-yellow.ico"), QIcon.Mode.Normal, QIcon.State.On)
        self.ordersButton1.setIcon(icon2)
        self.ordersButton1.setIconSize(QSize(20, 20))
        self.ordersButton1.setCheckable(True)
        self.ordersButton1.setAutoExclusive(True)
        self.bodyIconsMenuLayout.addWidget(self.ordersButton1)

        self.productsButton1 = QPushButton(self.sideBarIconsMenuWidget)
        self.productsButton1.setText("")
        icon3 = QIcon()
        icon3.addPixmap(QPixmap(":/icon/icon/product-32.ico"), QIcon.Mode.Normal, QIcon.State.Off)
        icon3.addPixmap(QPixmap(":/icon/icon/product-48.ico"), QIcon.Mode.Normal, QIcon.State.On)
        self.productsButton1.setIcon(icon3)
        self.productsButton1.setIconSize(QSize(20, 20))
        self.productsButton1.setCheckable(True)
        self.productsButton1.setAutoExclusive(True)
        self.productsButton1.setObjectName("productsButton1")
        self.bodyIconsMenuLayout.addWidget(self.productsButton1)

        self.customersButton1 = QPushButton(self.sideBarIconsMenuWidget)
        self.customersButton1.setText("")
        icon4 = QIcon()
        icon4.addPixmap(QPixmap(":/icon/icon/group-32.ico"), QIcon.Mode.Normal, QIcon.State.Off)
        icon4.addPixmap(QPixmap(":/icon/icon/group-48.ico"), QIcon.Mode.Normal, QIcon.State.On)
        self.customersButton1.setIcon(icon4)
        self.customersButton1.setIconSize(QSize(20, 20))
        self.customersButton1.setCheckable(True)
        self.customersButton1.setAutoExclusive(True)
        self.customersButton1.setObjectName("customersButton1")
        self.bodyIconsMenuLayout.addWidget(self.customersButton1)
        
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
        self.logoLabel2.setMinimumSize(QSize(40, 40))
        self.logoLabel2.setMaximumSize(QSize(40, 40))
        self.logoLabel2.setText("")
        self.logoLabel2.setPixmap(QPixmap(":/icon/icon/Logo.png"))
        self.logoLabel2.setScaledContents(True)
        self.headerFullMenuLayout.addWidget(self.logoLabel2)

        self.logoLabel3 = QLabel(self.siderBarFullMenuWidget)
        font = QFont()
        font.setPointSize(15)
        self.logoLabel3.setFont(font)
        self.headerFullMenuLayout.addWidget(self.logoLabel3)

        

        self.bodyFullMenuLayout = QVBoxLayout()
        self.bodyFullMenuLayout.setSpacing(0)
        self.homeButton2 = QPushButton(self.siderBarFullMenuWidget)
        self.homeButton2.setIcon(icon)
        self.homeButton2.setIconSize(QSize(14, 14))
        self.homeButton2.setCheckable(True)
        self.homeButton2.setAutoExclusive(True)        
        self.bodyFullMenuLayout.addWidget(self.homeButton2)

        self.dashboradButton2 = QPushButton(self.siderBarFullMenuWidget)
        self.dashboradButton2.setIcon(icon1)
        self.dashboradButton2.setIconSize(QSize(14, 14))
        self.dashboradButton2.setCheckable(True)
        self.dashboradButton2.setAutoExclusive(True)
        self.bodyFullMenuLayout.addWidget(self.dashboradButton2)


        self.ordersButton2 = QPushButton(self.siderBarFullMenuWidget)
        self.ordersButton2.setIcon(icon2)
        self.ordersButton2.setIconSize(QSize(14, 14))
        self.ordersButton2.setCheckable(True)
        self.ordersButton2.setAutoExclusive(True)
        self.bodyFullMenuLayout.addWidget(self.ordersButton2)

        self.productsButton2 = QPushButton(self.siderBarFullMenuWidget)
        self.productsButton2.setIcon(icon3)
        self.productsButton2.setIconSize(QSize(14, 14))
        self.productsButton2.setCheckable(True)
        self.productsButton2.setAutoExclusive(True)
        self.bodyFullMenuLayout.addWidget(self.productsButton2)


        self.customersButton2 = QPushButton(self.siderBarFullMenuWidget)
        self.customersButton2.setIcon(icon4)
        self.customersButton2.setIconSize(QSize(14, 14))
        self.customersButton2.setCheckable(True)
        self.customersButton2.setAutoExclusive(True)
        self.bodyFullMenuLayout.addWidget(self.customersButton2)

        
        spacerItem2 = QSpacerItem(20, 373, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        
        self.exitButton2 = QPushButton(self.siderBarFullMenuWidget)
        self.exitButton2.setIcon(icon5)
        self.exitButton2.setIconSize(QSize(14, 14))

        self.siderBarFullMenuWidget.setFixedWidth(150)
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


        self.user_btn = QPushButton(self.mainContentAreaWidget)
        self.user_btn.setText("")
        icon8 = QIcon()
        icon8.addPixmap(QPixmap(":/icon/icon/user-48.ico"), QIcon.Mode.Normal, QIcon.State.Off)
        self.user_btn.setIcon(icon8)
        self.user_btn.setObjectName("user_btn")
        self.headerMainContentLayout.addWidget(self.user_btn)

        self.stackedWidget=QStackedWidget(self.mainContentAreaWidget)

        self.page1= QWidget()
        self.gridLayout_2 = QGridLayout(self.page1)
        self.label4=QLabel(self.page1)
        font=QFont()
        font.setPointSize(20)
        self.label4.setFont(font)
        self.label4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gridLayout_2.addWidget(self.label4,0,0,1,1)
        self.stackedWidget.addWidget(self.page1)

        self.page2=QWidget()
        self.gridLayout_3 = QGridLayout(self.page1)
        self.label5=QLabel(self.page1)
        font=QFont()
        font.setPointSize(20)
        self.label5.setFont(font)
        self.label5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gridLayout_3.addWidget(self.label5,0,0,1,1)
        self.stackedWidget.addWidget(self.page1)

        self.page3=QWidget()
        self.gridLayout_3 = QGridLayout(self.page1)
        self.label6=QLabel(self.page1)
        font=QFont()
        font.setPointSize(20)
        self.label6.setFont(font)
        self.label6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gridLayout_3.addWidget(self.label6,0,0,1,1)
        self.stackedWidget.addWidget(self.page3)


        self.label4.setText("page 1")
        self.label5.setText("page 2")
        self.label6.setText("page 3")

        self.mainContentAreaLayout.addWidget(self.widget)
        self.mainContentAreaLayout.addWidget(self.stackedWidget)
        

        self.gridLayout= QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.addWidget(self.sideBarIconsMenuWidget, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.siderBarFullMenuWidget,0,1,1,1)
        self.gridLayout.addWidget(self.mainContentAreaWidget,0,2,1,1)
        
       
        self.change_btn.toggled['bool'].connect(self.sideBarIconsMenuWidget.setVisible)
        self.change_btn.toggled['bool'].connect(self.siderBarFullMenuWidget.setHidden) 

        
import resource_rc