N, M = map(int, input().split())

tree_list = list(map(int, input().split()))

start = 1
end = max(tree_list)

while start <= end:
    mid = (start + end) // 2

    sum = 0
    for tree in tree_list:
        if tree > mid:
            sum += tree - mid

    if sum < M:
        end = mid - 1
        ans = end
    else:
        start = mid + 1

print(ans)