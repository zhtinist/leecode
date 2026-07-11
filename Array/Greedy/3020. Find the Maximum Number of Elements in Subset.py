"""
LeetCode #3020 - Find the Maximum Number of Elements in Subset
子集中元素的最大数量
https://leetcode.cn/problems/find-the-maximum-number-of-elements-in-subset/

给你一个 正整数 数组 `nums` 。
你需要从数组中选出一个满足下述条件的子集：
你可以将选中的元素放置在一个下标从 0 开始的数组中，并使其遵循以下模式：`[x, x^2, x^4, ..., x^k/2, x^k, x^k/2, ..., x^4, x^2, x]`（注意，`k` 可以是任何 非负 的 2 的幂）。例如，`[2, 4, 16, 4, 2]` 和 `[3, 9, 3]` 都符合这一模式，而 `[2, 4, 8, 4, 2]` 则不符合。
返回满足这些条件的子集中，元素数量的 最大值 。

示例 1：
输入：nums = [5,4,1,2,2] 输出：3 解释：选择子集 {4,2,2} ，将其放在数组 [2,4,2] 中，它遵循该模式，且 2^2 == 4 。因此答案是 3 。
示例 2：
输入：nums = [1,3,2,4] 输出：1 解释：选择子集 {1}，将其放在数组 [1] 中，它遵循该模式。因此答案是 1 。注意我们也可以选择子集 {2} 、{4} 或 {3} ，可能存在多个子集都能得到相同的答案。

提示：
`2 <= nums.length <= 10^5`
`1 <= nums[i] <= 10^9`
"""

from typing import List, Optional


class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        """
        Pattern: [x, x^2, x^4, ..., x^k, ..., x^4, x^2, x] where k is a power of 2.
        For each starting x, greedily extend: need 2 copies of each level
        except 1 copy for the peak. Handle x=1 separately.
        """
        from collections import Counter

        count = Counter(nums)
        ans = 0

        # Special case: x = 1
        if 1 in count:
            c = count[1]
            # Pattern of all 1s: length must be odd (symmetric with peak)
            ans = c if c % 2 == 1 else c - 1

        for x in count:
            if x == 1:
                continue

            length = 1  # at minimum, just the peak = x
            power = x

            # Greedily extend the pattern
            while count.get(power, 0) >= 2:
                nxt = power * power
                if nxt > 10**9:  # max value constraint
                    break
                if count.get(nxt, 0) >= 1:
                    length += 2
                    power = nxt
                else:
                    break

            ans = max(ans, length)

        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Hash Table, Enumeration
#
# 解题思路:
# 统计每个数字的出现频率。对于 x=1 特殊处理（所有 1 都是幂等元素），最大长度为不超过 count[1] 的最大奇数。
# 对于其他 x，贪心地从 x 开始逐层扩展：每层需要 2 个该层元素，下一层需要至少 1 个。
# 每成功扩展一层长度 +2，直到无法继续（平方值超出范围或数量不足）。
#
# 时间复杂度: O(U * log log M)，U 为不同元素数，每次平方增长极快
# 空间复杂度: O(U)，哈希表存储频率
#
# 关键点:
# - 模式的指数是 2 的幂次：1, 2, 4, 8, ...，每步对值求平方
# - 对称模式要求两侧各有一个副本（共 2 个），但峰值只需 1 个
# - x=1 是特殊情况：1 的任意次幂都是 1，模式退化为一串 1
