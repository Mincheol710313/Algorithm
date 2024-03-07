N, M = map(int, input().split())
basket_list = [i for i in range(1, N+1)]

for _ in range(M):
    first_idx, last_idx = map(int, input().split())
    if first_idx == last_idx:
        continue

    basket_list[first_idx-1], basket_list[last_idx-1] = basket_list[last_idx-1], basket_list[first_idx-1]

for num in basket_list:
    print(num, end=" ")
