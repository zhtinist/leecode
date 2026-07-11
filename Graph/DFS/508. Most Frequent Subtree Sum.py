"""
LeetCode #508 - Most Frequent Subtree Sum
中文题名：出现次数最多的子树元素和
https://leetcode.com/problems/most-frequent-subtree-sum/

Given the root of a tree, you are asked to find the most frequent subtree sum. The subtree
sum of a node is defined as the sum of all the node values formed by the subtree rooted at
that node (including the node itself). So what is the most frequent subtree sum value? If
there is a tie, return all the values with the highest frequency in any order.

Examples 1

Input:

5
/  \
2   -3

return [2, -3, 4], since all the values happen only once, return all of them in any order.

Examples 2

Input:

5
/  \
2   -5

return [2], since 2 happens twice, however -5 only occur once.

Note:
You may assume the sum of values in any subtree is in the range of 32-bit signed integer.

【中文翻译】
给定一棵二叉树的根节点，找出出现次数最多的子树元素和。
子树元素和定义为以该节点为根的子树中所有节点值之和（包括该节点本身）。
如果出现次数最多的和有多个，以任意顺序返回所有这些值。

示例 1：
    输入：
       5
      / \
     2  -3
    返回 [2, -3, 4]，因为所有值都只出现一次，以任意顺序返回所有值。
    （子树和：2, -3, 2+5+(-3)=4）

示例 2：
    输入：
       5
      / \
     2  -5
    返回 [2]，因为 2 出现了两次（两个叶子节点），而 -5 只出现一次。
    （子树和：2, -5, 2+5+(-5)=2）

注意：
    可以假设任何子树的元素和都在 32 位有符号整数的范围内。
"""

from typing import List, Optional
from collections import Counter


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        freq = Counter()

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            # 后序遍历：先计算左右子树和，再计算当前子树和
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            subtree_sum = node.val + left_sum + right_sum
            freq[subtree_sum] += 1
            return subtree_sum

        dfs(root)
        max_freq = max(freq.values())
        return [s for s, count in freq.items() if count == max_freq]


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用后序遍历（DFS）自底向上计算每个节点的子树元素和。
# 对于当前节点：子树和 = 节点值 + 左子树和 + 右子树和。
# 用 Counter 统计每个子树和出现的频率，最后找出频率最高的所有子树和。
# 如果多个子树和频率相同（并列最高），全部返回。
#
# 时间复杂度: O(N) — 每个节点被访问一次
# 空间复杂度: O(N) — 递归栈深度最坏 O(N)（退化为链表），Counter 最多存 N 个不同的和
#
# 关键点:
# - 后序遍历确保子树的子树和先被计算
# - 使用 Counter 统计频率既简洁又高效
# - 并列最高频率时需要返回所有对应的子树和
# - 空树返回空列表 []
