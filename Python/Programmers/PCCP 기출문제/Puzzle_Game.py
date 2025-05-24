# Binary Search 
def func(level, diffs, times):
    total_time = 0
    prev_time = 0

    for diff, time in zip(diffs, times):
        if level < diff:
            total_time += (diff-level)*(prev_time+time)+time
        else:
            total_time += time

        prev_time = time
    
    return total_time

def solution(diffs, times, limit):
    min_level = 1
    max_level = max(diffs)

    while min_level < max_level:
        mid_level = (min_level + max_level) // 2

        mid_total = func(mid_level, diffs, times)

        if mid_total <= limit:
            max_level = mid_level
        else:
            min_level = mid_level + 1

    return min_level

# 테스테 케이스  
print(solution([1, 5, 3], [2, 4, 7], 30))
print(solution([1, 4, 4, 2], [6, 3, 8, 2], 59))
print(solution([1, 328, 467, 209, 54], [2, 7, 1, 4, 3], 1723))
print(solution([1, 99999, 100000, 99995], [9999, 9001, 9999, 9001], 3456789012))