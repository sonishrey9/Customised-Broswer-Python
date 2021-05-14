from PyQt5.QtWidgets import * #importing everything from PyQt5
from PyQt5.QtWebEngineWidgets import * #improting this module for QWebEngineView
from PyQt5.QtCore import *
import sys #builtin python environements

class MainWindow(QMainWindow): #creating class
    def __init__(self): # constructor
        super(MainWindow, self).__init__() #super connection wiith parent class
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.google.com/")) #setting up desired serach engine
        self.setCentralWidget(self.browser)
        self.showMaximized()

        #navigation bar creation

        navbbar = QToolBar()
        self.addToolBar(navbbar)

        back_btn = QAction("back", self) #creation of back button
        back_btn.triggered.connect(self.browser.back)
        navbbar.addAction((back_btn)) #adding bacl button to navigation bar

        #forward navigation
        forward_btn = QAction("forward",self)
        forward_btn.triggered.connect(self.browser.forward)
        navbbar.addAction((forward_btn)) #adding forward button to navigation

        #reload button to navigation bar

        reload_btn = QAction("reload",self)
        reload_btn.triggered.connect(self.browser.reload)
        navbbar.addAction((reload_btn))

        #home button to navigation bar
        home_btn = QAction("home",self)
        home_btn.triggered.connect(self.navigate_home)
        navbbar.addAction((home_btn))

        #searching from navigation bar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbbar.addWidget(self.url_bar)


        #updating url_bar
        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self): #home navigation bar function
        self.browser.setUrl(QUrl("https://www.google.com/"))

    def navigate_to_url(self): #to search from navigation bar
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q): #updating url evrytime it is reloaded to new webiste url
        self.url_bar.setText(q.toString())




app = QApplication(sys.argv)
QApplication.setApplicationName("shrey soni Browser")
window = MainWindow()
app.exec_()
