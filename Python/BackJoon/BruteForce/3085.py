"""
사탕 게임
Algorithm : Brute Force
보드판 하나를 기준으로 "오른쪽과 아래쪽"의 보드판을 비교한 후 다르면 교환한 후 Board 내의 행/열 연속성 파악
"""
def swap(a, b):
    return b, a

def CheckContinue(board):
    result = 0
    # 행 내에서 연속성 파악
    for i in range(len(board)):
        count = 1
        for j in range(len(board)-1):
            if board[i][j] == board[i][j+1]:
                count += 1
                if result < count:
                    result = count
            else:
                count = 1

    # 열 내에서 연속성 파악
    for i in range(len(board)):
        count = 1
        for j in range(len(board)-1):
            if board[j][i] == board[j+1][i]:
                count += 1
                if result < count:
                    result = count
            else:
                count = 1
    return result


N = int(input())
candy_board = []
for _ in range(N):
    candy_board.append(list(input()))

result = CheckContinue(candy_board)
for i in range(N):
    for j in range(N):
        if i == N-1:
            if j == N-1:
                pass
            else:
                if candy_board[i][j] != candy_board[i][j+1]:
                    candy_board[i][j], candy_board[i][j+1] = swap(candy_board[i][j], candy_board[i][j+1])
                    if result < CheckContinue(candy_board):
                        result = CheckContinue(candy_board)
                    candy_board[i][j], candy_board[i][j + 1] = swap(candy_board[i][j], candy_board[i][j + 1])
        else:
            if j == N-1:
                if candy_board[i][j] != candy_board[i+1][j]:
                    candy_board[i][j], candy_board[i+1][j] = swap(candy_board[i][j], candy_board[i+1][j])
                    if result < CheckContinue(candy_board):
                        result = CheckContinue(candy_board)
                    candy_board[i][j], candy_board[i + 1][j] = swap(candy_board[i][j], candy_board[i + 1][j])
            else:
                if candy_board[i][j] != candy_board[i][j + 1] or candy_board[i][j] != candy_board[i+1][j]:
                    candy_board[i][j], candy_board[i][j + 1] = swap(candy_board[i][j], candy_board[i][j + 1])
                    if result < CheckContinue(candy_board):
                        result = CheckContinue(candy_board)
                    candy_board[i][j], candy_board[i][j + 1] = swap(candy_board[i][j], candy_board[i][j + 1])
                    candy_board[i][j], candy_board[i + 1][j] = swap(candy_board[i][j], candy_board[i + 1][j])
                    if result < CheckContinue(candy_board):
                        result = CheckContinue(candy_board)
                    candy_board[i][j], candy_board[i + 1][j] = swap(candy_board[i][j], candy_board[i + 1][j])

print(result)

