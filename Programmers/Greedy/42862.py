def solution(n, lost, reserve):
    student = [1 for _ in range(n)]

    lost.sort()

    for num in reserve:
        student[num-1] += 1

    for num in lost:
        student[num-1] -=1

    for idx in range(n):
        if student[idx] == 0:
            if idx == 0:
                if student[idx+1] >= 2:
                    student[idx+1] -= 1
                    student[idx] += 1
            elif idx == n-1:
                if student[idx-1] >= 2:
                    student[idx-1] -= 1
                    student[idx] += 1
            else:
                if student[idx-1] >= 2:
                    student[idx-1] -= 1
                    student[idx] += 1
                elif student[idx+1] >= 2:
                    student[idx+1] -= 1
                    student[idx] += 1 

    ans = 0
    for num in student:
        if num >= 1:
            ans += 1
    return ans

# 테스트 케이스 
print(solution(5, [2, 3], [3, 4]))
print(solution(5, [2, 4], [3]))
print(solution(3, [3], [1]))
