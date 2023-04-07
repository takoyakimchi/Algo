T = int(input())
dp = [[] for _ in range(10)]
answer = [[] for _ in range(10)]
dp[2] += ["1+2", "1-2", "12"]
answer[2] += ["1+2", "1-2", "1 2"]

final_answer = []

for i in range(3, 10):
    for j in range(len(dp[i-1])):
        dp[i].append(dp[i-1][j] + "+" + str(i))
        dp[i].append(dp[i-1][j] + "-" + str(i))
        dp[i].append(dp[i-1][j] + str(i))
        answer[i].append(answer[i-1][j] + "+" + str(i))
        answer[i].append(answer[i-1][j] + "-" + str(i))
        answer[i].append(answer[i-1][j] + " " + str(i))

for _ in range(T):
    n = int(input())
    answer_list = []

    for i in range(len(dp[n])):
        if eval(dp[n][i]) == 0:
            answer_list.append(answer[n][i])

    final_answer.append(sorted(answer_list))


for i in final_answer:
    for j in i:
        print(j)
    if i != len(final_answer) - 1:
        print()