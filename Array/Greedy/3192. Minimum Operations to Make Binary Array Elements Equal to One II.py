"""
LeetCode #3192 - Minimum Operations to Make Binary Array Elements Equal to One II
使二进制数组全部等于 1 的最少操作次数 II
https://leetcode.cn/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-ii/

给你一个二进制数组 `nums` 。
你可以对数组执行以下操作 任意 次（也可以 0 次）：
选择数组中 任意 一个下标 `i` ，并将从下标 `i` 开始一直到数组末尾 所有 元素 反转 。
反转 一个元素指的是将它的值从 0 变 1 ，或者从 1 变 0 。
请你返回将 `nums` 中所有元素变为 1 的 最少 操作次数。

示例 1：

输入：nums = [0,1,1,0,1]
输出：4
解释：
我们可以执行以下操作：
选择下标 `i = 1` 执行操作，得到 `nums = [0,0,0,1,0]` 。
选择下标 `i = 0` 执行操作，得到 `nums = [1,1,1,0,1]` 。
选择下标 `i = 4` 执行操作，得到 `nums = [1,1,1,0,0]` 。
选择下标 `i = 3` 执行操作，得到 `nums = [1,1,1,1,1]` 。
示例 2：

输入：nums = [1,0,0,0]
输出：1
解释：
我们可以执行以下操作：
选择下标 `i = 1` 执行操作，得到 `nums = [1,1,1,1]` 。

提示：
`1 <= nums.length <= 10^5`
`0 <= nums[i] <= 1`
"""

from typing import List, Optional


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ops = 0
        for x in nums:
            val = x ^ (ops % 2)  # 经过ops次翻转后的实际值
            if val == 0:
                ops += 1
        return ops



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Array, Dynamic Programming
#
# 解题思路:
# 贪心从左到右。操作从i翻转到末尾，等价于翻转当前位置及之后的所有元素。
# 维护当前已执行的翻转次数ops，每个位置的当前真实值 = nums[i] ^ (ops % 2)。
# 若当前值为0，必须在此处执行一次翻转（延迟处理不会更优），ops++。
# 最终ops即为答案。
#
# 时间复杂度: O(n)
# 空间复杂度: O(1)
#
# 关键点:
# - 翻转后缀操作，从左到右贪心
# - 奇数次翻转取反，偶数次不变
# - 遇到0必须翻转，延迟无益
