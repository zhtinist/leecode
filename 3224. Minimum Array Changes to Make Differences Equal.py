"""
LeetCode #3224 - Minimum Array Changes to Make Differences Equal
使差值相等的最少数组改动次数
https://leetcode.cn/problems/minimum-array-changes-to-make-differences-equal/

给你一个长度为 `n` 的整数数组 `nums` ，`n` 是 偶数 ，同时给你一个整数 `k` 。
你可以对数组进行一些操作。每次操作中，你可以将数组中 任一 元素替换为 `0` 到 `k` 之间的 任一 整数。
执行完所有操作以后，你需要确保最后得到的数组满足以下条件：
存在一个整数 `X` ，满足对于所有的 `(0 <= i < n)` 都有 `abs(a[i] - a[n - i - 1]) = X` 。
请你返回满足以上条件 最少 修改次数。

示例 1：

输入：nums = [1,0,1,2,4,3], k = 4
输出：2
解释：
我们可以执行以下操作：
将 `nums[1]` 变为 2 ，结果数组为 `nums = [1,2,1,2,4,3]` 。
将 `nums[3]` 变为 3 ，结果数组为 `nums = [1,2,1,3,4,3]` 。
整数 `X` 为 2 。
示例 2：

输入：nums = [0,1,2,3,3,6,5,4], k = 6
输出：2
解释：
我们可以执行以下操作：
将 `nums[3]` 变为 0 ，结果数组为 `nums = [0,1,2,0,3,6,5,4]` 。
将 `nums[4]` 变为 4 ，结果数组为 `nums = [0,1,2,0,4,6,5,4]` 。
整数 `X` 为 4 。

提示：
`2 <= n == nums.length <= 10^5`
`n` 是偶数。
`0 <= nums[i] <= k <= 10^5`
"""

from typing import List, Optional


class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        n = len(nums)
        diff = [0] * (k + 2)  # 差分数组

        for i in range(n // 2):
            a, b = nums[i], nums[n - 1 - i]
            d = abs(a - b)
            # 修改一个元素能达到的最大差值
            max_one = max(a, k - a, b, k - b)

            # 默认所有 X 需要 2 次修改
            diff[0] += 2
            diff[k + 1] -= 2

            # [0, max_one] 区间只需 1 次修改（减 1）
            diff[0] -= 1
            diff[max_one + 1] += 1

            # X == d 时只需 0 次修改（再减 1）
            diff[d] -= 1
            diff[d + 1] += 1

        ans = float('inf')
        cur = 0
        for x in range(k + 1):
            cur += diff[x]
            ans = min(ans, cur)
        return ans










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Hash Table, Prefix Sum
#
# 解题思路:
# 对于每对对称元素 (a, b)，当前差值 d = |a-b|。目标差值 X：
# - X == d 时：0 次修改
# - X in [0, max_one] 且 X != d 时：1 次修改（其中 max_one = max(a, k-a, b, k-b)）
# - X > max_one 时：2 次修改
# 使用差分数组优化：对每对元素，先默认所有 X 需要 2 次修改，
# 然后对 [0, max_one] 区间减 1，再对 X == d 减 1。
# 最后扫描差分数组的前缀和，取最小值即为答案。
#
# 时间复杂度: O(n + k)
# 空间复杂度: O(k)
#
# 关键点:
# - 差分数组技巧避免对每对元素的每个 X 都 O(k) 处理
# - 修改一个元素能达成的差值范围由 0 到 max(element, k-element) 决定
