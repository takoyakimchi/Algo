import sys
import heapq
input = sys.stdin.readline
INF = 10 ** 10

V, E = map(int, input().split()) # vertex, edge
K = int(input()) # start node
graph = [[] for _ in range(V+1)] # i부터 i[0]까지의 거리가 i[1] // graph[vertex] == [(next_vertex, cost), ... ]
min_cost = [INF] * (V+1) # i번째 노드까지의 최단거리

for _ in range(E):
    v1, v2, c = map(int, input().split())
    graph[v1].append((v2, c))

def dijkstra(start):
    q = [] # heapq => (비용, 노드번호)
    heapq.heappush(q, (0, start))
    min_cost[start] = 0
    while q:
        cost, node = heapq.heappop(q) # 현재 비용 / 현재 확인중인 노드 넘버
        if cost > min_cost[node]:
            continue # 최소 비용보다 크면 확인하는 의미가 없음
        for next_node, next_cost in graph[node]: # 다음 갈 수 있는 노드를 루프
            if cost + next_cost < min_cost[next_node]:
                min_cost[next_node] = cost + next_cost
                heapq.heappush(q, (cost + next_cost, next_node))

dijkstra(K)

for i in range(1, V+1):
    if min_cost[i] == INF:
        print("INF")
    else:
        print(min_cost[i])