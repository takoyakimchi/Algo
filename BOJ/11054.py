N = int(input())
arr = list(map(int, input().split()))
dp_ascend = [1] * N     # i번째를 포함하는 가장 긴 증가하는 수열의 길이
dp_descend = [1] * N    # i번째를 포함하는 가장 긴 감소하는 수열의 길이

for i in range(1, N):
    for j in range(0, i):
        if arr[j] < arr[i]:
            if dp_ascend[j] + 1 > dp_ascend[i]:
                dp_ascend[i] = dp_ascend[j] + 1

for i in range(N-2, -1, -1):    # 현재 비교중인 값
    for j in range(N-1, i, -1):     # 뒤 값들
        if arr[i] > arr[j]:
            if dp_descend[j] + 1 > dp_descend[i]:
                dp_descend[i] = dp_descend[j] + 1

print(max([n1 + n2 for n1, n2 in zip(dp_ascend, dp_descend)]) - 1)