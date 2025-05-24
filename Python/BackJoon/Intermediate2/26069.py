"""
붙임성 좋은 총총이
총총이가 무지개 댄스를 추고 있고 총총이를 만난다면 해당 사람은 무지개 댄스를 추게 된다.
사람들이 만난 기록이 주어질 때 마지막에 무지개 댄스를 추고 있는 사람 수를 출력
기록 이전에 무지개 댄스를 추고 있는 사람은 "총총이"뿐이다!!
사람 이름은 대소문자를 구분한다!
"""
N = int(input())
dance_list = set()
for _ in range(N):
    A, B = input().split()
    if "ChongChong" in dance_list:
        if A in dance_list:
            dance_list.add(B)
        elif B in dance_list:
            dance_list.add(A)
    elif A == "ChongChong" or B == "ChongChong":
        dance_list.add(A)
        dance_list.add(B)
    else:
        continue
print(len(dance_list))

    