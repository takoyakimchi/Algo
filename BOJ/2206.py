from collections import deque
import copy

N, M = map(int, input().split())
graph = []
wall_xy = []
answers = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[[False] * 2 for _ in range(M)] for _ in range(N)]   # visited[x][y][0] 안 부수고 방문
                                                                # visited[x][y][1] 부수고 방문

for _ in range(N):
    graph.append(list(map(int, input())))

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            graph[i][j] = -1
            wall_xy.append((i, j))

def bfs(start):
    queue = deque([start])
    while queue:
        (x, y), can_break, cnt = queue.popleft()

        if (x, y) == (N-1, M-1):
            print(cnt)
            return True

        for i in range(4):
            _x = x + dx[i]
            _y = y + dy[i]

            if 0 <= _x < N and 0 <= _y < M:
                if can_break: # 벽을 부수지 않은 경우
                    # 다음에도 벽을 부수지 않는다.
                    if graph[_x][_y] == 0 and not visited[_x][_y][0]:
                        visited[_x][_y][0] = True
                        queue.append(((_x, _y), True, cnt + 1))
                    # 다음에는 벽을 부순다.
                    if graph[_x][_y] == -1 and not visited[_x][_y][1]:
                        visited[_x][_y][1] = True
                        queue.append(((_x, _y), False, cnt + 1))
                else: # 이미 벽을 부순 경우
                    if graph[_x][_y] == 0 and not visited[_x][_y][1]:
                        visited[_x][_y][1] = True
                        queue.append(((_x, _y), False, cnt + 1))

graph[0][0] = 1
if not bfs(((0, 0), True, 1)):
    print(-1)

"""
5 5
00001
11101
00001
01111
00010

5 8
01000000
01010000
01010000
01010011
00010010
"""
