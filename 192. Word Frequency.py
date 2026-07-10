"""
LeetCode #192 - Word Frequency
https://leetcode.com/problems/word-frequency/

Write a bash script to calculate the frequency of each word in a text file
`words.txt`.

For simplicity sake, you may assume:

`words.txt` contains only lowercase characters and space `'
'` characters.

Each word must consist of lowercase characters only.

Words are separated by one or more whitespace characters.

Example:

Assume that `words.txt` has the following content:

the day is sunny the the
the sunny is is

Your script should output the following, sorted by descending frequency:

the 4
is 3
sunny 2
day 1

Note:

Don't worry about handling ties, it is guaranteed that each word's frequency
count is unique.

Could you write it in one-line using Unix pipes?
"""

from typing import List, Optional


class Solution:
    def wordFrequency(self) -> str:
        return """cat words.txt | tr -s ' ' '\\n' | sort | uniq -c | sort -rn | awk '{print $2, $1}'"""


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用 Unix 管道组合多个命令：
# 1. cat words.txt — 读取文件内容
# 2. tr -s ' ' '\n' — 将所有空格替换为换行符，-s 压缩连续空格
# 3. sort — 排序所有单词（为 uniq 做准备）
# 4. uniq -c — 统计每个单词出现的次数，输出格式为 "次数 单词"
# 5. sort -rn — 按数字降序排列（-r 反转，-n 数字排序）
# 6. awk '{print $2, $1}' — 交换列顺序，输出 "单词 次数"
#
# 时间复杂度: O(N log N) — 排序主导
# 空间复杂度: O(N) — 排序需要临时存储
#
# 关键点:
# - tr 将空格转成换行符，让每个单词独占一行
# - uniq -c 必须在 sort 之后使用（uniq 只合并相邻重复行）
# - sort -rn 降序排列频率
# - awk 交换输出格式
