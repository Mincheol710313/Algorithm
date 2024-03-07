import sys
num_stack = []

N = int(input())  # 명령의 수
for _ in range(N):
    order = sys.stdin.readline().rstrip()
    if len(order) > 1:
        num = int(order[2:])
        num_stack.append(num)
    else:
        order = int(order[0])
        if order == 2:
            if len(num_stack) == 0:
                print(-1)
            else:
                print(num_stack[-1])
                num_stack.pop()
        elif order == 3:
            print(len(num_stack))
        elif order == 4:
            if len(num_stack) == 0:
                print(1)
            else:
                print(0)
        elif order == 5:
            if len(num_stack) == 0:
                print(-1)
            else:
                print(num_stack[-1])

