from itertools import combinations
from collections import deque
import copy

N, M = map(int, input().split())
graph = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

zero_points = []    # 0
virus_points = []   # 2

answers = []

for _ in range(N):
    graph.append(list(map(int, input().split())))

for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            zero_points.append((i, j))
        elif graph[i][j] == 2:
            virus_points.append((i, j))

def bfs(start, __graph):
    _graph = copy.deepcopy(__graph)
    queue = deque(start)
    count = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            _x = x + dx[i]
            _y = y + dy[i]
            if 0 <= _x < N and 0 <= _y < M:
                if _graph[_x][_y] == 0:
                    _graph[_x][_y] = 2
                    queue.append((_x, _y))

    for i in range(N):
        for j in range(M):
            if _graph[i][j] == 0:
                count += 1

    return count

for cases in combinations(zero_points, 3):
    for x, y in cases:
        graph[x][y] = 1
    answer = bfs(virus_points, graph)
    answers.append(answer)
    for x, y in cases:
        graph[x][y] = 0

print(max(answers))