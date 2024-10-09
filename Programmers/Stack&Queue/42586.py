from math import ceil

def solution(progresses, speeds):
    answer = []
    
    stack = []
    
    for progress, speed in zip(progresses, speeds):
        day = ceil((100-progress) / speed)

        if len(stack) == 0 or stack[0] >= day:
            stack.append(day)
        else:
            count = 0
            while len(stack) != 0:
                stack.pop()
                count += 1
            
            answer.append(count)
            stack.append(day)

    if len(stack) != 0:
        answer.append(len(stack))
        stack.clear()    

    return answer

# 테스트 케이스
print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
print(solution([90, 90, 90], [1, 5, 4]))