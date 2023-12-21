# На вход автоматически подаются две строки frac1 и frac2 вида a/b - дробь с числителем и знаменателем.
# Напишите программу, которая должна возвращать сумму и произведение дробей.
# Для проверки своего кода используйте модуль fractions.

frac1 = "1/2"
frac2 = "1/3"

from fractions import Fraction

nums1 = [int(n) for n in frac1.split("/")]
nums2 = [int(n) for n in frac2.split("/")]

ch1 = nums1[0]
ch2 = nums2[0]
zn1 = nums1[-1]
zn2 = nums2[-1]

s1 = ch2 * zn1
s2 = ch1 * zn2
b = zn1 * zn2
summ = s1 + s2
print(f'Сумма дробей: {summ}/{b}')

p1 = ch1 * ch2
p2 = zn1 * zn2
print(f'Произведение дробей: {p1}/{p2}')

print(f'Сумма дробей: {Fraction(ch1, zn1) + Fraction(ch2, zn2)}')
print(f'Произведение дробей: {Fraction(ch1, zn1) * Fraction(ch2, zn2)}')
