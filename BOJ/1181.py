arr = []
for _ in range(int(input())):
    arr.append(input())
arr = list(set(arr))
arr.sort(key= lambda x: (len(x), x))
print(*arr, sep="\n")