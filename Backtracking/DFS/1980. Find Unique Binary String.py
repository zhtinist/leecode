"""
LeetCode #1980 - Find Unique Binary String
找出不同的二进制字符串
https://leetcode.cn/problems/find-unique-binary-string/

给你一个字符串数组 `nums` ，该数组由 `n` 个 互不相同 的二进制字符串组成，且每个字符串长度都是 `n` 。请你找出并返回一个长度为 `n` 且 没有出现 在 `nums` 中的二进制字符串。如果存在多种答案，只需返回 任意一个 即可。

示例 1：
输入：nums = ["01","10"] 输出："11" 解释："11" 没有出现在 nums 中。"00" 也是正确答案。
示例 2：
输入：nums = ["00","01"] 输出："11" 解释："11" 没有出现在 nums 中。"10" 也是正确答案。
示例 3：
输入：nums = ["111","011","001"] 输出："101" 解释："101" 没有出现在 nums 中。"000"、"010"、"100"、"110" 也是正确答案。

提示：
`n == nums.length`
`1 <= n <= 16`
`nums[i].length == n`
`nums[i] `为 `'0'` 或 `'1'`
`nums` 中的所有字符串 互不相同
"""

from typing import List, Optional


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        """
        Cantor's diagonal argument: for each string at index i,
        flip the i-th character. The result differs from every string
        at position i, so it's guaranteed to be unique.
        """
        n = len(nums)
        result = []
        for i in range(n):
            # Flip the i-th character of nums[i]
            result.append("0" if nums[i][i] == "1" else "1")
        return "".join(result)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Hash Table, String, Backtracking
#
# 解题思路:
# 使用康托对角线法 (Cantor's diagonal argument)。
# 对于 n 个长度为 n 的二进制字符串，构造一个新的字符串：
# 取第 i 个字符串的第 i 个字符，将其翻转（0变1，1变0）作为结果的第 i 位。
# 这样构造出的字符串与第 i 个字符串至少在第 i 位不同，因此不在 nums 中。
# 这是确定性 O(N) 构造，不需要暴力枚举或哈希。
#
# 时间复杂度: O(N)，单次遍历
# 空间复杂度: O(N)，结果字符串
#
# 关键点:
# - 对角线法的巧妙构造
# - 每个位置只需翻转对应字符串的对应位
# - 保证与所有原字符串至少有一个位置不同
