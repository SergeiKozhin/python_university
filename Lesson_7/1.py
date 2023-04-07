from docxtpl import DocxTemplate

doc = DocxTemplate('document_template.docx')

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
doc.render(context)
doc.save('document.docx')