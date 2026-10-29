import random
print('Задание 1')
s = input('Введите текст: ')
wrds,w = [],''
for i in s + ' ':
    if i in ' .,!?\n':
        if len(w) > 0: wrds.append(w); w = ''
    else: w += i
lttrs,cnt = [],[]
for word in wrds:
    f1 = word[0].lower()
    f = False
    for i in range(len(lttrs)):
        if lttrs[i] == f1:
            cnt[i] += 1; f = True; break
    if not f:
        lttrs.append(f1);cnt.append(1)
bl,mc = '',0
for i in range(len(cnt)):
    if cnt[i] > mc: mc,bl = cnt[i],lttrs[i]
print(f'На Букву {bl} встречается больше всего слов: {mc}')
print('Задание 2 ')
s = input('Введите текст: ')
wrds,w = [],''
for i in s + ' ':
    if i in ' .,!?\n':
        if len(w) > 0: wrds.append(w); w = ''
    else: w += i
g = 'аеёиоуыэюяaeiouy'
mg,bw = -1,''
for word in wrds:
    c = 0
    for i in word.lower():
        if i in g: c += 1
    if c > mg: mg,bw = c,word
print(f'Слово с наибольшим количеством гласных: {bw}')
print('Задание 3')
while True:
    try:
        n = int(input("Введите размер списка(целое, положительное число): "))
        if n < 1: raise ValueError
        break
    except ValueError: pass
a = [random.randint(-100,100) for _ in range(n)]
print(f'Исходный список:\n {a}')
m,mi = -10**10,0
for i in range(len(a)):
    if a[i] > m: m = a[i]; mi = i
s = 0
for i in range(mi):
    if a[i] > 0: s += a[i]
print(f'Сумма положительных чисел до максимального: {s}')
b = a[:]
a = []
for i in range(len(b)-1,-1,-1):
    a.append(b[i])
print(f'Обратный список: \n {a}')
