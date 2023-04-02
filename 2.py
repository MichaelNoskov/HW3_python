# Пока строка не достигла нужной длины, прибавляем к ней символы, согласно последовательности
amount = int(input())
diction = {'1': '0', '0': '1'}
a = '0'
b = ''
while len(a) < amount:
    b = ''
    for char in a:
        if len(a+b) < amount:
            b += diction[char]
    a += b
print(a)
