def solution(n):
    for idx in range(2, n):
        if n % idx == 1:
            return idx
        
# 테스트 케이스
print(solution(10))
print(solution(12))
