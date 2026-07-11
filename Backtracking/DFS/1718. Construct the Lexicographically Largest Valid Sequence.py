"""
LeetCode #1718 - Construct the Lexicographically Largest Valid Sequence
中文题名：构建字典序最大的可行序列
https://leetcode.com/problems/construct-the-lexicographically-largest-valid-sequence/

Given an integer `n`, find a sequence that satisfies all of the
following:

The integer `1` occurs once in the sequence.

Each integer between `2` and `n` occurs twice in the
sequence.

For every integer `i` between `2` and `n`, the
distance between the two occurrences of `i` is
exactly `i`.

The distance between two numbers on the sequence, `a[i]`
and `a[j]`, is the absolute difference of their indices, `|j -
i|`.

Return the lexicographically largest sequence. It is
guaranteed that under the given constraints, there is always a solution.

A sequence `a` is lexicographically larger than a sequence `b`
(of the same length) if in the first position where `a` and
`b` differ, sequence `a` has a number greater than the
corresponding number in `b`. For example, `[0,1,9,0]` is
lexicographically larger than `[0,1,5,6]` because the first position they
differ is at the third number, and `9` is greater than `5`.

Example 1:

Input: n = 3
Output: [3,1,2,3,2]
Explanation: [2,3,2,1,3] is also a valid sequence, but [3,1,2,3,2] is the lexicographically largest valid sequence.

Example 2:

Input: n = 5
Output: [5,3,1,4,3,5,2,4,2]

Constraints:

`1 <= n <= 20`

【中文翻译】
给定整数 n，构造一个长度为 2*n-1 的序列，使得：
- 1 到 n 中每个整数都出现，其中 1 出现一次，2 到 n 各出现两次
- 对于每个出现在两个位置的整数 i（2 <= i <= n），两个 i 之间的距离恰好为 i
返回字典序最大的可行序列。

示例 1：
输入: n = 3
输出: [3,1,2,3,2]
解释: 3 的距离为3，2 的距离为2，1 出现一次。这是字典序最大的。
"""

from typing import List, Optional


class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        length = 2 * n - 1
        result = [0] * length
        used = [False] * (n + 1)

        def backtrack(pos: int) -> bool:
            if pos == length:
                return True
            if result[pos] != 0:
                return backtrack(pos + 1)

            for num in range(n, 0, -1):  # 从大到小尝试，保证字典序最大
                if used[num]:
                    continue
                if num == 1:
                    result[pos] = 1
                    used[1] = True
                    if backtrack(pos + 1):
                        return True
                    result[pos] = 0
                    used[1] = False
                else:
                    second = pos + num
                    if second < length and result[second] == 0:
                        result[pos] = result[second] = num
                        used[num] = True
                        if backtrack(pos + 1):
                            return True
                        result[pos] = result[second] = 0
                        used[num] = False
            return False

        backtrack(0)
        return result
# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 回溯法。从位置0开始，尝试放置数字（从大到小保证字典序最大）。
# - 数字1：只需放置一个位置
# - 数字 k > 1：需放在 pos 和 pos+k 两个位置
# 使用 used 数组记录已使用的数字，result 数组记录当前序列。
# 回溯时先找空位，从大到小尝试数字，找到可行解立即返回（因为从大到小，第一个解就是字典序最大）。
#
# 时间复杂度: O(N!) — 回溯最坏情况，但 n <= 20 且剪枝有效
# 空间复杂度: O(N) — result 和 used 数组
#
# 关键点:
# - 从大到小尝试数字保证第一个找到的解就是字典序最大的
# - 回溯剪枝：跳过已占用的位置
# - 数2到n需要检查第二个位置是否在范围内且未被占用
