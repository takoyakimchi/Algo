from collections import deque

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(input())

red_position = (0, 0)
blue_position = (0, 0)
goal_position = (0, 0)
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for i in range(N):
    for j in range(M):
        if graph[i][j] == 'R':
            red_position = (i, j)
        elif graph[i][j] == 'B':
            blue_position = (i, j)
        elif graph[i][j] == 'O':
            goal_position = (i, j)

# 한쪽 끝까지 움직이고 결과좌표 반환하는 함수
def move(red_pos, blue_pos, dx, dy):
    redX, redY = red_pos
    blueX, blueY = blue_pos
    red_move_count = 0
    blue_move_count = 0
    is_red_movable = True

    # move red
    while True:
        # 벽과 부딪히면 끝
        if graph[redX + dx][redY + dy] == '#':
            break
        # 파란공을 만나면 끝
        if (redX + dx, redY + dy) == (blueX, blueY) and (blueX, blueY) != goal_position:
            break
        # 한칸 움직임
        redX += dx
        redY += dy
        red_move_count += 1
        # 구멍에 빠지면 끝
        if graph[redX][redY] == 'O':
            is_red_movable = False
            break
    # move blue
    while True:
        # 벽과 부딪히면 끝
        if graph[blueX + dx][blueY + dy] == '#':
            break
        # 빨간공을 만나면 끝
        if (blueX + dx, blueY + dy) == (redX, redY) and (redX, redY) != goal_position:
            break
        # 한칸 움직임
        blueX += dx
        blueY += dy
        blue_move_count += 1
        # 구멍에 빠지면 끝
        if graph[blueX][blueY] == 'O':
            break

    while True:
        if not is_red_movable:
            break
        # 벽과 부딪히면 끝
        if graph[redX + dx][redY + dy] == '#':
            break
        # 파란공을 만나면 끝
        if (redX + dx, redY + dy) == (blueX, blueY) and (blueX, blueY) != goal_position:
            break
        # 한칸 움직임
        redX += dx
        redY += dy
        red_move_count += 1
        # 구멍에 빠지면 끝
        if graph[redX][redY] == 'O':
            break

    return (redX, redY), (blueX, blueY), red_move_count + blue_move_count

def bfs(red_pos, blue_pos):
    queue = deque([(red_pos, blue_pos, 0)])
    while queue:
        red, blue, count = queue.popleft()
        if red == goal_position and blue == goal_position:
            continue
        if red != goal_position and blue == goal_position:
            continue
        if red == goal_position and blue != goal_position:
            print(count)
            return
        if count > 10:
            print(-1)
            return
        for i in range(4):
            new_red, new_blue, total_moves = move(red, blue, dx[i], dy[i])
            if total_moves > 0:
                queue.append((new_red, new_blue, count + 1))
    print(-1)

bfs(red_position, blue_position)