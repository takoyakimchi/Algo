from collections import deque
N = int(input())
graph = []
visited = [[False] * N for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer_a = 0
answer_b = 0

for _ in range(N):
    graph.append(input())

def bfs(start, is_blind):
    queue = deque([start])
    visited[start[0]][start[1]] = True
    while queue:
        x, y = queue.popleft()
        color = graph[x][y]
        for i in range(4):
            _x = x + dx[i]
            _y = y + dy[i]
            if 0 <= _x < N and 0 <= _y < N and not visited[_x][_y]:
                if is_blind:
                    if graph[_x][_y] == color or (graph[_x][_y] == 'R' and color == 'G') or (graph[_x][_y] == 'G' and color == 'R'):
                        queue.append((_x, _y))
                        visited[_x][_y] = True
                else:
                    if graph[_x][_y] == color:
                        queue.append((_x, _y))
                        visited[_x][_y] = True

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs((i, j), False)
            answer_a += 1

visited = [[False] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs((i, j), True)
            answer_b += 1

print(answer_a, answer_b)