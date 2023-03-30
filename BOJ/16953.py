from collections import deque
A, B = map(int, input().split())
counts = {A: 1}


def bfs():
    queue = deque([])
    queue.append(A)
    while queue:
        num = queue.popleft()

        new_num1 = int(str(num) + '1')
        if new_num1 <= B:
            queue.append(new_num1)
            counts[new_num1] = counts[num] + 1

        new_num2 = num * 2
        if new_num2 <= B:
            queue.append(new_num2)
            counts[new_num2] = counts[num] + 1

bfs()
if B in counts:
    print(counts[B])
else:
    print(-1)