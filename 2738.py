N, M = map(int, input().split())

matrix_A = []
matrix_B = []

for i in range(N):
    matrix_A.append(list(map(int, input().split())))

for i in range(N):
    matrix_B.append(list(map(int, input().split())))

result_matrix = []
for i in range(N):
    result_matrix.append([0]*M)
for i in range(N):
    for j in range(M):
        result_matrix[i][j] = matrix_A[i][j] + matrix_B[i][j]

for i in range(N):
    print(*result_matrix[i])
# *의 사용이 무엇인지 잘 모르겠다.
    