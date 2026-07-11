"""
LeetCode #3106 - Lexicographically Smallest String After Operations With Constraint
满足距离约束且字典序最小的字符串
https://leetcode.cn/problems/lexicographically-smallest-string-after-operations-with-constraint/

给你一个字符串 `s` 和一个整数 `k` 。
定义函数 `distance(s_1, s_2)` ，用于衡量两个长度为 `n` 的字符串 `s_1` 和 `s_2` 之间的距离，即：
字符 `'a'` 到 `'z'` 按 循环 顺序排列，对于区间 `[0, n - 1]` 中的 `i` ，计算所有「 `s_1[i]` 和 `s_2[i]` 之间 最小距离」的 和 。
例如，`distance("ab", "cd") == 4` ，且 `distance("a", "z") == 1` 。
你可以对字符串 `s` 执行 任意次 操作。在每次操作中，可以将 `s` 中的一个字母 改变 为 任意 其他小写英文字母。
返回一个字符串，表示在执行一些操作后你可以得到的 字典序最小 的字符串 `t` ，且满足 `distance(s, t) <= k` 。

示例 1：
输入：s = "zbbz", k = 3 输出："aaaz" 解释：在这个例子中，可以执行以下操作： 将 s[0] 改为 'a' ，s 变为 "abbz" 。 将 s[1] 改为 'a' ，s 变为 "aabz" 。 将 s[2] 改为 'a' ，s 变为 "aaaz" 。 "zbbz" 和 "aaaz" 之间的距离等于 k = 3 。 可以证明 "aaaz" 是在任意次操作后能够得到的字典序最小的字符串。 因此，答案是 "aaaz" 。
示例 2：
输入：s = "xaxcd", k = 4 输出："aawcd" 解释：在这个例子中，可以执行以下操作： 将 s[0] 改为 'a' ，s 变为 "aaxcd" 。 将 s[2] 改为 'w' ，s 变为 "aawcd" 。 "xaxcd" 和 "aawcd" 之间的距离等于 k = 4 。 可以证明 "aawcd" 是在任意次操作后能够得到的字典序最小的字符串。 因此，答案是 "aawcd" 。
示例 3：
输入：s = "lol", k = 0 输出："lol" 解释：在这个例子中，k = 0，更改任何字符都会使得距离大于 0 。 因此，答案是 "lol" 。

提示：
`1 <= s.length <= 100`
`0 <= k <= 2000`
`s` 只包含小写英文字母。
"""

from typing import List, Optional


class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        t = list(s)
        for i, ch in enumerate(t):
            if k == 0:
                break
            # 到'a'的最小循环距离
            dist_down = ord(ch) - ord('a')       # 向下到'a'
            dist_up = 26 - dist_down              # 向上绕到'a'
            dist_to_a = min(dist_down, dist_up)
            if dist_to_a <= k:
                k -= dist_to_a
                t[i] = 'a'
            else:
                # 无法到达'a'，尽量向减小的方向移动k步
                t[i] = chr(ord(ch) - k)
                k = 0
        return ''.join(t)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, String
#
# 解题思路:
# 贪心从左到右处理。为了字典序最小，应优先让靠前的字符尽可能小（目标是'a'）。
# 对于每个字符，计算到'a'的最小循环距离（向下或向上绕），如果距离<=剩余预算k，
# 则变为'a'并扣除预算；否则尽量减小k步（向下方向），预算归零后停止。
# 后续字符保持不变。
#
# 时间复杂度: O(n)
# 空间复杂度: O(n)
#
# 关键点:
# - 循环距离取两个方向的最小值
# - 字典序最小要求优先优化靠前位置
# - 预算不足时只走k步（向下减小方向）
