import sys
sys.setrecursionlimit(10 ** 7)

nodemap = []
nodes = []
tree = []
answer = [[], []]

def make_tree(root, left_end, right_end):
    if left_end < root:
        _, left = max((y, idx) for x, y, idx in nodes[left_end:root])
        tree[root][0] = left
        make_tree(left, left_end, root - 1)
    
    if root < right_end:
        _, right = max((y, idx) for x, y, idx in nodes[root + 1:right_end + 1])
        tree[root][1] = right
        make_tree(right, root + 1, right_end)

def preorder(root):
    answer[0].append(nodemap[root])
    if tree[root][0] != -1: preorder(tree[root][0])
    if tree[root][1] != -1: preorder(tree[root][1])
    

def postorder(root):
    if tree[root][0] != -1: postorder(tree[root][0])
    if tree[root][1] != -1: postorder(tree[root][1])
    answer[1].append(nodemap[root])
    

def solution(nodeinfo):
    sorted_nodeinfo = sorted([(x, y, idx + 1) for idx, (x, y) in enumerate(nodeinfo)])
    
    global nodemap, nodes, tree
    nodemap = [num for x, y, num in sorted_nodeinfo]
    nodes = [(x, y, idx) for idx, (x, y, num) in enumerate(sorted_nodeinfo)]
    tree = [[-1, -1] for _ in range(len(nodeinfo))]
    
    _, root = max((y, idx) for x, y, idx in nodes)
    make_tree(root, 0, len(nodes) - 1)
    preorder(root)
    postorder(root)
    return answer