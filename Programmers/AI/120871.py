def solution(n):
    arr = []

    count = 1
    while len(arr) <= n:
        if count % 3 != 0 and '3' not in str(count):
            arr.append(count)
        count += 1

    return arr[n-1]

# 테스트 케이스
print(solution(15))
print(solution(40))