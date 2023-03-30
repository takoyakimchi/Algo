from collections import deque
N = int(input())
connected = [[] for _ in range(N+1)]
visited = [False] * (N+1)
parent_node = [-1] * (N+1)

for _ in range(N-1):
    node1, node2 = map(int, input().split())
    connected[node1].append(node2)
    connected[node2].append(node1)

def bfs():
    queue = deque([])
    queue.append(1)
    visited[1] = True
    while queue:
        node = queue.popleft()
        visited[node] = True
        for n in connected[node]:
            if not visited[n]:
                queue.append(n)
                parent_node[n] = node

bfs()
print(*parent_node[2:], sep='\n')