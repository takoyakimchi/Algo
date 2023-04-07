"""
A -> 1, B -> 2, ..., Z -> 26
BEAN -> 25114
2 5 1 1 4


25
2/5, 25

251
2/5/1, 25/1

2511
2/5/1/1, 25/1/1
뒤에 두글자 <= 26이므로
2/5/11, 25/11

뒤 첫글자 봄 -> 0이 아니면 dp[i-1] 추가
뒤 두글자 봄 -> 10~26이면 dp[i-2] 추가
둘다 추가되지 않음 -> 잘못된 암호 -> 0 출력
"""

def main():
    code = input()
    size = len(code)
    dp = [0] * size

    if code[0] == '0':
        print(0)
        return 0

    # dp[0] and dp[1] 채우기
    dp[0] = 1
    if size > 1:
        if code[1] != '0':
            dp[1] += 1
        if 10 <= int(code[0] + code[1]) <= 26:
            dp[1] += 1

    # dp[2] ~ 마지막 채우기
    for i in range(2, size):
        did_change = False
        if code[i] != '0':
            dp[i] += dp[i-1] % 1000000
            did_change = True
        if 10 <= int(code[i-1] + code[i]) <= 26:
            dp[i] += dp[i-2] % 1000000
            did_change = True
        if not did_change:
            print(0)
            return

    print(dp[size-1] % 1000000)

if __name__ == "__main__":
    main()