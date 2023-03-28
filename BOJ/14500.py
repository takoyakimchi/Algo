from itertools import combinations

N, M = map(int, input().split())
graph = []
answers = []
visited = [[False] * M for _ in range(N)]
# done = [[False] * M for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(N):
    graph.append(list(map(int, input().split())))

def dfs(count, _sum, x, y, visited):
    if count == 4:
        answers.append(_sum)
        return

    for i in range(4):
        _x = x + dx[i]
        _y = y + dy[i]
        if 0 <= _x < N and 0 <= _y < M:
            if not visited[_x][_y]:
                visited[_x][_y] = True
                dfs(count + 1, _sum + graph[_x][_y], _x, _y, visited)
                visited[_x][_y] = False

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(1, graph[i][j], i, j, visited)
        visited[i][j] = False

for x in range(N):
    for y in range(M):
        movable = []
        for i in range(4):
            _x = x + dx[i]
            _y = y + dy[i]
            if 0 <= _x < N and 0 <= _y < M:
                movable.append(graph[_x][_y])
        if len(movable) >= 3:
            for case in combinations(movable, 3):
                answer = sum(case) + graph[x][y]
                answers.append(answer)

print(max(answers))