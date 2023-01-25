
#1. Методами строк очистить текст от знаков препинания;

with open ('text.txt', 'r') as a:
    text = a.read()
print(text)
