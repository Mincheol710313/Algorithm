"""
체스판 다시 칠하기
M x N 크기의 보드를 잘라서 8 x 8 크기의 board를 만들려고 함.
8 x 8 크기의 보드로 자른 후 정사각형을 다시 칠해야 할 때, 다시 칠해야하는 정사각형의 최소 개수
Algorithm : Brute Force
1. 8 x 8 크기의 모든 board 파악
2. 해당 board가 체스 보드 처럼 되기 위해서 칠해야하는 정사각형 Count
3. 모든 board에 대한 Count 비교 후 최소값 출력
"""
def chees_board_count(array):
    check_chess_board_1 = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
           ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
           ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
           ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
           ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
           ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
           ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
           ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
           ]
    check_chess_board_2 = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
           ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
           ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
           ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
           ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
           ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
           ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
           ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
           ]
    # count 파악
    count_1 = 0
    count_2 = 0
    for i in range(8):
        for j in range(8):
            if array[i][j] != check_chess_board_1[i][j]:
                count_1 += 1
            if array[i][j] != check_chess_board_2[i][j]:
                count_2 += 1
    count = min(count_1, count_2)

    return count 

import sys
input = sys.stdin.readline
N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(input().rstrip()))

results = []
for i in range(N-8+1):
    for j in range(M-8+1):
        chess_board = [x[j:j+8] for x in board[i:i+8]]
        results.append(chees_board_count(chess_board))

print(min(results))