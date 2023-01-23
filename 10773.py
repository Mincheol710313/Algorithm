import sys

Stack = []

N = int(sys.stdin.readline())

for i in range(N):
    number = int(sys.stdin.readline())

    if number != 0:
        Stack.append(number)
    else:
        Stack.pop()

print(sum(Stack))