graph = []
zero_points = []
solved = False

for _ in range(9):
    graph.append(list(map(int, input().split())))

for i in range(9):
    for j in range(9):
        if graph[i][j] == 0:
            zero_points.append((i, j))

def dfs(idx):
    global solved
    if idx == len(zero_points):
        for r in graph:
            print(*r)
        solved = True
        return

    x, y = zero_points[idx]
    case = {1, 2, 3, 4, 5, 6, 7, 8, 9}

    # 같은 행에서 나타나는 숫자 제거
    for col in graph[x]:
        if col in case:
            case.remove(col)

    # 같은 열에서 나타나는 숫자 제거
    for row in range(0, 9):
        if graph[row][y] in case:
            case.remove(graph[row][y])

    # 같은 블럭에서 나타나는 숫자 제거
    start_x, start_y = (x // 3) * 3, (y // 3) * 3
    for i in range(start_x, start_x + 3):
        for j in range(start_y, start_y + 3):
            if graph[i][j] in case:
                case.remove(graph[i][j])

    # print(case)
    for num in case:
        if solved:
            break
        graph[x][y] = num
        dfs(idx + 1)
        graph[x][y] = 0

dfs(0)