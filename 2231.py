import sys

N = int(sys.stdin.readline())

i = 1
while True:
    result = i
    num = str(i)

    for j in range(len(num)):
        result += int(num[j])

    if result == N:
        break

    i += 1

print(i)
