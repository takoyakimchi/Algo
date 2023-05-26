from itertools import combinations

while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break

    new_arr = arr[1:]
    for comb in combinations(new_arr, 6):
        print(*comb)
    print()