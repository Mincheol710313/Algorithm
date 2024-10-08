import sys
# 문제 변수
N = int(sys.stdin.readline().rstrip())

dp = [0 for i in range(1000001)]

# Bottom-Up 방식 사용
for i in range(2, N+1):
    dp[i] = dp[i-1] + 1
    if i%2 == 0 and dp[i] > dp[i//2] + 1:
        dp[i] = dp[i//2] + 1
    if i%3 == 0 and dp[i] > dp[i//3] + 1:
        dp[i] = dp[i//3] + 1

print(dp[N])
