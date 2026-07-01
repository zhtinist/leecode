"""
LeetCode #20 - Valid Parentheses
https://leetcode.com/problems/valid-parentheses/

Given a string s containing just the characters '(', ')', '{', '}', '[' and
']', determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Example 1:
    Input: s = "()"
    Output: true

Example 2:
    Input: s = "()[]{}"
    Output: true

Example 3:
    Input: s = "(]"
    Output: false

Example 4:
    Input: s = "([])"
    Output: true

Example 5:
    Input: s = "([)]"
    Output: false

Constraints:
    1 <= s.length <= 10^4
    s consists of parentheses only '()[]{}'.
"""


class Solution:
    CLOSING_TO_OPENING = {
        ")": "(",
        "]": "[",
        "}": "{",
    }

    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char in self.CLOSING_TO_OPENING:
                if not stack or stack[-1] != self.CLOSING_TO_OPENING[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)

        return len(stack) == 0
