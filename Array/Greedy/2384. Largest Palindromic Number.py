"""
LeetCode #2384 - Largest Palindromic Number
最大回文数字
https://leetcode.cn/problems/largest-palindromic-number/

给你一个仅由数字（`0 - 9`）组成的字符串 `num` 。
请你找出能够使用 `num` 中数字形成的 最大回文 整数，并以字符串形式返回。该整数不含 前导零 。
注意：
你 无需 使用 `num` 中的所有数字，但你必须使用 至少 一个数字。
数字可以重新排序。

示例 1：
输入：num = "444947137" 输出："7449447" 解释： 从 "444947137" 中选用数字 "4449477"，可以形成回文整数 "7449447" 。 可以证明 "7449447" 是能够形成的最大回文整数。
示例 2：
输入：num = "00009" 输出："9" 解释： 可以证明 "9" 能够形成的最大回文整数。 注意返回的整数不应含前导零。

提示：
`1 <= num.length <= 10^5`
`num` 由数字（`0 - 9`）组成
"""

from typing import List, Optional


class Solution:
    def largestPalindromic(self, num: str) -> str:
        """
        Count digits (0-9), build the largest palindrome by constructing
        the left half from digits 9 down to 0, picking the largest digit
        with an odd count as the middle.
        """
        from collections import Counter

        count = Counter(num)
        # count is a dict-like, but we need counts for all digits 0-9
        freq = [0] * 10
        for ch in num:
            freq[int(ch)] += 1

        # Build left half: iterate digits from 9 down to 0
        left = []
        for d in range(9, -1, -1):
            if freq[d] >= 2:
                pairs = freq[d] // 2
                left.append(str(d) * pairs)

        left_str = ''.join(left)
        # Remove leading zeros (only valid when there's no non-zero middle)
        left_str = left_str.lstrip('0')

        # Middle digit: largest digit with an odd count
        middle = ''
        for d in range(9, -1, -1):
            if freq[d] % 2 == 1:
                middle = str(d)
                break

        result = left_str + middle + left_str[::-1]

        # Edge case: if result is empty (all zeros and no middle), return "0"
        if not result:
            return "0"
        return result



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Hash Table, String, Counting
#
# 解题思路:
# 1. 统计每个数字(0-9)在字符串中出现的次数。
# 2. 构造回文数的左半部分：从9到0遍历，对于每个数字，取 count//2 个加入左半部分。
# 3. 去掉左半部分的前导零（因为最大回文数不能有前导零）。
# 4. 选择中间数字：从9到0找到第一个出现次数为奇数的数字，作为回文中心。
# 5. 拼接：左半 + 中间数字 + 左半的逆序。若结果为空，返回 "0"。
#
# 时间复杂度: O(n) — 遍历字符串统计频率，然后固定10个数字的处理
# 空间复杂度: O(n) — 存储结果字符串和左半部分
#
# 关键点:
# - 从大到小遍历数字(9到0)确保构造的回文数最大
# - 去除左半部分的前导零，但要注意全零的情况（返回 "0"）
# - 中间数字选择奇数次出现的最大数字
