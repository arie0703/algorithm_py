class Node(object):
    def __init__(self, value: int) -> None:
        self.value = value
        self.left = None
        self.right = None


class BinarySearch(object):

    def __init__(self) -> None:
        self.root = None
    
    def insert(self, value: int) -> None:
        if self.root is None:
            self.root = Node(value)
            return

        def _insert (node: Node, value: int) -> Node:
            if node is None:
                return Node(value)

            if value < node.value:
                node.left = _insert(node.left, value)
            else:
                node.right = _insert(node.right, value)
            return node
        _insert(self.root, value)



    # left -> root -> Rightの順に出力
    def inorder(self) -> None:
        def _inorder(node: Node) -> None:
            if node is not None:
                _inorder(node.left)
                print(node.value)
                _inorder(node.right)
        _inorder(self.root)

    # node ある指定のnode value 探したい値
    def search(self, value: int) -> bool:
        def _search(node: Node, value: int) -> bool:
            if node is None:
                return False
            
            if node.value == value:
                return True
            elif node.value > value:
                _search(node.left, value)
        return _search(self.root, value)


    def min_value(self, node: Node) -> None:
        current = node
        while current.left is not None:
            current = current.left
        
        return current

    def remove(self, value: int) -> None:
        def _remove(node: None, value: int) -> Node:
            if node is None:
                return node

            #nodeがvalueと一致するまで再帰させる
            if value < node.value:
                node.left = _remove(node.left, value)
            elif value > node.value:
                node.right = _remove(node.right, value)
            else:
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left

                temp = self.min_value(node.right)
                node.value = temp.value
                node.right = _remove(node.right, temp.value)
            return node
        _remove(self.root, value)


binary_tree = BinarySearch()
binary_tree.insert(3)
binary_tree.insert(6)
binary_tree.insert(5)
binary_tree.insert(7)
binary_tree.insert(1)
binary_tree.insert(10)
binary_tree.insert(2)
binary_tree.inorder()
# binary_tree.remove(6)

print('########')
binary_tree.inorder()


