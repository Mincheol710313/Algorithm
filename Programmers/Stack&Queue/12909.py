def solution(s):
    answer = True
    
    stack = []

    for par in s:
        if par == '(':
            stack.append(par)
        elif par == ')':
            if len(stack) == 0 or stack[-1] != '(':
                return False
            else:
                stack.pop()

    if len(stack) != 0:
        return False

    return True

# 테스트 케이스
print(solution("()()"))
print(solution(")()("))
print(solution("(()("))