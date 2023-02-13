from tkinter import *


root = Tk()

def main():
    print('Hello')

root.title('Первая программа с GUI')
root.geometry('200x150')
label = Label(root, text='Выберите нужное из меню')
label.pack()
button = Button(root, text='Викторина', command=main)
button.pack()

root.mainloop()