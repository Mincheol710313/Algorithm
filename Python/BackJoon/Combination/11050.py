from itertools import combinations
N, K = map(int, input().split())
ls = [i for i in range(1, N+1)]
print(len(list(combinations(ls, K))))