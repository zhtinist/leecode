"""
LeetCode #3527 - Find the Most Common Response
找到最常见的回答
https://leetcode.cn/problems/find-the-most-common-response/

给你一个二维字符串数组 `responses`，其中每个 `responses[i]` 是一个字符串数组，表示第 `i` 天调查的回答结果。
请返回在对每个 `responses[i]` 中的回答 去重 后，所有天数中 最常见 的回答。如果有多个回答出现频率相同，则返回 字典序最小 的那个回答。

示例 1：

输入： responses = [["good","ok","good","ok"],["ok","bad","good","ok","ok"],["good"],["bad"]]
输出： "good"
解释：
每个列表去重后，得到 `responses = [["good", "ok"], ["ok", "bad", "good"], ["good"], ["bad"]]`。
`"good"` 出现了 3 次，`"ok"` 出现了 2 次，`"bad"` 也出现了 2 次。
返回 `"good"`，因为它出现的频率最高。
示例 2：

输入： responses = [["good","ok","good"],["ok","bad"],["bad","notsure"],["great","good"]]
输出： "bad"
解释：
每个列表去重后，`responses = [["good", "ok"], ["ok", "bad"], ["bad", "notsure"], ["great", "good"]]`。
`"bad"`、`"good"` 和 `"ok"` 都出现了 2 次。
返回 `"bad"`，因为它在这些最高频率的词中字典序最小。

提示：
`1 <= responses.length <= 1000`
`1 <= responses[i].length <= 1000`
`1 <= responses[i][j].length <= 10`
`responses[i][j]` 仅由小写英文字母组成
"""

from typing import List, Optional


class Solution:
    def mostCommonResponse(self, responses: List[List[str]]) -> str:
        from collections import Counter
        freq = Counter()
        for day in responses:
            for word in set(day):
                freq[word] += 1
        max_cnt = max(freq.values())
        candidates = [w for w, c in freq.items() if c == max_cnt]
        return min(candidates)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Hash Table, String, Counting
#
# 解题思路:
# 1. 对每天的回答列表进行去重（使用 set）
# 2. 统计所有天中去重后每个回答出现的总天数
# 3. 找到最大出现次数
# 4. 在出现次数最多的回答中，返回字典序最小的
#
# 时间复杂度: O(N * M) 其中 N 是天数，M 是每天的回答数
# 空间复杂度: O(U) 其中 U 是不同回答的总数
#
# 关键点:
# - 每天内部先 set 去重
# - 多个最高频回答时取字典序最小
