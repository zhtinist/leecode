"""
LeetCode #2601 - Prime Subtraction Operation
质数减法运算
https://leetcode.cn/problems/prime-subtraction-operation/

给你一个下标从 0 开始的整数数组 `nums` ，数组长度为 `n` 。
你可以执行无限次下述运算：
选择一个之前未选过的下标 `i` ，并选择一个 严格小于 `nums[i]` 的质数 `p` ，从 `nums[i]` 中减去 `p` 。
如果你能通过上述运算使得 `nums` 成为严格递增数组，则返回 `true` ；否则返回 `false` 。
严格递增数组 中的每个元素都严格大于其前面的元素。

示例 1：
输入：nums = [4,9,6,10] 输出：true 解释： 在第一次运算中：选择 i = 0 和 p = 3 ，然后从 nums[0] 减去 3 ，nums 变为 [1,9,6,10] 。 在第二次运算中：选择 i = 1 和 p = 7 ，然后从 nums[1] 减去 7 ，nums 变为 [1,2,6,10] 。 第二次运算后，nums 按严格递增顺序排序，因此答案为 true 。
示例 2：
输入：nums = [6,8,11,12] 输出：true 解释：nums 从一开始就按严格递增顺序排序，因此不需要执行任何运算。
示例 3：
输入：nums = [5,8,3] 输出：false 解释：可以证明，执行运算无法使 nums 按严格递增顺序排序，因此答案是 false 。

提示：
`1 <= nums.length <= 1000`
`1 <= nums[i] <= 1000`
`nums.length == n`
"""

from typing import List, Optional


class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        # precompute primes up to 1000
        max_val = 1000
        is_prime = [True] * (max_val + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(max_val ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, max_val + 1, i):
                    is_prime[j] = False
        primes = [i for i in range(2, max_val + 1) if is_prime[i]]

        prev = 0  # previous value after adjustment
        for x in nums:
            # we need to choose a prime p < x such that x - p > prev
            # equivalently, p < x - prev
            # find the largest prime p < x - prev (or minimal x - p > prev)
            # Strategy: try to subtract the largest possible prime to make x as small
            # as possible while still > prev
            found = False
            for p in reversed(primes):
                if p < x and x - p > prev:
                    prev = x - p
                    found = True
                    break
            if not found:
                # can't subtract, check if x itself > prev
                if x > prev:
                    prev = x
                else:
                    return False
        return True



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Array, Math, Binary Search, Number Theory
#
# 解题思路:
# 贪心策略：从左到右处理数组，对每个数尝试减去一个最大可能的质数，
# 使得结果严格大于前一个数且尽可能小。预处理1000以内的所有质数，
# 对每个数二分查找或倒序遍历质数列表，选择能减去的最大质数。
#
# 时间复杂度: O(n * P) 其中P是质数数量(~168)
# 空间复杂度: O(P)
#
# 关键点:
# - 贪心策略：让每个数尽可能小但严格大于前一个数
# - 预处理质数表，对每个数倒序遍历找最大可减质数
# - 如果无法减去任何质数，检查原数本身是否满足递增条件
