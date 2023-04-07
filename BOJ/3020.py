N, H = map(int, input().split())
road = [[0] * N for _ in range(H)]
answer = 10 ** 10
cnt = 0

for i in range(N):
    num = int(input())
    if i % 2 == 0: # 0, 2, 4, ... -> 석순(아래서)
        for j in range(H-num, H):
            road[j][i] = 1
    else: # 1, 3, 5, ... -> 종유석(위에서)
        for j in range(0, num):
            road[j][i] = 1

for row in road:
    _sum = sum(row)
    if _sum == answer:
        cnt += 1
    elif _sum < answer:
        answer = _sum
        cnt = 1

print(answer, cnt)