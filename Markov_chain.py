import random

# Парсер
file_name = r'C:\Users\vasill\Desktop\file1.txt'
words = ['START']
f = open(file_name, 'r', encoding="utf-8")
text = f.read().replace('\n', ' ')
word = ''
for char in text:
    if char == ' ':
        if words[-1] == 'END':
            words.append('START')
        else:
            words.append(word)
        word = ''
    elif char == '.':
        words.append(word)
        words.append('END')
        word = ''
    else:
        word += char
f.close()

print(words)

# Создание цепи
markov_chain = {}
for word_iter in range(len(words)):
    word = words[word_iter]
    if word not in markov_chain:
        markov_chain[word] = {}
    if words[word_iter] != 'END':
        next_word = words[word_iter+1]
        if next_word in markov_chain[word]:
            markov_chain[word][words[word_iter+1]] += 1
        else:
            markov_chain[word][words[word_iter + 1]] = 1

# print(markov_chain)
# Генерация текста
generated_words_num = 0
generated_str = ''
current_word = 'START'
while (generated_words_num < 50):
    random_num = random.randint(0, sum(markov_chain[current_word].values()))
    for key in markov_chain[current_word]:
        random_num -= markov_chain[current_word][key]
        if random_num <= 0:
            current_word = key
            break
    if current_word == 'END':
        current_word = 'START'
        generated_str += '.'
        continue
    generated_str += ' ' + current_word
    generated_words_num += 1

print(generated_str)