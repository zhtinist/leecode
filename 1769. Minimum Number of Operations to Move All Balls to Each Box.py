"""
LeetCode #1769 - Minimum Number of Operations to Move All Balls to Each Box
中文题名：移动所有球到每个盒子所需的最小操作数
https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/

You have `n` boxes. You are given a binary string `boxes` of length `n`, where `boxes[i]` is `'0'` if the `ith` box is empty, and `'1'` if it contains one ball.

In one operation, you can move one ball from a box to an adjacent box. Box `i` is adjacent to box `j` if `abs(i - j) == 1`. Note that after doing so, there may be more than one ball in some boxes.

Return an array `answer` of size `n`, where `answer[i]` is the minimum number of operations needed to move all the balls to the `ith` box.

Each `answer[i]` is calculated considering the initial state of the boxes.

Example 1:

Input: boxes = "110"
Output: [1,1,3]
Explanation: The answer for each box is as follows:
1) First box: you will have to move one ball from the second box to the first box in one operation.
2) Second box: you will have to move one ball from the first box to the second box in one operation.
3) Third box: you will have to move one ball from the first box to the third box in two operations, and move one ball from the second box to the third box in one operation.

Example 2:

Input: boxes = "001011"
Output: [11,8,5,4,3,4]

Constraints:

`n == boxes.length`

`1 <= n <= 2000`

`boxes[i]` is either `'0'` or `'1'`.

【中文翻译】
给定一个由 n 个盒子组成的字符串 boxes，boxes[i] = '1' 表示第 i 个盒子中有球，'0' 表示没有。
一次操作可以将一个球移动到相邻的盒子中。
返回长度为 n 的数组 answer，answer[i] 是将所有球移动到第 i 个盒子所需的最小操作数。

示例 1：
输入: boxes = "110"
输出: [1,1,3]
解释: 移到盒子0：盒1的球移1步=1操作。移到盒子1：盒0移1步+盒2无球=1。移到盒子2：盒0移2步+盒1移1步=3。
"""

from typing import List, Optional


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        answer = [0] * n

        # 从左到右：计算左侧球对当前位置的贡献
        count = 0  # 左侧球的数量
        ops = 0    # 左侧球移动到当前位置的总操作数
        for i in range(n):
            answer[i] += ops
            if boxes[i] == '1':
                count += 1
            ops += count  # 每个左侧球到下一个位置都需要多一步

        # 从右到左：计算右侧球对当前位置的贡献
        count = 0
        ops = 0
        for i in range(n - 1, -1, -1):
            answer[i] += ops
            if boxes[i] == '1':
                count += 1
            ops += count

        return answer
# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 两次扫描（前缀和思想）。
# 左到右扫描：维护左侧球的数量 count 和它们移到当前位置的总操作数 ops。
#   对于位置 i，左侧球的贡献 = ops。每移至下一个位置，每个左侧球需多走一步：ops += count。
# 右到左扫描：同理处理右侧球。
# answer[i] = 左侧球的贡献 + 右侧球的贡献。
#
# 时间复杂度: O(N) — 两次扫描
# 空间复杂度: O(1) — 除输出数组外
#
# 关键点:
# - 利用每步移动操作数的线性增长关系
# - ops += count 表示每右移一格，所有左侧球多一步
# - 两次扫描可以 O(N) 解决，无需 O(N^2) 暴力
