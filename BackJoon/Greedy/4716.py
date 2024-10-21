while True:   
    N, A, B = map(int, input().split())

    if N == A == B == 0:
        break

    ballon = []

    for i in range(N):
        ballon.append(list(map(int, input().split())))

    ballon.sort(key=lambda x : abs(x[1] - x[2]), reverse=True)

    answer = 0

    for i in range(N):
        count, A_dist, B_dist = ballon[i][0], ballon[i][1], ballon[i][2]
        if A_dist < B_dist:
            if count <= A:
                answer += A_dist * count
                A -= count
            else:
                answer += A_dist * A
                count -= A
                A = 0
                answer += B_dist * count
                B -= count           
        elif A_dist == B_dist:
            if count <= A:
                answer += A_dist * count
                A -= count
            else:
                answer += A_dist * A
                count -= A
                A = 0
                answer += B_dist * count
                B -= count  
        else:
            if count <= B:
                answer += B_dist * count
                B -= count
            else:
                answer += B_dist * B
                count -= B
                B = 0
                answer += A_dist * count
                A -= count

    print(answer)