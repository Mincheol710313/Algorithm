while True:
    num = int(input())
    if num == -1:
        break

    measure_list = []
    for i in range(1, num):
        if num % i == 0:
            measure_list.append(i)

    measure_sum = sum(measure_list)
    if measure_sum == num:
        print(f"{num} = ", end="")
        for idx in range(len(measure_list)):
            if idx == len(measure_list)-1:
                print(f"{measure_list[idx]}")
            else:
                print(f"{measure_list[idx]} +", end=" ")
    else:
        print(f"{num} is NOT perfect.")