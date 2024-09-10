dN, M, K, X = map(int, input().split())

# 방향을 고려하여 인접리스트 방식의 Graph 구현
graph = [[] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

# DFS를 통해서 X에서 출발해서 거리가 K인 도시 반환

