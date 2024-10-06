array = [True for i in range(1000001)]
array[0] = False
array[1] = False
for i in range(2, 1000001):
    if array[i]:
        for j in range(2*i, 1000001, i):
            array[j] = False

T = int(input())  # 테스트 개수
for _ in range(T):
    N = int(input())
    count = 0
    for i in range(2, int(N/2)+1):
        if array[i] and array[N-i]:
            count += 1
    print(count)

