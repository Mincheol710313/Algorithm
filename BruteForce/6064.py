T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())
    year = 1
    result = -1
    while not (year % M == 0 and year % N == 0):
        if (year-1) % M + 1 == x and (year-1) % N + 1 == y:
            result = year
            break
        year +=1
    print(result)