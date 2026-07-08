"""
LeetCode #93 - Restore IP Addresses
https://leetcode.com/problems/restore-ip-addresses/

A valid IP address consists of exactly four integers separated by single dots.
Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

Given a string s containing only digits, return all possible valid IP addresses
that can be formed by inserting dots into s.

Example 1:
    Input: s = "25525511135"
    Output: ["255.255.11.135","255.255.111.35"]

Example 2:
    Input: s = "0000"
    Output: ["0.0.0.0"]

Example 3:
    Input: s = "101023"
    Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]

Constraints:
    1 <= s.length <= 20
    s consists of digits only.
"""

from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        parts: List[str] = []

        def is_valid(segment: str) -> bool:
            if not segment or len(segment) > 3:
                return False
            if segment[0] == "0" and len(segment) > 1:
                return False
            return 0 <= int(segment) <= 255

        def dfs(start: int) -> None:
            if len(parts) == 4:
                if start == len(s):
                    result.append(".".join(parts))
                return
            if len(parts) == 3:
                segment = s[start:]
                if is_valid(segment):
                    result.append(".".join(parts + [segment]))
                return

            for end in range(start + 1, min(start + 4, len(s) + 1)):
                segment = s[start:end]
                if not is_valid(segment):
                    continue
                parts.append(segment)
                dfs(end)
                parts.pop()

        dfs(0)
        return result
