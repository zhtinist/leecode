"""
LeetCode #1104 - Path In Zigzag Labelled Binary Tree
中文题名：二叉树寻路
https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/

In an infinite binary tree where every node has two children, the nodes are labelled in row
order.

In the odd numbered rows (ie., the first, third, fifth,...), the labelling is left to right,
while in the even numbered rows (second, fourth, sixth,...), the labelling is right to
left.

Given the `label` of a node in this tree, return the labels in the path from the
root of the tree to the node with that `label`.

Example 1:

Input: label = 14
Output: [1,3,4,14]

Example 2:

Input: label = 26
Output: [1,2,6,10,26]

Constraints:

`1 <= label <= 10^6`

【中文翻译】
在一棵无限的二叉树中（每个节点都有两个子节点），节点按行顺序标记。

在奇数行（即第一、三、五...行），标记方向为从左到右，
而在偶数行（第二、四、六...行），标记方向为从右到左。

给定这棵树中某个节点的 label，返回从树的根节点到该 label 节点的路径上的所有标签。

示例 1：

输入：label = 14
输出：[1,3,4,14]

示例 2：

输入：label = 26
输出：[1,2,6,10,26]

约束条件：

`1 <= label <= 10^6`
"""

from typing import List, Optional


class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        result = []
        while label >= 1:
            result.append(label)
            label //= 2
        result.reverse()

        n = len(result)
        for i in range(n):
            level = n - 1 - i
            if level % 2 == 1:
                level_start = 1 << level
                level_end = (1 << (level + 1)) - 1
                result[i] = level_end - (result[i] - level_start)

        return result










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 1. 首先忽略"之"字形编号，按照普通完全二叉树的规则向上回溯：每次将 label // 2 得到父节点的编号。
#    例如 label=14: 14 -> 7 -> 3 -> 1，得到路径 [1,3,7,14]。
# 2. 然后从根到叶子遍历该路径，对于在"偶数层"（从根开始，根为第0层）的节点，需要将其值翻转为
#    该层在之字形规则下的实际值。翻转公式：实际值 = 层起始值 + 层末尾值 - 当前值。
#    其中第 k 层的起始值为 2^k，末尾值为 2^(k+1) - 1。
# 3. 判断层数：根在第0层（奇数行，左到右），第1层（偶数行，右到左），以此类推。
#    从底层算起：level = len(path) - 1 - index，若 level % 2 == 1 则需要翻转。
#
# 时间复杂度: O(log n) - label 最多有 log2(label) 位，路径长度即为层数
# 空间复杂度: O(log n) - 存储路径数组
#
# 关键点:
# - 之字形二叉树中，偶数行的编号是逆序的，需要翻转恢复
# - 翻转公式：若第 k 层正常编号范围为 [2^k, 2^{k+1}-1]，翻转后对称位置的值 = 2^k + 2^{k+1} - 1 - x
# - 另一种解法：在向上回溯时直接计算正确父节点，无需两遍遍历
