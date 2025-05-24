def solution(s):
    answer = ''
    
    num_list = list(s.split(' '))
    len_num_list = len(num_list)
    
    for idx in range(len_num_list):
        num_list[idx] = int(num_list[idx])
        
    num_list.sort()
    
    answer = str(num_list[0])+ " " + str(num_list[-1])
    
    return answer

# 테스트 케이스
print(solution("1 2 3 4"))
print(solution("-1 -2 -3 -4"))
print(solution("-1 -1"))
