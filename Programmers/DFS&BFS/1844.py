import sys
from collections import deque
sys.setrecursionlimit(10**6)

def solution(maps):
    answer = -1

    # 이동 방향 벡터 -> 남, 동, 북, 서
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    # visited 설정
    n = len(maps)
    m = len(maps[0])

    visited = [[0] * m for _ in range(n)]
    dis = [[0] * m for _ in range(n)]
    dis[0][0] = 1

    q = deque()
    q.append((0, 0))
    
    while q:
        position = q.popleft()

        x, y = position[0], position[1]
        if visited[x][y] == 0:
            visited[x][y] = 1

            for idx in range(4):
                nx = x + dx[idx]
                ny = y + dy[idx]

                if nx >= 0 and nx < n and ny >=0 and ny < m:
                    if maps[nx][ny] == 1 and visited[nx][ny] == 0:
                        dis[nx][ny] = dis[x][y] + 1
                        q.append((nx, ny))
    
    if dis[n-1][m-1] != 0:
        answer = dis[n-1][m-1]

    return answer

# 테스트 케이스
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))