from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

# 가로 세로 대각
dp = [[[0, 0, 0] for _ in range(N)] for _ in range(N)]

dp[0][1] = [1, 0, 0]

for i in range(0, N):
    for j in range(1, N):
        if sum(dp[i][j]) > 0:
            # 가로
            if dp[i][j][0] > 0:
                # 가로
                if j + 1 < N and graph[i][j + 1] == 0:
                    dp[i][j + 1][0] += dp[i][j][0]
                # 대각선
                if i + 1 < N and j + 1 < N and graph[i + 1][j] == graph[i][j + 1] == graph[i + 1][j + 1] == 0:
                    dp[i+1][j+1][2] += dp[i][j][0]
            # 세로
            if dp[i][j][1] > 0:
                # 세로
                if i + 1 < N and graph[i+1][j] == 0:
                    dp[i+1][j][1] += dp[i][j][1]
                # 대각선
                if i + 1 < N and j + 1 < N and graph[i + 1][j] == graph[i][j + 1] == graph[i + 1][j + 1] == 0:
                    dp[i + 1][j + 1][2] += dp[i][j][1]
            # 대각선
            if dp[i][j][2] > 0:
                # 가로
                if j + 1 < N and graph[i][j + 1] == 0:
                    dp[i][j + 1][0] += dp[i][j][2]
                # 세로
                if i + 1 < N and graph[i + 1][j] == 0:
                    dp[i + 1][j][1] += dp[i][j][2]
                # 대각선
                if i + 1 < N and j + 1 < N and graph[i + 1][j] == graph[i][j + 1] == graph[i + 1][j + 1] == 0:
                    dp[i + 1][j + 1][2] += dp[i][j][2]
print(sum(dp[N-1][N-1]))