import datetime
today = datetime.datetime.now()
timedelta = datetime.timedelta(days=10)
time = today + timedelta
print (time)


import math
x=7.9

print (math.floor(x))
print (math.ceil(x))

y=8
print (math.pow(y , 2))

z=-9
print (math.fabs(z))


import json

# Python-словарь
data = {
    "name": "Alice",
    "age": 25,
    "is_student": False,
    "courses": ["Math", "Physics"]
}

# Преобразование в JSON
json_data = json.dumps(data)
print(json_data)



import json

# Строка в формате JSON
json_data = '{"name": "Alice", "age": 25, "is_student": false, "courses": ["Math", "Physics"]}'

# Преобразование JSON в Python-объект
data = json.loads(json_data)
print(data)


import re
text="anu edil olj mans"
x= "anu"

match = re.search(x , text)
if match :
    print("Naideno", match.group())
else:
    print("Ne naideno")



import re

text = "яблоко, апельсин, банан, яблоко"
pattern = "яблоко"

matches = re.findall(pattern, text)
print(matches)


import re

text = "яблоко, апельсин, банан, яблоко"
pattern = ", "

split_text = re.split(pattern, text)
print(split_text)




import re

text = "яблоко, апельсин, банан"
pattern = "банан"
replacement = "груша"

new_text = re.sub(pattern, replacement, text)
print(new_text)



import re

text = "Мой номер телефона: 123-456-7890."
pattern = r"\d+"  # Ищем последовательность цифр

matches = re.findall(pattern, text)
print(matches)




import re

text = "Это пример текста, который мы будем разбирать."
pattern = r"\b\w+\b"  # Находим все слова

words = re.findall(pattern, text)
print(words)



import re

text = "Hello World! How are you?"
pattern = r"\s"  # Находим все пробельные символы
replacement = "_"

new_text = re.sub(pattern, replacement, text)
print(new_text)






import json

data = {
    "name": "Alice",
    "age": 25,
    "is_student": False,
    "courses": ["Math", "Physics"]
}

# Преобразование в JSON с отступами
json_data = json.dumps(data, indent=4)
print(json_data)
