import sys
from collections import deque

N = int(sys.stdin.readline())

Cards = deque()
Cards.extend(i for i in range(1, N+1))

while len(Cards) != 1:
    Cards.popleft()
    Cards.rotate(-1)

print(Cards[0])