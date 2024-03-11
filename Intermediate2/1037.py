N = int(input())
measure_list = list(map(int, input().split()))
if len(measure_list) == 1:
    print(pow(measure_list[0], 2))
else:
    measure_list.sort()
    print(measure_list[0] * measure_list[-1])