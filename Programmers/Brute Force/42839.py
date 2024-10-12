from math import sqrt
from itertools import permutations

def prime_number(num):
    if num == 0 or num == 1:
        return False

    for i in range(2, int(sqrt(num)+1)):
        if num % i == 0:
            return False

    return True

def solution(numbers):
    answer = 0

    # Num List 생성
    num_list = []
    for num in numbers:
        num_list.append(num)
    num_len = len(num_list)
    
    new_numbers = []
    for l in range(1, num_len+1):
        for num_set in permutations(num_list, l):
            number = ''
            for num in num_set:
                number = number + num
                
            if int(number) not in new_numbers:
                new_numbers.append(int(number))

    for number in new_numbers:
        if prime_number(number):
            answer += 1 

    return answer

# 테스트 케이스
print(solution("17"))
print(solution("011"))
print(solution("222"))