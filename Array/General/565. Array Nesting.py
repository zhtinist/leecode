"""
LeetCode #565 - Array Nesting
中文题名：数组嵌套
https://leetcode.com/problems/array-nesting/

A zero-indexed array A of length N contains all integers from 0 to N-1. Find and return the
longest length of set S, where S[i] = {A[i], A[A[i]], A[A[A[i]]], ... } subjected to the
rule below.

Suppose the first element in S starts with the selection of element A[i] of index = i, the
next element in S should be A[A[i]], and then A[A[A[i]]]&hellip; By that analogy, we stop
adding right before a duplicate element occurs in S.

Example 1:

Input: A = [5,4,0,3,1,6,2]
Output: 4
Explanation:
A[0] = 5, A[1] = 4, A[2] = 0, A[3] = 3, A[4] = 1, A[5] = 6, A[6] = 2.

One of the longest S[K]:
S[0] = {A[0], A[5], A[6], A[2]} = {5, 6, 2, 0}

Note:

N is an integer within the range [1, 20,000].

The elements of A are all distinct.

Each element of A is an integer within the range [0, N-1].

【中文翻译】
给定一个长度为 N 的零索引数组 A，包含 0 到 N-1 的所有整数。找出并返回集合 S 的最长长度，其中
S[i] = {A[i], A[A[i]], A[A[A[i]]], ...}，规则如下：

假设 S 的第一个元素从索引 i 的元素 A[i] 开始，S 的下一个元素应为 A[A[i]]，然后是 A[A[A[i]]]，以此类推。
在出现重复元素之前停止添加。

示例 1：
    输入：A = [5,4,0,3,1,6,2]
    输出：4
    解释：
    A[0] = 5, A[1] = 4, A[2] = 0, A[3] = 3, A[4] = 1, A[5] = 6, A[6] = 2。
    其中一个最长的 S[K]：
    S[0] = {A[0], A[5], A[6], A[2]} = {5, 6, 2, 0}

注意：
    N 是 [1, 20,000] 范围内的整数。
    A 中的元素各不相同。
    A 中的每个元素是 [0, N-1] 范围内的整数。
"""

from typing import List, Optional


class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        """
        Find the longest length of a set S[k] = {nums[k], nums[nums[k]], ...}.
        Each number appears exactly once as an element (0..N-1), so the array
        decomposes into disjoint cycles.  We traverse each cycle once,
        marking visited elements in-place.
        """
        max_len = 0
        visited = [False] * len(nums)

        for i in range(len(nums)):
            if visited[i]:
                continue
            # Start a new cycle
            count = 0
            cur = i
            while not visited[cur]:
                visited[cur] = True
                cur = nums[cur]
                count += 1
            max_len = max(max_len, count)

        return max_len



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 由于数组中每个元素都在 [0, N-1] 范围内且互不相同，数组必然由若干个互不相交的环
# (cycle) 组成。问题转化为求最长环的长度。遍历每个未被访问的索引，沿着 nums 链路
# 遍历直到回到起点（或遇到已访问元素），统计环的长度并更新最大值。使用 visited 数组
# 标记已访问元素，避免重复遍历同一个环。
#
# 时间复杂度: O(N) — 每个元素恰好被访问一次
# 空间复杂度: O(N) — visited 数组；若允许修改原数组，可优化为 O(1)
#
# 关键点:
# - 数组元素互不相同且范围[0, N-1]意味着必然形成不相交的环
# - 每个环只需遍历一次，用 visited 标记避免重复
# - 不使用 visited 而将访问过的元素改为 -1 可将空间优化到 O(1)
