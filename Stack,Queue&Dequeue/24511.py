from collections import deque

# queuestack 구조 설정
N = int(input())  # 자료 구조 개수
ls = deque()
col_list = list(map(int, input().split()))  # 자료구조 list
col_num_list = list(map(int, input().split()))  # 자료구조에 들어있는 원소 list
for idx in range(N):
    if col_list[idx] == 0:
        ls.append(col_num_list[idx])

# 수열 처리
M = int(input())  # 삽입할 수열의 길이
num_list = list(map(int, input().split()))  # 수열 list
for num in num_list:
    ls.appendleft(num)
    print(ls.pop(), end=" ")
