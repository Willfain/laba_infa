import random
print('Задание 1')
while True:
    try:
        m = int(input('Введите кол-во строк списка(целое, положительное число): '))
        if m < 1: raise ValueError
        break
    except ValueError: pass
while True:
    try:
        n = int(input('Введите кол-во столбцов списка(целое, положительное число): '))
        if n < 1: raise ValueError
        break
    except ValueError: pass
a = [[random.randint(0,100) for _ in range(n)] for _ in range(m)]
b = []
for s in a:
    k = 1
    for i in range(n):
        k *= s[i]
    b.append(k**(1/n))
print(f'Исходный список: \n {a} \n Список среднегеометрических: \n {b}')
print('Задание 2')
colors = {
    "red": "красный",
    "blue": "синий",
    "green": "зелёный",
    "yellow": "жёлтый",
    "black": "чёрный",
    "white": "белый",
    "orange": "оранжевый",
    "purple": "фиолетовый",
    "pink": "розовый",
    "brown": "коричневый",
    "gray": "серый",
    "gold": "золотой",
    "silver": "серебряный",
    "beige": "бежевый",
    "violet": "фиолетовый",
    "turquoise": "бирюзовый",
    "cyan": "голубой",
    "navy": "тёмно-синий",
    "lime": "лаймовый",
    "maroon": "бордовый",
    "coral": "коралловый",
    "salmon": "лососёвый",
    "olive": "оливковый",
    "teal": "сине-зелёный",
    "indigo": "индиго",
    "lavender": "лавандовый",
    "magenta": "пурпурный",
    "peach": "персиковый",
    "crimson": "малиновый",
    "khaki": "хаки"
}
print(f'Весь словарь: \n {colors}')
print(f'Перевод последнего слова: \n {colors['khaki']}')