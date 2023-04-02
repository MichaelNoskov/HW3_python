# Простая итерация и сравнение с элементом противоположной стороны (для этого приходится использовать вложенный список)
def IsSymmetric(a):
    l = len(a)
    for i in range(l):
        for j in range(i + 1, l):
            if a[i][j] != a[j][i]:
                return 'NO'
    return 'YES'


n = int(input())
A = []
for i in range(n):
    A.append(list(map(int, input().split())))
print(IsSymmetric(A))
