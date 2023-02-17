from tkinter import *


root = Tk()

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

people = ['Юрий Гагарин', '01.03.1934', 'Линус Торвальдс', '28.12.1969', 'Гвидо ван Россум', '31.01.1956', 'Павел Дуров', '10.10.1984', 'Стив Джобс', '24.02.1955']

right = 0
wrong= 0
a = 0
b = 1


def main():
    global answer
    global question
    label.destroy()
    button.destroy()
    question = Label(root, text='Когда родился ' + str(people[a]) + ' ? Ответ введите в формате dd.mm.yyyy').pack()
    answer = Entry(root)
    answer.pack()
    button_1 = Button(root, text='Ввод', command=lambda: answer_func(main)).pack()
    
    def answer_func(main):
        global answer
        global people
        global a
        global b
        global right
        global wrong
        global question
        global answer
        global button_1
        
        end_answer = answer.get()
        if end_answer == people[b]:
            # print('Верно')
            label_1 = Label(root, text='Верно!').pack()
            right += 1
            a += 2
            b += 2
            # question.destroy()
            # answer.destroy()
            # button_1.destroy()
        else:
            otvet = ('Он родился ' + days[people[b][:2]] + ' ' + month[people[b][3:5]] + ' ' + people[b][-4:] + ' года')
            label_2 = Label(root, text=otvet).pack()
            wrong += 1
            a += 2
            b += 2
        while a < 8:
            main()
        # question.destroy()
        # answer.destroy()
        # button_1.destroy()
    # print('Количество правильных ответов: ', right)
    # print('Количество неправильных ответов: ', wrong)
    # print('Процент правильных ответов: ', 20 * right)

root.title('Викторина')
root.geometry('800x600')
label = Label(root, text='Выберите нужное из меню')
label.pack()
button = Button(root, text='Викторина', command=main)
button.pack()


root.mainloop()


