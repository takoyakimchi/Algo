n = int(input())
tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    parent, child, cost = map(int, input().split())
    tree[parent].append(child)

def dfs(node):
    if len(tree[node]) == 0:
        return
    else:
        dfs(tree[node][0])
        dfs(tree[node][1])