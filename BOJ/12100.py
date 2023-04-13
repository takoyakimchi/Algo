N = int(input())
maps = []
for _ in range(N):
    maps.append(list(map(int, input().split())))

max_val = 0

def move(arr):
    global max_val

    answer = []
    stack = []
    for num in arr:
        if num != 0:
            if len(stack) == 0:
                stack.append(num)
                if num > max_val:
                    max_val = num
            else:
                # 같은 값이면 스택에서 지우고 정답에 넣기
                if stack[-1] == num:
                    _num = stack.pop() + num
                    answer.append(_num)
                    if _num > max_val:
                        max_val = _num
                # 다른 값이면 이전 값은 합쳐질 수 없으므로 스택에서 버리고, 현재 값은 스택에 넣음
                else:
                    answer.append(stack.pop())
                    stack.append(num)
                    if num > max_val:
                        max_val = num
    answer += stack
    while len(answer) < N:
        answer.append(0) # 뒤에 0 채우기
    return answer

def move_left(_map):
    result = []
    for row in _map:
        result.append(move(row))
    return result

def move_right(_map):
    result = []
    for row in _map:
        temp = move(reversed(row))
        temp.reverse()
        result.append(temp)
    return result

def move_up(_map):
    result = [[0] * N for _ in range(N)]
    for col in range(N):
        column = []
        for row in range(N):
            column.append(_map[row][col])
        for row in range(N):
            result[row][col] = move(column)[row]
    return result

def move_down(_map):
    result = [[0] * N for _ in range(N)]
    for col in range(N):
        column = []
        for row in range(N-1, -1, -1):
            column.append(_map[row][col])
        for row in range(N):
            result[row][col] = move(column)[(N-1)-row]
    return result

def dfs(_map, cnt):
    if cnt == 5:
        return
    dfs(move_up(_map), cnt + 1)
    dfs(move_down(_map), cnt + 1)
    dfs(move_left(_map), cnt + 1)
    dfs(move_right(_map), cnt + 1)

dfs(maps, 0)
print(max_val)