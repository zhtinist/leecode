"""
LeetCode #1530 - Number of Good Leaf Nodes Pairs
中文题名：好叶子节点对的数量
https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/

Given the `root` of a binary tree and an integer `distance`. A
pair of two different leaf nodes of a binary tree is said to be good if
the length of the shortest path between them is less than or equal to
`distance`.

Return the number of good leaf node pairs in the tree.

Example 1:

Input: root = [1,2,3,null,4], distance = 3
Output: 1
Explanation: The leaf nodes of the tree are 3 and 4 and the length of the shortest path between them is 3. This is the only good pair.

Example 2:

Input: root = [1,2,3,4,5,6,7], distance = 3
Output: 2
Explanation: The good pairs are [4,5] and [6,7] with shortest path = 2. The pair [4,6] is not good because the length of ther shortest path between them is 4.

Example 3:

Input: root = [7,1,4,6,null,5,3,null,null,null,null,null,2], distance = 3
Output: 1
Explanation: The only good pair is [2,5].

Example 4:

Input: root = [100], distance = 1
Output: 0

Example 5:

Input: root = [1,1,1], distance = 2
Output: 1

Constraints:

The number of nodes in the `tree` is in the
range `[1, 2^10].`

Each node's value is between `[1, 100]`.

`1 <= distance <= 10`

【中文翻译】
给定二叉树的根节点 root 和整数 distance。
如果二叉树中两个不同的叶子节点之间的最短路径长度小于等于 distance，则称它们为"好叶子节点对"。
返回树中好叶子节点对的数量。

示例 1：

输入：root = [1,2,3,null,4], distance = 3
输出：1
解释：叶子节点 3 和 4 之间的最短路径长度为 3，是唯一的好对。

示例 2：

输入：root = [1,2,3,4,5,6,7], distance = 3
输出：2
解释：好对为 [4,5] 和 [6,7]，最短路径均为 2。[4,6] 的最短路径为 4，不是好对。

示例 3：

输入：root = [7,1,4,6,null,5,3,null,null,null,null,null,2], distance = 3
输出：1
解释：唯一的好对是 [2,5]。

示例 4：

输入：root = [100], distance = 1
输出：0

示例 5：

输入：root = [1,1,1], distance = 2
输出：1
"""

from typing import List, Optional


class Solution:
    def countPairs(self, root: Optional[TreeNode], distance: int) -> int:
        self.result = 0

        def dfs(node: Optional[TreeNode]) -> List[int]:
            """Returns list of distances from this node to all leaves in its subtree."""
            if not node:
                return []
            if not node.left and not node.right:
                return [1]  # leaf: distance 1 to itself

            left_dists = dfs(node.left)
            right_dists = dfs(node.right)

            # Count good pairs crossing this node
            for ld in left_dists:
                for rd in right_dists:
                    if ld + rd <= distance:
                        self.result += 1

            # Return incremented distances (pass up to parent)
            return [d + 1 for d in left_dists + right_dists if d + 1 < distance]

        dfs(root)
        return self.result



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用 DFS 后序遍历。每个节点返回一个列表，包含从该节点到其子树中每个叶子节点的距离。
# 叶子节点返回 [1]（到自己的距离为 1）。
# 对于内部节点，合并左右子树的距离列表，对每一对 (ld, rd) 如果 ld+rd <= distance，则计入答案。
# 向上传递时将距离 +1，并剪枝：如果 d+1 >= distance，不再向上传递（因为不可能再形成好对）。
#
# 时间复杂度: O(N * D^2) — N 个节点，每个节点合并左右子树距离列表
# 空间复杂度: O(N * D) — 递归栈 + 距离列表
#
# 关键点:
# - 好叶子节点对的路径必然经过它们的最近公共祖先 (LCA)
# - 在 LCA 处统计跨越左右子树的好对
# - 向上传递前剪枝：距离已经 >= distance 的叶子不可能再参与形成好对
