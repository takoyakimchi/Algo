from collections import deque

T = int(input())

for _ in range(T):
    queue = deque(input())
    n = int(input())
    nums = input()
    _list = []
    is_error = False
    reversed = False

    if n > 0:
        _list += (list(map(int, nums.lstrip('[').rstrip(']').split(','))))
    numbers = deque(_list)

    while queue:
        command = queue.popleft()
        if command == 'R':
            # numbers.reverse()
            reversed = not reversed
        elif command == 'D':
            if len(numbers) == 0:
                is_error = True
                break
            else:
                if reversed:
                    numbers.pop()
                else:
                    numbers.popleft()

    if is_error:
        print("error")
    else:
        if reversed:
            numbers.reverse()

        print('[' + ','.join(map(str, numbers)) + ']')