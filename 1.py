# Чтобы проверить,что конь попадёт на следующую клетку, нужно посмотреть различие по иксу и по игрику. Нужно сравнивать
# по модулю, ведь идти может понадобиться и в обратную сторону. Мне лень это делать, поэтому в список проверки я добавил
# отрицательные значения.
# Также нужно проверить, что он идет по горизонтали на 2, а по вертикали на 1, или на оборот, но не одновременно
def can_eat(a, b):
    x1, y1 = a
    x2, y2 = b
    keys = [1, 2, -1, -2]
    x = x1 - x2
    y = y1 - y2
    if x in keys and y in keys and x != y:
        return True
    return False


result = can_eat((2, 1), (4, 2))
print(result)
