T = int(input())

for _ in range(T):
    n = int(input())
    arr = []
    dp = [[0] * n for _ in range(2)]

    for _ in range(2):
        arr.append(list(map(int, input().split())))

    dp[0][0] = arr[0][0]
    dp[1][0] = arr[1][0]

    if n >= 2:
        dp[0][1] = arr[1][0] + arr[0][1]
        dp[1][1] = arr[0][0] + arr[1][1]

    if n >= 3:
        for i in range(2, n):
            dp[0][i] = arr[0][i] + max(dp[1][i-1], dp[1][i-2])
            dp[1][i] = arr[1][i] + max(dp[0][i-1], dp[0][i-2])

    print(max(dp[0][n-1], dp[1][n-1]))