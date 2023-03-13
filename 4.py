n = -1 # создаём переменную с любым значением, кроме 0
count_a = 0
i = 0
count_b = 0
while(n != 0):
    n = int(input()) # перезаписываем значение
    if n == 0:
        break
    if i < n and i != 0: # сравниваем наименьшее
        count_a += 1
    if i > n and i != 0: # сравниваем наибольшее
        count_b += 1
    i = n # запоминаем новое значение для последующего сравнения
if count_a > count_b: # какой из случаев больше
    print(count_a)
else:
    print(count_b)