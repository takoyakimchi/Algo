import sys
import heapq
input = sys.stdin.readline
INF = 10 ** 10

N = int(input()) # node
M = int(input()) # edge
graph = [[] for _ in range(N+1)]
min_cost = [INF] * (N+1)

for _ in range(M):
    v1, v2, c = map(int, input().split())
    graph[v1].append((v2, c))

start_node, end_node = map(int, input().split())

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
                min_cost[next_node] = cost + next_cost
                heapq.heappush(q, (cost + next_cost, next_node))

dijkstra(start_node)
print(min_cost[end_node])