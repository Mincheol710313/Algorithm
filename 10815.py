# list 안에 있는 원소를 찾을 때에는 O(n)의 시간 복잡도를 가지지만
# set 안에 원소가 있는지를 확인할 때에는 O(1)의 시간 복잡도를 가지기 떄문에 set 자료구조를 사용하는 것이 좋다!

import sys

N = int(sys.stdin.readline())
cards = set(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

for i in nums:
    if i in cards:
        print(1, end=" ")
    else:
        print(0, end=" ")