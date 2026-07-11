"""
LeetCode #1558 - Minimum Numbers of Function Calls to Make Target Array
中文题名：得到目标数组的最少函数调用次数
https://leetcode.com/problems/minimum-numbers-of-function-calls-to-make-target-array/


Your task is to form an integer array `nums` from an initial array of
zeros `arr` that is the same size as `nums`.

Return the minimum number of function calls to make `nums` from
`arr`.

The answer is guaranteed to fit in a 32-bit signed integer.

Example 1:

Input: nums = [1,5]
Output: 5
Explanation: Increment by 1 (second element): [0, 0] to get [0, 1] (1 operation).
Double all the elements: [0, 1] -> [0, 2] -> [0, 4] (2 operations).
Increment by 1 (both elements)  [0, 4] -> [1, 4] -> [1, 5] (2 operations).
Total of operations: 1 + 2 + 2 = 5.

Example 2:

Input: nums = [2,2]
Output: 3
Explanation: Increment by 1 (both elements) [0, 0] -> [0, 1] -> [1, 1] (2 operations).
Double all the elements: [1, 1] -> [2, 2] (1 operation).
Total of operations: 2 + 1 = 3.

Example 3:

Input: nums = [4,2,5]
Output: 6
Explanation: (initial)[0,0,0] -> [1,0,0] -> [1,0,1] -> [2,0,2] -> [2,1,2] -> [4,2,4] -> [4,2,5](nums).

Example 4:

Input: nums = [3,2,2,4]
Output: 7

Example 5:

Input: nums = [2,4,8,16]
Output: 8

Constraints:

`1 <= nums.length <= 10^5`

`0 <= nums[i] <= 10^9`

【中文翻译】
有一个初始全零数组 arr。可以执行两种操作：
1. 对任意一个元素加 1。
2. 将数组中每个元素乘以 2。
返回使 arr 变成 nums 的最少操作次数。

示例 1：
输入：nums = [1,5]
输出：5
解释：[0,0] -> [0,1] -> [0,2] -> [0,4] -> [0,5] -> [1,5]。

示例 2：
输入：nums = [2,2]
输出：3

示例 3：
输入：nums = [4,2,5]
输出：6
"""

from typing import List, Optional


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # Count total +1 operations (set bits) and max *2 operations
        total_adds = 0
        max_mults = 0
        for num in nums:
            if num == 0:
                continue
            total_adds += bin(num).count('1')  # number of +1 ops
            max_mults = max(max_mults, num.bit_length() - 1)  # number of *2 ops
        return total_adds + max_mults



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 逆向思考：从目标数组反向操作到全零数组。
# 乘以 2 的操作对所有元素同时进行，因此 *2 的次数 = 所有元素二进制位数的最大值 - 1。
# +1 操作每个元素独立，每个 1 比特需要一次 +1 操作（考虑到进位）。
# 总操作次数 = 所有元素二进制中 1 的总数 + 最大二进制位数 - 1。
#
# 时间复杂度: O(N * log M) — M 为元素最大值
# 空间复杂度: O(1)
#
# 关键点:
# - 逆向操作：从目标推导到全零
# - *2 对所有元素同时进行，取最大值
# - +1 每个 1 比特需要一次












