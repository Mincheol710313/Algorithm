def solution(arr):
    answer = []

    stack = [arr[0]]

    for idx in range(1, len(arr)):
        if arr[idx] == stack[0]:
            continue
        elif arr[idx] != stack[0]:
            answer.append(stack.pop())
            stack.append(arr[idx])
        
    if len(stack) != 0:
        answer.append(stack.pop())

    return answer

# 테스트 케이스
print(solution([1,1,3,3,0,1,1]))
print(solution([4,4,4,3,3]))