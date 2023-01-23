# 2중 배열 선언 방법
num_list = [[0 for col in range(100)] for row in range(100)]

N = int(input())
num = 0
for i in range(N):
    x, y = map(int, input().split())

    for j in range(y-1,y+9):
        for k in range(x-1, x+9):
            if num_list[j][k] == 0:
                num_list[j][k] = 1
                num += 1
print(num)




