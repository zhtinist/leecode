"""
LeetCode #3201 - Find the Maximum Length of Valid Subsequence I
找出有效子序列的最大长度 I
https://leetcode.cn/problems/find-the-maximum-length-of-valid-subsequence-i/

给你一个整数数组 `nums`。
`nums` 的子序列 `sub` 的长度为 `x` ，如果其满足以下条件，则称其为 有效子序列：
`(sub[0] + sub[1]) % 2 == (sub[1] + sub[2]) % 2 == ... == (sub[x - 2] + sub[x - 1]) % 2`
返回 `nums` 的 最长的有效子序列 的长度。
一个 子序列 指的是从原数组中删除一些元素（也可以不删除任何元素），剩余元素保持原来顺序组成的新数组。

示例 1：

输入： nums = [1,2,3,4]
输出： 4
解释：
最长的有效子序列是 `[1, 2, 3, 4]`。
示例 2：

输入： nums = [1,2,1,1,2,1,2]
输出： 6
解释：
最长的有效子序列是 `[1, 2, 1, 2, 1, 2]`。
示例 3：

输入： nums = [1,3]
输出： 2
解释：
最长的有效子序列是 `[1, 3]`。

提示：
`2 <= nums.length <= 2 * 10^5`
`1 <= nums[i] <= 10^7`
"""

from typing import List, Optional


class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        # 统计奇数和偶数的数量
        odd = sum(1 for x in nums if x % 2 == 1)
        even = len(nums) - odd
        # 情况1: 全奇数 或 全偶数 (相邻和为偶数)
        ans = max(odd, even)
        # 情况2: 交替奇偶 (相邻和为奇数) - 贪心取最长的交替子序列
        # 先奇后偶
        need_odd = True
        cnt1 = 0
        for x in nums:
            if need_odd and x % 2 == 1:
                cnt1 += 1
                need_odd = False
            elif not need_odd and x % 2 == 0:
                cnt1 += 1
                need_odd = True
        # 先偶后奇
        need_even = True
        cnt2 = 0
        for x in nums:
            if need_even and x % 2 == 0:
                cnt2 += 1
                need_even = False
            elif not need_even and x % 2 == 1:
                cnt2 += 1
                need_even = True
        ans = max(ans, cnt1, cnt2)
        return ans










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Dynamic Programming
#
# 解题思路:
# 条件要求所有相邻元素之和的奇偶性相同。设目标和奇偶性为 target % 2：
# - 若 target % 2 == 0（和为偶数），则相邻元素必须同奇偶（奇+奇=偶, 偶+偶=偶）
#   → 整个子序列要么全奇要么全偶
# - 若 target % 2 == 1（和为奇数），则相邻元素必须不同奇偶（奇+偶=奇）
#   → 子序列必须奇偶交替
# 因此答案 = max(奇数个数, 偶数个数, 贪心取最长奇偶交替子序列)
#
# 时间复杂度: O(n)
# 空间复杂度: O(1)
#
# 关键点:
# - 分析奇偶性条件，将问题简化为三类情况取最大值
# - 交替子序列用贪心：依次寻找需要的奇偶性元素
