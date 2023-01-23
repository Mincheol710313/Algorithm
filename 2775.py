import math

T = int(input())  # Test Case 수
persons = []

for i in range(T):
    floor = int(input())
    room = int(input())

    person = 0
    # 2중 배열을 이용하여서 푸는 방법
    ap = [[0 for i in range(room)] for j in range(floor+1)]
    for i in range(floor+1):
        for j in range(room):
            if i == 0:
                ap[i][j] = j+1
            else:
                sum = 0
                for k in range(j+1):
                    sum += ap[i-1][k]

                ap[i][j] = sum
                person = ap[i][j]

    persons.append(person)


for i in range(T):
    print(persons[i])
