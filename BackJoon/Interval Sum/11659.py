"""
Interval Sum(구간 합) 알고리즘
Prefix Sum을 구해두자!!
Prefix Sum은 N개의 수의 위치 각각에 대한 합
그렇게 구한 후 Query에 대한 값은 P[Right] - P[Left-1]로 구한다.
Query는 [Left, Right]로 구간을 나타낸다.
해당 알고리즘의 수행 시간은 O(N + M)이다!
"""
N, M = map(int, input().split())
num_list = list(map(int, input().split()))
sum_value = 0
prefix_sum = [0]
for i in num_list:
    sum_value += i
    prefix_sum.append(sum_value)

for _ in range(M):
    l, r = map(int, input().split())
    print(prefix_sum[r]-prefix_sum[l-1])