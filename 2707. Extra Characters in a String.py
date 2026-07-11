"""
LeetCode #2707 - Extra Characters in a String
字符串中的额外字符
https://leetcode.cn/problems/extra-characters-in-a-string/

给你一个下标从 0 开始的字符串 `s` 和一个单词字典 `dictionary` 。你需要将 `s` 分割成若干个 互不重叠 的子字符串，每个子字符串都在 `dictionary` 中出现过。`s` 中可能会有一些 额外的字符 不在任何子字符串中。
请你采取最优策略分割 `s` ，使剩下的字符 最少 。

示例 1：
输入：s = "leetscode", dictionary = ["leet","code","leetcode"] 输出：1 解释：将 s 分成两个子字符串：下标从 0 到 3 的 "leet" 和下标从 5 到 8 的 "code" 。只有 1 个字符没有使用（下标为 4），所以我们返回 1 。
示例 2：
输入：s = "sayhelloworld", dictionary = ["hello","world"] 输出：3 解释：将 s 分成两个子字符串：下标从 3 到 7 的 "hello" 和下标从 8 到 12 的 "world" 。下标为 0 ，1 和 2 的字符没有使用，所以我们返回 3 。

提示：
`1 <= s.length <= 50`
`1 <= dictionary.length <= 50`
`1 <= dictionary[i].length <= 50`
`dictionary[i]` 和 `s` 只包含小写英文字母。
`dictionary` 中的单词互不相同。
"""

from typing import List, Optional


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        word_set = set(dictionary)
        n = len(s)
        # dp[i] = min extra chars for prefix s[0:i]
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            # default: treat s[i-1] as extra character
            dp[i] = dp[i - 1] + 1
            # try all substrings ending at i-1
            for j in range(i):
                if s[j:i] in word_set:
                    dp[i] = min(dp[i], dp[j])
        return dp[n]



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Trie, Array, Hash Table, String, Dynamic Programming
#
# 解题思路:
# 动态规划。dp[i]表示s前i个字符的最小额外字符数。对每个位置i，
# 默认将s[i-1]作为额外字符(dp[i]=dp[i-1]+1)，然后尝试所有以i-1结尾的子串s[j:i]，
# 如果该子串在字典中，则dp[i]=min(dp[i], dp[j])。
#
# 时间复杂度: O(n^2) 其中n = len(s)
# 空间复杂度: O(n + m) 其中m是字典单词总长度
#
# 关键点:
# - dp状态定义：前i个字符的最小额外字符
# - 遍历所有可能的子串检查是否在字典中
# - 将字典转为set实现O(1)查找
