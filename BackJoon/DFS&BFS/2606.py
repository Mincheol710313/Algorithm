import sys
from collections import deque
input = sys.stdin.readline
N = int(input().rstrip())  # 컴퓨터의 수
M = int(input().rstrip())  # 직접 연결 되어 있는 컴퓨터의 쌍 수

# graph 구현 - 인접 리스트 방식
graph = [[] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# BFS 구현
queue = deque()
queue.append(1)
visited = [False] * (N+1)
visited[1] = True
cnt = 0
while queue:
    v = queue.popleft()
    if v != 1 and not visited[v]:
        cnt += 1
        visited[v] = True
    for next_node in graph[v]:
        if not visited[next_node]:
            queue.append(next_node)

print(cnt)