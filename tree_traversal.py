from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def inorderRecursive(node):
    if not node:
        return
    inorderRecursive(node.left)
    print(node.val)
    inorderRecursive(node.right)

def inorderIterative(node):
    stack = []
    curr = node
    while curr or stack:
        if curr:
            while curr:
                stack.append(curr)
                curr = curr.left
        elif stack:
            n = stack.pop()
            print(n.val)
            if n.right:
                curr = n.right


def preorderRecursive(node):
    if not node:
        return
    print(node.val)
    preorderRecursive(node.left)
    preorderRecursive(node.right)


def preorderIterative(node):
    stack = [node]
    while stack:
        n = stack.pop()
        print(n.val)
        if n.right:
            stack.append(n.right)
        if n.left:
            stack.append(n.left)


def postorderRecursive(node):
    if not node:
        return
    postorderRecursive(node.left)
    postorderRecursive(node.right)
    print(node.val)

def postorderIterative(node):
    stack = [node]
    postorder = []
    while stack:
        n = stack.pop()
        postorder.append(n.val)
        if n.left:
            stack.append(n.left)
        if n.right:
            stack.append(n.right)
    while postorder:
        print(postorder.pop())


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    print("Inorder Recursive")
    inorderRecursive(root)
    print("Inorder Iterative")
    inorderIterative(root)
    print("------------------")
    print("Preorder Recursive")
    preorderRecursive(root)
    print("Preorder Iterative")
    preorderIterative(root)
    print("------------------")
    print("Postorder Recursive")
    postorderRecursive(root)
    print("Postorder Iterative")
    postorderIterative(root)