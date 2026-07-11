"""
LeetCode #3295 - Report Spam Message
举报垃圾信息
https://leetcode.cn/problems/report-spam-message/

给你一个字符串数组 `message` 和一个字符串数组 `bannedWords`。
如果数组中 至少 存在两个单词与 `bannedWords` 中的任一单词 完全相同，则该数组被视为 垃圾信息。
如果数组 `message` 是垃圾信息，则返回 `true`；否则返回 `false`。

示例 1：

输入： message = ["hello","world","leetcode"], bannedWords = ["world","hello"]
输出： true
解释：
数组 `message` 中的 `"hello"` 和 `"world"` 都出现在数组 `bannedWords` 中。
示例 2：

输入： message = ["hello","programming","fun"], bannedWords = ["world","programming","leetcode"]
输出： false
解释：
数组 `message` 中只有一个单词（`"programming"`）出现在数组 `bannedWords` 中。

提示：
`1 <= message.length, bannedWords.length <= 10^5`
`1 <= message[i].length, bannedWords[i].length <= 15`
`message[i]` 和 `bannedWords[i]` 都只由小写英文字母组成。
"""

from typing import List, Optional


class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        banned_set = set(bannedWords)
        count = 0
        for word in message:
            if word in banned_set:
                count += 1
                if count >= 2:
                    return True
        return False










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Hash Table, String
#
# 解题思路:
# 将 bannedWords 存入哈希集合，遍历 message 统计出现在 bannedWords 中的单词数。
# 如果计数 >= 2，返回 True（是垃圾信息），否则返回 False。
# 可以提前终止：一旦计数达到 2 立即返回。
#
# 时间复杂度: O(n + m) — n = len(message), m = len(bannedWords)
# 空间复杂度: O(m)
#
# 关键点:
# - 使用 set 实现 O(1) 查找
# - 提前终止优化：两个匹配就足够判断
