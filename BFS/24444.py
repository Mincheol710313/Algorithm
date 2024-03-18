"""
너비 우선 탐색 1
BFS를 직접 구현해보는 문제
오름차순(낮은 숫자 부터)으로 방문
양방향 edge, weight 는 모두 1
"""
import sys
from collections import deque

def bfs(R):
    count = 1
    queue = deque([R])
    visited[R] = True
    while queue:
        v = queue.popleft()
        sequence[v] = count
        count += 1
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

input = sys.stdin.readline
N, M, R = map(int, input().split())  # N : Node 수, M : edge 수, R : 시작 Node

# 인접 리스트 형식
graph = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# graph 노드 순서 sort(오름차순)
for i in range(1, N+1):
    graph[i].sort()

sequence = [0] * (N+1)
visited = [False] * (N+1)

bfs(R)

for i in range(1, N+1):
    print(sequence[i])