# from getmac import get_mac_address as gma
#
# print(gma())
import time
import random
import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QFontDatabase

from Ui_MainWindow import Ui_MainWindow


class keyboard_trainer(QMainWindow):
    def __init__(self):
        super(keyboard_trainer, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.current_page = ''
        self.current_difficulty = 'низкая'
        self.current_language = 'ru'
        self.last_pressed_key = ''
        self.remaining_text = ''
        self.print_line = ''
        self.input_text = ''
        self.words = {}
        self.current_input_key_index = 0
        self.start_time = 0
        self.current_input_key_index = 0
        # self.print_line_size = 0
        self.show_information_page()
        # Buttons
        self.ui.start_button.clicked.connect(self.show_training_page)
        self.ui.stat_button.clicked.connect(self.show_statistics_page)
        self.ui.info_button.clicked.connect(self.show_information_page)
        self.ui.difficulty_button.clicked.connect(self.change_difficulty)
        self.ui.ru_button.clicked.connect(lambda x: self.change_language('ru'))
        self.ui.en_button.clicked.connect(lambda x: self.change_language('en'))

    def show_training_page(self):
        if self.current_page == 'training_page':
            return
        self.current_page = 'training_page'
        self.ui.start_button.setText('Пауза')
        self.ui.info_frame.hide()
        self.ui.stat_frame.hide()
        self.ui.training_window.show()
        self.words['rus1'] = self.get_words_from_db()
        self.start_time = time.perf_counter()
        self.generate_words()



    def show_information_page(self):
        if self.current_page == 'information_page':
            return
        self.current_page = 'information_page'
        self.ui.training_window.hide()
        self.ui.stat_frame.hide()
        self.ui.info_frame.show()

    def show_statistics_page(self):
        if self.current_page == 'statistics_page':
            return
        self.current_page = 'statistics_page'
        user_stats = self.get_user_stats()
        self.ui.stat_tab_day_1.setText('за 1 день: ' + str(user_stats[0]))
        self.ui.stat_tab_day_3.setText('за 3 дня: ' + str(user_stats[1]))
        self.ui.stat_tab_day_10.setText('за 10 дней: ' + str(user_stats[2]))
        self.ui.stat_tab_day_30.setText('за 30 дней: ' + str(user_stats[3]))

        self.ui.training_window.hide()
        self.ui.info_frame.hide()
        self.ui.stat_frame.show()

    def change_difficulty(self):
        if self.current_page == 'training_page':
            return
        difficulty = ['низкая', 'средняя', 'высокая']
        difficulty_colors = {'низкая': [[121, 216, 88], [101, 196, 68], [71, 166, 38]],
                             'средняя': [[255, 222, 104], [235, 202, 84], [205, 172, 54]],
                             'высокая': [[255, 125, 141], [235, 105, 121], [205, 75, 91]]}
        new_difficulty_index = ((difficulty.index(self.current_difficulty) + 1) % 3)
        self.current_difficulty = difficulty[new_difficulty_index]
        button_stylesheet_part_1 = u"\nQPushButton { \n"

        background_color_1 = "background-color:rgb(" + str(difficulty_colors[self.current_difficulty][0][0]) + \
                             ", " + str(difficulty_colors[self.current_difficulty][0][1]) + ", " \
                             + str(difficulty_colors[self.current_difficulty][0][2]) + ")"
        button_stylesheet_part_2 = " ;\nborder-radius: 20px; \nfont: 24pt \"MS Shell Dlg 2\";\ncolor: #000000;\n}\nQPushButton:hover { \n"
        background_color_2 = "background-color:rgb(" + str(difficulty_colors[self.current_difficulty][1][0]) + ", " \
                             + str(difficulty_colors[self.current_difficulty][1][1]) + ", " \
                             + str(difficulty_colors[self.current_difficulty][1][2]) + ");"
        button_stylesheet_part_3 = "\nborder-radius: 20px; \nfont: 24pt \"MS Shell Dlg 2\";\ncolor: #000000;\n}\nQPushButton:pressed { \n"
        background_color_3 = "background-color:rgb(" + str(difficulty_colors[self.current_difficulty][2][0]) + ", " \
                             + str(difficulty_colors[self.current_difficulty][2][1]) + ", " \
                             + str(difficulty_colors[self.current_difficulty][2][2]) + ")"
        button_stylesheet_part_4 = " ;\nborder-radius: 20px; \nfont: 24pt \"MS Shell Dlg 2\";\ncolor: #000000;\n}"
        stylesheet_string = button_stylesheet_part_1 + background_color_1 + button_stylesheet_part_2 + background_color_2 + button_stylesheet_part_3 + background_color_3 + button_stylesheet_part_4
        self.ui.difficulty_button.setStyleSheet(stylesheet_string)

    def change_language(self, language):
        if language == self.current_language or self.current_page == 'training_page':
            return
        self.current_language = language
        inactive_button_stylesheet = u"QPushButton { \nbackground-color:rgb(0, 0, 0) ;\n" \
                                     + "border-radius: 20px; \nfont: 24pt \"MS Shell Dlg 2\";\ncolor: #FFFFF;\n}\nQPushButton:hover { \n" \
                                     + "background-color:rgb(80, 80, 80) ;\nborder-radius: 20px; \nfont: 24pt \"MS Shell Dlg 2\";\ncolor: #FFFFF;\n}"
        active_button_stylesheet = u"QPushButton { \nbackground-color:rgb(255, 255, 255) ;\n" \
                                   + "border-radius: 20px; \nfont: 24pt \"MS Shell Dlg 2\";\ncolor: #000000;\n}"
        if language == 'ru':
            self.ui.ru_button.setStyleSheet(active_button_stylesheet)
            self.ui.en_button.setStyleSheet(inactive_button_stylesheet)
        else:
            self.ui.en_button.setStyleSheet(active_button_stylesheet)
            self.ui.ru_button.setStyleSheet(inactive_button_stylesheet)

    def get_user_stats(self):
        # TODO: Вытягивание с БД
        user_stats = [4.65, 4.21, 3.56, 2.69]
        return user_stats

    def generate_words(self):
        max_print_line_size = 30
        print_line = ''
        self.current_input_key_index = 0
        words = self.words['rus1']
        if len(words) == 0:
            self.show_statistics_page()
            print(self.start_time - time.perf_counter())
        while len(words) > 0 and max_print_line_size > len(words[0] + ' '):
            max_print_line_size -= len(words[0])
            print_line += words.pop(0) + ' '
        remaining_text = ' '.join(words)
        self.input_text = ''
        self.ui.text_for_input_printed.setText(self.input_text)
        self.print_line = print_line
        self.remaining_text = remaining_text
        self.ui.text_for_input.setText(print_line)
        self.ui.text.setText(remaining_text)
        # self.ui.start_button.setEnabled(False)


    def check_key(self, key):
        if key == self.print_line[self.current_input_key_index]:
            self.input_text += self.print_line[self.current_input_key_index]
            self.ui.text_for_input_printed.setText(self.input_text)
            self.current_input_key_index += 1
        if self.current_input_key_index == len(self.print_line):
            self.generate_words()

    def keyPressEvent(self, event):
        if self.current_page != 'training_page':
            return
        key = event.text()
        print(key)
        self.check_key(key)

    def get_words_from_db(self):
        # TODO: Вытягивание с БД
        return [str(random.randint(9,100000)) for i in range(1000, 100000, 10000)]


# testing
user_stats = {1: 4.65, 3: 4.21, 10: 3.56, 30: 2.69}


app = QApplication(sys.argv)
app.setStyle("Windows")

window = keyboard_trainer()
window.show()
# window.ui.info_frame.hide()
# window.ui.stat_frame.hide()
# window.ui.training_window.show()

sys.exit(app.exec())
