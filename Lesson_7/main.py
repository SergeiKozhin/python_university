from docxtpl import DocxTemplate
import csv
import json

data = [
    ['Mazda', 'CX-5', '7.4', '2390000']
]

with open('data.txt', 'w') as file:
    for row in data:
        file.write(','.join(row))

template = DocxTemplate('document_template.docx')

with open('data.txt', 'r') as file:
    rows = [line.strip().split(',') for line in file]

context = {'cars': []}
for row in rows:
    context['cars'].append({
        'brand': row[0],
        'model': row[1],
        'fuel_consumption': row[2],
        'price': row[3]
    })
template.render(context['cars'][0])
template.save('document.docx')

with open('data.txt', 'r') as in_file, open('data.csv', 'w', newline='') as out_file:
    writer = csv.writer(out_file)
    for row in csv.reader(in_file):
        writer.writerow(row)

with open('data.txt', 'r') as file:
    rows = [line.strip().split(',') for line in file]

cars = []
for row in rows:
    cars.append({
        'brand': row[0],
        'model': row[1],
        'fuel_consumption': row[2],
        'price': row[3]
    })

with open('data.json', 'w') as file:
    json.dump(cars, file)
