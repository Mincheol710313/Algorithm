"""
깊이 우선 탐색 1
DFS를 직접 구현해보는 문제
오름차순(낮은 숫자 부터)으로 방문
또한, 양방향 edge이고 weight는 모두 1이다.
항상 문제의 '입력'과 '출력' 조건을 제대로 읽고 파악하자!!
"""
import sys
sys.setrecursionlimit(10**5)

def dfs(v):
    global count
    sequence[v] = count
    count += 1
    for i in graph[v]:
        if sequence[i] == 0 and not visited[i]:
            dfs(i)

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
count = 1

dfs(R)

for i in range(1, N+1):
    print(sequence[i])