N = int(input())
M = int(input())
vip_seats = []

for _ in range(M):
    vip_seats.append(int(input()))

dp = [1] * 41
dp[1] = 1
dp[2] = 2
for i in range(3, 41):
    dp[i] = dp[i-1] + dp[i-2]

cnts = []
idx = 0
for seat in vip_seats:
    cnts.append(seat - idx - 1)
    idx = seat

cnts.append(N - idx)

answer = 1
for i in cnts:
    answer *= dp[i]

print(answer)