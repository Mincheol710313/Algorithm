from collections import deque

def solution(n, computers):
    answer = 0
    
    # 인접 행렬을 사용한 Graph 
    graph = [[0] * n for _ in range(n)]

    visited = [0] * n

    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if computers[i][j] == 1:
                graph[i][j] = 1

    q = deque()
    count = 1
    
    for i in range(n):
        past = visited[i]
        q.append(i)

        while q:
            v = q.popleft()

            if visited[v] == 0:
                visited[v] = count

                for idx in range(n):
                    if graph[v][idx] == 1 and visited[idx] == 0:
                        q.append(idx)
        
        if past != visited[i]:
            count += 1

    answer = max(visited)

    return answer

# 테스트 케이스
print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))

