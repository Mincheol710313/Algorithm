"""
가로수
가로수들이 모두 "같은" 간격이 되도록 가로수를 추가로 심는 사업 추진 -> 가장 적은 수의 나무를 심고 싶다!
추가되는 나무는 기존의 나무들 사이에만 심을 수 있다.
Point
차이에 해당하는 숫자들의 "최대 공약수"를 찾으면 된다!
"""
from math import gcd
N = int(input())
pos_list = []
for _ in range(N):
    pos_list.append(int(input()))
length_list = []
for i in range(N-1):
    length_list.append(pos_list[i+1] - pos_list[i])

# 최대 공약수 구하기
gcd_length = length_list[0]
for i in range(1, len(length_list)):
    gcd_length = gcd(gcd_length, length_list[i])

# 결과 도출
result = 0
for length in length_list:
    result += int(length / gcd_length) - 1

print(result)
