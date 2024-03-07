import sys
from collections import deque

deq = deque()

N = int(sys.stdin.readline().rstrip())

for _ in range(N):
    command = list(map(int, sys.stdin.readline().split()))
    num = 0
    if len(command) != 1:
        num = command[-1]
    command = int(command[0])

    if command == 1:
        deq.appendleft(num)
    elif command == 2:
        deq.append(num)
    elif command == 3:
        if deq:
            print(deq.popleft())
        else:
            print(-1)
    elif command == 4:
        if deq:
            print(deq.pop())
        else:
            print(-1)
    elif command == 5:
        print(len(deq))
    elif command == 6:
        if deq:
            print(0)
        else:
            print(1)
    elif command == 7:
        if deq:
            print(deq[0])
        else:
            print(-1)
    elif command == 8:
        if deq:
            print(deq[-1])
        else:
            print(-1)