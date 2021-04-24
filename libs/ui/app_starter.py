import sys

from PyQt5.QtWidgets import QApplication

from gui_project2 import GuiProject2
from main_gui import MainGui


class AppStarter:

    def __init__(self):
        self.__app = QApplication(sys.argv)
        # self.gui = MainGui()
        self.gui = GuiProject2()
        self.__app.exec_()
