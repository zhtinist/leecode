"""
LeetCode #38 - Count and Say
https://leetcode.com/problems/count-and-say/

The count-and-say sequence is a sequence of digit strings defined by the
recursive formula:

    countAndSay(1) = "1"
    countAndSay(n) is the way you would "say" the digit string from
    countAndSay(n - 1), which is converted into a different digit string.

To determine how you "say" a digit string, split it into the minimal number of
groups so that each group is a contiguous section all of the same character.
Then for each group, say the number of characters, then say the character.

For example, the digit string "3322251" becomes:
    "2 3's, 3 2's, 1 5, and 1 1"
or
    "23321511"

Given a positive integer n, return the nth term of the count-and-say sequence.

Example 1:
    Input: n = 4
    Output: "1211"
    Explanation:
        countAndSay(1) = "1"
        countAndSay(2) = say "1" = one 1 = "11"
        countAndSay(3) = say "11" = two 1's = "21"
        countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"

Example 2:
    Input: n = 1
    Output: "1"

Constraints:
    1 <= n <= 30
"""


class Solution:
    def countAndSay(self, n: int) -> str:
        result = "1"
        for _ in range(n - 1):
            result = self._say(result)
        return result

    def _say(self, s: str) -> str:
        parts = []
        i = 0
        while i < len(s):
            j = i
            while j < len(s) and s[j] == s[i]:
                j += 1
            parts.append(str(j - i) + s[i])
            i = j
        return "".join(parts)
