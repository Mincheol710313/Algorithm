import math

def solution(left, right):
    answer = 0

    arr = [0 for _ in range(right+1)]

    for i in range(1, right+1):
        j = 1
        while i * j <= right:
            arr[i*j] += 1
            j += 1
    
    for idx in range(left, right+1):
        if arr[idx] % 2 == 0:
            answer += idx
        else:
            answer -= idx

    return answer

# 테스트 케이스
print(solution(13, 17))