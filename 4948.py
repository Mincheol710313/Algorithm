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


while True:
    N = int(input())
    if N == 0:
        break
    prime_array = primeNumberSieve(2*N)

    num = 0
    for i in range(N+1, (2*N)+1):
        if prime_array[i] != 0:
            num += 1

    print(num)


