"""
LeetCode #2149 - Rearrange Array Elements by Sign
按符号重排数组
https://leetcode.cn/problems/rearrange-array-elements-by-sign/

给你一个下标从 0 开始的整数数组 `nums` ，数组长度为 偶数 ，由数目 相等 的正整数和负整数组成。
你需要返回满足下述条件的数组 `nums`：
任意 连续 的两个整数 符号相反
对于符号相同的所有整数，保留 它们在 `nums` 中的 顺序 。
重排后数组以正整数开头。
重排元素满足上述条件后，返回修改后的数组。

示例 1：
输入：nums = [3,1,-2,-5,2,-4] 输出：[3,-2,1,-5,2,-4] 解释： nums 中的正整数是 [3,1,2] ，负整数是 [-2,-5,-4] 。 重排的唯一可行方案是 [3,-2,1,-5,2,-4]，能满足所有条件。 像 [1,-2,2,-5,3,-4]、[3,1,2,-2,-5,-4]、[-2,3,-5,1,-4,2] 这样的其他方案是不正确的，因为不满足一个或者多个条件。
示例 2：
输入：nums = [-1,1] 输出：[1,-1] 解释： 1 是 nums 中唯一一个正整数，-1 是 nums 中唯一一个负整数。 所以 nums 重排为 [1,-1] 。

提示：
`2 <= nums.length <= 2 * 10^5`
`nums.length` 是 偶数
`1 <= |nums[i]| <= 10^5`
`nums` 由 相等 数量的正整数和负整数组成

不需要原地进行修改。
"""

from typing import List, Optional


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        pos_idx, neg_idx = 0, 1
        for x in nums:
            if x > 0:
                result[pos_idx] = x
                pos_idx += 2
            else:
                result[neg_idx] = x
                neg_idx += 2
        return result



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Two Pointers, Simulation
#
# 解题思路:
# 使用两个指针分别指向结果数组中正数和负数的目标位置。结果数组要求正数在偶数位置（0, 2, 4, ...），
# 负数在奇数位置（1, 3, 5, ...），且各自保持原数组中的相对顺序。遍历原数组，
# 遇到正数放入 pos_idx 位置，遇到负数放入 neg_idx 位置，每次放置后对应指针 +2。
# 这种方法一次遍历即可完成，不需要分别收集正负数再交叉合并。
#
# 时间复杂度: O(N)，一次遍历即可完成重排。
# 空间复杂度: O(N)，需要一个新的结果数组（题目允许不原地修改）。
#
# 关键点:
# - 双指针交替放置：pos_idx 从 0 开始，neg_idx 从 1 开始，各步长 2
# - 保证正负数相对顺序不变：按原数组顺序依次放置
