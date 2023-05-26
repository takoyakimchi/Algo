import sys
input = sys.stdin.readline
arr = list(map(int, input().split()))

dp = [[(2, arr[0], 0), (2, 0, arr[0])]] # 왼발 (최소힘, 왼발위치, 오른발위치), 오른발 (최소힘, 왼발위치, 오른발위치)

def move(n1, n2):
    if n1 == n2:
        return 1
    elif n1 == 0:
        return 2
    elif abs(n1 - n2) == 1 or abs(n1 - n2) == 3:
        return 3
    else:
        return 4

for i in range(1, len(arr) - 1):
    ls = []

    Lmin, Lleft, Lright = dp[i-1][0]
    Rmin, Rleft, Rright = dp[i-1][1]

    LtoL = move(Lleft, i)
    RtoL = move(Rleft, i)
    if LtoL < RtoL:
        ls.append((Lmin + LtoL, i, Lright))
    else:
        ls.append((Rmin + RtoL, i, Rright))

    LtoR = move(Lright, i)
    RtoR = move(Rright, i)
    if LtoR < RtoR:
        ls.append((Lmin + LtoL, Lleft, i))
    else:
        ls.append((Rmin + RtoL, Rleft, i))

    dp.append(ls)

print(dp[-1])