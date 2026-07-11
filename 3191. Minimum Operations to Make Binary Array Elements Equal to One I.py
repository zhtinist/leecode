"""
LeetCode #3191 - Minimum Operations to Make Binary Array Elements Equal to One I
使二进制数组全部等于 1 的最少操作次数 I
https://leetcode.cn/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i/

给你一个二进制数组 `nums` 。
你可以对数组执行以下操作 任意 次（也可以 0 次）：
选择数组中 任意连续 3 个元素，并将它们 全部反转 。
反转 一个元素指的是将它的值从 0 变 1 ，或者从 1 变 0 。
请你返回将 `nums` 中所有元素变为 1 的 最少 操作次数。如果无法全部变成 1 ，返回 -1 。

示例 1：

输入：nums = [0,1,1,1,0,0]
输出：3
解释：
我们可以执行以下操作：
选择下标为 0 ，1 和 2 的元素并反转，得到 `nums = [1,0,0,1,0,0]` 。
选择下标为 1 ，2 和 3 的元素并反转，得到 `nums = [1,1,1,0,0,0]` 。
选择下标为 3 ，4 和 5 的元素并反转，得到 `nums = [1,1,1,1,1,1]` 。
示例 2：

输入：nums = [0,1,1,1]
输出：-1
解释：
无法将所有元素都变为 1 。

提示：
`3 <= nums.length <= 10^5`
`0 <= nums[i] <= 1`
"""

from typing import List, Optional


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        from collections import deque
        n = len(nums)
        ops = 0
        q = deque()  # 记录翻转操作的起始位置

        for i in range(n):
            # 移除过期的翻转（影响范围i-2到i）
            while q and q[0] + 2 < i:
                q.popleft()

            val = nums[i] ^ (len(q) % 2)  # 当前值经过所有活跃翻转后的结果
            if val == 0:
                if i + 2 >= n:
                    return -1
                ops += 1
                q.append(i)

        return ops



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Bit Manipulation, Queue, Array, Prefix Sum, Sliding Window
#
# 解题思路:
# 贪心从左到右扫描。每次操作翻转连续3个元素。若当前元素为0（考虑历史翻转后），
# 必须在此处开始一次翻转（否则无法改变该位置）。用队列记录活跃翻转，
# 超出3个位置范围的翻转自动过期移除。若在倒数后两个位置还需要翻转则返回-1。
#
# 时间复杂度: O(n)
# 空间复杂度: O(n)
#
# 关键点:
# - 贪心：遇到0必须翻转，无其他选择
# - 用队列跟踪活跃翻转及过期时间
# - 活跃翻转数量%2决定当前元素是否被翻转
