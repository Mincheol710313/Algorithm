""" 매일 한 번씩 익숙해질 때까지 구현해보기! 
Daily
D-1 : 2024.10.10
D-2 : 2024.10.12
D-Day : 2024.10.13
"""
"""
Graph 자료구조
1. 인접 행렬(Adjacency Matrix) : 2차원 배열로 그래프의 연결관계를 표현 -> 해당 방식이 더 빠르다!
2. 인접 리스트(Adjacency List) : 리스트로 그래프의 연결관계를 표현 
"""

""" 
DFS(Binary-First Search) : 깊이 우선 탐색, 깊은 부분을 우선적으로 탐색하는 알고리즘
Stack(FILO) 자료구조 or Recursive Function(재귀 함수) 이용 -> Recursive Function 사용 방법 익히기!
"""

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

def dfs(s, n):

    if not visited[s]:
        visited[s] = True
        print(chr(s + ord('A')), end=" ")

    for idx in range(n):
        if graph[s][idx] == 1 and not visited[idx]:
            dfs(idx, n)
    
dfs(0, n)