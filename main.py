import datetime
from getmac import get_mac_address
import time
import sys
import psycopg2
from PySide6 import QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QComboBox
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
        # self.print_line_size = 0
        self.show_information_page()
        # Buttons
        self.ui.start_button.clicked.connect(self.show_training_page)
        self.ui.stat_button.clicked.connect(self.show_statistics_page)
        self.ui.info_button.clicked.connect(self.show_information_page)
        self.ui.delete_button.clicked.connect(self.delete_records)
        self.ui.difficulty_button.clicked.connect(self.change_difficulty)
        self.ui.ru_button.clicked.connect(lambda x: self.change_language('ru'))
        self.ui.en_button.clicked.connect(lambda x: self.change_language('en'))
        self.connect_cursor = self.create_connection()

    def delete_records_dorm_db(self, btn):
        if btn.text() == 'OK':
            language = "'" + self.current_language + "'"
            self.execute_query('Delete from training_data where lanquage = ' + language + 'and difficulty = ' + str(
                self.current_difficulty), True)
            self.show_statistics_page(True)

    def delete_records(self):
        warning = QMessageBox()
        warning.setWindowTitle('Предупреждение')
        warning.setText('Будут стерты все данные о ваших попытка, продолжить?')
        warning.setIcon(QMessageBox.Icon.Warning)
        warning.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        warning.buttonClicked.connect(self.delete_records_dorm_db)
        warning.exec()

    def show_training_page(self):
        if self.ui.start_button.text() == 'Стоп':
            self.show_result_page()
            if self.current_page == 'training_page':
                return
            else:
                self.ui.start_button.setText('Старт')
                self.ui.stat_button.setEnabled(True)
                self.ui.info_button.setEnabled(True)
                self.ui.difficulty_button.setEnabled(True)
                self.ui.ru_button.setEnabled(True)
                self.ui.en_button.setEnabled(True)
                return
        if self.current_page == 'training_page':
            return
        self.current_page = 'training_page'
        self.ui.stat_button.setEnabled(False)
        self.ui.info_button.setEnabled(False)
        self.ui.difficulty_button.setEnabled(False)
        self.ui.ru_button.setEnabled(False)
        self.ui.en_button.setEnabled(False)
        warning = QMessageBox()
        combo = QComboBox(warning)
        combo.addItem("30")
        combo.addItem("50")
        combo.addItem("80")
        combo.addItem("100")
        combo.addItem("200")
        combo.setGeometry(296, 10, 50, 20)
        warning.setWindowTitle('Количество слов')
        warning.setText('Выберите количество слов для генерации .................')
        warning.setIcon(QMessageBox.Icon.Question)

        warning.exec()
        words_num = int(combo.currentText())
        generator_name = self.current_language + str(self.current_difficulty)
        if generator_name not in self.words_generators:
            new_generator = words_generator.WordsGenerator()
            new_generator.read_words_from_file('dictionaries\\' + generator_name + '.txt')
            new_generator.create_markov_chain()
            self.words_generators[generator_name] = new_generator
        self.current_generated_words = self.words_generators[generator_name].generate_words(words_num)
        if self.ui.start_button.text() == 'Старт':
            self.ui.start_button.setText('Стоп')
        self.ui.info_frame.hide()
        self.ui.stat_frame.hide()
        self.ui.result_frame.hide()
        self.ui.training_window.show()
        self.start_time = time.perf_counter()
        self.current_error_num = 0
        self.current_printed_word_num = 0
        self.current_printed_char_num = 0
        self.words_output()

    def show_information_page(self):
        if self.current_page in ['information_page', 'training_page']:
            return
        self.ui.start_button.setText('Старт')
        self.current_page = 'information_page'
        self.ui.training_window.hide()
        self.ui.stat_frame.hide()
        self.ui.result_frame.hide()
        self.ui.info_frame.show()

    def show_statistics_page(self, refresh=False):
        if self.current_page in ['statistics_page', 'training_page'] and refresh is False:
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
        self.current_page = 'result_page'
        training_time = round(time.perf_counter() - self.start_time, 2)
        char_input_speed = round(self.current_printed_char_num / training_time, 2)
        if self.current_printed_char_num == 0:
            accuracy = 0
        else:
            accuracy = round(1 - self.current_error_num / (self.current_printed_char_num + self.current_error_num), 2)
        self.ui.result_stat_tab2.setText('Время (секунд): ' + str(training_time))
        self.ui.result_stat_tab3.setText('Напечатано слов: ' + str(self.current_printed_word_num))
        self.ui.result_stat_tab4.setText('Верно напечатанных символов: ' + str(self.current_printed_char_num))
        self.ui.result_stat_tab5.setText('Совершенно ошибок: ' + str(self.current_error_num))
        self.ui.result_stat_tab6.setText('Скорость набора (символов в секунду): ' + str(char_input_speed))
        self.ui.result_stat_tab7.setText('Точность: ' + str(accuracy))
        self.ui.result_stat_tab1.setText('Итоги тренировки')
        self.save_result(str(training_time), str(char_input_speed), str(accuracy))
        self.ui.training_window.hide()
        self.ui.info_frame.hide()
        self.ui.stat_frame.hide()
        self.ui.result_frame.show()

    def save_result(self, training_time, char_input_speed, accuracy):
        mac_address = "'" + str(get_mac_address()) + "'"
        date = datetime.datetime.now()
        date = "'" + str(date.date()) + "'"
        insert_data = ', '.join([mac_address, date, training_time, str(self.current_printed_word_num),
                                 str(self.current_printed_char_num), str(self.current_error_num), char_input_speed,
                                 accuracy, "'" + self.current_language + "'", str(self.current_difficulty)])
        insert_quary = 'INSERT INTO training_data (mac_address, training_date, print_time, ' + \
                       'printed_words_num, printed_chars_num, errors_num, ' + \
                       'print_speed, accuracy, lanquage, difficulty) values ( ' + insert_data + ');'
        self.execute_query(insert_quary, True)

    def create_connection(self):
        connection = psycopg2.connect(
            database="kp0092_27",
            user="st0092",
            password="qwerty92",
            host="172.20.8.18",
            port="5432"
        )
        return connection.cursor()

    def execute_query(self, quary, is_insert):
        if is_insert:
            try:
                self.connect_cursor.execute(quary)
                self.connect_cursor.execute("COMMIT")
            except psycopg2.Error as error:
                # print(error.pgcode )
                # print(error.pgerror)
                self.connect_cursor.execute("ROLLBACK")
        else:
            try:
                self.connect_cursor.execute(quary)
                return self.connect_cursor.fetchall()
            except psycopg2.Error:
                return None

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
        button_stylesheet_part_2 = ";\nborder-radius: 20px; \nfont: 24pt \"MS Shell Dlg 2\";\ncolor: " \
                                   "#000000;\n}\nQPushButton:hover { \n "
        background_color_2 = "background-color:rgb(" + str(difficulty_colors[self.current_difficulty][1][0]) + ", " \
                             + str(difficulty_colors[self.current_difficulty][1][1]) + ", " \
                             + str(difficulty_colors[self.current_difficulty][1][2]) + ");"
        button_stylesheet_part_3 = "\nborder-radius: 20px; \nfont: 24pt \"MS Shell Dlg 2\";\ncolor: " \
                                   "#000000;\n}\nQPushButton:pressed { \n "
        background_color_3 = "background-color:rgb(" + str(difficulty_colors[self.current_difficulty][2][0]) + ", " \
                             + str(difficulty_colors[self.current_difficulty][2][1]) + ", " \
                             + str(difficulty_colors[self.current_difficulty][2][2]) + ")"
        button_stylesheet_part_4 = " ;\nborder-radius: 20px; \nfont: 24pt \"MS Shell Dlg 2\";\ncolor: #000000;\n}"
        stylesheet_string = button_stylesheet_part_1 + background_color_1 + button_stylesheet_part_2 + background_color_2 + button_stylesheet_part_3 + background_color_3 + button_stylesheet_part_4
        self.ui.difficulty_button.setStyleSheet(stylesheet_string)
        if self.current_page == 'statistics_page':
            self.show_statistics_page(True)

    def change_language(self, language):
        if language == self.current_language or self.current_page == 'training_page':
            return
        self.current_language = language
        inactive_button_stylesheet = u"QPushButton { \nbackground-color:rgb(0, 0, 0) ;\n" \
                                     + "border-radius: 20px; \nfont: 24pt \"MS Shell Dlg 2\";\ncolor: " \
                                       "#FFFFF;\n}\nQPushButton:hover { \n" \
                                     + "background-color:rgb(80, 80, 80) ;\nborder-radius: 20px; \nfont: 24pt \"MS " \
                                       "Shell Dlg 2\";\ncolor: #FFFFF;\n} "
        active_button_stylesheet = u"QPushButton { \nbackground-color:rgb(255, 255, 255) ;\n" \
                                   + "border-radius: 20px; \nfont: 24pt \"MS Shell Dlg 2\";\ncolor: #000000;\n}"
        if language == 'ru':
            self.ui.ru_button.setStyleSheet(active_button_stylesheet)
            self.ui.en_button.setStyleSheet(inactive_button_stylesheet)
        else:
            self.ui.en_button.setStyleSheet(active_button_stylesheet)
            self.ui.ru_button.setStyleSheet(inactive_button_stylesheet)
        if self.current_page == 'statistics_page':
            self.show_statistics_page(True)

    def get_user_stats(self):
        mac_address = "'" + str(get_mac_address()) + "'"
        date = datetime.datetime.now()
        date_3_days_ago = "'" + str((date - datetime.timedelta(days=3)).date()) + "'"
        date_10_days_ago = "'" + str((date - datetime.timedelta(days=10)).date()) + "'"
        current_date = "'" + str(date.date()) + "'"
        language = "'" + self.current_language + "'"
        fetch_1_day = self.execute_query(
            'SELECT AVG(print_time), AVG(printed_words_num), AVG(printed_chars_num), AVG(errors_num), AVG(print_speed), AVG(accuracy) from training_data where mac_address = ' + mac_address + ' and training_date = ' + current_date + 'and lanquage = ' + language + 'and difficulty = ' + str(
                self.current_difficulty), False)
        fetch_3_day = self.execute_query(
            'SELECT AVG(print_time), AVG(printed_words_num), AVG(printed_chars_num), AVG(errors_num), AVG(print_speed), AVG(accuracy) from training_data where mac_address = ' + mac_address + ' and training_date BETWEEN  ' + date_3_days_ago + ' AND ' + current_date + 'and lanquage = ' + language + 'and difficulty = ' + str(
                self.current_difficulty), False)
        fetch_10_day = self.execute_query(
            'SELECT AVG(print_time), AVG(printed_words_num), AVG(printed_chars_num), AVG(errors_num), AVG(print_speed), AVG(accuracy) from training_data where mac_address = ' + mac_address + ' and training_date BETWEEN  ' + date_10_days_ago + ' AND ' + current_date + 'and lanquage = ' + language + 'and difficulty = ' + str(
                self.current_difficulty), False)
        user_stats = []
        for fetch in [fetch_1_day, fetch_3_day, fetch_10_day]:
            stat = []
            for row in fetch:
                for value in row:
                    if value is None:
                        stat.append('Нет данных')
                    else:
                        stat.append(round(value, 2))
            user_stats.append(stat.copy())
        return user_stats

    def words_output(self):
        max_print_line_size = 50
        print_line = ''
        self.current_input_key_index = 0
        words = self.current_generated_words
        if len(words) == 0:
            self.show_statistics_page()
            print(time.perf_counter() - self.start_time)
            self.show_result_page()
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

    def check_key(self, key):
        if key == self.print_line[self.current_input_key_index]:
            self.input_text += self.print_line[self.current_input_key_index]
            self.ui.text_for_input_printed.setText(self.input_text)
            self.current_input_key_index += 1
            self.current_printed_char_num += 1
            if key == ' ':
                self.current_printed_word_num += 1
        elif key != '':
            self.current_error_num += 1
        if self.current_input_key_index == len(self.print_line):
            self.words_output()

    def keyPressEvent(self, event):
        if self.current_page != 'training_page':
            return
        key = event.text()
        # print(key)
        self.check_key(key)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("Windows")
    window = keyboard_trainer()
    window.show()
    sys.exit(app.exec())
