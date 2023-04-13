from collections import deque
N, M = map(int, input().split())
maps = []
for _ in range(N):
    maps.append(input())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(start):
    counts = [[0] * M for _ in range(N)]
    queue = deque([start])
    counts[start[0]][start[1]] = 1
    longest_dist = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            _x = x + dx[i]
            _y = y + dy[i]
            if 0 <= _x < N and 0 <= _y < M:
                if counts[_x][_y] == 0 and maps[_x][_y] == 'L':
                    counts[_x][_y] = counts[x][y] + 1
                    if longest_dist < counts[_x][_y] - 1:
                        longest_dist = counts[_x][_y] - 1
                    queue.append((_x, _y))
    return longest_dist

answers = []
for i in range(N):
    for j in range(M):
        if maps[i][j] == 'L':
            answers.append(bfs((i, j)))


# print(answers)
print(max(answers))