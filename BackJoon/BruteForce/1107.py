from itertools import product
# 전체 리모컨 버튼
button = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
present = 100
result = []

N = int(input())  # 이동하고 싶은 채널
M = int(input())  # 고장난 버튼 개수
if M != 0:
    broken_button = list(input().split())

    # 고장난 리모컨 버튼 삭제
    for broken_bt in broken_button:
        button.remove(broken_bt)

# button으로 만들 수 있는 채널 번호 중에 이동하고 싶은 채널과 가장 가까운 채널 파악
# 가능한 채널 모두 만들기
channel_list = []
for i in range(1, 7):
    for channel in product(button, repeat=i):
        channel = int(''.join(channel))
        channel_list.append(channel)

# 가능한 채널 중에 이동하고 싶은 채널과 가장 차이가 나지않는 채널 파악
min_channel = present
diff = abs(N-min_channel)
for channel in channel_list:
    if abs(channel-N) < diff:
        min_channel = channel
        diff = abs(channel-N)
print(min_channel)

# result 파악
result = 0
result += len(str(min_channel))
if min_channel < N:
    result += N-min_channel
elif min_channel > N:
    result += min_channel - N

if abs(present-N) < result:
    result = abs(present-N)

print(result)