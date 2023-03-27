from collections import deque

N, M = map(int, input().split())
graph = [[0] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(N):
    graph[i] = list(map(int, input()))

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start[0]][start[1]] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            _x = x + dx[i]
            _y = y + dy[i]
            if 0 <= _x < N and 0 <= _y < M and graph[_x][_y] > 0 and not visited[_x][_y]:
                queue.append((_x, _y))
                visited[_x][_y] = True
                graph[_x][_y] = graph[x][y] + 1

bfs(graph, (0, 0), visited)
print(graph[N-1][M-1])