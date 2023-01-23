def primeNumberSieve(N):
    prime_array = [0] * (N+1)
    for i in range(2, N+1):
        prime_array[i] = i

    for i in range(2, N+1):
        if prime_array[i] == 0:
            continue

        for j in range(2*i, N+1, i):
            prime_array[j] = 0

    return prime_array


T = int(input())  # Test Case 개수

for i in range(T):
    N = int(input())

    prime_array = primeNumberSieve(N)
    mid = N // 2

    if prime_array[mid] != 0:
        print(mid, mid)
    else:
        small = 0
        big = 0
        diff = 10000
        cor_s = small
        cor_b = big

        for i in range(2, N+1):
            if prime_array[i] != 0:
                small = i
                big = N - small

                if prime_array[big] == 0:
                    continue
                else:
                    if diff > abs(big - small):
                        diff = big - small
                        cor_s = small
                        cor_b = big
        print(cor_s, cor_b)

