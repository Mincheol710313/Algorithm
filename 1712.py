n = int(input())
n = n-1

num = 1
if n == 0:
    print(num)
else:
    for i in range(1000000000):
        if n > 6 * i:
            n = n - (6*i)
            num += 1
        else:
            print(num)
            break