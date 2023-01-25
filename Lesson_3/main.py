
#1. Методами строк очистить текст от знаков препинания;

import string
with open('text.txt', encoding='UTF-8') as f:
    file = f.read()
f.close()

punc = string.punctuation


for i in file:
    if i in punc:
        row = file.replace(i, '')
print(row)
