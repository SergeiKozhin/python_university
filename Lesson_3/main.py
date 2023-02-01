
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

from collections import Counter

d = dict(Counter(c))
#print(d)

#5. вывести 5 наиболее часто встречающихся слов (sort), вывести количество разных слов в тексте (set).

sorted_dict = {}
sorted_keys = sorted(d, key=d.get)  # [1, 3, 2]

for w in sorted_keys:
    sorted_dict[w] = d[w]

print(tuple(sorted_dict))