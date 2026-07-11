"""
LeetCode #1324 - Print Words Vertically
中文题名：竖直打印单词
https://leetcode.com/problems/print-words-vertically/

Given a string `s`. Return all the words vertically in the same
order in which they appear in `s`.

Words are returned as a list of strings, complete with spaces when is necessary.
(Trailing spaces are not allowed).

Each word would be put on only one column and that in one column there will be only one
word.

Example 1:

Input: s = "HOW ARE YOU"
Output: ["HAY","ORO","WEU"]
Explanation: Each word is printed vertically.
"HAY"
"ORO"
"WEU"

Example 2:

Input: s = "TO BE OR NOT TO BE"
Output: ["TBONTB","OEROOE","   T"]
Explanation: Trailing spaces is not allowed.
"TBONTB"
"OEROOE"
"   T"

Example 3:

Input: s = "CONTEST IS COMING"
Output: ["CIC","OSO","N M","T I","E N","S G","T"]

Constraints:

`1 <= s.length <= 200`

`s` contains only upper case English letters.

It's guaranteed that there is only one space between 2 words.

【中文翻译】
给定一个字符串 s，按单词在 s 中出现的顺序，竖直打印所有单词。
单词以字符串列表的形式返回，必要时用空格补全（但末尾空格不允许）。
每个单词只占一列，每列只有一个单词。

示例 1：

输入：s = "HOW ARE YOU"
输出：["HAY","ORO","WEU"]
解释：每个单词竖直打印。
"HAY"
"ORO"
"WEU"

示例 2：

输入：s = "TO BE OR NOT TO BE"
输出：["TBONTB","OEROOE","   T"]
解释：不允许末尾空格。
"TBONTB"
"OEROOE"
"   T"

示例 3：

输入：s = "CONTEST IS COMING"
输出：["CIC","OSO","N M","T I","E N","S G","T"]
"""

from typing import List, Optional


class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        max_len = max(len(w) for w in words)
        result = []
        for i in range(max_len):
            col = []
            for w in words:
                col.append(w[i] if i < len(w) else ' ')
            # Remove trailing spaces
            while col and col[-1] == ' ':
                col.pop()
            result.append(''.join(col))
        return result



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 先将字符串按空格分割成单词列表，找到最长单词的长度 max_len。
# 对于每一列 i (0 到 max_len-1)，遍历每个单词，如果单词长度 > i 则取该字符，
# 否则补空格。构建完一列后，去掉末尾的多余空格，加入结果列表。
#
# 时间复杂度: O(N * K) — N 为单词数，K 为最长单词长度
# 空间复杂度: O(N * K) — 存储结果
#
# 关键点:
# - 关键是去掉每列末尾的 trailing spaces
# - 当单词长度不足时用空格填充
# - 确保返回的字符串列表中没有末尾空格
