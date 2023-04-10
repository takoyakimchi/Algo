from collections import deque

N, M = map(int, input().split())
graph = []
r, c, d = map(int, input().split()) # 초기 위치 (r,c) 방향 d

# 0: 북 // 1: 동 // 2: 남 // 3: 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for _ in range(N):
    graph.append(list(map(int, input().split())))

def bfs(r, c, d):
    cnt = 0
    queue = deque([])
    queue.append((r, c, d))
    while queue:
        x, y, dir = queue.popleft()
        # 현재 칸이 청소되지 않은 경우 현재 칸을 청소한다
        if graph[x][y] == 0:
            graph[x][y] = -1
            cnt += 1

        # 주변 네 칸 확인
        temp = 1
        for i in range(4):
            _x = x + dx[i]
            _y = y + dy[i]
            if 0 <= x < N and 0 <= y < M:
                if graph[_x][_y] != 1:
                    temp *= graph[_x][_y]

        # 빈칸이 있음
        if temp == 0:
            # 반시계 90도 회전
            dir = (dir - 1) % 4

            # 앞쪽 빈칸이면 전진
            _x = x + dx[dir]
            _y = y + dy[dir]
            if graph[_x][_y] == 0:
                queue.append((_x, _y, dir))
            else:
                queue.append((x, y, dir))

        # 빈칸이 없음
        else:
            # 방향 그대로 / 후진할 수 있으면 후진
            dir = (dir - 2) % 4
            _x = x + dx[dir]
            _y = y + dy[dir]
            dir = (dir - 2) % 4
            if graph[_x][_y] != 1:
                queue.append((_x, _y, dir))

    return cnt

print(bfs(r, c, d))
# for g in graph:
#     print(*g)