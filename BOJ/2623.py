from collections import deque
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
incoming_edges = [0] * (N+1)
visited = [0] * (N+1)
answer = []

for _ in range(M):
    arr = list(map(int, input().split()))
    for i in range(1, len(arr) - 1):
        graph[arr[i]].append(arr[i+1])
        incoming_edges[arr[i+1]] += 1

queue = deque([])
for i in range(1, N+1):
    if incoming_edges[i] == 0:
        queue.append(i)

while queue:
    node = queue.popleft()
    visited[node] = 1
    answer.append(node)
    for next_node in graph[node]:
        incoming_edges[next_node] -= 1
        if incoming_edges[next_node] == 0:
            queue.append(next_node)

if len(answer) == 0 or sum(visited) != N:
    print(0)
else:
    print(*answer, sep='\n')