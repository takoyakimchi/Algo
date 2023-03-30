from collections import deque
import sys
input = sys.stdin.readline

exp = input().strip()

def to_postfix(s):
    operator = deque([])  # 연산자
    operand = deque([])  # 피연산자
    bracket = 0
    start_idx = 0
    answer = ""
    bracket_mode = False

    for i in range(len(s)):
        if s[i] == '(':
            bracket += 1
            if not bracket_mode:
                start_idx = i + 1
            bracket_mode = True
        elif s[i] == ')':
            bracket -= 1
            if bracket == 0:
                inside_str = s[start_idx:i]
                if len(operator) > 0 and operator[-1] in '*/':
                    left = operand.pop()
                    right = to_postfix(inside_str)
                    o = operator.pop()
                    operand.append(left + right + o)
                else:
                    operand.append(to_postfix(inside_str))
                bracket_mode = False
        elif s[i] in '/*-+':
            if not bracket_mode:
                operator.append(s[i])
        else: # 알파벳
            if not bracket_mode:
                if len(operator) > 0 and operator[-1] in '*/':
                    left = operand.pop()
                    o = operator.pop()
                    operand.append(left + s[i] + o)
                else:
                    operand.append(s[i])

    # print(operand)
    # print(operator)
    answer += operand.popleft()
    while operand:
        answer += operand.popleft()
        answer += operator.popleft()

    return answer

print(to_postfix(exp))