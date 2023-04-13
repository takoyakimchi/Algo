x = int(input())
dp = [0] * (x+1)    # dp[0] ~ dp[x]
before_num = [0] * (x+1)
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
        before_num[i] = i + 1
    elif min_idx == 1:
        before_num[i] = i * 2
    elif min_idx == 2:
        before_num[i] = i * 3

    dp[i] = answer + 1

print(dp[1])

nums = []
current_num = 1
while current_num != x:
    nums.append(current_num)
    current_num = before_num[current_num]

print(*reversed(nums))