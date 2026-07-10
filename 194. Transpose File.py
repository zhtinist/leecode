"""
LeetCode #194 - Transpose File
中文题名：转置文件
https://leetcode.com/problems/transpose-file/

Given a text file `file.txt`, transpose its content.

You may assume that each row has the same number of columns and each field is separated by
the `' '` character.

Example:

If `file.txt` has the following content:

name age
alice 21
ryan 30

Output the following:

name alice ryan
age 21 30

【中文翻译】
给定一个文本文件 `file.txt`，转置其内容。

你可以假设每一行具有相同数量的列，且每个字段由 `' '` 字符分隔。

示例：

如果 `file.txt` 的内容如下：

name age
alice 21
ryan 30

输出以下内容：

name alice ryan
age 21 30
"""

from typing import List, Optional


class Solution:
    def transposeFile(self) -> str:
        return """awk '{
    for (i = 1; i <= NF; i++) {
        if (NR == 1) {
            a[i] = $i
        } else {
            a[i] = a[i] " " $i
        }
    }
}
END {
    for (i = 1; i <= NF; i++) {
        print a[i]
    }
}' file.txt"""


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用 awk 进行矩阵转置。NR 是当前行号，NF 是当前行的字段数。
# 遍历每行的每个字段 (for i = 1 to NF)：
# - 如果是第一行 (NR == 1)，直接初始化数组 a[i] = $i
# - 否则追加：a[i] = a[i] " " $i
#
# 在 END 块中，按列输出转置后的结果：for i = 1 to NF print a[i]。
#
# 例如：
# name age       ->    name alice ryan
# alice 21       ->    age 21 30
# ryan 30
#
# 时间复杂度: O(R * C) — 遍历所有元素
# 空间复杂度: O(R * C) — 存储转置结果
#
# 关键点:
# - awk 的 NR（行号）和 NF（字段数）内置变量
# - 数组 a[i] 累积每列的值
# - END 块在所有行处理完后执行
# - 用空格连接同列不同行的值
