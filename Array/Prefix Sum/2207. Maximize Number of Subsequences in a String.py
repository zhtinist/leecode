"""
LeetCode #2207 - Maximize Number of Subsequences in a String
字符串中最多数目的子序列
https://leetcode.cn/problems/maximize-number-of-subsequences-in-a-string/

给你一个下标从 0 开始的字符串 `text` 和另一个下标从 0 开始且长度为 `2` 的字符串 `pattern` ，两者都只包含小写英文字母。
你可以在 `text` 中任意位置插入 一个 字符，这个插入的字符必须是 `pattern[0]` 或者 `pattern[1]` 。注意，这个字符可以插入在 `text` 开头或者结尾的位置。
请你返回插入一个字符后，`text` 中最多包含多少个等于 `pattern` 的 子序列 。
子序列 指的是将一个字符串删除若干个字符后（也可以不删除），剩余字符保持原本顺序得到的字符串。

示例 1：
输入：text = "abdcdbc", pattern = "ac" 输出：4 解释： 如果我们在 text[1] 和 text[2] 之间添加 pattern[0] = 'a' ，那么我们得到 "abadcdbc" 。那么 "ac" 作为子序列出现 4 次。 其他得到 4 个 "ac" 子序列的方案还有 "aabdcdbc" 和 "abdacdbc" 。 但是，"abdcadbc" ，"abdccdbc" 和 "abdcdbcc" 这些字符串虽然是可行的插入方案，但是只出现了 3 次 "ac" 子序列，所以不是最优解。 可以证明插入一个字符后，无法得到超过 4 个 "ac" 子序列。
示例 2：
输入：text = "aabb", pattern = "ab" 输出：6 解释： 可以得到 6 个 "ab" 子序列的部分方案为 "aaabb" ，"aaabb" 和 "aabbb" 。

提示：
`1 <= text.length <= 10^5`
`pattern.length == 2`
`text` 和 `pattern` 都只包含小写英文字母。
"""

from typing import List, Optional


class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        p0, p1 = pattern[0], pattern[1]

        # Count existing subsequences matching pattern
        count_p0 = 0
        existing = 0
        for ch in text:
            if ch == p1:
                existing += count_p0
            if ch == p0:
                count_p0 += 1

        # Adding p0 at the beginning: it will form a new subsequence with
        # every existing p1 in text: existing + count_p1
        # Adding p1 at the end: it will form a new subsequence with
        # every existing p0 in text: existing + count_p0
        # Count p1 occurrences
        count_p1 = text.count(p1)

        return existing + max(count_p0, count_p1)


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, String, Prefix Sum
#
# 解题思路:
# 1. 首先计算原字符串 text 中 pattern 作为子序列出现的次数 existing。
#    遍历 text，维护已遇到的 pattern[0] 的数量 count_p0。
#    每遇到一个 pattern[1]，就将当前 count_p0 累加到 existing 中。
# 2. 在最优策略下，我们只有两种插入方式能最大化子序列数量：
#    a) 在 text 最前面插入 pattern[0]：每插入一个 pattern[0]，
#       会与 text 中每一个 pattern[1] 形成一个新的子序列，增加 count_p1 个。
#    b) 在 text 最后面插入 pattern[1]：每插入一个 pattern[1]，
#       会与 text 中每一个 pattern[0] 形成一个新的子序列，增加 count_p0 个。
# 3. 取 existing + max(count_p0, count_p1) 即为最终答案。
#    注意：当 pattern[0] == pattern[1] 时，同样适用上述逻辑，
#    因为此时 count_p0 和 count_p1 是同一个值，existing = count_p0 * (count_p0 - 1) // 2，
#    插入后变为 count_p0 * (count_p0 + 1) // 2，增加量为 count_p0，与公式一致。
#
# 时间复杂度: O(N)，其中 N 为 text 的长度。只需一次遍历。
# 空间复杂度: O(1)，只使用常数个额外变量。
#
# 关键点:
# - 插入位置应选在最优位置：pattern[0] 插最前面，pattern[1] 插最后面。
# - 子序列计数使用前缀计数法（一边扫描一边统计），避免 O(N^2) 的暴力枚举。
# - 注意处理 pattern 中两个字符相同的情况，但上述算法天然兼容。
