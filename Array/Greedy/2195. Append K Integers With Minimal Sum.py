"""
LeetCode #2195 - Append K Integers With Minimal Sum
向数组中追加 K 个整数
https://leetcode.cn/problems/append-k-integers-with-minimal-sum/

给你一个整数数组 `nums` 和一个整数 `k` 。请你向 `nums` 中追加 `k` 个 未 出现在 `nums` 中的、互不相同 的 正 整数，并使结果数组的元素和 最小 。
返回追加到 `nums` 中的 `k` 个整数之和。

示例 1：
输入：nums = [1,4,25,10,25], k = 2 输出：5 解释：在该解法中，向数组中追加的两个互不相同且未出现的正整数是 2 和 3 。 nums 最终元素和为 1 + 4 + 25 + 10 + 25 + 2 + 3 = 70 ，这是所有情况中的最小值。 所以追加到数组中的两个整数之和是 2 + 3 = 5 ，所以返回 5 。
示例 2：
输入：nums = [5,6], k = 6 输出：25 解释：在该解法中，向数组中追加的两个互不相同且未出现的正整数是 1 、2 、3 、4 、7 和 8 。 nums 最终元素和为 5 + 6 + 1 + 2 + 3 + 4 + 7 + 8 = 36 ，这是所有情况中的最小值。 所以追加到数组中的两个整数之和是 1 + 2 + 3 + 4 + 7 + 8 = 25 ，所以返回 25 。

提示：
`1 <= nums.length <= 10^5`
`1 <= nums[i], k <= 10^9`
"""

from typing import List, Optional


class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        """
        排序 + 贪心：将 nums 去重排序后，从小到大扫描数组。
        在相邻数字之间的空隙中取尽可能多的小正整数（这些数不在 nums 中），
        直到取满 k 个数为止。空隙中可取的数用等差数列求和公式计算。
        """
        nums = sorted(set(nums))  # 去重并排序
        ans = 0
        prev = 0  # 上一个已检查过的数，初始为 0（下一个候选是 1）

        for num in nums:
            # 在 prev+1 到 num-1 之间的数都可以选
            if num - prev > 1:
                gap = num - prev - 1          # 空隙中可选的数字个数
                take = min(gap, k)            # 实际取多少个数
                # 等差数列求和：prev+1 到 prev+take
                first = prev + 1
                last = prev + take
                ans += (first + last) * take // 2
                k -= take
                if k == 0:
                    return ans
            prev = num

        # 如果 nums 中的空隙都取完了还没凑够 k 个数，
        # 则从 max(nums)+1 开始继续取 k 个最小的正整数
        if k > 0:
            first = prev + 1
            last = prev + k
            ans += (first + last) * k // 2

        return ans


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Array, Math, Sorting
#
# 解题思路:
# 1. 题目要求选出 k 个不在 nums 中的正整数，使它们的和最小。
#    显然应该从小到大选，即依次检查 1, 2, 3, ... 跳过 nums 中已有的数。
# 2. 优化方法：将 nums 去重排序后，扫描 nums 中每个数，检查当前数与上一个数
#    之间有多少个"空隙"（即可选的连续正整数范围）。
# 3. 对于每个空隙 [prev+1, num-1]，用等差数列求和公式一次性算出
#    从中取 min(空隙大小, 剩余需要的 k) 个数的和。
# 4. 如果扫完 nums 中所有空隙后仍不足 k 个，则从 max(nums)+1 开始
#    继续取剩余数量。
# 5. 返回累加的和。
#
# 时间复杂度: O(n log n)
# - 排序和去重 O(n log n)，后续扫描 O(n)。
#
# 空间复杂度: O(n) 或 O(1)
# - 排序需要 O(n) 额外空间（若使用 sorted 创建新列表）。
#
# 关键点:
# - 去重很重要，因为 nums 中可能有重复元素。
# - 使用等差数列求和公式 ((首项 + 末项) * 项数 // 2) 避免逐个累加。
# - 扫描完 nums 后要处理尾部剩余情况。
