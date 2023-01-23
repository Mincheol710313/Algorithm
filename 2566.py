import sys

num_list = []
for i in range(9):
    num_list.append(list(map(int, sys.stdin.readline().split())))

max_num = 0
for i in range(9):
    if max_num < max(num_list[i]):
        max_num = max(num_list[i])
print(max_num)

for i in range(9):
    for j in range(9):
        if num_list[i][j] == max_num:
            print(i+1, j+1)