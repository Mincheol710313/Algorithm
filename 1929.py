# 에라토스테네스의 체 : 소수를 판별하는 알고리즘, 소수들을 대량으로 빠르고 정확하게 구하는 방법
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
M, N = map(int, input().split())
prime_array = primeNumberSieve(N)

for i in range(M, N+1):
    if prime_array[i] != 0:
        print(prime_array[i])



