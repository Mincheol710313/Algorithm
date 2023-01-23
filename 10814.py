import sys

N = int(sys.stdin.readline())

personal = []
for i in range(N):
    personal.append(list(map(str, sys.stdin.readline().split())))

personal.sort(key=lambda x: (int(x[0])))

for i in range(N):
    print(personal[i][0], personal[i][1])