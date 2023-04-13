x = int(input())
INF = 10 ** 10
dp = [INF] * (x + 1)  # dp[0] ~ dp[x]
dp[1] = 0
before_num = [1] * (x + 1)

for i in range(1, x):
    if dp[i + 1] > dp[i] + 1:
        dp[i + 1] = dp[i] + 1
        before_num[i + 1] = i
    if i * 2 <= x and dp[i * 2] > dp[i] + 1:
        dp[i * 2] = dp[i] + 1
        before_num[i * 2] = i
    if i * 3 <= x and dp[i * 3] > dp[i] + 1:
        dp[i * 3] = dp[i] + 1
        before_num[i * 3] = i

print(dp[x])
nums = [x]
current_num = x

while current_num != 1:
    current_num = before_num[current_num]
    nums.append(current_num)

print(*nums)