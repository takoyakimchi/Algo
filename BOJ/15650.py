from itertools import combinations

N, M = map(int, input().split())
arr = [i for i in range(1, N+1)]
for case in combinations(arr, M):
    print(*case)