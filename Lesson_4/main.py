# 1. Напишите функцию (F): на вход список имен и целое число N; на выходе список длины N случайных имен из первого списка (могут повторяться, можно взять значения: количество имен 20, N = 100, рекомендуется использовать функцию random);

import random
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

def last_time():
    time_list = []
    with open('log.txt', encoding='UTF-8') as f:
        file = f.read()
    f.close()
    log_list = file.split('\n')
    for i in log_list:
        time_list.append(i.split()[1][:-4])
    max_value_time = max(time_list)
    max_index = time_list.index(max_value_time)
    return log_list[max_index]

# print(last_time())


# 5. переписать программу "Викторина" (из прошлого домашнего задания), используя функции

days = {
    '01' : 'первого',
    '02' : 'второго',
    '03' : 'третьего',
    '04' : 'четвертого',
    '05' : 'пятого',
    '06' : 'шестого',
    '07' : 'седьмого',
    '08' : 'восьмого',
    '09' : 'девятого',
    '10' : 'десятого',
    '11' : 'одинадцатого',
    '12' : 'двенадцатого',
    '13' : 'тринадцатого',
    '14' : 'четырнадцатого',
    '15' : 'пятнадцатого',
    '16' : 'шестнадцатого',
    '17' : 'семнадцатого',
    '18' : 'восемнадцатого',
    '19' : 'девятнацатого',
    '20' : 'двадцатого',
    '21' : 'двадцать первого',
    '22' : 'двадцать второго',
    '23' : 'двадцать третьего',
    '24' : 'двадцать четвертого',
    '25' : 'двадцать пятого',
    '26' : 'двадцать шестого',
    '27' : 'двадцать седьмого',
    '28' : 'двадцать восьмого',
    '29' : 'двадцать девятго',
    '30' : 'тридцатого',
    '31' : 'тридцать первого'
}

month = {
    '01' : 'января',
    '02' : 'февраля',
    '03' : 'марта',
    '04' : 'апреля',
    '05' : 'мая',
    '06' : 'июня',
    '07' : 'июля',
    '08' : 'августа',
    '09' : 'сентября',
    '10' : 'октября',
    '11' : 'ноября',
    '12' : 'декабря'
}

people = {
    'Юрий Гагарин' : '01.03.1934',
    'Линус Торвальдс' : '28.12.1969',
    'Гвидо ван Россум' : '31.01.1956',
    'Павел Дуров' : '10.10.1984',
    'Стив Джобс' : '24.02.1955'
}

right = 0
wrong = 0
i = 0

def right_answer():
    global right
    print('Верно')
    print('-----------------------------------')
    right += 1

def wrong_answer():
    global wrong
    global i
    print('Он родился ' + days[people[i][:2]] + ' ' + month[people[i][3:5]] + ' ' + people[i][-4:] + ' года')
    print('-----------------------------------')
    wrong += 1

def result():
    print('Количество правильных ответов: ', right)
    print('Количество неправильных ответов: ', wrong)
    print('Процент правильных ответов: ', 20 * right)

def main():
    global right
    global wrong
    global i

    for i in people:
        answer = input('Когда родился ' + str(i) + ' ? Ответ введите в формате dd.mm.yyyy     ')
        if answer == people[i]:
            right_answer()
        else:
            wrong_answer()

# main()
# result()


# 6. написать программу "Личный счет"

balance = 0
purchase_history = []

def top_wallet():
    global balance
    top = int(input('Введите сумму, на которую хотите пополнить баланс \n'))
    balance = balance + top
    print('')

def purchase():
    global balance
    global purchase_history
    purchase_list = []
    purchase_cost = int(input('Введите сумму покупки \n'))
    if purchase_cost > balance:
        print('Недостаточно средств. Пополните баланс')
        print('')
    else:
        purchase_name = input('Введите название покупки \n')
        purchase_list.append(purchase_name)
        purchase_list.append(purchase_cost)
        purchase_history.append(purchase_list)
        balance = balance - purchase_cost
    print('')

def history():
    print('История ваших покупок:')
    print('')
    for i in purchase_history:
        print(f'Покупка: {i[0]}. Стоимость: {i[1]} рублей')
    print('')


def main():
    global answer
    global balance
    while True:
        print(f'Ваш баланс: {balance} рублей')
        print('')
        answer = int(input('Что вы хотите сделать? Введите цифру \n 1 - пополнить баланс \n 2 - совершить покупку \n 3 - посмотреть историю покупок \n 4 - выйти \n'))
        print('')
        if answer == 1:
            top_wallet()
        elif answer == 2:
            purchase()
        elif answer == 3:
            history()
        elif answer == 4:
            print('До новых встреч!')
            print('')
            break
    

# main()



# 7. задание 4 через регулярное выражение


import re
def last_time():
    with open('log.txt', encoding='UTF-8') as f:
        file = f.read()
    f.close()
    max_time = max(re.findall(r'\d\d:\d\d:\d\d', file))
    return [i for i in file.split('\n') if i.find(max_time) != -1][0]

print(last_time())
