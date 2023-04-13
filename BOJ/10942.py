import sys
input = sys.stdin.readline

N = int(input())
arr = [0] + list(map(int, input().split()))  # arr[N]까지 액세스 가능
M = int(input())
is_palin = [[False] * (N+1) for _ in range(N+1)]
palindrome = [[] for _ in range(N+1)]

# 1글자 팰린드롬
for i in range(1, N+1):
    is_palin[i][i] = True
    palindrome[1].append((i, i))

# 2글자 팰린드롬
for i in range(1, N+1):
    if arr[i-1] == arr[i]:
        is_palin[i-1][i] = True
        palindrome[2].append((i-1, i))

# n글자 팰린드롬 --> (n-2)글자 팰린드롬이고 좌우 끝 글자 같으면
for n in range(2, N+1):
    for start, end in palindrome[n-2]:
        if end != N and arr[start-1] == arr[end+1]:
            is_palin[start-1][end+1] = True
            palindrome[n].append((start-1, end+1))

for _ in range(M):
    S, E = map(int, input().split())
    if is_palin[S][E]:
        print(1)
    else:
        print(0)