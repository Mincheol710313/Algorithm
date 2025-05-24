T = int(input())
cent_list = [25, 10, 5, 1]
count_list = [0, 0, 0, 0]
for i in range(T):
    change = int(input())
    for j in range(4):
        count_list[j] = change // cent_list[j]
        change -= cent_list[j] * count_list[j]
        print(count_list[j], end=" ")
    print()