N, M = map(int, input().split())

baskets = [0 for i in range(N)]

for _ in range(M):
    start_idx, last_idx, num = map(int, input().split())
    for idx in range(start_idx-1, last_idx):
        baskets[idx] = num

for num in baskets:
    print(num, end=" ")