import sys
import unittest

import psycopg2

import KeyboardTrainer
import words_generator

class TestKeyboardTrainer(unittest.TestCase):

    def setUp(self):
        self.word_generator = words_generator.WordsGenerator()
        self.word_generator.read_words_from_file('dictionaries\\en1.txt')
        self.word_generator.create_markov_chain()
        if not KeyboardTrainer.QApplication.instance():
            self.app = KeyboardTrainer.QApplication(sys.argv)
        else:
            self.app = KeyboardTrainer.QApplication.instance()
        self.window = KeyboardTrainer.keyboard_trainer()

    # Each test method starts with the keyword test_
    def test_generate_words_list_size(self):
        self.assertEqual(len(self.word_generator.generate_words(30)), 30)

    def test_generate_words_returned_type(self):
        self.assertEqual(type(self.word_generator.generate_words(30)), list)

    def test_create_connection(self):
        self.assertEqual(type(self.window.create_connection()), psycopg2.extensions.cursor)

    def test_get_user_stats_returned_type(self):
        self.assertEqual(type(self.window.get_user_stats()), list)

    def test_get_user_stats_list_size(self):
        self.assertEqual(len(self.window.get_user_stats()), 3)

    def test_execute_query(self):
        self.assertNotEqual(self.window.execute_query('Select current_date', False), None)


if __name__ == "__main__":
    unittest.main()