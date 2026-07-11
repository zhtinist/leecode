"""
LeetCode #1339 - Maximum Product of Splitted Binary Tree
中文题名：分裂二叉树的最大乘积
https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/

Given a binary tree `root`. Split the binary tree into two subtrees
by removing 1 edge such that the product of the sums of the subtrees are maximized.

Since the answer may be too large, return it modulo 10^9 + 7.

Example 1:

Input: root = [1,2,3,4,5,6]
Output: 110
Explanation: Remove the red edge and get 2 binary trees with sum 11 and 10. Their product is 110 (11*10)

Example 2:

Input: root = [1,null,2,3,4,null,null,5,6]
Output: 90
Explanation:  Remove the red edge and get 2 binary trees with sum 15 and 6.Their product is 90 (15*6)

Example 3:

Input: root = [2,3,9,10,7,8,6,5,4,11,1]
Output: 1025

Example 4:

Input: root = [1,1]
Output: 1

Constraints:

Each tree has at most `50000` nodes and at least `2`
nodes.

Each node's value is between `[1, 10000]`.

【中文翻译】
给定一个二叉树的根节点 `root`。通过移除一条边将二叉树分成两棵子树，
使得两棵子树的节点值之和的乘积最大化。

由于答案可能过大，返回其对 10^9 + 7 取模的结果。

示例 1：

输入: root = [1,2,3,4,5,6]
输出: 110
解释: 移除红色边（连接节点 1 和节点 2 的边），得到两棵和分别为 11 和 10 的二叉树。
它们的乘积为 110（11*10）。

示例 2：

输入: root = [1,null,2,3,4,null,null,5,6]
输出: 90
解释: 移除红色边，得到两棵和分别为 15 和 6 的二叉树。它们的乘积为 90（15*6）。

示例 3：

输入: root = [2,3,9,10,7,8,6,5,4,11,1]
输出: 1025

示例 4：

输入: root = [1,1]
输出: 1

约束条件：

每棵树最多有 50000 个节点，至少 2 个节点。

每个节点的值在 [1, 10000] 之间。
"""

from typing import List, Optional


class Solution:
    def maxProduct(self, root: Optional['TreeNode']) -> int:
        MOD = 10 ** 9 + 7

        # 第一次 DFS：计算整棵树的总和
        def get_total_sum(node):
            if not node:
                return 0
            return node.val + get_total_sum(node.left) + get_total_sum(node.right)

        total = get_total_sum(root)

        # 第二次 DFS：计算每个子树的节点和，并更新最大乘积
        self.max_prod = 0

        def dfs(node):
            if not node:
                return 0
            subtree_sum = node.val + dfs(node.left) + dfs(node.right)
            # 候选乘积：当前子树和 * 剩余部分和
            candidate = subtree_sum * (total - subtree_sum)
            if candidate > self.max_prod:
                self.max_prod = candidate
            return subtree_sum

        dfs(root)

        return self.max_prod % MOD



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 1. 关键洞察：切断一条边后，树被分成两部分——一棵子树（以切断边下方节点为根）和其余部分。
#    两部分的节点和分别为 subtree_sum 和 total - subtree_sum。
# 2. 第一次 DFS：遍历整棵树计算所有节点的总和 total。
# 3. 第二次 DFS：对每个节点，计算以该节点为根的子树节点和 subtree_sum。
#    - 候选乘积 = subtree_sum * (total - subtree_sum)
#    - 用此候选乘积更新全局最大乘积
# 4. 最后返回 max_prod % (10^9 + 7)。
#
# 注意：取模应在最后进行，而不是在比较乘积大小时，因为取模后的值不反映原始大小关系。
#
# 时间复杂度: O(N) — 两次 DFS 各遍历所有节点一次
# 空间复杂度: O(H) — 递归调用栈深度为树高，最坏情况 O(N)
#
# 关键点:
# - 第一次 DFS 必须先完成以获取整棵树的总和
# - 乘积可能超过 32 位整数范围，Python 自动支持大整数
# - 只在最后返回时取模，中间比较使用原始乘积值
# - 需要 Optional['TreeNode'] 类型提示或导入 TreeNode










