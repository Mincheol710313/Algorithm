"""
단어 암기장
1. 자주 나오는 단어일수록 앞에 배치
2. 해당 단어의 길이가 길수록 앞에 배치
3. 알파벳 사전 순으로 앞에 있는 단어일수록 앞에 배치
"""
N, M = map(int, input().split())  # N : 단어의 개수, 단어의 길이 기준
voca = dict()
for _ in range(N):
    word = input()
    if len(word) < M:
        continue
    else:
        if word in voca.keys():
            voca[word] += 1
        else:
            voca[word] = 1

voca = sorted(voca.items(), key=lambda item:(-item[1], -len(item[0]), item[0]))
for word in voca:
    print(word[0])