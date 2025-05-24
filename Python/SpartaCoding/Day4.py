from collections import deque

N, M, R = map(int, input().split())

visited = [0] * N

graph = [[0] * N for _ in range(N)]

# 간선 관계 파악
for _ in range(M):
    x, y = map(int, input().split())

    graph[x-1][y-1] = 1
    graph[y-1][x-1] = 1

q = deque()
q.append(R)

count = 1

while q:
    v = q.popleft()

    if visited[v-1] == 0:
        visited[v-1] = count
        count += 1

    for idx in range(N):
        if graph[v-1][idx] == 1 and visited[idx] == 0:
            q.append(idx+1)

for idx in range(N):
    print(visited[idx])