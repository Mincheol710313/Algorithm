N, k = map(int, input().split())

score_list = list(map(int, input().split()))
score_list.sort()
score_list.reverse()

print(score_list[k-1])