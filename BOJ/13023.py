N, M = map(int, input().split())
graph = [[] for _ in range(N)]
visited = [False] * N
answer = 0

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v, cnt, visited):
    global answer
    if cnt == 5:
        answer = 1
        return

    for node in graph[v]:
        if not visited[node]:
            visited[node] = True
            dfs(node, cnt + 1, visited)
            visited[node] = False

for i in range(N):
    visited[i] = True
    dfs(i, 1, visited)
    if answer == 1:
        break
    visited[i] = False

print(answer)