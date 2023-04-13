x = int(input())
dp = [0] * (x+1)    # dp[0] ~ dp[x]
nums = [[] for _ in range(x+1)]
nums[x].append(x)
INF = 10 ** 10

for i in range(x-1, 0, -1):
    ls = []
    # 1 빼기
    ls.append(dp[i + 1])
    # 2 나누기
    if i * 2 < x:
        ls.append(dp[i * 2])
    else:
        ls.append(INF)
    # 3 나누기
    if i * 3 < x:
        ls.append(dp[i * 3])
    else:
        ls.append(INF)

    answer = min(ls)
    min_idx = ls.index(answer)

    if min_idx == 0:
        nums[i] = nums[i+1] + [i]
    elif min_idx == 1:
        nums[i] = nums[i*2] + [i]
    elif min_idx == 2:
        nums[i] = nums[i*3] + [i]

    dp[i] = answer + 1

print(dp[1])
print(*nums[1])