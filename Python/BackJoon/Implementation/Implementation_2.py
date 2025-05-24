N = int(input())

# 00분 00초 ~ 59분 59초까지의 3이 포함된 시각 경우의 수 확인
count = 0
just_count = 0
minute, second = 0, 0
while minute != 59 or second != 59:
    just_count += 1
    second += 1
    if second == 60:
        minute += 1
        second = 0

    if '3' in str(minute) or '3' in str(second):
        count += 1

time_table = [0] * 24
for i in range(24):
    if '3' in str(i):
        time_table[i] = just_count
    else:
        time_table[i] = count

print(sum(time_table[:N+1]))