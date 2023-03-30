N = int(input())
tree = {}

for _ in range(N):
    root, left, right = input().split()
    tree[root] = (left, right)

def preorder(root, left, right):
    print(root, end='')
    if left != '.':
        preorder(left, tree[left][0], tree[left][1])
    if right != '.':
        preorder(right, tree[right][0], tree[right][1])

def inorder(left, root, right):
    if left != '.':
        inorder(tree[left][0], left, tree[left][1])
    print(root, end='')
    if right != '.':
        inorder(tree[right][0], right, tree[right][1])

def postorder(left, right, root):
    if left != '.':
        postorder(tree[left][0], tree[left][1], left)
    if right != '.':
        postorder(tree[right][0], tree[right][1], right)
    print(root, end='')


preorder('A', tree['A'][0], tree['A'][1])
print()
inorder(tree['A'][0], 'A', tree['A'][1])
print()
postorder(tree['A'][0], tree['A'][1], 'A')