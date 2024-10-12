""" 프로그래머스  요격 시스템 : https://school.programmers.co.kr/learn/courses/30/lessons/181188 """

def solution(targets):
    answer = 0

    targets.sort(key=lambda x : x[1])
    check = -1
    for idx in range(len(targets)):
        if check <= targets[idx][0]:
            check = targets[idx][1]
            answer += 1

    return answer

# 테스트 케이스
print(solution([[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]))
