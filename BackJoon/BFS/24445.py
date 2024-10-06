"""
너비 우선 탐색 2
BFS를 직접 구현해보는 문제
내림차순(낮은 숫자 부터)으로 방문
양방향 edge, weight 는 모두 1
"""
import sys
from collections import deque

input = sys.stdin.readline
N, M, R = map(int, input().split())  # N : Node 수, M : edge 수, R : 시작 Node

# 인접 리스트 형식
graph = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# graph 노드 순서 sort(내림차순)
for i in range(1, N+1):
    graph[i].sort(reverse=True)

sequence = [0] * (N+1)
queue = deque()
queue.append(R)
sequence[R] = 1
cnt = 2

while queue:
    cur_node = queue.popleft()
    for next_node in graph[cur_node]:
        if sequence[next_node] == 0:
            sequence[next_node] = cnt
            cnt += 1
            queue.append(next_node)

for i in sequence[1:]:
    print(i)