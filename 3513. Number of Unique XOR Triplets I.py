"""
LeetCode #3513 - Number of Unique XOR Triplets I
不同 XOR 三元组的数目 I
https://leetcode.cn/problems/number-of-unique-xor-triplets-i/

给你一个长度为 `n` 的整数数组 `nums`，其中 `nums` 是范围 `[1, n]` 内所有数的 排列 。
XOR 三元组 定义为三个元素的异或值 `nums[i] XOR nums[j] XOR nums[k]`，其中 `i <= j <= k`。
返回所有可能三元组 `(i, j, k)` 中 不同 的 XOR 值的数量。
排列 是一个集合中所有元素的重新排列。

示例 1：

输入： nums = [1,2]
输出： 2
解释：
所有可能的 XOR 三元组值为：
`(0, 0, 0) → 1 XOR 1 XOR 1 = 1`
`(0, 0, 1) → 1 XOR 1 XOR 2 = 2`
`(0, 1, 1) → 1 XOR 2 XOR 2 = 1`
`(1, 1, 1) → 2 XOR 2 XOR 2 = 2`
不同的 XOR 值为 `{1, 2}`，因此输出为 2。
示例 2：

输入： nums = [3,1,2]
输出： 4
解释：
可能的 XOR 三元组值包括：
`(0, 0, 0) → 3 XOR 3 XOR 3 = 3`
`(0, 0, 1) → 3 XOR 3 XOR 1 = 1`
`(0, 0, 2) → 3 XOR 3 XOR 2 = 2`
`(0, 1, 2) → 3 XOR 1 XOR 2 = 0`
不同的 XOR 值为 `{0, 1, 2, 3}`，因此输出为 4。

提示：
`1 <= n == nums.length <= 10^5`
`1 <= nums[i] <= n`
`nums` 是从 `1` 到 `n` 的整数的一个排列。
"""

from typing import List, Optional


class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
        # For n >= 3, answer is smallest power of 2 >= n (actually > highest element)
        # Since nums is permutation of [1, n], max value is n
        # All XOR values from 0 to 2^k - 1 are achievable where k = n.bit_length()
        return 1 << n.bit_length()



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Bit Manipulation, Array, Math
#
# 解题思路:
# 1. nums 是 [1, n] 的排列
# 2. 当 n >= 3 时，可以生成 [0, 2^k - 1] 范围内的所有 XOR 值，
#    其中 k = bit_length(n)（n 的二进制位数）
# 3. 理由：
#    - a ^ a ^ b = b → 所有元素值本身可达
#    - 三个不同元素 XOR 可以生成剩余值
#    - 有足够的数构建线性基覆盖所有 k 位二进制数
# 4. n <= 2 时答案 = n（只能生成元素本身）
#
# 时间复杂度: O(1)
# 空间复杂度: O(1)
#
# 关键点:
# - 充分大的排列可以生成所有小于 2^k 的 XOR 值
# - n=1, n=2 是特殊情况需要直接返回
# - bit_length() 是 Python 获取二进制位数的方法
