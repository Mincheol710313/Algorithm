from collections import deque

N = int(input())

A, B = map(int, input().split())

M = int(input())

f = [[0] * N for _ in range(N)]
related = [0] * N
 
for i in range(M):
    x, y = map(int, input().split())

    f[x-1][y-1] = 1
    f[y-1][x-1] = 1

s = deque()
s.append(A-1)

while s:
    v = s.pop()

    for idx in range(N):
        if f[v][idx] == 1 and related[idx] == 0 and idx != (A-1):
            related[idx] = related[v] + 1
            s.append(idx)

if related[B-1] == 0:
    print(-1)
else:
    print(related[B-1])