from itertools import permutations

def solution(k, dungeons):
    answer = -1
    
    len_dungeons = len(dungeons)
    dungeons_num_list = []
    for idx in range(1, len_dungeons+1):
        dungeons_num_list.append(idx)
        
    for seq in permutations(dungeons_num_list, len_dungeons):
        count = 0
        fatigue = k
        for num in seq:
            if fatigue >= dungeons[num-1][0]:
                count += 1
                fatigue -= dungeons[num-1][1]
        if count > answer:
            answer = count
    
    return answer

# 테스트 케이스
print(solution(80, [[80,20],[50,40],[30,10]]))