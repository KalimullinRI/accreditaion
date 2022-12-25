import random
import math

while (True):
    try:
        original = float(input('Введи исходное число: '))
        result = float(input('Введи итоговое среднее число: '))
        procent = int(input('Введи процент отклонения: '))
        sko_result = float(input('Введи СКО: '))
        r = int(input('Сколько списков показать? '))
        break
    except ValueError:
        print("Неверный ввод. В десятичных числах должна быть (.) - не (,)")


'''Создаем список с учетом процента
отклонения с шагом 0.001.'''

delta_proc = original * procent * 0.01
minimum = original - delta_proc
maximum = original + delta_proc

# Создаем функцию, которая генерирует и записывает значения в список


def float_range(start, stop, step):
    while start <= stop:
        yield float(start)
        start += float(step)


# Вызываем функцию, в качестве аргументов передаем возможное
# Минимальное и максимальное значения, с шагом 0.001
x = list(float_range(minimum, maximum, 0.001))
numbers = [round(i, 3) for i in x]  # Округляем все значения до тысячных

print(' \n')
print(numbers)


def foo(numbers):
    '''Функция, которая будет
находить значения с заданным условием.'''
    while (True):
        x = ''
        x = random.choices(numbers, k=3)
        summ = sum(x)
        diff = (result * 5 - summ) * 1000

        def number_split(diff):
            remains = [diff//2, diff//2+diff % 2]
            round_remains = [round(i*0.001, 3) for i in remains]
            return round_remains
        xx = x + number_split(diff)
        random.shuffle(xx)
        sko = round(math.sqrt(sum([((((i-result)**2)/4)) for i in xx])), 4)
        low = result * 5 - maximum * 2
        high = result * 5 - (minimum + maximum)
        if low <= summ <= high and sko == sko_result:
            print(f'{xx} {sko}')
            break


print(' \n')
[foo(numbers) for i in range(r)]
