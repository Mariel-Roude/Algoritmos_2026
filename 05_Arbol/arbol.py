from typing import Any, Optional
from cola import Queue


class Node:
    def __init__(self, value=None, other_values=None):
        self.value = value
        self.left = None
        self.right = None
        self.other_values = other_values
        self.height = 0

    def __str__(self):
        return str(self.value)


class BinaryTree:
    def __init__(self):
        self.root = None

   
    def height(self, root):
        if root is None:
            return -1
        return root.height

    def update_height(self, root):
        if root is not None:
            left_height = self.height(root.left)
            right_height = self.height(root.right)
            root.height = (left_height if left_height > right_height else right_height) + 1

   
    def insert_node(self, value: Any, other_value=None) -> None:
        def __insert_node(root, value, other_value=None):
            if root is None:
                root = Node(value, other_value)
            elif value < root.value:
                root.left = __insert_node(root.left, value, other_value)
            else:
                root.right = __insert_node(root.right, value, other_value)

            root = self.auto_balance(root)
            self.update_height(root)
            return root

        self.root = __insert_node(self.root, value, other_value)

    
    def delete_node(self, value: Any) -> Optional[Any]:
        def __replace(root):
            aux = None
            if root.right is None:
                return root.left, root
            else:
                root.right, aux = __replace(root.right)
            return root, aux

        def __delete_node(root, value):
            x = None
            other_value = None
            if root is not None:
                if value < root.value:
                    root.left, x, other_value = __delete_node(root.left, value)
                elif value > root.value:
                    root.right, x, other_value = __delete_node(root.right, value)
                else:
                    x = root.value
                    other_value = root.other_values
                    if root.left is None:
                        return root.right, x, other_value
                    elif root.right is None:
                        return root.left, x, other_value
                    else:
                        root.left, aux = __replace(root.left)
                        root.value = aux.value
                        root.other_values = aux.other_values  

            root = self.auto_balance(root)
            self.update_height(root)
            return root, x, other_value

        self.root, x, other_value = __delete_node(self.root, value)
        return x, other_value

   
    def search(self, value) -> Optional[Any]:
        def __search(root, value):
            aux = None
            if root is not None:
                if root.value == value:
                    aux = root
                elif value < root.value:
                    aux = __search(root.left, value)
                elif value > root.value:
                    aux = __search(root.right, value)
            return aux

        return __search(self.root, value)

   
    def auto_balance(self, root):
        if root is not None:
            if self.height(root.left) - self.height(root.right) == 2:
                if self.height(root.left.left) >= self.height(root.left.right):
                    root = self.simple_rotation(root, True)
                else:
                    root = self.double_rotation(root, True)
            elif self.height(root.right) - self.height(root.left) == 2:
                if self.height(root.right.right) >= self.height(root.right.left):
                    root = self.simple_rotation(root, False)
                else:
                    root = self.double_rotation(root, False)
        return root

    def simple_rotation(self, root, control):
        if control:  # rotación a la derecha
            aux = root.left
            root.left = aux.right
            aux.right = root
        else:  # rotación a la izquierda
            aux = root.right
            root.right = aux.left
            aux.left = root

        self.update_height(root)
        self.update_height(aux)
        return aux

    def double_rotation(self, root, control):
        if control:  # rotación doble a la derecha
            root.left = self.simple_rotation(root.left, False)
            root = self.simple_rotation(root, True)
        else:  # rotación doble a la izquierda
            root.right = self.simple_rotation(root.right, True)
            root = self.simple_rotation(root, False)
        return root

  
    def inorden(self) -> None:
        def __inorden(root):
            if root is not None:
                __inorden(root.left)
                print(root.value)
                __inorden(root.right)
        __inorden(self.root)

    def preorden(self) -> None:
        def __preorden(root):
            if root is not None:
                print(root.value)
                __preorden(root.left)
                __preorden(root.right)
        __preorden(self.root)

    def postorden(self) -> None:
        def __postorden(root):
            if root is not None:
                __postorden(root.right)
                print(root.value)
                __postorden(root.left)
        __postorden(self.root)

    def by_level(self) -> None:
        pendings = Queue()
        if self.root is not None:
            pendings.arrive(self.root)
            while pendings.size() > 0:
                node = pendings.attention()
                print(node.value)
                if node.left is not None:
                    pendings.arrive(node.left)
                if node.right is not None:
                    pendings.arrive(node.right)

  
    def inorden_villain(self) -> None:
        def __inorden_villain(root):
            if root is not None:
                __inorden_villain(root.left)
                if root.other_values and root.other_values.get('is_villain'):
                    print(root.value)
                __inorden_villain(root.right)
        __inorden_villain(self.root)

    def postorden_hero(self) -> None:
        def __postorden_hero(root):
            if root is not None:
                __postorden_hero(root.right)
                if root.other_values and not root.other_values.get('is_villain'):
                    print(root.value)
                __postorden_hero(root.left)
        __postorden_hero(self.root)

    def inorden_hero_star_with(self, prefix: str) -> None:
        def __inorden_hero_star_with(root, prefix):
            if root is not None:
                __inorden_hero_star_with(root.left, prefix)
                if str(root.value).startswith(prefix) and root.other_values and not root.other_values.get('is_villain'):
                    print(root.value)
                __inorden_hero_star_with(root.right, prefix)
        __inorden_hero_star_with(self.root, prefix)

    def proxy_search(self, prefix: str) -> None:
        def __proxy_search(root, prefix):
            if root is not None:
                __proxy_search(root.left, prefix)
                if prefix in str(root.value).lower():
                    print(root.value)
                __proxy_search(root.right, prefix)
        __proxy_search(self.root, prefix)

    def count_heroes(self) -> int:
        def __count_heroes(root):
            count = 0
            if root is not None:
                count += __count_heroes(root.left)
                if root.other_values and not root.other_values.get('is_villain'):
                    count += 1
                count += __count_heroes(root.right)
            return count
        return __count_heroes(self.root)