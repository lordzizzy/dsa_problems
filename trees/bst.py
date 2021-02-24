from __future__ import annotations
from typing import Deque, Generic, List, Optional, TypeVar, Union


T = TypeVar("T")
Numeric = Union[int, float]


class Node(Generic[T]):
    def __init__(
        self, val: T, left: Optional[Node[T]] = None, right: Optional[Node[T]] = None
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


def insert_node(root: Node[Numeric], node: Node[Numeric]) -> Node[Numeric]:
    if root == node:
        return root
    assert (
        node.left is None and node.right is None
    ), f"Node that should be inserted should have no children."
    if root.val < node.val:
        if root.right is None:
            root.right = node
        else:
            insert_node(root.right, node)
    else:
        if root.left is None:
            root.left = node
        else:
            insert_node(root.left, node)
    return root


def level_order_traverse(root: Node[Numeric]) -> None:
    q = Deque([root])
    while q:
        node = q.popleft()
        print(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)


def in_order_traverse(root: Node[Numeric]) -> None:
    if root.left:
        in_order_traverse(root.left)
    print(root.val)
    if root.right:
        in_order_traverse(root.right)


def pre_order_traverse(root: Node[Numeric]) -> None:
    print(root.val)
    if root.left:
        pre_order_traverse(root.left)
    if root.right:
        pre_order_traverse(root.right)


def post_order_traverse(root: Node[Numeric]) -> None:
    if root.left:
        post_order_traverse(root.left)
    if root.right:
        post_order_traverse(root.right)
    print(root.val)


def build_tree(nodes: List[Numeric]) -> Node[Numeric]:
    assert len(nodes) > 0, f"Length of nodes must be greater than 0"
    root = Node(nodes[0])
    for i in range(1, len(nodes)):
        val = nodes[i]
        insert_node(root, Node(val))
    return root


if __name__ == "__main__":
    root = build_tree(nodes=[4, 2, 3, 1, 5])

    print("pre order traverse")
    pre_order_traverse(root)

    print("in order traverse")
    in_order_traverse(root)

    print("post order traverse")
    post_order_traverse(root)

    print("level order traverse")
    level_order_traverse(root)
