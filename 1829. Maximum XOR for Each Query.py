"""
LeetCode #1829 - Maximum XOR for Each Query
中文题名：每个查询的最大异或值
https://leetcode.com/problems/maximum-xor-for-each-query/

You are given a sorted array `nums` of `n` non-negative integers and an integer `maximumBit`. You want to perform the following query `n` times:

Find a non-negative integer `k < 2maximumBit` such that `nums[0] XOR nums[1] XOR ... XOR nums[nums.length-1] XOR k` is maximized. `k` is the answer to the `ith` query.

Remove the last element from the current array `nums`.

Return an array `answer`, where `answer[i]` is the answer to the `ith` query.

Example 1:

Input: nums = [0,1,1,3], maximumBit = 2
Output: [0,3,2,3]
Explanation: The queries are answered as follows:
1st query: nums = [0,1,1,3], k = 0 since 0 XOR 1 XOR 1 XOR 3 XOR 0 = 3.
2nd query: nums = [0,1,1], k = 3 since 0 XOR 1 XOR 1 XOR 3 = 3.
3rd query: nums = [0,1], k = 2 since 0 XOR 1 XOR 2 = 3.
4th query: nums = [0], k = 3 since 0 XOR 3 = 3.

Example 2:

Input: nums = [2,3,4,7], maximumBit = 3
Output: [5,2,6,5]
Explanation: The queries are answered as follows:
1st query: nums = [2,3,4,7], k = 5 since 2 XOR 3 XOR 4 XOR 7 XOR 5 = 7.
2nd query: nums = [2,3,4], k = 2 since 2 XOR 3 XOR 4 XOR 2 = 7.
3rd query: nums = [2,3], k = 6 since 2 XOR 3 XOR 6 = 7.
4th query: nums = [2], k = 5 since 2 XOR 5 = 7.

Example 3:

Input: nums = [0,1,2,2,5,7], maximumBit = 3
Output: [4,3,6,4,6,7]

Constraints:

`nums.length == n`

`1 <= n <= 105`

`1 <= maximumBit <= 20`

`0 <= nums[i] < 2maximumBit`

`nums`​​​ is sorted in ascending order.

【中文翻译】

给定一个已排序的非负整数数组 `nums` 和一个整数 `maximumBit`。执行以下查询n次：

1. 找出一个非负整数 `k < 2^maximumBit`，使得 `nums[0] XOR nums[1] XOR ... XOR nums[nums.length-1] XOR k` 最大化。k为第i次查询的答案。
2. 从当前数组中移除最后一个元素。

返回答案数组 `answer`，其中 `answer[i]` 是第i次查询的答案。

示例：
输入：nums = [0,1,1,3], maximumBit = 2
输出：[0,3,2,3]
解释：第1次：全数组XOR=3，k=0使结果=3最大；第2次：去掉3后XOR=0，k=3使结果=3最大；等等。

"""

from typing import List, Optional


class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        xor_total = 0
        for num in nums:
            xor_total ^= num

        mask = (1 << maximumBit) - 1
        n = len(nums)
        answer = [0] * n

        for i in range(n):
            # k = xor_total XOR mask 使结果最大化
            answer[i] = xor_total ^ mask
            xor_total ^= nums[n - 1 - i]  # 移除最后一个元素

        return answer










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 对于异或运算，要使结果最大化，需要让每一位尽可能为1。
# 给定mask = (1 << maximumBit) - 1（所有maximumBit位都是1），
# 当前异或和与mask异或可以得到该范围内的最大值（因为 X XOR k = mask 时最大）。
# 每次查询后移除最后一个元素，可以反向计算：先算全数组XOR，然后逆序移除。
#
# 时间复杂度: O(N)，一次遍历计算总异或，一次遍历填充答案
# 空间复杂度: O(1)，除了输出数组外使用常数空间
#
# 关键点:
# - k = xor_total ^ mask 可使每位都达到1（在maximumBit范围内最大）
# - 从后向前移除元素，每次移除末尾元素即异或掉该值
# - mask = (1 << maximumBit) - 1
