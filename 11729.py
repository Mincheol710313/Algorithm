def hanoi(n, start, to, end):
    global ans
    hanoi.counter += 1

    if n == 1:
        ans.append([start, end])
    else:
        hanoi(n-1, start, end, to)
        ans.append([start, end])
        hanoi(n-1, to, start, end)


n = int(input())
ans = []
hanoi.counter = 0

hanoi(n, 1, 2, 3)
print(hanoi.counter)
for i in range(len(ans)):
    print(ans[i][0], ans[i][1])
