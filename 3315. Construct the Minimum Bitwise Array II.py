"""
LeetCode #3315 - Construct the Minimum Bitwise Array II
构造最小位运算数组 II
https://leetcode.cn/problems/construct-the-minimum-bitwise-array-ii/

给你一个长度为 `n` 的 质数 数组 `nums` 。你的任务是返回一个长度为 `n` 的数组 `ans` ，对于每个下标 `i` ，以下 条件 均成立：
`ans[i] OR (ans[i] + 1) == nums[i]`
除此以外，你需要 最小化 结果数组里每一个 `ans[i]` 。
如果没法找到符合 条件 的 `ans[i]` ，那么 `ans[i] = -1` 。
质数 指的是一个大于 1 的自然数，且它只有 1 和自己两个因数。

示例 1：

输入：nums = [2,3,5,7]
输出：[-1,1,4,3]
解释：
对于 `i = 0` ，不存在 `ans[0]` 满足 `ans[0] OR (ans[0] + 1) = 2` ，所以 `ans[0] = -1` 。
对于 `i = 1` ，满足 `ans[1] OR (ans[1] + 1) = 3` 的最小 `ans[1]` 为 `1` ，因为 `1 OR (1 + 1) = 3` 。
对于 `i = 2` ，满足 `ans[2] OR (ans[2] + 1) = 5` 的最小 `ans[2]` 为 `4` ，因为 `4 OR (4 + 1) = 5` 。
对于 `i = 3` ，满足 `ans[3] OR (ans[3] + 1) = 7` 的最小 `ans[3]` 为 `3` ，因为 `3 OR (3 + 1) = 7` 。
示例 2：

输入：nums = [11,13,31]
输出：[9,12,15]
解释：
对于 `i = 0` ，满足 `ans[0] OR (ans[0] + 1) = 11` 的最小 `ans[0]` 为 `9` ，因为 `9 OR (9 + 1) = 11` 。
对于 `i = 1` ，满足 `ans[1] OR (ans[1] + 1) = 13` 的最小 `ans[1]` 为 `12` ，因为 `12 OR (12 + 1) = 13` 。
对于 `i = 2` ，满足 `ans[2] OR (ans[2] + 1) = 31` 的最小 `ans[2]` 为 `15` ，因为 `15 OR (15 + 1) = 31` 。

提示：
`1 <= nums.length <= 100`
`2 <= nums[i] <= 10^9`
`nums[i]` 是一个质数。
"""

from typing import List, Optional


class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for x in nums:
            if x == 2:
                ans.append(-1)
            else:
                # 计算 x 末尾连续 1 的个数
                t = 0
                temp = x
                while temp & 1:
                    t += 1
                    temp >>= 1
                if t == 0:
                    ans.append(-1)
                else:
                    ans.append(x ^ (1 << (t - 1)))
        return ans










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Bit Manipulation, Array
#
# 解题思路:
# ans | (ans + 1) = x。设 ans 最低位的 0 在位置 k（从 0 开始），
# 则 ans+1 会将位 0..k-1 清零、位 k 置 1，OR 结果位 0..k 全为 1。
# 因此 x 的二进制必然以连续的 1 结尾。设末尾有 t 个连续 1：
# - t == 0 → x 为偶数 → 无解（但题目中 nums[i] 是质数，只有 2 为偶数）
# - t > 0 → ans = x ^ (1 << (t-1))（将末尾连续 1 中最高位翻成 0）
# 这是唯一解且最小化 ans[i]。
#
# 时间复杂度: O(n * log x)
# 空间复杂度: O(1)
#
# 关键点:
# - ans | (ans + 1) 的位运算规律：结果末尾一定是连续的 1
# - 通过 trailing ones 计算 ans = x ^ (1 << (t-1))
# - x = 2 是唯一无解的质数情况
