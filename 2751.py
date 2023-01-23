import sys

N = int(sys.stdin.readline().strip())

num_list = []
for i in range(N):
    num_list.append(int(sys.stdin.readline().strip()))
num_list.sort()

for i in range(N):
    print(num_list[i])