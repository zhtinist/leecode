"""
LeetCode #2844 - Minimum Operations to Make a Special Number
生成特殊数字的最少操作
https://leetcode.cn/problems/minimum-operations-to-make-a-special-number/

给你一个下标从 0 开始的字符串 `num` ，表示一个非负整数。
在一次操作中，您可以选择 `num` 的任意一位数字并将其删除。请注意，如果你删除 `num` 中的所有数字，则 `num` 变为 `0`。
返回最少需要多少次操作可以使 `num` 变成特殊数字。
如果整数 `x` 能被 `25` 整除，则该整数 `x` 被认为是特殊数字。

示例 1：
输入：num = "2245047" 输出：2 解释：删除数字 num[5] 和 num[6] ，得到数字 "22450" ，可以被 25 整除。 可以证明要使数字变成特殊数字，最少需要删除 2 位数字。
示例 2：
输入：num = "2908305" 输出：3 解释：删除 num[3]、num[4] 和 num[6] ，得到数字 "2900" ，可以被 25 整除。 可以证明要使数字变成特殊数字，最少需要删除 3 位数字。
示例 3：
输入：num = "10" 输出：1 解释：删除 num[0] ，得到数字 "0" ，可以被 25 整除。 可以证明要使数字变成特殊数字，最少需要删除 1 位数字。

提示
`1 <= num.length <= 100`
`num` 仅由数字 `'0'` 到 `'9'` 组成
`num` 不含任何前导零
"""

from typing import List, Optional


class Solution:
    def minimumOperations(self, num: str) -> int:
        n = len(num)
        ans = n  # worst case: delete all digits to get "0"
        # Try to find "00", "25", "50", "75" as suffix
        for target in ("00", "25", "50", "75"):
            j = len(target) - 1
            ops = 0
            for i in range(n - 1, -1, -1):
                if num[i] == target[j]:
                    j -= 1
                    if j < 0:
                        ans = min(ans, ops)
                        break
                else:
                    ops += 1
        # Also consider leaving a single '0'
        zero_count = num.count('0')
        if zero_count > 0:
            ans = min(ans, n - 1)  # delete all except one '0'
        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Math, String, Enumeration
#
# 解题思路:
# 能被25整除的数字必须以"00"、"25"、"50"或"75"结尾。从右向左扫描，尝试匹配每种结尾模式。
# 遇到不匹配的字符就计数为删除操作，找到完整匹配时更新最小操作数。
# 另外，如果字符串中有'0'，可以删除除一个'0'外的所有数字得到0（也能被25整除）。
#
# 时间复杂度: O(n)
# 空间复杂度: O(1)
#
# 关键点:
# - 被25整除等价于以00/25/50/75结尾（或结果为0）
# - 从右到左逐个匹配目标结尾，不匹配的字符视为删除
# - 单独处理保留一个'0'的情况（删除其余所有字符）
