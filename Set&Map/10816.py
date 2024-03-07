N = int(input())

card_dict = {}

num_list = list(map(int, input().split()))
for num in num_list:
    if card_dict.get(num):
        card_dict[num] += 1
    else:
        card_dict[num] = 1

M = int(input())
check_list = list(map(int, input().split()))
for check_num in check_list:
    print(card_dict.get(check_num, 0), end=" ")