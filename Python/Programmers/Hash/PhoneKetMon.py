def solution(nums):
    poncatmon_kind_num = len(set(nums))

    catch_num = len(nums) // 2

    answer = min(poncatmon_kind_num, catch_num)

    return answer

# 테스트 케이스
print(solution([3,1,2,3]))
print(solution([3,3,3,2,2,4]))
print(solution([3,3,3,2,2,2]))
