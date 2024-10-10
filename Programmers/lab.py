import math

arr = [1 for _ in range(1001)]

for i in range(1, int(math.sqrt(1000))+1):
    j = 2
    while i * j <= 1000:
        arr[i*j] += 1
        j += 1

print(arr)