# Сортируем элементы, а именно, подсчитываем, сколько раз встречается в списке каждый из них
my_list = list(map(int, input().split()))
a = {}
b = 0
for i in my_list:
    if i in a:
        a[i] += 1
    else:
        a[i] = 1
# Подсчитываем по формуле количество возможных пар из каждого значения.
for i in a:
    b += a[i]*(a[i]-1)
print(int(b/2))