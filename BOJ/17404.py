N = int(input())
INF = 10 ** 10
cost = []
dp = [[[INF] * 3 for _ in range(3)] for _ in range(N)] # dp[i][0][2]: 현재 0을 선택했을 때 최소값 (0번째에서는 2 선택)

for _ in range(N):
    cost.append(list(map(int, input().split())))

# row == 0
dp[0][0][0] = cost[0][0]
dp[0][1][1] = cost[0][1]
dp[0][2][2] = cost[0][2]
# row == 1
dp[1][0][1] = cost[0][1] + cost[1][0]
dp[1][0][2] = cost[0][2] + cost[1][0]
dp[1][1][0] = cost[0][0] + cost[1][1]
dp[1][1][2] = cost[0][2] + cost[1][1]
dp[1][2][0] = cost[0][0] + cost[1][2]
dp[1][2][1] = cost[0][1] + cost[1][2]

for i in range(2, N):
    if i == N-1:
        # 현재 0 초기 1
        dp[i][0][1] = min(dp[i-1][1][1], dp[i-1][2][1]) + cost[i][0]
        # 현재 0 초기 2
        dp[i][0][2] = min(dp[i-1][1][2], dp[i-1][2][2]) + cost[i][0]

        # 현재 1 초기 0
        dp[i][1][0] = min(dp[i - 1][0][0], dp[i - 1][2][0]) + cost[i][1]
        # 현재 1 초기 2
        dp[i][1][2] = min(dp[i - 1][0][2], dp[i - 1][2][2]) + cost[i][1]

        # 현재 2 초기 0
        dp[i][2][0] = min(dp[i - 1][0][0], dp[i - 1][1][0]) + cost[i][2]
        # 현재 2 초기 1
        dp[i][2][1] = min(dp[i - 1][0][1], dp[i - 1][1][1]) + cost[i][2]

    else:
        for j in range(0, 3):
            dp[i][0][j] = min(dp[i - 1][1][j], dp[i - 1][2][j]) + cost[i][0]
            dp[i][1][j] = min(dp[i - 1][0][j], dp[i - 1][2][j]) + cost[i][1]
            dp[i][2][j] = min(dp[i - 1][0][j], dp[i - 1][1][j]) + cost[i][2]


print(min(min(dp[N-1][0]), min(dp[N-1][1]), min(dp[N-1][2])))