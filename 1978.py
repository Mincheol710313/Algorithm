def prime(X):
    num = 0
    for i in range(1,X+1):
        if X % i == 0:
            num += 1

    if num == 2:
        return 1
    else:
        return 0


N = int(input())

num_list = list(map(int, input().split()))

num = 0
for i in range(N):
    if prime(num_list[i]) == 1:
       num += 1

print(num)