from collections import deque

# 나이트가 이동할 수 있는 위치
dx = [-2, -1, 1, 2, 2, 1, -1, -2] 
dy = [1, 2, 2, 1, -1, -2, -2, -1]

T = int(input()) # 테스트 케이스 개수

for _ in range(T):
    I = int(input()) # 체스판의 한변의 길이
    graph = [[0] * I for _ in range(I)]

    X, Y = map(int, input().split()) # 현재 위치
    wX, wY = map(int, input().split()) # 이동하려고 하는 위치

    ans = 0

    q = deque()
    q.append((X, Y))

    while q:
        v = q.popleft()

        x, y = v[0], v[1]

        if x == wX and y == wY:
            ans = graph[x][y] 
            break

        for idx in range(8):
            nx = x + dx[idx]
            ny = y + dy[idx]

            if 0 <= nx < I and 0 <= ny < I and graph[nx][ny] == 0:
                q.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1    
    
    ans = graph[wX][wY]
    print(ans)
