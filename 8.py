operand = ['+', '-', '*']


def math(a, b, c):
    # Просто функция, позволяющая выполнять операции, если те записаны в строковом формате
    a = int(a)
    b = int(b)
    if c == '+':
        return str(a + b)
    elif c == '-':
        return str(a - b)
    elif c == '*':
        return str(a * b)


operations = input().split()

# В постфиксной форме доходим до знака - затем делаем с двумя предыдущими значениями то, что говорит знак (*;+;-)
# Потом заменяем действие и два этих числа на полученное значение и повторяем всё снова, пока длина не станет равняться
# одному. Этот элемент - результат выражения
while len(operations) > 1:
    for i, element in enumerate(operations):
        if element in operand:
            operations[i] = math(operations[i-2], operations[i-1], element)
            operations.pop(i-1)
            operations.pop(i-2)
            break
print(*operations)
