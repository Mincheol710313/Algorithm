""" 게임 개발 """
# 방향 벡터 -> 북 동 남 서
dx = [-1, 0, 1, 0] 
dy = [0, 1, 0, -1]

N, M = map(int, input().split()) # 맵 크기 세로 X 가로
A, B, d = map(int, input().split()) # (A, B) 위치에 방향은 d -> 0 : 북쪽, 1 : 동쪽, 2 : 남쪽, 3 : 서쪽

# 맵 제작
# 0 : 육지, 1: 바다 
m = []
for i in range(N):
    m.append(list(map(int, input().split())))

visited = [(A, B)]

# 이동 구현
turn_time = 0
while(True):
    if (d - 1) < 0:
        d = 3
    else:
        d -= 1

    # 다음 위치
    nA = A + dx[d]
    nB = B + dy[d]

    # 회전한 후 전진한 경우
    if m[nA][nB] == 0 and (nA, nB) not in visited:
        A = nA
        B = nB
        visited.append((A, B))
        turn_time = 0
        continue
    else: # 회전한 후 전진하지 못하는 경우
        turn_time += 1
        if turn_time == 4: # 네 방향 모두 회전한 경우
            nA = A - dx[d]
            nB = B - dy[d]
            if m[nA][nB] == 0:
                A = nA
                B = nB
            else:
                break
            turn_time = 0

# 방문한 칸 수 출력
print(len(visited))