import heapq
import sys
input = sys.stdin.readline

n = int(input())
q = []
answer = []

for _ in range(n):
    x = int(input())
    if x == 0:
        if q:
            num = heapq.heappop(q)
            if num % 2 == 0:
                answer.append(num // 2)
            else:
                answer.append((num + 1) // 2 * (-1))
        else:
            answer.append(0)
    else:
        if x > 0:
            heapq.heappush(q, x * 2)
        else:
            heapq.heappush(q, -(x * 2) - 1)

for i in answer:
    print(i)