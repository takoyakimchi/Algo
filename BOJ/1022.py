def answer(row, col):
    group = max(abs(row), abs(col))

    bottom_right = 1 + 4 * (group * (group + 1))
    bottom_left = bottom_right - group * 2
    top_left = bottom_left - group * 2
    top_right = top_left - group * 2

    if row == group:
        return bottom_left + (col + group)
    elif row == -group:
        return top_left - (col + group)
    elif col == -group:
        return top_left + (row + group)
    elif col == group:
        return top_right - (row + group)

def main():
    r1, c1, r2, c2 = map(int, input().split())
    r_d, c_d = 0 - r1, 0 - c1
    result = [[0] * (c2-c1+1) for _ in range(r2-r1+1)]
    max_digit = 1

    for row in range(r1, r2+1):
        for col in range(c1, c2+1):
            ans = answer(row, col)
            result[row + r_d][col + c_d] = ans
            if ans >= 10 ** max_digit:
                max_digit = int(len(str(ans)))

    for i in range(len(result)):
        for j in range(len(result[i])):
            if j == len(result[i]) - 1:
                if i == len(result) - 1:
                    print("%*d" % (max_digit, result[i][j]), end = '')
                else:
                    print("%*d" % (max_digit, result[i][j]))
            else:
                print("%*d" % (max_digit, result[i][j]), end=' ')

if __name__ == '__main__':
    main()