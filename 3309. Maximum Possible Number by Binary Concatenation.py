"""
LeetCode #3309 - Maximum Possible Number by Binary Concatenation
连接二进制表示可形成的最大数值
https://leetcode.cn/problems/maximum-possible-number-by-binary-concatenation/

给你一个长度为 `3` 的整数数组 `nums`。
现以某种顺序 连接 数组 `nums` 中所有元素的 二进制表示 ，请你返回可以由这种方法形成的 最大 数值。
注意 任何数字的二进制表示 不含 前导零。

示例 1:

输入: nums = [1,2,3]
输出: 30
解释:
按照顺序 `[3, 1, 2]` 连接数字的二进制表示，得到结果 `"11110"`，这是 30 的二进制表示。
示例 2:

输入: nums = [2,8,16]
输出: 1296
解释:
按照顺序 `[2, 8, 16]` 连接数字的二进制表述，得到结果 `"10100010000"`，这是 1296 的二进制表示。

提示:
`nums.length == 3`
`1 <= nums[i] <= 127`
"""

from typing import List, Optional


class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        import itertools
        ans = 0
        for perm in itertools.permutations(nums):
            # 连接三个数的二进制表示
            binary = ''.join(bin(x)[2:] for x in perm)
            ans = max(ans, int(binary, 2))
        return ans










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Bit Manipulation, Array, Enumeration
#
# 解题思路:
# nums 只有 3 个元素，暴搜所有 6 种排列即可。
# 对每种排列，将三个数的二进制表示（不含前导零）连接起来，
# 转换为十进制整数，取最大值。
#
# 时间复杂度: O(3!) = O(1)
# 空间复杂度: O(1)
#
# 关键点:
# - 固定长度 3，全排列枚举可行
# - bin(x)[2:] 获取不含 '0b' 前缀的二进制字符串
