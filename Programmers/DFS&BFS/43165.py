from collections import deque

def solution(numbers, target):
    answer = 0

    len_numbers = len(numbers)
    q = deque()
    q.append((numbers[0], 1))
    q.append((-numbers[0], 1))

    while q:
        comp = q.popleft()
        res, count = comp[0], comp[1]

        if count < len_numbers:
            plus_res = res + numbers[count]
            minus_res = res - numbers[count]
            count += 1
            q.append((plus_res, count))
            q.append((minus_res, count))
        elif count == len_numbers:
            if res == target:
                answer += 1

    return answer

# 테스트 케이스
print(solution([1, 1, 1, 1, 1], 3))
print(solution([4, 1, 2, 1], 4))