def prime(X):
    num = 0
    for i in range(1,X+1):
        if X % i == 0:
            num += 1

    if num == 2:
        return 1
    else:
        return 0


M = int(input())
N = int(input())


prime_list = []
for i in range(M, N+1):
    if prime(i) == 1:
        prime_list.append(i)

if len(prime_list) == 0:
    print(-1)
else:
    print(sum(prime_list))
    print(min(prime_list))
