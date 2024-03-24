import sys
input = sys.stdin.readline

N = int(input().rstrip())
move_plan = list(map(str, input().split()))

# Direction Vector Setting -> 동, 서, 남, 북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# move_plan setting
move_plan_len = len(move_plan)
for i in range(move_plan_len):
    if move_plan[i] == 'R':
        move_plan[i] = 0
    elif move_plan[i] == 'L':
        move_plan[i] = 1
    elif move_plan[i] == 'D':
        move_plan[i] = 2
    else:
        move_plan[i] = 3

x, y = 1, 1
for move in move_plan:
    nx = x + dx[move]
    ny = y + dy[move]
    if nx <= 0 or nx > N or ny <= 0 or ny > N:
        continue
    x, y = nx, ny

print(x, y)
