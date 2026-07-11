"""
LeetCode #2375 - Construct Smallest Number From DI String
根据模式串构造最小数字
https://leetcode.cn/problems/construct-smallest-number-from-di-string/

给你下标从 0 开始、长度为 `n` 的字符串 `pattern` ，它包含两种字符，`'I'` 表示 上升 ，`'D'` 表示 下降 。
你需要构造一个下标从 0 开始长度为 `n + 1` 的字符串，且它要满足以下条件：
`num` 包含数字 `'1'` 到 `'9'` ，其中每个数字 至多 使用一次。
如果 `pattern[i] == 'I'` ，那么 `num[i] < num[i + 1]` 。
如果 `pattern[i] == 'D'` ，那么 `num[i] > num[i + 1]` 。
请你返回满足上述条件字典序 最小 的字符串 `num`。

示例 1：
输入：pattern = "IIIDIDDD" 输出："123549876" 解释： 下标 0 ，1 ，2 和 4 处，我们需要使 num[i] < num[i+1] 。 下标 3 ，5 ，6 和 7 处，我们需要使 num[i] > num[i+1] 。 一些可能的 num 的值为 "245639871" ，"135749862" 和 "123849765" 。 "123549876" 是满足条件最小的数字。 注意，"123414321" 不是可行解因为数字 '1' 使用次数超过 1 次。
示例 2：
输入：pattern = "DDD" 输出："4321" 解释： 一些可能的 num 的值为 "9876" ，"7321" 和 "8742" 。 "4321" 是满足条件最小的数字。

提示：
`1 <= pattern.length <= 8`
`pattern` 只包含字符 `'I'` 和 `'D'` 。
"""

from typing import List, Optional


class Solution:
    def smallestNumber(self, pattern: str) -> str:
        result = []
        stack = []
        n = len(pattern)

        for i in range(1, n + 2):  # 1 to n+1 inclusive
            stack.append(str(i))
            if i == n + 1 or pattern[i - 1] == 'I':
                while stack:
                    result.append(stack.pop())

        return ''.join(result)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Stack, Greedy, String, Backtracking
#
# 解题思路:
# 使用栈来构造最小字典序的数字。遍历数字 i 从 1 到 n+1（其中 n=len(pattern)）：
# 将 i 压入栈中。如果 i 已经到达末尾（i == n+1），或者当前模式字符是 'I'，
# 则将栈中所有元素弹出并加入结果列表。
# 栈的特性保证了：当遇到 'I' 时，栈中存放的是上一段连续 'D' 的数字，
# 弹出时得到递减序列，再配合之后的递增，形成字典序最小的排列。
#
# 时间复杂度: O(n) 其中 n 为 pattern 的长度，每个数字最多入栈出栈一次
# 空间复杂度: O(n) 栈和结果列表的空间
#
# 关键点:
# - 栈的使用：连续 D 的部分先压栈暂存，遇到 I 时统一弹出
# - 遍历范围是 1 到 n+1（共 n+1 个数字）
# - 弹出栈时是逆序的，将 D 段反转，得到最小字典序
