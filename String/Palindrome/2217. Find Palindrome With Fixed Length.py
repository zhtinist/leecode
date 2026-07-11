"""
LeetCode #2217 - Find Palindrome With Fixed Length
找到指定长度的回文数
https://leetcode.cn/problems/find-palindrome-with-fixed-length/

给你一个整数数组 `queries` 和一个 正 整数 `intLength` ，请你返回一个数组 `answer` ，其中 `answer[i]` 是长度为 `intLength` 的 正回文数 中第 `queries[i]` 小的数字，如果不存在这样的回文数，则为 `-1` 。
回文数 指的是从前往后和从后往前读一模一样的数字。回文数不能有前导 0 。

示例 1：
输入：queries = [1,2,3,4,5,90], intLength = 3 输出：[101,111,121,131,141,999] 解释： 长度为 3 的最小回文数依次是： 101, 111, 121, 131, 141, 151, 161, 171, 181, 191, 202, ... 第 90 个长度为 3 的回文数是 999 。
示例 2：
输入：queries = [2,4,6], intLength = 4 输出：[1111,1331,1551] 解释： 长度为 4 的前 6 个回文数是： 1001, 1111, 1221, 1331, 1441 和 1551 。

提示：
`1 <= queries.length <= 5 * 10^4`
`1 <= queries[i] <= 10^9`
`1 <= intLength <= 15`
"""

from typing import List, Optional


class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        # 计算半长度：长度为 intLength 的回文数由前半部分决定
        half = (intLength + 1) // 2
        # 前半部分的范围：从 10^(half-1) 到 10^half - 1
        base = 10 ** (half - 1)
        max_count = 9 * base  # 长度为 intLength 的回文数总数

        def get_palindrome(k: int) -> int:
            """返回第 k 小的回文数（1-indexed），不存在返回 -1"""
            if k > max_count:
                return -1
            # 前半部分数字 = base + k - 1
            first_half = str(base + k - 1)
            # 根据长度奇偶性拼接回文
            if intLength % 2 == 0:
                second_half = first_half[::-1]
            else:
                second_half = first_half[-2::-1]  # 去掉中间位再反转
            return int(first_half + second_half)

        return [get_palindrome(q) for q in queries]


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Math
#
# 解题思路:
# 长度为 L 的回文数由前半部分（长度为 half = ceil(L/2)）唯一决定。
# 前半部分的范围是从 10^(half-1) 到 10^half - 1，共 9 * 10^(half-1) 个。
# 第 k 小的回文数的前半部分 = base + k - 1（base = 10^(half-1)）。
# 然后根据 intLength 的奇偶性拼接：偶数长度直接反转前半部分拼接；
# 奇数长度则去掉中间字符后再反转前半部分剩余部分拼接。
# 如果 k 超过总数，返回 -1。
#
# 时间复杂度: O(N) 其中 N 为 queries 长度，每个查询 O(1) 构造
# 空间复杂度: O(1) 不计输出数组
#
# 关键点:
# - 回文数的前半部分决定整个数：长度为 L 的回文数数量 = 9 * 10^(ceil(L/2)-1)
# - 第 k 个回文数的前半部分 = base + k - 1（base 是最小前半部分）
# - 奇数长度时，中间位不参与反转（只取前半部分去掉最后一位再反转拼接）
