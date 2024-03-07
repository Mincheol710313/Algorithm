import sys

N = int(sys.stdin.readline().rstrip())

stairs = [0 for i in range(N+1)]
for i in range(1, N+1):
    stairs[i] = int(sys.stdin.readline().rstrip())

# 예외 처리
if N == 1:
    print(stairs[1])
    exit(0)
elif N == 2:
    print(stairs[1] + stairs[2])
    exit(0)

# Dynamic Programming
dp = [0 for i in range(N+1)]
dp[1] = stairs[1]
dp[2] = stairs[1] + stairs[2]
dp[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])

for i in range(4, N+1):
    dp[i] = max(dp[i-3] + stairs[i-1] + stairs[i], dp[i-2] + stairs[i])

print(dp[N])