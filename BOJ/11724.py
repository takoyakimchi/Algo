from collections import deque
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
answer = 0

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(graph, start, visited):
    global answer
    if not visited[start]:
        queue = deque([start])
        visited[start] = True
        while queue:
            node = queue.popleft()
            for i in graph[node]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
        answer += 1

for i in range(1, N+1):
    bfs(graph, i, visited)

print(answer)