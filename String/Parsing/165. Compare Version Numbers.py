"""
LeetCode #165 - Compare Version Numbers
https://leetcode.com/problems/compare-version-numbers/

Given two version strings, version1 and version2, compare them. A version string
consists of revisions separated by dots '.'. The value of the revision is its
integer conversion ignoring leading zeros.

Return the following:
- If version1 < version2, return -1.
- If version1 > version2, return 1.
- Otherwise, return 0.

Example 1:
    Input: version1 = "1.2", version2 = "1.10"
    Output: -1
    Explanation: version1's second revision is "2" and version2's second
    revision is "10": 2 < 10, so version1 < version2.

Example 2:
    Input: version1 = "1.01", version2 = "1.001"
    Output: 0
    Explanation: Ignoring leading zeroes, both "01" and "001" represent the same
    revision "1".

Example 3:
    Input: version1 = "1.0", version2 = "1.0.0"
    Output: 0
    Explanation: version1 does not specify revision 2, which means it is
    treated as "0".

Constraints:
    1 <= version1.length, version2.length <= 500
    version1 and version2 consist of only digits and '.'.
    version1 and version2 are valid version strings.
    All the given revisions in version1 and version2 can be stored in a 32-bit
    integer.
"""


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        parts1 = version1.split(".")
        parts2 = version2.split(".")
        length = max(len(parts1), len(parts2))

        for i in range(length):
            v1 = int(parts1[i]) if i < len(parts1) else 0
            v2 = int(parts2[i]) if i < len(parts2) else 0
            if v1 < v2:
                return -1
            if v1 > v2:
                return 1

        return 0
