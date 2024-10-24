N = int(input())

sum_cost = []

for i in range(N):
    sum_cost.append(list(map(int, input().split())))

for idx in range(1, N):
    sum_cost[idx][0] = min(sum_cost[idx-1][1], sum_cost[idx-1][2]) + sum_cost[idx][0]
    sum_cost[idx][1] = min(sum_cost[idx-1][0], sum_cost[idx-1][2]) + sum_cost[idx][1]
    sum_cost[idx][2] = min(sum_cost[idx-1][0], sum_cost[idx-1][1]) + sum_cost[idx][2]

print(min(sum_cost[-1][0], sum_cost[-1][1], sum_cost[-1][2]))
