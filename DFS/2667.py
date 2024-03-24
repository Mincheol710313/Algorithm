import sys

def dfs(x, y):
    global house
    if x <= -1 or x >= N or y <= -1 or y >= N:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        house += 1
        dfs(x - 1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

sys.setrecursionlimit(10**5)
input = sys.stdin.readline
N = int(input().rstrip())  # 아파트 단지의 가로, 세로의 길이

# 2차원 리스트로 map 구현
graph = []
for _ in range(N):
    graph.append(list(map(int, input().rstrip())))

result = 0
apart_dict = {}
for i in range(N):
    for j in range(N):
        house = 0
        if dfs(i, j) == True:
            result += 1
            apart_dict[result] = house

print(result)
for i in sorted(apart_dict.values()):
    print(i)
