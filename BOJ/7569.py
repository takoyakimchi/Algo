from collections import deque
M, N, H = map(int, input().split()) # [H][N][M]

graph = []
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]
tomato_xyz = []
ans = 0

for _ in range(H):
    _list = []
    for _ in range(N):
        _list.append(list(map(int, input().split())))
    graph.append(_list)

for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 1:
                tomato_xyz.append((i, j, k))

def bfs(start_list):
    queue = deque(start_list)
    answer = 0
    while queue:
        x, y, z = queue.popleft()
        for i in range(6):
            _x = x + dx[i]
            _y = y + dy[i]
            _z = z + dz[i]
            if 0 <= _x < H and 0 <= _y < N and 0 <= _z < M:
                if graph[_x][_y][_z] == 0:
                    graph[_x][_y][_z] = graph[x][y][z] + 1
                    answer = graph[x][y][z] + 1
                    queue.append((_x, _y, _z))
    return answer

ans = bfs(tomato_xyz)

if ans > 0:
    ans -= 1

for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 0:
                ans = -1

print(ans)