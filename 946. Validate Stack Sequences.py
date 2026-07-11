"""
LeetCode #946 - Validate Stack Sequences
中文题名：验证栈序列
https://leetcode.com/problems/validate-stack-sequences/

Given two sequences `pushed` and `popped` with distinct
values, return `true` if and only if this could have been the
result of a sequence of push and pop operations on an initially empty stack.

Example 1:

Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true
Explanation: We might do the following sequence:
push(1), push(2), push(3), push(4), pop() -> 4,
push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1

Example 2:

Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
Output: false
Explanation: 1 cannot be popped before 2.

Note:

`0 <= pushed.length == popped.length <= 1000`

`0 <= pushed[i], popped[i] < 1000`

`pushed` is a permutation of `popped`.

`pushed` and `popped` have distinct values.

【中文翻译】
给定两个具有不同值的序列 pushed 和 popped，当且仅当它们可能是在
最初为空的栈上进行一系列压入和弹出操作的结果时，返回 true。

"""

from typing import List, Optional


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        pop_idx = 0

        for val in pushed:
            stack.append(val)
            while stack and stack[-1] == popped[pop_idx]:
                stack.pop()
                pop_idx += 1

        return len(stack) == 0



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 1. 模拟压栈和弹栈：使用一个辅助栈 stack 模拟实际的栈操作。
# 2. 遍历 pushed 数组，每次将当前元素压入 stack。
# 3. 每次压入后，检查栈顶元素是否等于 popped[pop_idx]：
#    - 如果相等，持续弹出栈顶并移动 pop_idx，直到不相等或栈为空。
# 4. 最终检查：如果栈为空，说明所有弹出操作均能按 popped 顺序完成，返回 true。
#
# 时间复杂度: O(N) — 每个元素最多压入和弹出各一次。
# 空间复杂度: O(N) — 辅助栈的空间。
#
# 关键点:
# - 贪心模拟：一旦栈顶匹配 popped 的下一个元素就立即弹出
# - 由于 pushed 是 popped 的排列且值各不相同，贪心策略总是正确的
# - 最终如果栈为空则序列有效
