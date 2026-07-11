"""
LeetCode #2055 - Plates Between Candles
蜡烛之间的盘子
https://leetcode.cn/problems/plates-between-candles/

给你一个长桌子，桌子上盘子和蜡烛排成一列。给你一个下标从 0 开始的字符串 `s` ，它只包含字符 `'*'` 和 `'|'` ，其中 `'*'` 表示一个 盘子 ，`'|'` 表示一支 蜡烛 。
同时给你一个下标从 0 开始的二维整数数组 `queries` ，其中 `queries[i] = [left_i, right_i]` 表示 子字符串 `s[left_i...right_i]` （包含左右端点的字符）。对于每个查询，你需要找到 子字符串中 在 两支蜡烛之间 的盘子的 数目 。如果一个盘子在 子字符串中 左边和右边 都 至少有一支蜡烛，那么这个盘子满足在 两支蜡烛之间 。
比方说，`s = "||**||**|*"` ，查询 `[3, 8]` ，表示的是子字符串 `"*||**|"` 。子字符串中在两支蜡烛之间的盘子数目为 `2` ，子字符串中右边两个盘子在它们左边和右边 都 至少有一支蜡烛。
请你返回一个整数数组 `answer` ，其中 `answer[i]` 是第 `i` 个查询的答案。

示例 1:

输入：s = "**|**|***|", queries = [[2,5],[5,9]] 输出：[2,3] 解释： - queries[0] 有两个盘子在蜡烛之间。 - queries[1] 有三个盘子在蜡烛之间。
示例 2:

输入：s = "***|**|*****|**||**|*", queries = [[1,17],[4,5],[14,17],[5,11],[15,16]] 输出：[9,0,0,0,0] 解释： - queries[0] 有 9 个盘子在蜡烛之间。 - 另一个查询没有盘子在蜡烛之间。

提示：
`3 <= s.length <= 10^5`
`s` 只包含字符 `'*'` 和 `'|'` 。
`1 <= queries.length <= 10^5`
`queries[i].length == 2`
`0 <= left_i <= right_i < s.length`
"""

from typing import List, Optional


class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        # Prefix sum of plates
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + (1 if s[i] == '*' else 0)

        # Nearest candle to the left (including self)
        left_candle = [-1] * n
        prev = -1
        for i in range(n):
            if s[i] == '|':
                prev = i
            left_candle[i] = prev

        # Nearest candle to the right (including self)
        right_candle = [-1] * n
        nxt = -1
        for i in range(n - 1, -1, -1):
            if s[i] == '|':
                nxt = i
            right_candle[i] = nxt

        result = []
        for left, right in queries:
            # Find the first candle on or after left
            l = right_candle[left]
            # Find the last candle on or before right
            r = left_candle[right]
            if l == -1 or r == -1 or l >= r:
                result.append(0)
            else:
                result.append(prefix[r + 1] - prefix[l])

        return result



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, String, Binary Search, Prefix Sum
#
# 解题思路:
# 预处理三个数组：1) 盘子数量前缀和；2) 每个位置左侧最近的蜡烛；
# 3) 每个位置右侧最近的蜡烛。对于每个查询[left, right]：
# 找到查询区间内最左的蜡烛l（通过right_candle[left]）和最右的蜡烛r（通过left_candle[right]）。
# 盘子数 = prefix[r+1] - prefix[l]（l和r之间的盘子），前提是l < r。
#
# 时间复杂度: O(n + q)
# 空间复杂度: O(n)
#
# 关键点:
# - 盘子只能在左右蜡烛之间计数
# - 预处理左右最近蜡烛位置
# - 前缀和快速计算区间盘子数
