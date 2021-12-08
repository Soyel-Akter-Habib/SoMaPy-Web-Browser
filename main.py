import os
import sys

from PyQt5.QtCore import  *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from PyQt5.QtWebEngineWidgets import  *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.browser=QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        navigationBar=QToolBar()
        self.addToolBar(navigationBar)


        backBtn = QAction('Back',self)
        backBtn.triggered.connect(self.browser.back)
        navigationBar.addAction(backBtn)

        forwardBtn = QAction('Forward',self)
        forwardBtn.triggered.connect(self.browser.forward)
        navigationBar.addAction(forwardBtn)

        refreshBtn = QAction('Reload',self)
        refreshBtn.triggered.connect(self.browser.reload)
        navigationBar.addAction(refreshBtn)

        homeBtn = QAction('Home',self)
        homeBtn.triggered.connect(self.navigateHome)
        navigationBar.addAction(homeBtn)

        self.urlBar = QLineEdit()
        self.urlBar.returnPressed.connect(self.navigateToUrl)
        navigationBar.addWidget((self.urlBar))

        self.browser.urlChanged.connect(self.updateUrl)

    def navigateHome(self):
        self.browser.setUrl(QUrl('http://www.soyelink.blogspot.com'))
    def navigateToUrl(self):
        url=self.urlBar.text()
        self.browser.setUrl(QUrl(url))

    def updateUrl(self,q):
        self.urlBar.setText(q.toString())


app=QApplication(sys.argv)
QApplication.setApplicationName('SoMaPy')
window=MainWindow()
app.exec_()
