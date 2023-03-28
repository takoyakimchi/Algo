n = int(input())
graph = []
dp = []
for i in range(n):
    dp.append([0] * (i+1))

for _ in range(n):
    graph.append(list(map(int, input().split())))

dp[0][0] = graph[0][0]
for i in range(1, n):
    for j in range(0, i + 1):
        if j == i:
            dp[i][j] = dp[i-1][j-1] + graph[i][j]
        elif j == 0:
            dp[i][j] = dp[i-1][j] + graph[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + graph[i][j]

print(max(dp[n-1]))