def solution(A,B):
    answer = 0

    A.sort() # 오름차순 정렬
    B.sort(reverse=True) # 내림차순 정렬
    
    len_list = len(A)
    
    for idx in range(len_list):
        answer += (A[idx] * B[idx])

    return answer

# 테스트 케이스
print(solution([1, 4, 2], [5, 4, 4]))
print(solution([1, 2], [3, 4]))