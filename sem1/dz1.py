# Треугольник существует только тогда,
# когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника.
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других,
# то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним,
# равнобедренным или равносторонним.

# Треугольник существует
# Треугольник с

# Треугольник существует
# Треугольник равнобедренный

# Треугольник существует
# Треугольник разносторонний

# Треугольник не существует

a = 4
b = 2
c = 2

if a + b < c or a + c < b or c + b < a:
    print('Треугольник не существует')
elif a == b == c:
    print('Треугольник существует')
    print('Треугольник равносторонний')

elif a == b or a == c or c == b:
    print('Треугольник существует')
    print('Треугольник равнобедренный')

elif a != b and b != c and c != a:
    print('Треугольник существует')
    print('Треугольник разносторонний')
