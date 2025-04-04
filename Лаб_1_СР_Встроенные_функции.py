# -*- coding: utf-8 -*-
"""ИТМ-23_Хабибуллина_Камилла_Лаб_1_СР_Встроенные функции.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10lALBa-sI19RJGFV2h8LJ0fb6soN-RlX

1.1 Задача: строка кодов
"""

str0 = input('Введи четыре цифры от 65 до 91 через пробел? ')
result = ','.join(map(chr, map(int, str0.split()))).lower()
print(result)

"""1.2 Задача: длина подстроки"""

str1 = '11000111101010111'
max_seq = max(map(len, str1.split('0')))
index = str1.split('0').index('1' * max_seq)
print(f'max substring({index + 1}): {max_seq} – {"1" * max_seq}')

"""1.3 Задача: сумма ряда"""

# Изначальная последовательность
x = list(range(1, 10))  # x = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Используем метод __add__ для итеративного суммирования
while len(x) > 1:
    # Сохраняем первое число
    first_number = x[0]

    # Используем один for для суммирования
    new_sequence = [first_number.__add__(num) for num in x[1:]]

    # Обновляем x для следующей итерации
    x = new_sequence

# Выводим результат
print("Результат суммирования:", x[0])

"""1.4 Задача: минимальное число единиц"""

str0 = input('Введи четыре цифры от 65 до 91 через пробел? ')
numbers = list(map(int, str0.split()))  # Преобразуем входные данные в список целых чисел

# Функция для нахождения буквы с минимальным количеством единиц
def find_min_ones(numbers):
    # Создаем список кортежей с бинарными представлениями и количеством единиц
    binary_counts = [(chr(num), bin(num).count('1')) for num in numbers]
    # Находим букву с минимальным количеством единиц
    min_letter = min(binary_counts, key=lambda x: x[1])
    return min_letter

letter, count = find_min_ones(numbers)  # Вызываем функцию
print(f"{letter.upper()} - {count}")  # Печатаем результат

"""1.5 Задача: словарь для шифра - qwerty"""

# Определяем строку шифрования
shifr = 'qwertyuiopasdfghjklzxcvbnm'

# Создаем латинский алфавит
alpha = ''.join(chr(i) for i in range(ord('a'), ord('z') + 1))

# Создаем словари шифрования и расшифровки
to_shifr = dict(zip(alpha, shifr))
from_shifr = dict(zip(shifr, alpha))

# Пример слова для шифрования и расшифровки
word0 = 'moskva'

# Шифруем слово
word1 = ''.join(to_shifr[char] for char in word0)
print("Зашифрованное слово:", word1)

# Расшифровываем слово
word2 = ''.join(from_shifr[char] for char in word1)
print("Расшифрованное слово:", word2)

"""1.6 Задача: сумма бит"""

# Определяем натуральный ряд
n = 3
m = 5

# Суммируем количество единиц в двоичном представлении
total_ones = sum(map(lambda x: bin(x).count("1"), range(n, m + 1)))

print("Суммарное количество 1 в двоичном представлении чисел от", n, "до", m, ":", total_ones)