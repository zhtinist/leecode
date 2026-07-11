"""
LeetCode #1361 - Validate Binary Tree Nodes
中文题名：验证二叉树
https://leetcode.com/problems/validate-binary-tree-nodes/

You have `n` binary tree nodes numbered from `0` to
`n - 1` where node `i` has two children `leftChild[i]` and `rightChild[i]`,
return `true` if and only if all the given nodes
form exactly one valid binary tree.

If node `i` has no left child
then `leftChild[i]` will equal `-1`, similarly
for the right child.

Note that the nodes have no values and that we only use the node numbers in this
problem.

Example 1:

Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]
Output: true

Example 2:

Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]
Output: false

Example 3:

Input: n = 2, leftChild = [1,0], rightChild = [-1,-1]
Output: false

Example 4:

Input: n = 6, leftChild = [1,-1,-1,4,-1,-1], rightChild = [2,-1,-1,5,-1,-1]
Output: false

Constraints:

`1 <= n <= 10^4`

`leftChild.length == rightChild.length == n`

`-1 <= leftChild[i], rightChild[i] <= n - 1`

【中文翻译】
有 `n` 个二叉树节点，编号从 `0` 到 `n - 1`，节点 `i` 有两个子节点 `leftChild[i]` 和 `rightChild[i]`。

只有当所有给定节点恰好构成一棵有效的二叉树时，返回 `true`；否则返回 `false`。

如果节点 `i` 没有左子节点，则 `leftChild[i]` 等于 `-1`，右子节点同理。

注意节点没有值，问题中仅使用节点编号。

示例 1：
输入：n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]
输出：true

示例 2：
输入：n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]
输出：false

示例 3：
输入：n = 2, leftChild = [1,0], rightChild = [-1,-1]
输出：false

示例 4：
输入：n = 6, leftChild = [1,-1,-1,4,-1,-1], rightChild = [2,-1,-1,5,-1,-1]
输出：false
"""

from typing import List
from collections import deque


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        # 计算每个节点的入度
        indegree = [0] * n
        for i in range(n):
            if leftChild[i] != -1:
                indegree[leftChild[i]] += 1
            if rightChild[i] != -1:
                indegree[rightChild[i]] += 1

        # 找到根节点（入度为 0 的节点）
        root = -1
        for i in range(n):
            if indegree[i] == 0:
                if root != -1:
                    return False  # 多个根节点
                root = i

        if root == -1:
            return False  # 没有根节点，存在环

        # BFS 验证是否所有节点都被访问且无环
        visited = set()
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if node in visited:
                return False  # 检测到环
            visited.add(node)

            if leftChild[node] != -1:
                queue.append(leftChild[node])
            if rightChild[node] != -1:
                queue.append(rightChild[node])

        return len(visited) == n



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 二叉树的有效性需满足三个条件：(1) 有且仅有一个根节点；(2) 无环；(3) 所有节点连通。
# 1. 计算每个节点的入度（被指向的次数）。二叉树的根节点入度为 0，其他节点入度应为 1。
# 2. 找到入度为 0 的节点作为根。如果没有或有多于一个根节点，返回 False。
# 3. 从根节点开始 BFS/DFS 遍历，用 visited 集合记录已访问节点。
#    如果遍历到已访问节点说明有环，返回 False。
# 4. 遍历结束后检查 visited 大小是否等于 n（确保所有节点可达）。
#
# 时间复杂度: O(N)，N 为节点数
# 空间复杂度: O(N)，入度数组、visited 集合和队列
#
# 关键点:
# - 通过入度确定唯一根节点
# - BFS/DFS 验证连通性和检测环
# - 三个条件缺一不可：唯一根、无环、全连通













