import sys
input = sys.stdin.readline

N, H = map(int, input().split())
road = [0] * H
cnt = 0

for i in range(N):
    num = int(input())
    if i % 2 == 0: # 0, 2, 4, ... -> 석순(아래서)
        for j in range(H-num, H):
            road[j] += 1
    else: # 1, 3, 5, ... -> 종유석(위에서)
        for j in range(0, num):
            road[j] += 1

answer = 10 ** 10
for num in road:
    if num == answer:
        cnt += 1
    elif num < answer:
        answer = num
        cnt = 1

print(answer, cnt)