from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

def bfs(head, tail):
    queue = deque([(head, tail)])
    count = 0
    while queue:
        ((headX, headY), (tailX, tailY)) = queue.popleft()
        if (headX, headY) == (N-1, N-1):
            count += 1

        # 가로
        if headX == tailX:
            # 가로로 이동
            if (headY + 1) < N:
                if graph[headX][headY + 1] != 1:
                    queue.append(((headX, headY + 1), (headX, headY)))
            # 대각선 이동
            if (headX + 1) < N and (headY + 1) < N:
                if graph[headX][headY + 1] != 1 and graph[headX + 1][headY] != 1 and graph[headX + 1][headY + 1] != 1:
                    queue.append(((headX + 1, headY + 1), (headX, headY)))
        # 세로
        elif headY == tailY:
            # 세로로 이동
            if (headX + 1) < N:
                if graph[headX + 1][headY] != 1:
                    queue.append(((headX + 1, headY), (headX, headY)))
            # 대각선 이동
            if (headX + 1) < N and (headY + 1) < N:
                if graph[headX][headY + 1] != 1 and graph[headX + 1][headY] != 1 and graph[headX + 1][headY + 1] != 1:
                    queue.append(((headX + 1, headY + 1), (headX, headY)))
        # 대각선
        else:
            # 가로로 이동
            if (headY + 1) < N:
                if graph[headX][headY + 1] != 1:
                    queue.append(((headX, headY + 1), (headX, headY)))
            # 세로로 이동
            if (headX + 1) < N:
                if graph[headX + 1][headY] != 1:
                    queue.append(((headX + 1, headY), (headX, headY)))
            # 대각선 이동
            if (headX + 1) < N and (headY + 1) < N:
                if graph[headX][headY + 1] != 1 and graph[headX + 1][headY] != 1 and graph[headX + 1][headY + 1] != 1:
                    queue.append(((headX + 1, headY + 1), (headX, headY)))

    return count

if graph[N-1][N-1] == 1:
    print(0)
else:
    print(bfs((0, 1), (0, 0)))