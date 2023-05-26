n = int(input())
dp = [0] * 1001
dp[1] = 1
dp[2] = 3
dp[3] = 5
for i in range(4, 1001):
    dp[i] = (dp[i-2] * 3 + dp[i-3] * 2) % 10007

print(dp)