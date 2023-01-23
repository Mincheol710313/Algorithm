num_list = [0 for i in range(30)]

for i in range(28):
    num = int(input())
    num_list[num-1] = 1

for i in range(30):
    if num_list[i] == 0:
        print(i+1)