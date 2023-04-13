import heapq
INF = 10 ** 10

n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        now_cost, now_node = heapq.heappop(q)
        if distance[now_node] < now_cost:
            continue
        for node, cost in graph[now_node]:
            next_cost = now_cost + cost
            if next_cost < distance[node]:
                distance[node] = next_cost
                heapq.heappush(q, (next_cost, node))

dijkstra(start)

for i in range(1, n+1):
    print(distance[i])