print('задание 1')
for i in range(10,21):
    print(i**2)
print('задание 2')
M, m1 = 80, 400
for m2 in range(100,301,20):
    print(f'M = {M}, m1 = {m1}, m2 = {m2}, a = {((m2-m1)/(m1 + m2 + M/2))*9.81}')
#задание 3
while True:
    try:
        N = int(input('Введите целое положительное число N '))
        s = 1
        for i in range(3,2*(N-1)+1,2):
            s += i
            print('Текущая сумма:',s)
        print('Квадрат N =',s)
        break
    except ValueError:
        print('Это не целое положительное число, Введите целое положительное число')

