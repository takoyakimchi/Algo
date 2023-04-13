n = int(input())
arr = list(map(int, input().split()))
answer = 0
arrow_flying = [0] * 1_000_001

for i in range(len(arr)):
    # 현재 높이에서 날고 있는 화살 없음
    if arrow_flying[arr[i]] == 0:
        answer += 1
        if arr[i]-1 >= 0:
            arrow_flying[arr[i]-1] += 1
    # 현재 높이에서 날고 있는 화살 존재
    else:
        arrow_flying[arr[i]] -= 1
        if arr[i]-1 >= 0:
            arrow_flying[arr[i]-1] += 1

print(answer)