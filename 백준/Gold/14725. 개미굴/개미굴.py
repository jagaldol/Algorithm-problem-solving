import sys

input = sys.stdin.readline

N = int(input())


class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def find_child(self, value):
        for child in self.children:
            if child.value == value:
                return child
        return None


root = Node(0)

for _ in range(N):
    A = input().rstrip().split()
    parent = root
    for i in range(1, len(A)):
        child = parent.find_child(A[i])
        if child is None:
            child = Node(A[i])
            parent.add_child(child)
        parent = child


def sort_children(node: Node):
    node.children.sort(key=lambda x: x.value)
    for child in node.children:
        sort_children(child)


sort_children(root)


def print_tree(node: Node, depth=-1):
    if depth >= 0:
        print("--" * depth + node.value)
    for child in node.children:
        print_tree(child, depth + 1)


print_tree(root)
