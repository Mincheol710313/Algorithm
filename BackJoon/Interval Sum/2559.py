N, M = map(int, input().split())
temp_list = list(map(int, input().split()))
sum_values = 0
prefix_sum = [0]
for temp in temp_list:
    sum_values += temp
    prefix_sum.append(sum_values)

result = prefix_sum[M] - prefix_sum[0]
for i in range(1, N-M+1):
    if result < prefix_sum[i+M] - prefix_sum[i]:
        result = prefix_sum[i+M] - prefix_sum[i]
print(result)