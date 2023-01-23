import sys
from collections import deque

deque = deque()

N = int(sys.stdin.readline())

for i in range(N):
    words = list(sys.stdin.readline().split())
    order = words[0]

    if order == "push_front":
        deque.appendleft(int(words[1]))
    elif order == "push_back":
        deque.append(int(words[1]))
    elif order == "pop_front":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.popleft())
    elif order == "pop_back":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.pop())
    elif order == "size":
        print(len(deque))
    elif order == "empty":
        if len(deque) == 0:
            print(1)
        else:
            print(0)
    elif order == "front":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])
    elif order == "back":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[len(deque)-1])