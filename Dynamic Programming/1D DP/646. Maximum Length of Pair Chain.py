"""
LeetCode #646 - Maximum Length of Pair Chain
中文题名：最长数对链
https://leetcode.com/problems/maximum-length-of-pair-chain/

You are given `n` pairs of numbers. In every pair, the first number is always
smaller than the second number.

Now, we define a pair `(c, d)` can follow another pair `(a, b)` if and
only if `b  [3,4]

Note:

The number of given pairs will be in the range [1, 1000].

【中文翻译】
给定 `n` 个数对。在每个数对中，第一个数总是小于第二个数。

现在，我们定义一个数对 `(c, d)` 可以跟在 `(a, b)` 之后，当且仅当 `b < c`。
这种形式的数对链可以用类似的方式扩展。

给定一组数对，找出可以形成的最长数对链的长度。你不需要用完所有给定的数对。
你可以按任意顺序选择数对。

示例 1：

输入：[[1,2], [2,3], [3,4]]
输出：2
解释：最长的链是 [1,2] -> [3,4]

注意：

给定数对的数量在 [1, 1000] 范围内。
"""

from typing import List, Optional


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # Greedy: sort by the second element (end time)
        pairs.sort(key=lambda x: x[1])

        curr_end = float('-inf')
        count = 0

        for start, end in pairs:
            if start > curr_end:
                count += 1
                curr_end = end

        return count



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 贪心算法（类似区间调度问题 / 无重叠区间）：
# 1. 按照每个数对的第二个元素（end）从小到大排序。
# 2. 初始化 curr_end 为一个极小值，count = 0。
# 3. 遍历排序后的数对：
#    - 如果当前数对的 start > curr_end（即不与前一个选中数对重叠），
#      则选中该数对，count++，更新 curr_end。
# 4. 返回 count。
#
# 也可用动态规划：按 start 排序后，dp[i] = max(dp[i], dp[j] + 1)（需要 pairs[j][1] < pairs[i][0]），
# 时间复杂度 O(n^2)。贪心更优 O(n log n)。
#
# 时间复杂度: O(n log n) - 排序时间
# 空间复杂度: O(1) - 只使用常数额外空间（不算排序栈空间）
#
# 关键点:
# - 按第二个元素排序是关键（贪心选择最早结束的数对）
# - 与 #435（无重叠区间）和 #452（用最少数量的箭引爆气球）问题思路相似
# - 数对链要求 b < c（严格小于），不是 b <= c
