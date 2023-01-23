# map 공부 필요! --> python 에서는 map 을 dictionary 자료구조와 비슷하게 사용한다.
N, M = list(map(int, input(). split()))

poketmonsters = {}
for i in range(1, N+1):
    poketmonster = input()

    poketmonsters[i] = poketmonster
reverse_poketmonsters = dict(map(reversed, poketmonsters.items()))

Quiz = []
for i in range(M):
    quiz = input()
    Quiz.append(quiz)

for i in range(M):
    if Quiz[i].isdigit():
        print(poketmonsters[int(Quiz[i])])
    else:
        print(reverse_poketmonsters[Quiz[i]])
