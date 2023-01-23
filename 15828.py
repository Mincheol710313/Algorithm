import sys
from collections import deque

N = int(sys.stdin.readline())
buffer = deque()

while True:
    num = int(sys.stdin.readline())

    if num == -1:
        break

    if num == 0:
        buffer.popleft()
        continue

    if len(buffer) == N:
        continue

    buffer.append(num)

if len(buffer) == 0:
    print("empty")
else:
    for i in range(len(buffer)):
        print(buffer[i], end=" ")
