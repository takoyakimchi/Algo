import heapq
N, K = map(int, input().split())
INF = 10 ** 10
graph = [[] for _ in range(100001)]
min_cost = [INF] * 100001

for i in range(0, 100001):
    if i > 0:
        graph[i].append((i-1, 1))
    if i < 100000:
        graph[i].append((i+1, 1))
    if 0 < i <= 50000:
        graph[i].append((i*2, 0))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    min_cost[start] = 0
    while q:
        cost, node = heapq.heappop(q)
        if cost > min_cost[node]:
            continue
        for next_node, next_cost in graph[node]:
            if cost + next_cost < min_cost[next_node]:
                heapq.heappush(q, (cost + next_cost, next_node))
                min_cost[next_node] = cost + next_cost

dijkstra(N)
print(min_cost[K])