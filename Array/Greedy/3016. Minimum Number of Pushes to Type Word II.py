"""
LeetCode #3016 - Minimum Number of Pushes to Type Word II
输入单词需要的最少按键次数 II
https://leetcode.cn/problems/minimum-number-of-pushes-to-type-word-ii/

给你一个字符串 `word`，由小写英文字母组成。
电话键盘上的按键与 不同 小写英文字母集合相映射，可以通过按压按键来组成单词。例如，按键 `2` 对应 `["a","b","c"]`，我们需要按一次键来输入 `"a"`，按两次键来输入 `"b"`，按三次键来输入 `"c"`。
现在允许你将编号为 `2` 到 `9` 的按键重新映射到 不同 字母集合。每个按键可以映射到 任意数量 的字母，但每个字母 必须 恰好 映射到 一个 按键上。你需要找到输入字符串 `word` 所需的 最少 按键次数。
返回重新映射按键后输入 `word` 所需的 最少 按键次数。
下面给出了一种电话键盘上字母到按键的映射作为示例。注意 `1`，`*`，`#` 和 `0` 不 对应任何字母。

示例 1：
输入：word = "abcde" 输出：5 解释：图片中给出的重新映射方案的输入成本最小。 "a" -> 在按键 2 上按一次 "b" -> 在按键 3 上按一次 "c" -> 在按键 4 上按一次 "d" -> 在按键 5 上按一次 "e" -> 在按键 6 上按一次 总成本为 1 + 1 + 1 + 1 + 1 = 5 。 可以证明不存在其他成本更低的映射方案。
示例 2：
输入：word = "xyzxyzxyzxyz" 输出：12 解释：图片中给出的重新映射方案的输入成本最小。 "x" -> 在按键 2 上按一次 "y" -> 在按键 3 上按一次 "z" -> 在按键 4 上按一次 总成本为 1 * 4 + 1 * 4 + 1 * 4 = 12 。 可以证明不存在其他成本更低的映射方案。 注意按键 9 没有映射到任何字母：不必让每个按键都存在与之映射的字母，但是每个字母都必须映射到按键上。
示例 3：
输入：word = "aabbccddeeffgghhiiiiii" 输出：24 解释：图片中给出的重新映射方案的输入成本最小。 "a" -> 在按键 2 上按一次 "b" -> 在按键 3 上按一次 "c" -> 在按键 4 上按一次 "d" -> 在按键 5 上按一次 "e" -> 在按键 6 上按一次 "f" -> 在按键 7 上按一次 "g" -> 在按键 8 上按一次 "h" -> 在按键 9 上按两次 "i" -> 在按键 9 上按一次 总成本为 1 * 2 + 1 * 2 + 1 * 2 + 1 * 2 + 1 * 2 + 1 * 2 + 1 * 2 + 2 * 2 + 6 * 1 = 24 。 可以证明不存在其他成本更低的映射方案。

提示：
`1 <= word.length <= 10^5`
`word` 仅由小写英文字母组成。
"""

from typing import List, Optional


class Solution:
    def minimumPushes(self, word: str) -> int:
        """
        Count letter frequencies, sort descending. Most frequent letters
        should be assigned to the first press of each key (8 keys).
        The i-th most frequent letter costs (i // 8 + 1) presses.
        """
        from collections import Counter

        freq = Counter(word)
        # Sort frequencies descending
        counts = sorted(freq.values(), reverse=True)

        total = 0
        for i, cnt in enumerate(counts):
            presses = i // 8 + 1  # 1st press for first 8, 2nd for next 8, etc.
            total += cnt * presses

        return total



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Hash Table, String, Counting, Sorting
#
# 解题思路:
# 贪心策略：统计每个字母的出现频率，按频率降序排列。
# 8 个按键（2-9）的第一个位置按 1 次，第二个位置按 2 次，以此类推。
# 将频率最高的前 8 个字母分配到各按键的第一位，接下来 8 个分配到第二位，依此类推。
# 第 i 个字母的按键次数为 i//8 + 1。
#
# 时间复杂度: O(n + 26*log26)，n 为 word 长度，26 个字母排序
# 空间复杂度: O(26) = O(1)，存储字母频率
#
# 关键点:
# - 按键次数与字母在按键上的位置相关（第一个位置 1 次，第二个 2 次...）
# - 高频字母应放在按键的第一个位置以最小化总次数
# - 每个按键可映射任意数量字母，因此 8 个按键足够覆盖 26 个字母
