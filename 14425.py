import sys

N, M = map(int, sys.stdin.readline().split())

words = set([])
for i in range(N):
    words.add(sys.stdin.readline())

num = 0
for j in range(M):
    word = sys.stdin.readline()

    if word in words:
        num += 1

print(num)