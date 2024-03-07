import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

people = deque()
people.extend(i for i in range(1, N+1))

remove_list = []

# 해당 위치에 있지 않으면 앞에 있는 원소가 뒤에 붙여진다!
while len(people) != 0:
    people.rotate(-(K-1))
    remove_list.append(people.popleft())

if N == 1:
    print("<1>")
else:
    for i in range(N):
        if i == 0:
            print(f"<{remove_list[i]},", end="")
        elif i == N - 1:
            print(f" {remove_list[i]}>", end="")
        else:
            print(f" {remove_list[i]},", end="")