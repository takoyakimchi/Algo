from collections import deque

M, N = map(int, input().split())
graph = []
tomato_points = []
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for _ in range(N):
    graph.append(list(map(int, input().split())))

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            tomato_points.append((i, j))

def bfs(start):
    queue = deque(start)
    x = 0
    y = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            _x = x + dx[i]
            _y = y + dy[i]
            if 0 <= _x < N and 0 <= _y < M:
                if graph[_x][_y] == 0:
                    queue.append((_x, _y))
                    graph[_x][_y] = graph[x][y] + 1

    return graph[x][y]

answer = bfs(tomato_points) - 1

flag = False
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            answer = -1
            flag = True
            break
    if flag:
        break

print(answer)