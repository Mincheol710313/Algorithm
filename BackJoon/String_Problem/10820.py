while True:
    try:
        line = input()
        char_num_list =[0 for _ in range(4)]

        for char in line:
            if char == ' ':
                char_num_list[3] += 1
            elif char.isdigit():
                char_num_list[2] += 1
            elif char.isupper():
                char_num_list[1] += 1
            else:
                char_num_list[0] += 1
        for num in char_num_list:
            print(num, end=" ")
        print()
    except EOFError:
        break