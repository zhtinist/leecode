"""
LeetCode #1946 - Largest Number After Mutating Substring
子字符串突变后可能得到的最大整数
https://leetcode.cn/problems/largest-number-after-mutating-substring/

给你一个字符串 `num` ，该字符串表示一个大整数。另给你一个长度为 `10` 且 下标从 0  开始 的整数数组 `change` ，该数组将 `0-9` 中的每个数字映射到另一个数字。更规范的说法是，数字 `d` 映射为数字 `change[d]` 。
你可以选择 突变  `num` 的任一子字符串。突变 子字符串意味着将每位数字 `num[i]` 替换为该数字在 `change` 中的映射（也就是说，将 `num[i]` 替换为 `change[num[i]]`）。
请你找出在对 `num` 的任一子字符串执行突变操作（也可以不执行）后，可能得到的 最大整数 ，并用字符串表示返回。
子字符串 是字符串中的一个连续序列。

示例 1：
输入：num = "132", change = [9,8,5,0,3,6,4,2,6,8] 输出："832" 解释：替换子字符串 "1"： - 1 映射为 change[1] = 8 。 因此 "132" 变为 "832" 。 "832" 是可以构造的最大整数，所以返回它的字符串表示。
示例 2：
输入：num = "021", change = [9,4,3,5,7,2,1,9,0,6] 输出："934" 解释：替换子字符串 "021"： - 0 映射为 change[0] = 9 。 - 2 映射为 change[2] = 3 。 - 1 映射为 change[1] = 4 。 因此，"021" 变为 "934" 。 "934" 是可以构造的最大整数，所以返回它的字符串表示。
示例 3：
输入：num = "5", change = [1,4,7,5,3,2,5,6,9,4] 输出："5" 解释："5" 已经是可以构造的最大整数，所以返回它的字符串表示。

提示：
`1 <= num.length <= 10^5`
`num` 仅由数字 `0-9` 组成
`change.length == 10`
`0 <= change[d] <= 9`
"""

from typing import List, Optional


class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        """
        Greedy: from left to right, find the first position where mutation
        increases the digit, then mutate a contiguous substring as long as
        it doesn't decrease.
        """
        s = list(num)
        i = 0
        n = len(s)

        # Find first position where mutating increases the digit
        while i < n and int(s[i]) >= change[int(s[i])]:
            i += 1

        # Mutate contiguous substring while it doesn't decrease
        while i < n and int(s[i]) <= change[int(s[i])]:
            s[i] = str(change[int(s[i])])
            i += 1

        return "".join(s)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Array, String
#
# 解题思路:
# 贪心策略：要使数字最大，应该从高位开始突变。
# 1. 从左到右找到第一个突变后变大的位置（change[d] > d）
# 2. 从该位置开始，连续突变直到突变会变小为止
# 3. 注意：如果某位突变后数值不变（change[d] == d），也可以继续突变，
#    因为这不会使数字变小
# 关键是不能突变前面的高位使其变小，也不能在突变区间之后继续突变（因为
# 子字符串必须是连续的）。
#
# 时间复杂度: O(N)，N 为字符串长度
# 空间复杂度: O(N)，将字符串转为列表
#
# 关键点:
# - 找到第一个 change[d] > d 的位置作为突变起点
# - 连续突变直到 change[d] < d
# - change[d] == d 时不中断（不会减小）
