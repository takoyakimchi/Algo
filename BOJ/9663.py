import sys
N = int(sys.stdin.readline().rstrip())

cnt = 0
placed = [0] * N

def can_place(row):
    for i in range(row): # i는 바로 이전까지의 행
        if placed[row] == placed[i] or abs(placed[row] - placed[i]) == abs(row - i):
            return False
    return True

def dfs(row):
    global cnt
    if row == N:
        cnt += 1
    else:
        for i in range(N):
            placed[row] = i
            if can_place(row):
                dfs(row + 1)

dfs(0)
print(cnt)