N = int(input())
K = {}
for i in range(8):
    K[3 ** i] = i

answer = [[[' '] * (3 ** i) for _ in range(3 ** i)] for i in range(8)]

def func(k, startX, startY, endX, endY):
    if k == 1:
        for i in range(startX, endX):
            for j in range(startY, endY):
                answer[1][i][j] = '*'
        answer[1][startX+1][startY+1] = ' '
    elif k > 1:
        size = 3 ** k

        for x in [startX, (startX + size // 3 * 1), (startX + size // 3 * 2)]:
            for y in [startY, (startY + size // 3 * 1), (startY + size // 3 * 2)]:
                if x == (startX + size // 3 * 1) and y == (startY + size // 3 * 1):
                    continue
                for i in range(3 ** (k-1)):
                    for j in range(3 ** (k-1)):
                        answer[k][i + x][j + y] = answer[k-1][i][j]


for i in range(1, 8):
    func(i, 0, 0, 3**i, 3**i)

for row in answer[K[N]]:
    print(*row, sep='')

# print(answer[7][0][0])