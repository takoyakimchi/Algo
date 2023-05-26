n = int(input())
graph = []

for _ in range(n):
    row = list(map(int,input().split()))
    graph.append(row)

for k in range(n):
    for a in range(n):
        for b in range(n):
            if graph[a][k] == 1 and graph[k][b] == 1:
                graph[a][b] = 1

for row in graph:
    print(*row)