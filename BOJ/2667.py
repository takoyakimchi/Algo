from collections import deque

N = int(input())
graph = []
visited = [[False] * N for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
answer = []

for _ in range(N):
    graph.append(list(map(int, input())))

def bfs(start):
    queue = deque([start])
    visited[start[0]][start[1]] = True
    count = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            _x = x + dx[i]
            _y = y + dy[i]
            if 0 <= _x < N and 0 <= _y < N:
                if graph[_x][_y] != 0 and not visited[_x][_y]:
                    queue.append((_x, _y))
                    visited[_x][_y] = True
                    graph[_x][_y] = -1
                    count += 1
    return count

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            answer.append(bfs((i, j)))

print(len(answer))
for element in sorted(answer):
    print(element)