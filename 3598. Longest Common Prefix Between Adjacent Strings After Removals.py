"""
LeetCode #3598 - Longest Common Prefix Between Adjacent Strings After Removals
相邻字符串之间的最长公共前缀
https://leetcode.cn/problems/longest-common-prefix-between-adjacent-strings-after-removals/

给你一个字符串数组 `words`，对于范围 `[0, words.length - 1]` 内的每个下标 `i`，执行以下步骤：
从 `words` 数组中移除下标 `i` 处的元素。
计算修改后的数组中所有 相邻对 之间的 最长公共前缀 的长度。
返回一个数组 `answer`，其中 `answer[i]` 是移除下标 `i` 后，相邻对之间最长公共前缀的长度。如果 不存在 相邻对，或者 不存在 公共前缀，则 `answer[i]` 应为 0。
字符串的前缀是从字符串的开头开始延伸到任意位置的子字符串。

示例 1：

输入： words = ["jump","run","run","jump","run"]
输出： [3,0,0,3,3]
解释：
移除下标 0：
`words` 变为 `["run", "run", "jump", "run"]`
最长的相邻对是 `["run", "run"]`，其公共前缀为 `"run"`（长度为 3）
移除下标 1：
`words` 变为 `["jump", "run", "jump", "run"]`
没有相邻对有公共前缀（长度为 0）
移除下标 2：
`words` 变为 `["jump", "run", "jump", "run"]`
没有相邻对有公共前缀（长度为 0）
移除下标 3：
`words` 变为 `["jump", "run", "run", "run"]`
最长的相邻对是 `["run", "run"]`，其公共前缀为 `"run"`（长度为 3）
移除下标 4：
`words` 变为 `["jump", "run", "run", "jump"]`
最长的相邻对是 `["run", "run"]`，其公共前缀为 `"run"`（长度为 3）
示例 2：

输入： words = ["dog","racer","car"]
输出： [0,0,0]
解释：
移除任意下标都会导致答案为 0。

提示：
`1 <= words.length <= 10^5`
`1 <= words[i].length <= 10^4`
`words[i]` 仅由小写英文字母组成。
`words[i]` 的长度总和不超过 `10^5`。
"""

from typing import List, Optional


class Solution:
    def longestCommonPrefixAfterRemovals(self, words: List[str]) -> List[int]:
        n = len(words)

        def lcp(s1: str, s2: str) -> int:
            """Return length of longest common prefix between s1 and s2."""
            i = 0
            while i < len(s1) and i < len(s2) and s1[i] == s2[i]:
                i += 1
            return i

        # Compute LCP for each original adjacent pair
        orig_lcp = [0] * (n - 1)
        for i in range(n - 1):
            orig_lcp[i] = lcp(words[i], words[i + 1])

        # Compute prefix max and suffix max of orig_lcp
        pref_max = [0] * (n - 1)
        if n > 1:
            pref_max[0] = orig_lcp[0]
            for i in range(1, n - 1):
                pref_max[i] = max(pref_max[i - 1], orig_lcp[i])

        suff_max = [0] * (n - 1)
        if n > 1:
            suff_max[-1] = orig_lcp[-1]
            for i in range(n - 3, -1, -1):
                suff_max[i] = max(suff_max[i + 1], orig_lcp[i])

        # Compute answer for each index
        answer = [0] * n
        for i in range(n):
            best = 0

            # LCP of the new adjacent pair formed by removal (words[i-1], words[i+1])
            if 0 < i < n - 1:
                best = max(best, lcp(words[i - 1], words[i + 1]))

            # Max LCP among unaffected original adjacent pairs
            if i >= 2 and n > 1:
                # Pairs 0..i-2 are unaffected
                best = max(best, pref_max[i - 2])
            if i <= n - 3 and n > 1:
                # Pairs i+1..n-2 are unaffected
                best = max(best, suff_max[i + 1])

            answer[i] = best

        return answer











# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, String
#
# 解题思路:
# 对于每个下标 i，移除 words[i] 后的相邻对有两类：
# 1. 原有的不涉及 i 的相邻对（原数组中不相邻于 i 的对）
# 2. 新形成的相邻对 (words[i-1], words[i+1])（如果 i 不在边界）
#
# 高效计算：
# 1. 预处理原始数组所有相邻对 (j, j+1) 的 LCP 长度，存入 orig_lcp 数组。
# 2. 计算 orig_lcp 的前缀最大值数组 pref_max 和后缀最大值数组 suff_max。
#    - pref_max[j] = max(orig_lcp[0..j])
#    - suff_max[j] = max(orig_lcp[j..n-2])
# 3. 对每个 i：
#    a. 新形成的对：直接计算 lcp(words[i-1], words[i+1])
#    b. 原有不受影响的对：
#       - 左侧：pref_max[i-2]（跳过 pairs i-2 和 i-1，i-1 受影响）
#       - 右侧：suff_max[i+1]（跳过 pairs i 和 i+1）
#    c. answer[i] = max(新对LCP, 左侧最大值, 右侧最大值)
#
# 时间复杂度: O(S)，S 是所有字符串的总长度。每个 LCP 计算的总字符比较次数不超过 S
# 空间复杂度: O(N)，存储 orig_lcp、pref_max、suff_max 和 answer 数组
#
# 关键点:
# - 移除一个元素只影响其相邻的两对（如果有），其余对保持不变
# - 前缀/后缀最大值数组将"排除某些位置求最大"的查询优化为 O(1)
# - LCP 函数提前终止于第一个不匹配字符，总比较次数有界
