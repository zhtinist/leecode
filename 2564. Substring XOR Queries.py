"""
LeetCode #2564 - Substring XOR Queries
子字符串异或查询
https://leetcode.cn/problems/substring-xor-queries/

给你一个 二进制字符串 `s` 和一个整数数组 `queries` ，其中 `queries[i] = [first_i, second_i]` 。
对于第 `i` 个查询，找到 `s` 的 最短子字符串 ，它对应的 十进制值 `val` 与 `first_i` 按位异或 得到 `second_i` ，换言之，`val ^ first_i == second_i` 。
第 `i` 个查询的答案是子字符串 `[left_i, right_i]` 的两个端点（下标从 0 开始），如果不存在这样的子字符串，则答案为 `[-1, -1]` 。如果有多个答案，请你选择 `left_i` 最小的一个。
请你返回一个数组 `ans` ，其中 `ans[i] = [left_i, right_i]` 是第 `i` 个查询的答案。
子字符串 是一个字符串中一段连续非空的字符序列。

示例 1：
输入：s = "101101", queries = [[0,5],[1,2]] 输出：[[0,2],[2,3]] 解释：第一个查询，端点为 `[0,2]` 的子字符串为 "101" ，对应十进制数字 `5 ，且` `5 ^ 0 = 5` ，所以第一个查询的答案为 `[0,2]。第二个查询中，`端点为 `[2,3] 的子字符串为 `"11" ，对应十进制数字 3 ，且 3` ^ 1 = 2`` 。所以第二个查询的答案为` `[2,3]` 。
示例 2：
输入：s = "0101", queries = [[12,8]] 输出：[[-1,-1]] 解释：这个例子中，没有符合查询的答案，所以返回 `[-1,-1] 。`
示例 3：
输入：s = "1", queries = [[4,5]] 输出：[[0,0]] 解释：这个例子中，端点为 `[0,0]` 的子字符串对应的十进制值为 `1`` ，且` `1 ^ 4 = 5`` 。所以答案为` `[0,0] 。`

提示：
`1 <= s.length <= 10^4`
`s[i]` 要么是 `'0'` ，要么是 `'1'` 。
`1 <= queries.length <= 10^5`
`0 <= first_i, second_i <= 10^9`
"""

from typing import List, Optional


class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        # val ^ first = second  =>  val = first ^ second
        # Precompute all substrings and their values, store first occurrence
        seen = {}
        n = len(s)
        for i in range(n):
            if s[i] == '0':
                if 0 not in seen:
                    seen[0] = [i, i]
                continue
            val = 0
            for j in range(i, min(n, i + 31)):
                val = (val << 1) | (ord(s[j]) - 48)
                if val not in seen:
                    seen[val] = [i, j]

        ans = []
        for first, second in queries:
            target = first ^ second
            if target in seen:
                ans.append(seen[target])
            else:
                ans.append([-1, -1])
        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Bit Manipulation, Array, Hash Table, String
#
# 解题思路:
# val ^ first = second 等价于 val = first ^ second。由于first/second <= 10^9 < 2^30，
# 目标值最多30位，只需考虑最长为31的子字符串。预处理所有长度<=31的子串及其十进制值，
# 用哈希表记录每个值的最早出现位置[left, right]。查询时直接查表O(1)。
#
# 时间复杂度: O(N * 30 + Q)，N为字符串长度，Q为查询数
# 空间复杂度: O(N * 30)
#
# 关键点:
# - 目标值到子串值的一一对应：val = first ^ second
# - 子串长度最多31就足够（2^30 ≈ 10^9）
# - 处理前导零：单独记录值为0的子串（因为'0'开头的子串不继续扩展）
# - 哈希表存最早出现，满足left最小的要求
