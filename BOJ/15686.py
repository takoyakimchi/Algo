from itertools import combinations

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

houses = []
shops = []


def get_chicken_distance(_graph, _houses, _shops):
    result = []
    for houseX, houseY in _houses:
        dist = []
        for shopX, shopY in _shops:
            dist.append(abs(houseX - shopX) + abs(houseY - shopY))
        result.append(min(dist))
    return sum(result)


for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            houses.append((i, j))
        elif graph[i][j] == 2:
            shops.append((i, j))


answer = []
for i in range(1, M+1):
    for case in combinations(shops, i):
        dist = get_chicken_distance(graph, houses, list(case))
        answer.append(dist)

print(min(answer))