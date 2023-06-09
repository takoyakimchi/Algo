x = int(input())
dp = [0] * (10 ** 6 + 1)
dp[2] = 1
dp[3] = 1

for i in range(4, 10 ** 6 + 1):
    candidates = [dp[i-1]]
    if i % 3 == 0:
        candidates.append(dp[i // 3])
    if i % 2 == 0:
        candidates.append(dp[i // 2])
    dp[i] = min(candidates) + 1

print(dp[x])