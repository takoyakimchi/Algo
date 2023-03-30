import sys
import heapq

input = sys.stdin.readline
INF = 10 ** 10

N, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(E):
    v1, v2, c = map(int, input().split())
    graph[v1].append((v2, c))
    graph[v2].append((v1, c))

node1, node2 = map(int, input().split())


def dijkstra(start):
    min_cost = [INF] * (N + 1)

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

    return min_cost

min_cost_start = dijkstra(1)
min_cost_node1 = dijkstra(node1)
min_cost_node2 = dijkstra(node2)

# print(min_cost_start)
# print(min_cost_node1)
# print(min_cost_node2)

answer = min(min_cost_start[node1] + min_cost_node1[node2] + min_cost_node2[N],
             min_cost_start[node2] + min_cost_node2[node1] + min_cost_node1[N]
             )

if answer >= INF:
    answer = -1

print(answer)