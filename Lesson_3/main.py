
# 1. Методами строк очистить текст от знаков препинания;

import string
with open('text.txt', encoding='UTF-8') as f:
    file = f.read()
f.close()

punc = string.punctuation + '—«»'

a = file.translate(str.maketrans('', '', punc))
#print(a)

# 2. сформировать list со словами (split);

b = a.split()
#print(b)

# 3. привести все слова к нижнему регистру (map);

c = list(map(str.lower, b))
#print(c)

# 4. получить из list пункта 3 dict, ключами которого являются слова, а значениями их количество появлений в тексте;

