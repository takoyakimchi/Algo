s = input()
bomb = list(map(str, input()))
size = len(bomb)

stack = []

for ch in s:
    stack.append(ch)
    if stack[-size:] == bomb:
        for _ in range(size):
            stack.pop()

if len(stack) == 0:
    print("FRULA")
else:
    print(*stack, sep='')