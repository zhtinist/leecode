"""
LeetCode #2442 - Count Number of Distinct Integers After Reverse Operations
反转之后不同整数的数目
https://leetcode.cn/problems/count-number-of-distinct-integers-after-reverse-operations/

给你一个由 正 整数组成的数组 `nums` 。
你必须取出数组中的每个整数，反转其中每个数位，并将反转后得到的数字添加到数组的末尾。这一操作只针对 `nums` 中原有的整数执行。
返回结果数组中 不同 整数的数目。

示例 1：
输入：nums = [1,13,10,12,31] 输出：6 解释：反转每个数字后，结果数组是 [1,13,10,12,31,1,31,1,21,13] 。 反转后得到的数字添加到数组的末尾并按斜体加粗表示。注意对于整数 10 ，反转之后会变成 01 ，即 1 。 数组中不同整数的数目为 6（数字 1、10、12、13、21 和 31）。
示例 2：
输入：nums = [2,2,2] 输出：1 解释：反转每个数字后，结果数组是 [2,2,2,2,2,2] 。 数组中不同整数的数目为 1（数字 2）。

提示：
`1 <= nums.length <= 10^5`
`1 <= nums[i] <= 10^6`
"""

from typing import List, Optional


class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            seen.add(num)
            # 反转数字：转字符串反转后转回整数（自动去掉前导零）
            reversed_num = int(str(num)[::-1])
            seen.add(reversed_num)
        return len(seen)


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Hash Table, Math, Counting
#
# 解题思路:
# 使用集合（set）去重。遍历 nums 中的每个数字 num：
# 1. 将 num 加入集合
# 2. 将 num 反转后的数字加入集合（将 num 转为字符串后反转再转回整数，自动去掉前导零）
# 最后返回集合的大小，即为不同整数的个数。
#
# 时间复杂度: O(n * log_m)，n 为数组长度，m 为数字最大值（每次反转字符串操作与数字位数成正比）
# 空间复杂度: O(n)
#
# 关键点:
# - int(str(num)[::-1]) 实现数字反转并自动去除前导零
# - 使用 set 去重统计不同整数的数量
