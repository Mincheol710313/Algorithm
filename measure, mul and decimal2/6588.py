import sys
import math

# 에라토스테네스의 체 구현 1000000까지
array = [True for i in range(1000001)]
array[0] = False
array[1] = False

for i in range(2, int(math.sqrt(1000000))+1):
    if array[i]:
        j = 2
        while i * j <= 1000000:
            array[i*j] = False
            j += 1

# 테스트 처리
while True:
    num = int(sys.stdin.readline().rstrip())
    if num == 0:
        break

    flag = 0

    for i in range(3, 1000001):
        if array[i] and array[num-i]:
            print(f"{num} = {i} + {num-i}")
            flag = 1
            break

    if flag == 0:
        print("Goldbach's conjecture is wrong.")