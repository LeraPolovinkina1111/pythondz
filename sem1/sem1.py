year = int(input("Введите год "))
REFORM = 1582
BIGYEAR = 400
SMALLYEAR = 4
LARGEYEAR = 100
MULTIPLE = 0
if year < REFORM:
    result = 'Григориантский календарь не введен'
elif year % BIGYEAR == MULTIPLE:
    result = 'Високосный год'
elif year % LARGEYEAR == MULTIPLE:
    (
        result) = 'Не високосный год'
elif year % SMALLYEAR == MULTIPLE:
    result = f'{year} - високосный год'

print(result)
