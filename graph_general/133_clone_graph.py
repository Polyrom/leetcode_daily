"""
https://leetcode.com/problems/clone-graph

133. Clone Graph

Given a reference of a node in a connected undirected graph.
Return a deep copy (clone) of the graph.
"""


class Node(object):
    def __init__(self, val: int = 0, neighbors: "list[Node] | None" = None):
        self.val = val
        self.neighbors = neighbors or []


def clone_graph(node: Node | None) -> Node | None:
    old_to_new = {}

    def clone(node: Node) -> Node:
        if node in old_to_new:
            return old_to_new[node]
        copy = Node(node.val)
        old_to_new[node] = copy
        for neighbor in node.neighbors:
            copy.neighbors.append(clone(neighbor))
        return copy

    return clone(node) if node else None


# or, just use copy.deepcopy :)
