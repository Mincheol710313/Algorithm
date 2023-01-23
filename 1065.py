def one_num(n):
    num = list(map(int, str(n)))

    if len(num) == 1:
        return 1

    else:
        diff = num[1] - num[0]

        for i in range(1, len(num)-1):
            if (num[i+1] - num[i]) != diff:
                return 0
        return 1


N = int(input())
ans = 0
for i in range(1, N+1):
    if one_num(i) == 1:
        ans += 1

print(ans)