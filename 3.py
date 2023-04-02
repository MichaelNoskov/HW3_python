my_list = list(map(int, input().split()))
my_list.insert(0, my_list[-1])
my_list.pop(-1)
print(*my_list)
