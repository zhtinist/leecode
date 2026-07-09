"""
LeetCode #133 - Clone Graph
https://leetcode.com/problems/clone-graph/

Given a reference of a node in a connected undirected graph, return a deep copy
(clone) of the graph.

Example 1:
    Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
    Output: [[2,4],[1,3],[2,4],[1,3]]

Example 2:
    Input: adjList = [[]]
    Output: [[]]

Example 3:
    Input: adjList = []
    Output: []

Constraints:
    The number of nodes in the graph is in the range [0, 100].
    1 <= Node.val <= 100
    Node.val is unique for each node.
    There are no repeated edges and no self-loops in the graph.
    The Graph is connected and all nodes can be visited starting from the given node.
"""


# class Node:
#     def __init__(self, val=0, neighbors=None):
#         self.val = val
#         self.neighbors = neighbors if neighbors is not None else []


from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        if not node:
            return None

        clones = {}

        def dfs(original: Node) -> Node:
            if original in clones:
                return clones[original]

            copy = Node(original.val)
            clones[original] = copy
            for neighbor in original.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy

        return dfs(node)
