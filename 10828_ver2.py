import sys

Stack = []

N = int(sys.stdin.readline())

for i in range(N):
    words = list(sys.stdin.readline().split())
    order = words[0]

    if order == "push":
        Stack.append(int(words[1]))
    elif order == "pop":
        if len(Stack) == 0:
            print(-1)
        else:
            print(Stack.pop())
    elif order == "size":
        print(len(Stack))
    elif order == "empty":
        if len(Stack) == 0:
            print(1)
        else:
            print(0)
    elif order == "top":
        if len(Stack) == 0:
            print(-1)
        else:
            print(Stack[-1])