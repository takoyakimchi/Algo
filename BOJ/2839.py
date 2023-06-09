n = int(input())
dp = [10 ** 10] * 5001
dp[3] = 1
dp[5] = 1
for i in range(6, 5001):
    dp[i] = min(dp[i-3], dp[i-5]) + 1

if dp[n] >= 10 ** 10:
    print(-1)
else:
    print(dp[n])