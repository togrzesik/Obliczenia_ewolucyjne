import sys

from PyQt5.QtWidgets import QApplication

from main_gui import MainGui


class AppStarter:

    def __init__(self):
        self.__app = QApplication(sys.argv)
        self.gui = MainGui()
        self.__app.exec_()
