"""
LeetCode #293 - Flip Game
中文题名：翻转游戏
https://leetcode.com/problems/flip-game/

You are playing the following Flip Game with your friend: Given a string that contains only
these two characters: `+` and `-`, you and your friend take turns to
flip two consecutive `"++"` into `"--"`.
The game ends when a person can no longer make a move and therefore the other person will be
the winner.

Write a function to compute all possible states of the string after one valid move.

Example:

Input: `s = "++++"`
Output:
[
"--++",
"+--+",
"++--"
]

Note: If there is no valid move, return an empty list `[]`.

【中文翻译】
你和你的朋友正在玩以下翻转游戏：给定一个只包含 `+` 和 `-` 两种字符的字符串，你和你的朋友轮流将两个连续的 `"++"` 翻转为 `"--"`。
当某人无法再进行移动时，游戏结束，另一人获胜。

编写一个函数，计算在一次有效移动后字符串的所有可能状态。

示例：

输入：`s = "++++"`
输出：
[
"--++",
"+--+",
"++--"
]

注意：如果没有有效移动，返回空列表 `[]`。
"""

from typing import List, Optional


class Solution:
    def generatePossibleNextMoves(self, s: str) -> List[str]:
        """Generate all possible states after one valid move.

        A valid move is flipping two consecutive "++" to "--".
        Scan the string and for each occurrence of "++", create a new
        string with those two chars replaced by "--".
        """
        result = []
        chars = list(s)
        for i in range(len(s) - 1):
            if s[i] == '+' and s[i + 1] == '+':
                chars[i] = '-'
                chars[i + 1] = '-'
                result.append(''.join(chars))
                chars[i] = '+'
                chars[i + 1] = '+'
        return result


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Easy
# Paid Only: Yes
#
# 解题思路:
# 简单遍历。扫描字符串中所有相邻的两个字符，如果是 "++"，则将其翻转为 "--"，
# 生成一个新的字符串加入结果列表。为了方便修改，可以将字符串转为列表，
# 修改后转回字符串，然后再恢复原始状态继续下一个位置的检查。
#
# 时间复杂度: O(N^2) 如果每次 join 整个字符串 / O(N) 如果使用字符串切片
#   优化：用 s[:i] + "--" + s[i+2:] 生成新字符串，总体 O(N^2)
#   其中 N 为字符串长度，最多有 N-1 个可能位置
# 空间复杂度: O(N) - 结果列表和临时字符串
#
# 关键点:
# - 每次移动翻转两个连续的 "++"
# - 使用字符串切片 s[:i] + "--" + s[i+2:] 更简洁
# - 空结果列表表示没有合法移动
