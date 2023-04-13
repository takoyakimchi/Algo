import heapq

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
incoming_edges = [0] * (N+1)
answer = []

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    incoming_edges[b] += 1

queue = []
for i in range(1, N+1):
    if incoming_edges[i] == 0:
        heapq.heappush(queue, i)

while queue:
    node = heapq.heappop(queue)
    answer.append(node)
    for next_node in graph[node]:
        incoming_edges[next_node] -= 1
        if incoming_edges[next_node] == 0:
            heapq.heappush(queue, next_node)

print(*answer)