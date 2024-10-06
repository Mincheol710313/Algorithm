length_list = list(map(int, input().split()))

length_list.sort()  # length_list 정렬

""" 가장 큰 변의 길이를 삼각형 조건에 맞게 설정 """
# 삼각형의 조건 : max < a + b
if length_list[2] >= length_list[1] + length_list[0]:
    length_list[2] = length_list[0] + length_list[1] - 1

print(sum(length_list))