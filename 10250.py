import math
T = int(input())  # 테스트 데이터 개수

person_data = []
for i in range(T):
    person_data.append(list(map(int, input().split())))


for i in range(T):
    H, W, N = person_data[i][0], person_data[i][1], person_data[i][2]

    if N % H == 0:
        floor = H
    else:
        floor = N % H

    room = 0
    if N % H == 0:
        room = N // H
    else:
        room = N // H + 1

    print(f"{floor}{room:02d}")

