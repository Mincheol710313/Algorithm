def solution(people, limit):
    answer = 0
    
    people.sort()
    left = 0
    right = len(people) - 1

    while left <= right:
        if left == right:
            answer += 1
            break
        if people[left] + people[right] <= limit:
            left += 1
        right -= 1
        answer += 1
        
    return answer

# 테스트 케이스
print(solution(	[70, 50, 80, 50], 100))
print(solution(	[100, 100, 50, 40], 140))