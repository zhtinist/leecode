"""
LeetCode #3012 - Minimize Length of Array Using Operations
通过操作使数组长度最小
https://leetcode.cn/problems/minimize-length-of-array-using-operations/

给你一个下标从 0 开始的整数数组 `nums` ，它只包含 正 整数。
你的任务是通过进行以下操作 任意次 （可以是 0 次） 最小化 `nums` 的长度：
在 `nums` 中选择 两个不同 的下标 `i` 和 `j` ，满足 `nums[i] > 0` 且 `nums[j] > 0` 。
将结果 `nums[i] % nums[j]` 插入 `nums` 的结尾。
将 `nums` 中下标为 `i` 和 `j` 的元素删除。
请你返回一个整数，它表示进行任意次操作以后 `nums` 的 最小长度 。

示例 1：
输入：nums = [1,4,3,1] 输出：1 解释：使数组长度最小的一种方法是： 操作 1 ：选择下标 2 和 1 ，插入 nums[2] % nums[1] 到数组末尾，得到 [1,4,3,1,3] ，然后删除下标为 2 和 1 的元素。 nums 变为 [1,1,3] 。 操作 2 ：选择下标 1 和 2 ，插入 nums[1] % nums[2] 到数组末尾，得到 [1,1,3,1] ，然后删除下标为 1 和 2 的元素。 nums 变为 [1,1] 。 操作 3 ：选择下标 1 和 0 ，插入 nums[1] % nums[0] 到数组末尾，得到 [1,1,0] ，然后删除下标为 1 和 0 的元素。 nums 变为 [0] 。 nums 的长度无法进一步减小，所以答案为 1 。 1 是可以得到的最小长度。
示例 2：
输入：nums = [5,5,5,10,5] 输出：2 解释：使数组长度最小的一种方法是： 操作 1 ：选择下标 0 和 3 ，插入 nums[0] % nums[3] 到数组末尾，得到 [5,5,5,10,5,5] ，然后删除下标为 0 和 3 的元素。 nums 变为 [5,5,5,5] 。 操作 2 ：选择下标 2 和 3 ，插入 nums[2] % nums[3] 到数组末尾，得到 [5,5,5,5,0] ，然后删除下标为 2 和 3 的元素。 nums 变为 [5,5,0] 。 操作 3 ：选择下标 0 和 1 ，插入 nums[0] % nums[1] 到数组末尾，得到 [5,5,0,0] ，然后删除下标为 0 和 1 的元素。 nums 变为 [0,0] 。 nums 的长度无法进一步减小，所以答案为 2 。 2 是可以得到的最小长度。
示例 3：
输入：nums = [2,3,4] 输出：1 解释：使数组长度最小的一种方法是： 操作 1 ：选择下标 1 和 2 ，插入 nums[1] % nums[2] 到数组末尾，得到 [2,3,4,3] ，然后删除下标为 1 和 2 的元素。 nums 变为 [2,3] 。 操作 2 ：选择下标 1 和 0 ，插入 nums[1] % nums[0] 到数组末尾，得到 [2,3,1] ，然后删除下标为 1 和 0 的元素。 nums 变为 [1] 。 nums 的长度无法进一步减小，所以答案为 1 。 1 是可以得到的最小长度。

提示：
`1 <= nums.length <= 10^5`
`1 <= nums[i] <= 10^9`
"""

from typing import List, Optional


class Solution:
    def minimumArrayLength(self, nums: List[int]) -> int:
        """
        Find the minimum element m and its frequency.
        If any other element is NOT divisible by m, we can create a smaller
        number (x % m < m), eventually getting m=1, reducing to length 1.
        Otherwise, all elements are multiples of m. Each pair of m's can
        become a 0. Answer = (cnt_m + 1) // 2.
        """
        m = min(nums)
        cnt = nums.count(m)

        for x in nums:
            if x % m != 0:
                return 1

        return (cnt + 1) // 2



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Array, Math, Number Theory
#
# 解题思路:
# 找到数组中的最小值 m 及其出现次数 cnt。
# 如果存在某个元素不能被 m 整除（x % m != 0），则可以通过取模操作创建一个比 m 更小的数，
# 逐步减小最小值直到产生 1，最终可以将数组缩减到长度为 1。
# 如果所有元素都能被 m 整除，则每次操作只能产生 m 的倍数或 0。两个 m 配对产生一个 0，
# m 与倍数配对也产生 0。剩余的非零元素即为未配对的 m，答案为 (cnt + 1) // 2。
#
# 时间复杂度: O(n)，遍历数组找最小值和计数
# 空间复杂度: O(1)
#
# 关键点:
# - 取模操作的关键：如果 a < b，a % b = a（相当于消除 b）；如果 a >= b，a % b < b
# - 能否产生比当前最小值更小的数，决定了能否继续缩减
# - 全倍数情况下的配对策略：两个 m 产生一个 0，长度减半向上取整
