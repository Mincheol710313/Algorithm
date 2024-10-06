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

print(func(3, [1,5,3], [2,4,7]))