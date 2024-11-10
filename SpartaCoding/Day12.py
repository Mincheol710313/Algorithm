import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, 1, -1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

M, N, H = map(int, input().split()) # M : 가로 칸 수, N : 세로 칸수, H : 높이 칸 수

graph = [[list(map(int,input().split())) for _ in range(N)] for _ in range(H)]

q = deque()

for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 1:
                q.append((i,j,k))

while q:
    z, x, y = q.popleft()

    for i in range(6):
        nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
        if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H:
            if graph[nz][nx][ny] == 0:
                graph[nz][nx][ny] = graph[z][x][y] + 1
                q.append((nz, nx, ny))

day = 0
flag = False
for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 0:
                flag = True
            day = max(day, graph[i][j][k])

if flag:
    print(-1)
else:
    print(day-1)