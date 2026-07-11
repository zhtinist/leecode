"""
LeetCode #3324 - Find the Sequence of Strings Appeared on the Screen
出现在屏幕上的字符串序列
https://leetcode.cn/problems/find-the-sequence-of-strings-appeared-on-the-screen/

给你一个字符串 `target`。
Alice 将会使用一种特殊的键盘在她的电脑上输入 `target`，这个键盘 只有两个 按键：
按键 1：在屏幕上的字符串后追加字符 `'a'`。
按键 2：将屏幕上字符串的 最后一个 字符更改为英文字母表中的 下一个 字符。例如，`'c'` 变为 `'d'`，`'z'` 变为 `'a'`。
注意，最初屏幕上是一个空字符串 `""`，所以她 只能 按按键 1。
请你考虑按键次数 最少 的情况，按字符串出现顺序，返回 Alice 输入 `target` 时屏幕上出现的所有字符串列表。

示例 1：

输入： target = "abc"
输出： ["a","aa","ab","aba","abb","abc"]
解释：
Alice 按键的顺序如下：
按下按键 1，屏幕上的字符串变为 `"a"`。
按下按键 1，屏幕上的字符串变为 `"aa"`。
按下按键 2，屏幕上的字符串变为 `"ab"`。
按下按键 1，屏幕上的字符串变为 `"aba"`。
按下按键 2，屏幕上的字符串变为 `"abb"`。
按下按键 2，屏幕上的字符串变为 `"abc"`。
示例 2：

输入： target = "he"
输出： ["a","b","c","d","e","f","g","h","ha","hb","hc","hd","he"]

提示：
`1 <= target.length <= 400`
`target` 仅由小写英文字母组成。
"""

from typing import List, Optional


class Solution:
    def stringSequence(self, target: str) -> List[str]:
        res = []
        cur = []
        for ch in target:
            cur.append('a')
            res.append(''.join(cur))
            while cur[-1] != ch:
                cur[-1] = chr(ord(cur[-1]) + 1)
                res.append(''.join(cur))
        return res



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: String, Simulation
#
# 解题思路:
# 模拟键盘输入过程。起始屏幕为空，每次要么追加'a'（按键1），要么将最后一个字符改为字母表中下一个（按键2）。
# 对于target中的每个字符，先追加'a'，然后逐步将其递增到目标字符。每一步都将当前屏幕字符串加入结果。
#
# 时间复杂度: O(n * 26)，n为target长度，每个字符最多递增25次
# 空间复杂度: O(1)不考虑输出，输出列表大小为O(n)
#
# 关键点:
# - 最优策略是逐个字符构建：先追加'a'，再递增到目标字符
# - 追加'a'比连续递增更优（对于非'a'字符，先追加再递增比一路递增过来更快）
