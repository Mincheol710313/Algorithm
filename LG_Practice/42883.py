""" 큰 수 만들기 https://school.programmers.co.kr/learn/courses/30/lessons/42883"""
def solution(number, k):
    answer = ''

    stack = []
    for num in number:
        while stack and int(stack[-1]) < int(num) and k > 0:
            stack.pop()
            k -= 1

        stack.append(num)

    for num in stack:
        answer += num

    if k != 0:
        answer = answer[:k]

    return answer

# 테스트 케이스
print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))
print(solution("10", 1))