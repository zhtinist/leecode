"""
LeetCode #337 - House Robber III
中文题名：打家劫舍 III
https://leetcode.com/problems/house-robber-iii/

The thief has found himself a new place for his thievery again. There is only one entrance to
this area, called the "root." Besides the root, each house has one and only one
parent house. After a tour, the smart thief realized that "all houses in this place
forms a binary tree". It will automatically contact the police if two directly-linked
houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the
police.

Example 1:

Input: [3,2,3,null,3,null,1]

3
/ \
2   3
\   \
3   1

Output: 7
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.

Example 2:

Input: [3,4,5,1,3,null,1]

3
/ \
4   5
/ \   \
1   3   1

Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.

【中文翻译】
小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，被称为"根"。
除了根之外，每栋房子有且只有一个父房子。一番侦察之后，聪明的小偷意识到这个地区的所有房子排列类似于一棵二叉树。
如果两个直接相连的房子在同一天晚上被闯入，会自动触发警报。

请计算小偷在不触发警报的情况下，一晚上能够偷窃到的最高金额。

示例 1：

输入：[3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \
     3   1

输出：7
解释：小偷一晚上能够偷窃到的最高金额 = 3 + 3 + 1 = 7。

示例 2：

输入：[3,4,5,1,3,null,1]

     3
    / \
   4   5
  / \   \
 1   3   1

输出：9
解释：小偷一晚上能够偷窃到的最高金额 = 4 + 5 = 9。
"""

from typing import List, Optional


class Solution:
    def rob(self, root: Optional['TreeNode']) -> int:
        def dfs(node):
            if not node:
                return (0, 0)
            left = dfs(node.left)
            right = dfs(node.right)
            rob_curr = node.val + left[1] + right[1]
            not_rob_curr = max(left) + max(right)
            return (rob_curr, not_rob_curr)

        return max(dfs(root))











# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 树形 DP：对每个节点，DFS 返回两个值 (rob, not_rob)：
# - rob：偷当前节点时，以该节点为根的子树能获得的最大金额
# - not_rob：不偷当前节点时，以该节点为根的子树能获得的最大金额
# 递推关系：
# - rob = node.val + left.not_rob + right.not_rob（偷当前节点，子节点不能偷）
# - not_rob = max(left) + max(right)（不偷当前节点，子节点可偷可不偷，取最大值）
# 叶子节点返回 (node.val, 0)。
# 空节点返回 (0, 0)。
# 最终答案 = max(dfs(root))。
#
# 时间复杂度: O(n)，每个节点访问一次
# 空间复杂度: O(H)，递归栈深度，H 为树的高度
#
# 关键点:
# - 每个节点返回两个状态，而不是依赖全局变量
# - 自底向上的后序遍历
# - 可以只维护当前层的 rob/not_rob，无需保留子树所有结果
# - 树的打家劫舍比数组版本多一个维度（选择当前节点时需跳过子节点）
