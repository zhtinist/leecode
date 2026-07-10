"""
LeetCode #277 - Find the Celebrity
https://leetcode.com/problems/find-the-celebrity/

Suppose you are at a party with `n` people (labeled from `0` to `n
- 1`) and among them, there may exist one celebrity. The definition of a celebrity is
that all the other `n - 1` people know him/her but he/she does not know any of
them.

Now you want to find out who the celebrity is or verify that there is not one. The only thing
you are allowed to do is to ask questions like: "Hi, A. Do you know B?" to get
information of whether A knows B. You need to find out the celebrity (or verify there is not
one) by asking as few questions as possible (in the asymptotic sense).

You are given a helper function `bool knows(a, b)` which tells you whether A knows
B. Implement a function `int findCelebrity(n)`. There will be exactly one
celebrity if he/she is in the party. Return the celebrity's label if there is a
celebrity in the party. If there is no celebrity, return `-1`.

Example 1:

*

Input: graph = [
[1,1,0],
[0,1,0],
[1,1,1]
]
Output: 1
Explanation: There are three persons labeled with 0, 1 and 2. graph[i][j] = 1 means person i knows person j, otherwise graph[i][j] = 0 means person i does not know person j. The celebrity is the person labeled as 1 because both 0 and 2 know him but 1 does not know anybody.

Example 2:

*

Input: graph = [
[1,0,1],
[1,1,0],
[0,1,1]
]
Output: -1
Explanation: There is no celebrity.

Note:

The directed graph is represented as an adjacency matrix, which is an `n x
n` matrix where `a[i][j] = 1` means person `i` knows
person `j` while `a[i][j] = 0` means the contrary.

Remember that you won't have direct access to the adjacency matrix.
"""

from typing import List, Optional


# The knows API is already defined for you.
# def knows(a: int, b: int) -> bool:
#     """Return whether person a knows person b."""


class Solution:
    def findCelebrity(self, n: int) -> int:
        """Find the celebrity among n people.

        Two-pass algorithm:
        Pass 1: Find a candidate. If knows(a, b) is True, a is NOT celebrity
                (celebrity knows nobody). If False, b is NOT celebrity
                (everyone knows celebrity). Iterate to narrow down to one candidate.
        Pass 2: Verify the candidate satisfies both celebrity conditions.
        """
        # Pass 1: Find candidate
        candidate = 0
        for i in range(1, n):
            if knows(candidate, i):
                # candidate knows i, so candidate cannot be celebrity
                # i could be celebrity
                candidate = i

        # Pass 2: Verify candidate
        for i in range(n):
            if i == candidate:
                continue
            # Celebrity should not know anyone, and everyone should know celebrity
            if knows(candidate, i) or not knows(i, candidate):
                return -1

        return candidate


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: Yes
#
# 解题思路:
# 两遍扫描法。
# 第一遍：找出候选者。从 candidate = 0 开始，遍历所有人。如果 knows(candidate, i)
# 为真，说明 candidate 认识 i，candidate 不可能是名人，将 candidate 更新为 i。
# 这样遍历完后，candidate 是唯一可能的候选人。因为如果一个人认识别人，他就不是
# 名人；名人不认识任何人。
# 第二遍：验证候选者。检查 candidate 是否不认识所有人，以及所有人是否都认识
# candidate。如果任一条件不满足，返回 -1。
#
# 时间复杂度: O(N) - 两遍扫描，每遍 O(N)
# 空间复杂度: O(1) - 只使用常数个变量
#
# 关键点:
# - 利用名人的定义（不认识任何人，所有人都认识他）来淘汰候选人
# - 第一遍扫描中， knows(a,b) 为真则 a 被淘汰，为假则 b 被淘汰
# - 第一遍的淘汰逻辑保证每步至少淘汰一人
# - 第二遍必须验证，因为第一步只保证找到一个"可能"的候选人
