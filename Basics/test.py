n, k = map(int, input().split())
dp = [1] * (n+1)
dp[0] = 0
dp[1] = 1
dp[2] = 1

for i in range(3, n+1):
    # i-k와 k로 나누기
    if i > k:
        dp[i] += dp[i-k] * dp[k]
        print(i, i-k, k)

    # 반으로 나누기
    if i % 2 == 0 and (i//2) != k:
        dp[i] += dp[i//2] * dp[i//2]
        print(i, i//2, i//2)

    # k를 제외하여 그것의 반을 자르기
    if i > k and i % 2 == 1:
        p = (i - k) // 2
        q = i - p
        if p != k and q != k:
            dp[i] += dp[p] * dp[q]
            print(i, p, q)

print(dp)
print(dp[n])