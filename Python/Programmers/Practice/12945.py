def solution(n):
    fibo_list = [0] * 100001
    fibo_list[0] = 0
    fibo_list[1] = 1
    
    for i in range(2, 100001):
        fibo_list[i] = fibo_list[i-1] + fibo_list[i-2]
        
    answer = fibo_list[n] % 1234567
    
    return answer

# 테스트 케이스
print(solution(3))
print(solution(5))