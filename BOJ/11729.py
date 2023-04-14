total = 0
answer = []

def hanoi(start, middle, end, cnt):
    global total
    if cnt == 1:
        answer.append((start, end))
        total += 1
    elif cnt > 1:
        hanoi(start, end, middle, cnt-1)
        answer.append((start, end))
        total += 1
        hanoi(middle, start, end, cnt-1)

n = int(input())
hanoi(1, 2, 3, n)
print(total)
for x in answer:
    print(*x)