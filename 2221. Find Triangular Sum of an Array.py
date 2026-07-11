"""
LeetCode #2221 - Find Triangular Sum of an Array
数组的三角和
https://leetcode.cn/problems/find-triangular-sum-of-an-array/

给你一个下标从 0 开始的整数数组 `nums` ，其中 `nums[i]` 是 `0` 到 `9` 之间（两者都包含）的一个数字。
`nums` 的 三角和 是执行以下操作以后最后剩下元素的值：
`nums` 初始包含 `n` 个元素。如果 `n == 1` ，终止 操作。否则，创建 一个新的下标从 0 开始的长度为 `n - 1` 的整数数组 `newNums` 。
对于满足 `0 <= i < n - 1` 的下标 `i` ，`newNums[i]` 赋值 为 `(nums[i] + nums[i+1]) % 10` ，`%` 表示取余运算。
将 `newNums` 替换 数组 `nums` 。
从步骤 1 开始 重复 整个过程。
请你返回 `nums` 的三角和。

示例 1：

输入：nums = [1,2,3,4,5] 输出：8 解释： 上图展示了得到数组三角和的过程。
示例 2：
输入：nums = [5] 输出：5 解释： 由于 nums 中只有一个元素，数组的三角和为这个元素自己。

提示：
`1 <= nums.length <= 1000`
`0 <= nums[i] <= 9`
"""

from typing import List, Optional


class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        # 模拟过程：每次将相邻两数相加取模 10，数组长度减 1
        # 原地修改：从前向后覆盖，nums[i] 被更新为 (nums[i] + nums[i+1]) % 10
        # 此时 nums[i+1] 还是本轮未修改的值，保证正确性
        while n > 1:
            for i in range(n - 1):
                nums[i] = (nums[i] + nums[i + 1]) % 10
            n -= 1
        return nums[0]


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Math, Combinatorics, Number Theory, Simulation
#
# 解题思路:
# 直接模拟题目描述的三角和过程：每次遍历数组，将相邻两元素相加取模 10，
# 覆盖到前一个位置。因为从前向后遍历时，nums[i+1] 尚未被本轮修改，
# 所以每次使用的都是正确的旧值。每轮结束后有效长度减 1，
# 直到只剩一个元素即最终答案。n <= 1000，O(n^2) 完全可行。
# （进阶解法：利用组合数学，最终结果 = sum(nums[i] * C(n-1, i)) % 10，
#  可使用卢卡斯定理或模 2 和模 5 分别计算再中国剩余定理合并。）
#
# 时间复杂度: O(n^2) 其中 n 为数组长度
# 空间复杂度: O(1) 原地修改
#
# 关键点:
# - 从前向后原地覆盖不会影响后续计算（nums[i+1] 尚未被本轮更新）
# - 也可用组合数学 C(n-1, i) mod 10 优化到 O(n)，但模拟足够通过
