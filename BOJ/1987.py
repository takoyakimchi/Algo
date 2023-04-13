R, C = map(int, input().split())
maps = []
answer = 0

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
visited = [False] * 26 # index 접근 예시: ord("A") - 65 == 0

for _ in range(R):
    maps.append(input())

def dfs(x, y, cnt):
    global answer
    if answer < cnt:
        answer = cnt

    for i in range(4):
        _x = x + dx[i]
        _y = y + dy[i]
        if 0 <= _x < R and 0 <= _y < C:
            if not visited[ord(maps[_x][_y]) - 65]:
                visited[ord(maps[_x][_y]) - 65] = True
                dfs(_x, _y, cnt + 1)
                visited[ord(maps[_x][_y]) - 65] = False

visited[ord(maps[0][0]) - 65] = True
dfs(0, 0, 1)
print(answer)