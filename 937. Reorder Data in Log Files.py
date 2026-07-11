"""
LeetCode #937 - Reorder Data in Log Files
中文题名：重新排列日志文件
https://leetcode.com/problems/reorder-data-in-log-files/

You have an array of `logs`.  Each log is a space delimited string of words.

For each log, the first word in each log is an alphanumeric identifier.  Then,
either:

Each word after the identifier will consist only of lowercase letters, or;

Each word after the identifier will consist only of digits.

We will call these two varieties of logs letter-logs and digit-logs.
It is guaranteed that each log has at least one word after its identifier.

Reorder the logs so that all of the letter-logs come before any digit-log.  The
letter-logs are ordered lexicographically ignoring identifier, with the identifier used in
case of ties.  The digit-logs should be put in their original order.

Return the final order of the logs.

Example 1:

Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]

Constraints:

`0 <= logs.length <= 100`

`3 <= logs[i].length <= 100`

`logs[i]` is guaranteed to have an identifier, and a word after the
identifier.

【中文翻译】
你有一个日志数组 logs。每条日志都是以空格分隔的字符串。

对于每条日志，第一个单词是字母数字标识符。然后，以下之一成立：
- 标识符后的每个单词仅由小写字母组成；或者
- 标识符后的每个单词仅由数字组成。

我们将这两种日志分别称为字母日志和数字日志。
保证每条日志的标识符后面至少有一个单词。

重新排列日志，使得所有字母日志都在任何数字日志之前。
字母日志按忽略标识符的字典顺序排序，如果内容相同则使用标识符进行排序。
数字日志应保持其原始顺序。

返回日志的最终顺序。

"""

from typing import List, Optional


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digit_logs = []

        for log in logs:
            # Split at the first space to get identifier and the rest
            idx = log.index(' ')
            content = log[idx + 1:]
            if content[0].isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append(log)

        # Sort letter-logs by (content, identifier)
        letter_logs.sort(key=lambda x: (x[x.index(' ') + 1:], x[:x.index(' ')]))

        return letter_logs + digit_logs



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 1. 分离日志：遍历 logs 数组，根据标识符后第一个单词的首字符是数字还是字母，
#    将日志分别放入字母日志列表和数字日志列表。
# 2. 排序字母日志：使用自定义排序键：(日志内容（忽略标识符）, 标识符)。
#    先按内容字典序排序，内容相同时按标识符排序。
# 3. 合并结果：将排序后的字母日志与原始顺序的数字日志拼接返回。
#
# 时间复杂度: O(N * log N) — 主要开销来自对字母日志的排序，其中 N 是日志数量。
# 空间复杂度: O(N) — 需要存储分离后的两个列表。
#
# 关键点:
# - 数字日志必须保持原始顺序（稳定不做任何排序）
# - 字母日志按内容排序时忽略标识符；内容相同时才看标识符
# - 判断字母/数字日志：检查标识符后第一个单词的首字符
