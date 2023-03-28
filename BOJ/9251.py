str_a = input()
str_b = input()

N = len(str_a)
M = len(str_b)

max_length = max(N, M)
same = [[False] * (M+1) for _ in range(N+1)]
answer = [[0] * (M+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        if str_a[i-1] == str_b[j-1]:
            same[i][j] = True

for i in range(1, N+1):
    for j in range(1, M+1):
        if same[i][j]:
            answer[i][j] = answer[i-1][j-1] + 1
        else:
            answer[i][j] = max(answer[i-1][j], answer[i][j-1])

print(answer[N][M])