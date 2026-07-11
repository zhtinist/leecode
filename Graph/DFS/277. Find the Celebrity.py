"""
LeetCode #277 - Find the Celebrity
中文题名：搜寻名人
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

【中文翻译】
假设你正在参加一个 `n` 人的派对（标记为 `0` 到 `n - 1`），其中可能存在一位「名人」。名人的定义是：其他所有 `n - 1` 人都认识他/她，而他/她不认识任何其他人。

现在你想找出谁是名人，或验证没有名人。你唯一允许的操作是向 A 提问：「你好，A，你认识 B 吗？」以获取 A 是否认识 B 的信息。你需要通过尽可能少的问题（在渐近意义上）找出名人（或验证没有名人）。

你会得到一个辅助函数 `bool knows(a, b)`，它告诉你 A 是否认识 B。实现一个函数 `int findCelebrity(n)`。如果派对中有名人，则恰好有一位。如果存在名人，返回名人的编号；如果没有名人，返回 `-1`。

示例 1：

*

输入：graph = [
[1,1,0],
[0,1,0],
[1,1,1]
]
输出：1
解释：有三个人标记为 0、1 和 2。graph[i][j] = 1 表示第 i 个人认识第 j 个人，否则 graph[i][j] = 0 表示不认识。名人是标记为 1 的人，因为 0 和 2 都认识他，但 1 不认识任何人。

示例 2：

*

输入：graph = [
[1,0,1],
[1,1,0],
[0,1,1]
]
输出：-1
解释：没有名人。

注意：

有向图表示为邻接矩阵，这是一个 `n x n` 矩阵，其中 `a[i][j] = 1` 表示第 `i` 个人认识第 `j` 个人，而 `a[i][j] = 0` 表示相反。

请记住，你无法直接访问邻接矩阵。
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
