""" 매일 한 번씩 익숙해질 때까지 구현해보기! 
Daily
D-1 : 2024.10.10
D-2 : 2024.10.12
"""
"""
Graph 자료구조
1. 인접 행렬(Adjacency Matrix) : 2차원 배열로 그래프의 연결관계를 표현 -> 해당 방식이 더 빠르다!
2. 인접 리스트(Adjacency List) : 리스트로 그래프의 연결관계를 표현 
"""

""" 
BFS(Binary-First Search) : 너비 우선 탐색, 가까운 노드부터 우선적으로 탐색하는 알고리즘
Queue(FIFO) 자료구조를 이용!!
"""
from collections import deque

n = 8

graph = [
    [0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 1],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 1, 0]
]

visited = [False] * 8

def bfs(s):
    q = deque()
    q.append(s)
    
    while q:
        v = q.popleft()

        if not visited[v]:
            visited[v] = True
            print(chr(v + ord('A')), end=" ")

        for idx in range(n):
            if graph[v][idx] == 1  and not visited[idx]:
                if idx not in q:
                    q.append(idx)  

bfs(0)
