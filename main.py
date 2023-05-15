# from getmac import get_mac_address as gma
#
# print(gma())
import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QFontDatabase

from Ui_MainWindow import Ui_MainWindow


class keyboard_trainer(QMainWindow):
    def __init__(self):
        super(keyboard_trainer, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.start_button.clicked.connect(self.show_training_page)
        self.ui.info_button.clicked.connect(self.show_information_page)
        self.ui.stat_button.clicked.connect(self.show_statistics_page)

    def show_training_page(self):
        self.ui.info_frame.hide()
        self.ui.stat_frame.hide()
        self.ui.training_window.show()
    def show_information_page(self):
        self.ui.training_window.hide()
        self.ui.stat_frame.hide()
        self.ui.info_frame.show()
    def show_statistics_page(self):
        self.ui.training_window.hide()
        self.ui.info_frame.hide()
        self.ui.stat_frame.show()


if __name__ == "__main__":
    #testing
    user_stats = {1:4.65, 3:4.21, 10: 3.56, 30: 2.69}
    rus_words = [i for i in range(1000, 1000000, 10000)]


    app = QApplication(sys.argv)
    app.setStyle("Windows")



    window = keyboard_trainer()
    window.show()
    # window.ui.info_frame.hide()
    # window.ui.stat_frame.hide()
    # window.ui.training_window.show()

    sys.exit(app.exec())