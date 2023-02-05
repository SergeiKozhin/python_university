import random

# 1. Напишите функцию (F): на вход список имен и целое число N; на выходе список длины N случайных имен из первого списка (могут повторяться, можно взять значения: количество имен 20, N = 100, рекомендуется использовать функцию random);
name_list = ['Kate', 'Alex', 'Dima', 'Misha', 'Bob', 'Mike']

def name_func(x, y = 100):
    new_name_list = []
    n = 0
    while n < y:
        new_name_list.append(random.choice(name_list))
        n += 1
    return new_name_list
new_list = name_func(name_list)
# print(new_list)
# 2. Напишите функцию вывода самого частого имени из списка на выходе функции F
from collections import Counter

def most_frequent(List):

    occurence_count = Counter(List)

    return occurence_count.most_common()[0][0]

most_frequent_name = most_frequent(new_list)
# print(most_frequent_name)

# 3. Напишите функцию вывода самой редкой буквы, с которого начинаются имена в списке на выходе функции F.

def rare_letter(i):
    rare_letter_list = list(map(lambda x:x[0], i))
    occurence_count = Counter(rare_letter_list)
    return occurence_count.most_common()[-1][0]

# print(rare_letter(new_list))

# 4. В файле с логами https://drive.google.com/open?id=1pKGu-u2Vvtx4xK8i2ZhOzE5rBXyO4qd8 найти дату самого позднего лога (по метке времени)

