from itertools import combinations, permutations

numbers = "011"

num_list = []
for num in numbers:
    num_list.append(num)
num_len = len(num_list)

new_numbers = []
for i in range(2, num_len+1):
    for num_set in permutations(num_list, i):
        number = ''
        for num in num_set:
            number = number + num
        
        if number not in new_numbers:
            new_numbers.append(number)