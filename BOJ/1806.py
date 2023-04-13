N, S = map(int, input().split())
arr = list(map(int, input().split()))
answers = []

# 누적합 구성
total = 0
_sum = []
for i in range(N):
    total += arr[i]
    _sum.append(total)

# 투포인터 초기 인덱스
start_idx = 0
end_idx = 0

if _sum[-1] < S:
    print(0)
else:
    while True:
        if start_idx == 0:
            sub_sum = _sum[end_idx]
        else:
            sub_sum = _sum[end_idx] - _sum[start_idx - 1]

        # 부분합이 S보다 작으면 end_idx 늘림
        if sub_sum < S:
            if end_idx == N-1:
                break # 더 늘릴 곳이 없음
            else:
                end_idx += 1

        # 부분합이 답에 만족하는 경우
        elif sub_sum >= S:
            answers.append(end_idx - start_idx + 1) # 답 후보로 등록

            if start_idx == end_idx:
                break
            else:
                start_idx += 1

    print(min(answers))