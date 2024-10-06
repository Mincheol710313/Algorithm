"""
깊이 우선 탐색 2
DFS를 직접 구현해보는 문제
내림차순(높은 숫자 부터)으로 방문
또한, 양방향 edge이고 weight는 모두 1이다.
재귀함수를 통해서 구현한 것이 아닌 Stack 자료구조와 반복문을 사용한 알고리즘!
왠만해서는 해당 알고리즘을 사용하자!!
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
    graph[i].sort()

sequence = [0] * (N+1)
visited = [False] * (N+1)
cnt = 1

stack = deque()
stack.append(R)
while stack:
    cur_node = stack.pop()
    visited[cur_node] = True
    if sequence[cur_node] == 0:
        sequence[cur_node] = cnt
        cnt += 1
    for next_node in graph[cur_node]:
        if not visited[next_node]:
            stack.append(next_node)

for i in sequence[1:]:
    print(i)