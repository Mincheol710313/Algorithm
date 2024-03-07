import math
import sys
M, N = map(int, sys.stdin.readline().split())

array = [True for i in range(N+1)]

for i in range(2, int(math.sqrt(N))+1):
    if array[i]:
        j = 2
        while i * j <= N:
            array[i * j] = False
            j += 1

for i in range(M, N+1):
    if array[i]:
        print(i)