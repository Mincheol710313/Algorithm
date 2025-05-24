T = int(input())

for _ in range(T):
    N = int(input())

    if N == 1:
        print(1)
        continue

    start = 1
    end = 10**16
    ans = 1

    while start <= end:
        mid = (start + end) // 2

        sum = mid * (mid + 1) // 2

        if sum > N:
            ans = mid - 1
            end = mid - 1
        else:
            start = mid + 1

    print(ans)
    