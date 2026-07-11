"""
LeetCode #386 - Lexicographical Numbers
中文题名：字典序排数
https://leetcode.com/problems/lexicographical-numbers/

Given an integer n, return 1 - n in lexicographical order.

For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].

Please optimize your algorithm to use less time and space. The input size may be as large as
5,000,000.

【中文翻译】
给定一个整数 n，返回从 1 到 n 的字典序排列。

例如，给定 13，返回：[1,10,11,12,13,2,3,4,5,6,7,8,9]。

请优化你的算法使其使用更少的时间和空间。输入大小可能高达 5,000,000。
"""

from typing import List, Optional


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []
        curr = 1
        for _ in range(n):
            result.append(curr)
            if curr * 10 <= n:
                curr *= 10
            else:
                while curr % 10 == 9 or curr + 1 > n:
                    curr //= 10
                curr += 1
        return result











# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用迭代法模拟十叉树的前序遍历（DFS），无需实际构建树。
# 从 curr = 1 开始，每次将 curr 加入结果后，按字典序找下一个数：
# 1. 如果 curr * 10 <= n，则尝试进入下一层（加一个 0 后缀），即 curr = curr * 10。
# 2. 否则，需要回溯：
#    - 如果 curr 的个位是 9，或者 curr + 1 > n，则不断除以 10（回到上一层）。
#    - 然后 curr = curr + 1（向右移动到兄弟节点）。
# 重复以上步骤 n 次，直到生成所有 n 个数。
# 这本质上是模拟了在数字 1~9 的十叉树上的 DFS 遍历。
#
# 时间复杂度: O(n) - 每个数字恰好访问一次
# 空间复杂度: O(1) - 除输出列表外只使用常数额外空间
#
# 关键点:
# - 字典序等价于十叉树的先序遍历
# - 迭代方式避免了递归的函数调用开销，适合 n 高达 5,000,000
# - 关键技巧：乘以 10 进入子树 / 除以 10 回溯 / 加 1 横向移动
# - 注意回溯条件：当前数个位为 9 或 curr+1 > n 时需要回溯
