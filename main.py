from getmac import get_mac_address


import time
import random
import sys
import psycopg2

from PySide6 import QtGui, QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QFontDatabase

import words_generator
from Ui_MainWindow import Ui_MainWindow


class keyboard_trainer(QMainWindow):
    def __init__(self):
        super(keyboard_trainer, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.current_page = ''
        self.current_difficulty = 1
        self.current_language = 'ru'
        self.last_pressed_key = ''
        self.remaining_text = ''
        self.print_line = ''
        self.input_text = ''
        self.current_generated_words = []
        self.words_generators = {}
        self.current_input_key_index = 0
        self.start_time = 0
        self.current_input_key_index = 0
        self.current_error_num = 0
        self.current_printed_word_num = 0
        self.current_printed_char_num = 0
        self.current_error_num = 0
        self.connect_cursor = None
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
        if self.ui.start_button.text() == 'Стоп':
            self.show_result_page()
        if self.current_page == 'training_page':
            return
        self.current_page = 'training_page'
        generator_name = self.current_language + str(self.current_difficulty)
        if generator_name not in self.words_generators:
            new_generator = words_generator.WordsGenerator()
            new_generator.read_words_from_file('dictionaries\\'+generator_name+'.txt')
            new_generator.create_markov_chain()
            self.words_generators[generator_name] = new_generator
        self.current_generated_words = self.words_generators[generator_name].generate_words(1)
        if self.ui.start_button.text() == 'Старт':
            self.ui.start_button.setText('Стоп')
        else:
            self.ui.start_button.setText('Старт')
        self.ui.info_frame.hide()
        self.ui.stat_frame.hide()
        self.ui.result_frame.hide()
        self.ui.training_window.show()
        self.start_time = time.perf_counter()
        self.current_error_num = 0
        self.current_printed_word_num = 0
        self.current_printed_char_num = 0
        self.generate_words()




    def show_information_page(self):
        if self.current_page == 'information_page':
            return
        self.ui.start_button.setText('Старт')
        self.current_page = 'information_page'
        self.ui.training_window.hide()
        self.ui.stat_frame.hide()
        self.ui.result_frame.hide()
        self.ui.info_frame.show()

    def show_statistics_page(self):
        if self.current_page == 'statistics_page':
            return
        self.ui.start_button.setText('Старт')
        self.current_page = 'statistics_page'
        user_stats = self.get_user_stats()
        for column in range(3):
            for row in range(6):
                table_item = QtWidgets.QTableWidgetItem()
                table_item.setTextAlignment(Qt.AlignCenter)
                table_item.setText(str(user_stats[column][row]))
                self.ui.stat_table.setItem(row, column, table_item)


        self.ui.training_window.hide()
        self.ui.info_frame.hide()
        self.ui.result_frame.hide()
        self.ui.stat_frame.show()

    def show_result_page(self):
        if self.current_page == 'result_page':
            return
        training_time = round(time.perf_counter() - self.start_time, 2)
        char_input_speed = round(self.current_printed_char_num / training_time, 2)
        if self.current_printed_char_num == 0:
            accuracy = 0
        else:
            accuracy = round(1 - self.current_error_num/self.current_printed_char_num, 2)
        self.ui.result_stat_tab_day_1.setText('Время (секунд): ' + str(training_time))
        self.ui.result_stat_tab_day_3.setText('Напечатано слов: ' + str(self.current_printed_word_num))
        self.ui.result_stat_tab_day_10.setText('Напечатано символов: ' + str(self.current_printed_char_num))
        self.ui.result_stat_tab_day_30.setText('Совершенно ошибок: ' + str(self.current_error_num))
        self.ui.result_stat_tab_day_4.setText('Скорость набора (символов в секунду): ' + str(char_input_speed))
        self.ui.result_stat_tab_day_5.setText('Точность: ' + str(accuracy))
        self.ui.result_stat_tab1.setText('Итоги тренировки')
        self.save_result()
        self.ui.training_window.hide()
        self.ui.info_frame.hide()
        self.ui.stat_frame.hide()
        self.ui.result_frame.show()

    def save_result(self):
        pass

    def change_difficulty(self):
        if self.current_page == 'training_page':
            return
        difficulty = [3, 1, 2]
        difficulty_colors = {1: [[121, 216, 88], [101, 196, 68], [71, 166, 38]],
                             2: [[255, 222, 104], [235, 202, 84], [205, 172, 54]],
                             3: [[255, 125, 141], [235, 105, 121], [205, 75, 91]]}
        current_difficulty_index = ((self.current_difficulty + 1) % 3)
        self.current_difficulty = difficulty[current_difficulty_index]
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
        if self.connect_cursor is None:
            connection = psycopg2.connect(
                database="kp0092_27",
                user="st0092",
                password="qwerty92",
                host="172.20.8.18",
                port="5432"
            )
            self.connect_cursor = connection.cursor()
        mac_address = str(get_mac_address())
        query = 'SELECT'

        user_stats = [[str(i) for i in range(0, 6)], [str(i) for i in range(6, 12)], [str(i) for i in range(12, 18)]]
        return user_stats

    def generate_words(self):
        max_print_line_size = 30
        print_line = ''
        self.current_input_key_index = 0
        words = self.current_generated_words
        if len(words) == 0:
            self.show_statistics_page()
            print(time.perf_counter() - self.start_time)
            self.show_result_page()
        while len(words) > 0 and max_print_line_size > len(words[0] + ' '):
            self.current_printed_word_num += 1
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
            self.current_printed_char_num += 1
        elif key != '':
            self.current_error_num += 1
        if self.current_input_key_index == len(self.print_line):
            self.generate_words()

    def keyPressEvent(self, event):
        if self.current_page != 'training_page':
            return
        key = event.text()
        # print(key)
        self.check_key(key)

    def get_words_from_db(self):
        # TODO: Вытягивание с БД
        return [str(random.randint(9,100000)) for i in range(1000, 20101, 10000)]


# testing
user_stats = {1: 4.65, 3: 4.21, 10: 3.56, 30: 2.69}


app = QApplication(sys.argv)
app.setStyle("Windows")

window = keyboard_trainer()
window.show()
# window.ui.info_frame.hide()
# window.ui.stat_frame.hide()
# window.ui.training_window.show()
if window.connect_cursor is not None:
    window.connect_cursor.close()
sys.exit(app.exec())
