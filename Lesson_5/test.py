from tkinter import *


root = Tk()

answer = 0
end_answer = 0
def answer_func():
    end_answer = answer.get()
    print(end_answer)

def main():
    global root
    global label
    global button
    label.destroy()
    button.destroy()
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
    wrong= 0
    count = 0
    for i in people:

        question = Label(root, text='Когда родился ' + str(i) + ' ? Ответ введите в формате dd.mm.yyyy')
        question.pack()
        global answer
        answer = Entry(root)
        answer.pack()
        answer.focus()
        button_1 = Button(root, text='Ввод', command=answer_func).pack()
        # button_1.pack()
        answer.focus()
        # count +=1
        # end_answer = answer.get()
        # print(end_answer)
        # if end_answer == people[i]:
        #     print('Верно')
        #     right += 1
        #     question.destroy()
        #     answer.destroy()
        #     button_1.destroy()
        # else:
        #     print('Он родился ' + days[people[i][:2]] + ' ' + month[people[i][3:5]] + ' ' + people[i][-4:] + ' года')
        #     wrong += 1
        #     question.destroy()
        #     answer.destroy()
        #     button_1.destroy()
    # print('Количество правильных ответов: ', right)
    # print('Количество неправильных ответов: ', wrong)
    # print('Процент правильных ответов: ', 20 * right)

root.title('Первая программа с GUI')
root.geometry('800x300')
label = Label(root, text='Выберите нужное из меню')
label.pack()
button = Button(root, text='Викторина', command=main)
button.pack()

root.mainloop()


