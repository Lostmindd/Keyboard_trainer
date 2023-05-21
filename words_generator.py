import random


class WordsGenerator:

    def __init__(self):
        self.words = []
        self.markov_chain = {}

    def read_words_from_file(self, file_path):
        self.words = ['START']
        f = open(file_path, 'r', encoding="utf-8")
        text = f.read().replace('\n', ' ')
        word = ''
        for char in text:
            if char == ' ':
                if self.words[-1] == 'END':
                    self.words.append('START')
                else:
                    self.words.append(word)
                word = ''
            elif char == '.':
                self.words.append(word)
                self.words.append('END')
                word = ''
            else:
                word += char
        f.close()

    def create_markov_chain(self):
        for word_iter in range(len(self.words)):
            word = self.words[word_iter]
            if word not in self.markov_chain:
                self.markov_chain[word] = {}
            if self.words[word_iter] != 'END':
                next_word = self.words[word_iter + 1]
                if next_word in self.markov_chain[word]:
                    self.markov_chain[word][self.words[word_iter + 1]] += 1
                else:
                    self.markov_chain[word][self.words[word_iter + 1]] = 1
        self.words.clear()

    def generate_words(self, words_count):
        generated_words_num = 0
        generated_words = []
        current_word = 'START'
        while generated_words_num < words_count:
            random_num = random.randint(0, sum(self.markov_chain[current_word].values()))
            for key in self.markov_chain[current_word]:
                random_num -= self.markov_chain[current_word][key]
                if random_num <= 0:
                    current_word = key
                    break
            if current_word == 'END':
                current_word = 'START'
                generated_words.append('.')
                continue
            generated_words.append(current_word)
            generated_words_num += 1
        return generated_words
