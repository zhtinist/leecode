"""
LeetCode #2284 - Sender With Largest Word Count
最多单词数的发件人
https://leetcode.cn/problems/sender-with-largest-word-count/

给你一个聊天记录，共包含 `n` 条信息。给你两个字符串数组 `messages` 和 `senders` ，其中 `messages[i]` 是 `senders[i]` 发出的一条 信息 。
一条 信息 是若干用单个空格连接的 单词 ，信息开头和结尾不会有多余空格。发件人的 单词计数 是这个发件人总共发出的 单词数 。注意，一个发件人可能会发出多于一条信息。
请你返回发出单词数 最多 的发件人名字。如果有多个发件人发出最多单词数，请你返回 字典序 最大的名字。
注意：
字典序里，大写字母小于小写字母。
`"Alice"` 和 `"alice"` 是不同的名字。

示例 1：
输入：messages = ["Hello userTwooo","Hi userThree","Wonderful day Alice","Nice day userThree"], senders = ["Alice","userTwo","userThree","Alice"] 输出："Alice" 解释：Alice 总共发出了 2 + 3 = 5 个单词。 userTwo 发出了 2 个单词。 userThree 发出了 3 个单词。 由于 Alice 发出单词数最多，所以我们返回 "Alice" 。
示例 2：
输入：messages = ["How is leetcode for everyone","Leetcode is useful for practice"], senders = ["Bob","Charlie"] 输出："Charlie" 解释：Bob 总共发出了 5 个单词。 Charlie 总共发出了 5 个单词。 由于最多单词数打平，返回字典序最大的名字，也就是 Charlie 。

提示：
`n == messages.length == senders.length`
`1 <= n <= 10^4`
`1 <= messages[i].length <= 100`
`1 <= senders[i].length <= 10`
`messages[i]` 包含大写字母、小写字母和 `' '` 。
`messages[i]` 中所有单词都由 单个空格 隔开。
`messages[i]` 不包含前导和后缀空格。
`senders[i]` 只包含大写英文字母和小写英文字母。
"""

from typing import List, Optional
from collections import defaultdict


class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        """
        Count total words for each sender, then return the sender with the
        maximum word count. On ties, return the lexicographically largest name.
        """
        word_count = defaultdict(int)

        for msg, sender in zip(messages, senders):
            # Count words: number of spaces + 1 (since words are single-space separated)
            word_count[sender] += msg.count(' ') + 1

        max_count = -1
        result = ""

        for sender, count in word_count.items():
            if count > max_count or (count == max_count and sender > result):
                max_count = count
                result = sender

        return result


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Hash Table, String, Counting
#
# 解题思路:
# 1. 使用哈希表统计每个发件人发出的总单词数。对于每条消息，单词数等于空格数加 1。
# 2. 遍历哈希表，同时维护最大单词数对应的发件人名字。
# 3. 当遇到单词数更大的发件人时更新结果；当单词数相同时，取字典序更大的名字。
# 4. 由于消息由单个空格分隔且无前后空格，直接用 count(' ') + 1 即可计算单词数。
#
# 时间复杂度: O(N * M)，其中 N 是消息数量，M 是单条消息的最大长度（用于 count 操作）
# 空间复杂度: O(S)，其中 S 是不同发件人的数量，用于哈希表存储
#
# 关键点:
# - 单词数 = 空格数 + 1（消息中单词由单个空格分隔）
# - 平局时返回字典序更大的名字，使用字符串直接比较 (Python 中 > 对应字典序)
# - 注意区分大小写："Alice" 和 "alice" 是不同的名字
