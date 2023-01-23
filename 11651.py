import sys

N = int(input())  # 좌표의 개수

pos = []
for i in range(N):
    pos.append(list(map(int, sys.stdin.readline().split())))

# sort 부분
pos.sort(key=lambda x: (x[1], x[0]))

for i in range(N):
    print(pos[i][0], pos[i][1])