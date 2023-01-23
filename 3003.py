chess_array = [1, 1, 2, 2, 2, 8]  # 체스에서 사용하는 말들의 개수
find_array = list(map(int, input().strip().split()))
for i in range(6):
    print(chess_array[i] - find_array[i], end=" ")