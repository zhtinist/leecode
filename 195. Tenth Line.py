"""
LeetCode #195 - Tenth Line
中文题名：第十行
https://leetcode.com/problems/tenth-line/

Given a text file `file.txt`, print just the 10th line of the file.

Example:

Assume that `file.txt` has the following content:

Line 1
Line 2
Line 3
Line 4
Line 5
Line 6
Line 7
Line 8
Line 9
Line 10

Your script should output the tenth line, which is:

Line 10

Note:

1. If the file contains less than 10 lines, what should you output?

2. There's at least three different solutions. Try to explore all possibilities.

【中文翻译】
给定一个文本文件 `file.txt`，仅打印该文件的第 10 行。

示例：

假设 `file.txt` 的内容如下：

Line 1
Line 2
Line 3
Line 4
Line 5
Line 6
Line 7
Line 8
Line 9
Line 10

你的脚本应输出第十行，即：

Line 10

注意：

1. 如果文件包含少于 10 行，你应该输出什么？

2. 至少有三种不同的解法。尝试探索所有可能性。
"""

from typing import List, Optional


class Solution:
    def tenthLine(self) -> str:
        return """sed -n '10p' file.txt"""


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Easy
# Paid Only: No
#
# 解题思路:
# 使用 sed -n '10p' 打印第 10 行。sed 默认会输出所有行，-n 选项禁止默认输出，
# 只输出由 p 命令指定的行。如果文件少于 10 行，sed 不会输出任何内容。
#
# 其他解法：
# - awk 'NR == 10' file.txt — awk 判断行号
# - head -n 10 file.txt | tail -n 1 — 取前 10 行后取最后 1 行
#
# 时间复杂度: O(N) — 读取到第 10 行为止
# 空间复杂度: O(1)
#
# 关键点:
# - sed -n 禁止默认输出
# - '10p' 指定打印第 10 行
# - 文件少于 10 行时自动无输出（满足题意）
