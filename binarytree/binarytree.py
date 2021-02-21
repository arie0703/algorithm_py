class Node(object):
    def __init__(self, value: int) -> None:
        self.value = value
        self.left = None
        self.right = None
    

def insert (node: Node, value: int) -> Node:
    if node is None:
        return Node(value)

    if value < node.value:
        node.left = insert(node.left, value)
    else:
        node.right = insert(node.right, value)
    return node

# left -> root -> Rightの順に出力
def inorder(node: Node) -> None:
    if node is not None:
        inorder(node.left)
        print(node.value)
        inorder(node.right)

# node ある指定のnode value 探したい値
def search(node: Node, value: int) -> bool:
    if node is None:
        return False
    
    if node.value == value:
        return True
    elif node.value > value:
        search(node.left, value)


def min_value(node: Node) -> None:
    current = node
    while current.left is not None:
        current = current.left
    
    return current

def remove(node: None, value: int) -> Node:
    if node is None:
        return node

    #nodeがvalueと一致するまで再帰させる
    if value < node.value:
        remove(node.left, value)
    elif value > node.value:
        remove(node.right, value)
    else:
        if node.left is None:
            return node.right
        elif node.right is None:
            return node.left

        temp = min_value(node.right)
        node.value = temp.value
        node.right = remove(node.right, temp.value)
    return node


root = None
root = insert(root, 3)
root = insert(root, 6)
root = insert(root, 5)
root = insert(root, 7)
root = insert(root, 1)
root = insert(root, 10)
root = insert(root, 2)


inorder(root)
# search(root, 6)
root = remove(root, 6)
print('########')
inorder(root)
