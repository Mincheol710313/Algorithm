N = int(input())  # 좌표의 개수

pos = []
for i in range(N):
    pos.append(list(map(int, input().split())))
pos.sort()

for i in range(N):
    print(pos[i][0], pos[i][1])