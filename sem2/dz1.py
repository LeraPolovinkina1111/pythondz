# Напишите программу, которая получает целое число num и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.
num=0
number = num
base = 16
letters = '0123456789ABCDEF'
new = ''

while num > 0:
    num, remainder = divmod(num, base)

    new = letters[remainder] + new

print(f'Шестнадцатеричное представление числа: {new}')
print(f'Проверка результата: {hex(number)}')
