import sys
import math

N = int(sys.stdin.readline())
num_list = []
for i in range(N):
    num_list.append(int(sys.stdin.readline()))
num_list.sort()

ave = round(sum(num_list) / N)
print(ave)

mid = num_list[int(N/2)]
print(mid)

check_list = [0] * 8001  # 최빈값을 파악하기 위한 list 0번째 리스트는 사용 x
for i in range(N):
    if num_list[i] < 0:  # 음수일 경우 그냥 절대값으로 파악해서 넣기
        check_list[4000 + num_list[i]] += 1
    else:  # 양수일 경우 +4000번째에 넣기
        check_list[num_list[i] + 4000] += 1

max_check = max(check_list)
num = 0
max_idx = 0
for i in range(len(check_list)):
    if check_list[i] == max_check:
        num += 1
        max_idx = i

    if num == 2:
        break

print(max_idx - 4000)

max_num = max(num_list)
min_num = min(num_list)
print(max_num - min_num)