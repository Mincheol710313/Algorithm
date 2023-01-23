# collection 패키지와 deque
import sys
from collections import deque

Queue = deque()

N = int(sys.stdin.readline())

for i in range(N):
    words = list(sys.stdin.readline().split())
    order = words[0]

    if order == "push":
        Queue.append(int(words[1]))
    elif order == "pop":
        if len(Queue) == 0:
            print(-1)
        else:
            print(Queue.popleft())
    elif order == "size":
        print(len(Queue))
    elif order == "empty":
        if len(Queue) == 0:
            print(1)
        else:
            print(0)
    elif order == "front":
        if len(Queue) == 0:
            print(-1)
        else:
            print(Queue[0])
    elif order == "back":
        if len(Queue) == 0:
            print(-1)
        else:
            print(Queue[len(Queue)-1])