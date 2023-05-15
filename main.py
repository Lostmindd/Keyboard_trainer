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

        self.ui.start_button.clicked.connect(self.test)

    def test(self):
        print('test')

if __name__ == "__main__":
    #testing
    user_stats = {1:4.65, 7: 3.56, 30: 2.69}
    rus_words = [i for i in range(1000, 1000000, 10000)]


    app = QApplication(sys.argv)

    window = keyboard_trainer()
    window.show()

    sys.exit(app.exec())