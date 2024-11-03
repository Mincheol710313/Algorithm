from itertools import product

def solution(word):
    answer = 0

    gather_list = ['A', 'E', 'I', 'O', 'U']

    word_list = []

    for i in range(1, 6):
        for w in product(gather_list, repeat=i):
            w = ''.join(w)
            word_list.append(w)

    word_list.sort()
    len_word_list = len(word_list)

    for idx in range(len_word_list):
        if word_list[idx] == word:
            answer = idx + 1

    return answer

# 테스트 케이스
print(solution("AAAAE"))
