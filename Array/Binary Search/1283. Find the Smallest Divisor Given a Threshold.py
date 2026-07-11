"""
LeetCode #1283 - Find the Smallest Divisor Given a Threshold
中文题名：使结果不超过阈值的最小除数
https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/

Given an array of integers `nums` and an integer `threshold`,
we will choose a positive integer divisor and divide all the array by it and
sum the result of the division. Find the smallest divisor such that the
result mentioned above is less than or equal to `threshold`.

Each result of division is rounded to the nearest integer greater than
or equal to that element. (For example: 7/3 = 3 and 10/2 = 5).

It is guaranteed that there will be an answer.

Example 1:

Input: nums = [1,2,5,9], threshold = 6
Output: 5
Explanation: We can get a sum to 17 (1+2+5+9) if the divisor is 1.
If the divisor is 4 we can get a sum to 7 (1+1+2+3) and if the divisor is 5 the sum will be 5 (1+1+1+2).

Example 2:

Input: nums = [2,3,5,7,11], threshold = 11
Output: 3

Example 3:

Input: nums = [19], threshold = 5
Output: 4

Constraints:

`1 <= nums.length <= 5 * 10^4`

`1 <= nums[i] <= 10^6`

`nums.length <= threshold <= 10^6`

【中文翻译】
给定一个整数数组 nums 和一个整数 threshold，我们需要选择一个正整数除数，将数组中所有数除以它，并对除法结果求和。找到最小的除数，使得上述结果小于或等于 threshold。

每个除法结果都向上取整（例如：7/3 = 3，10/2 = 5）。

保证一定有答案。

示例 1：

输入：nums = [1,2,5,9], threshold = 6
输出：5
解释：如果除数为 1，和为 17（1+2+5+9）。
如果除数为 4，和为 7（1+1+2+3），如果除数为 5，和为 5（1+1+1+2）。

示例 2：

输入：nums = [2,3,5,7,11], threshold = 11
输出：3

示例 3：

输入：nums = [19], threshold = 5
输出：4

约束条件：

1 <= nums.length <= 5 * 10^4
1 <= nums[i] <= 10^6
nums.length <= threshold <= 10^6
"""

from typing import List, Optional


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        import math

        def sum_division(divisor: int) -> int:
            total = 0
            for num in nums:
                total += (num + divisor - 1) // divisor
            return total

        left, right = 1, max(nums)

        while left < right:
            mid = (left + right) // 2
            if sum_division(mid) <= threshold:
                right = mid
            else:
                left = mid + 1

        return left










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用二分查找。除数越大，除法结果之和越小，满足单调性，
# 因此可以使用二分查找来确定最小的满足条件的除数。
# 搜索范围为 [1, max(nums)]：
# 1. 定义辅助函数计算给定除数下的除法结果之和（向上取整）。
# 2. 如果当前除数的和 <= threshold，则尝试更小的除数（right = mid）。
# 3. 如果当前除数的和 > threshold，则需要更大的除数（left = mid + 1）。
# 4. 最终 left 即为满足条件的最小除数。
# 向上取整公式：(num + divisor - 1) // divisor 等价于 ceil(num / divisor)。
#
# 时间复杂度: O(n * log(max(nums))) - 二分查找 O(log max)，每次需要 O(n) 计算和
# 空间复杂度: O(1) - 仅使用常量额外空间
#
# 关键点:
# - 二分查找的单调性：除数越大和越小
# - 上界为 max(nums)，因为当除数 >= max(nums) 时，每个元素除完向上取整都为 1
# - 向上取整的整数实现：(a + b - 1) // b
