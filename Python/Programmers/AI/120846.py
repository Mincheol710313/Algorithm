import math

def solution(n):
    # 에라토스테네스의 체
    array = [True for i in range(n+1)]

    for i in range(2, int(math.sqrt(n)+1)):
        if array[i]:
            j = 2
            while i * j <= n:
                array[i*j] = False
                j += 1
    
    answer = array.count(False)

    return answer

# 테스트 케이스
print(solution(10))