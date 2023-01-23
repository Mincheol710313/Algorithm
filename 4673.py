def d(n):
    result = n
    num = str(n)
    for i in num:
        result += int(i)
    return result


ans = [0] * 10001
for i in range(1, 10001):
    ans[i] = i

for i in range(1, 10001):
    n = d(i)
    while n <= 10000:
        ans[n] = 0
        n = d(n)

for i in range(1, 10001):
    if ans[i] != 0:
        print(i)

