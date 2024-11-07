from collections import deque

# 도시의 개수, 도로의 개수, 거리 정보(최단 거리), 출발 도시의 번호
N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N)]
dist = [0] * N

for _ in range(M):
    x, y = map(int, input().split())

    graph[x-1].append(y)
    
q = deque()
q.append(X)

while q:
    v = q.popleft()

    for i in graph[v-1]:
        if dist[i-1] == 0 and i != X:
            q.append(i)
            dist[i-1] = dist[v-1] + 1

exist = False
for idx in range(N):
    if dist[idx] == K:
        print(idx+1)
        exist = True

if not exist: print(-1)