"""
풍선 터뜨리기
1번 왼쪽 -> N번, N번 오른쪽 -> 1번(중요)
풍선 안에 들어있는 종이에 적혀있는 값만큼 이동하여 풍선 터뜨리기
터진 풍선의 번호 차례대로 나열하여 출력
Dictionary와 
"""
from collections import deque
N = int(input()) # 최대 숫자
num_list = list(map(int, input().split())) 
num_deq = deque()
for i in range(1, N+1):
    num_deq.append([i,num_list[i-1]]) 
print(num_deq)

for _ in range(N):
    num = num_deq.popleft()
    print(num[0])
    rot = num[1]
    if rot > 0:
        rot -= 1
    num_deq.rotate(-rot)
    print(num_deq)