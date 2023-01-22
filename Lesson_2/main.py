#1. Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.

'''
stroka = 1
while stroka < 6:
    print(str(stroka) + '.  ' + '0')
    stroka += 1
'''

#2. Пользователь в цикле вводит 10 цифр. Найти количество введенных пользователем цифр 5.

'''
list_of_digits = []
attempt = 0
while attempt < 10:
    answer = int(input('Введите любую цифру:  '))
    list_of_digits.append(answer)
    attempt += 1
count = 0
for i in list_of_digits:
    if i == 5:
        count += 1
print('Количество цифр 5 в цикле равно: ', count)
'''

#3. Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.

'''
summa = 0
for i in range(101):
    summa += i
print(summa)
'''

#4. Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.

'''
product_of_numbers = 1
for i in range(1, 11):
    product_of_numbers *= i
print(product_of_numbers)
'''

#5. Вывести цифры числа на каждой строчке.

'''
number = input('Введите любое число: ')
for i in number:
    print(i)
'''

#6. Найти сумму цифр числа.

'''
summa = 0
number = input('Введите любое число: ')
for i in number:
    summa += int(i)
print(summa)
'''

#7. Найти произведение цифр числа.

'''
product_of_numbers = 1
number = input('Введите любое число: ')
for i in number:
    product_of_numbers *= int(i)
print(product_of_numbers)
'''

#8. Дать ответ на вопрос: есть ли среди цифр числа 5?

'''
list_of_digits = []
number = input('Введите любое число: ')
for i in number:
    list_of_digits.append(int(i))
if 5 in list_of_digits:
    print('В числе есть цифра 5')
else:
    print('В числе нет цифры 5')
'''