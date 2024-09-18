"""
음료수 얼려 먹기
"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # N : 세로, M : 가로

# Graph 생성
# 입력이 숫자들로 연속된 문자열일 경우
graph = []
for i in range(N):
    graph.append(list(map(int, input().strip()))) # strip() 메서드를 이용하여 불필요한 공백 문자를 제거

# DFS를 이용한 연결요소 개수 파악
def dfs(x, y):
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    
    if graph[x][y] == 0:
        graph[x][y] = 1
        # 상, 하, 좌, 우의 위치도 모두 재귀적으로 호출
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

count = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j) == True:
            count += 1
    
# 연결 요소 개수 출력
print(count)