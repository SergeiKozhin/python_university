import requests

data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
result = (data['Valute']['USD']['Value'])
print('Стоимость доллара: ' + str(result) + ' рублей')