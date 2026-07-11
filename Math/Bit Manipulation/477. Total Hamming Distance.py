"""
LeetCode #477 - Total Hamming Distance
中文题名：汉明距离总和
https://leetcode.com/problems/total-hamming-distance/

The Hamming
distance between two integers is the number of positions at which the corresponding bits
are different.

Now your job is to find the total Hamming distance between all pairs of the given numbers.

Example:

Input: 4, 14, 2

Output: 6

Explanation: In binary representation, the 4 is 0100, 14 is 1110, and 2 is 0010 (just
showing the four bits relevant in this case). So the answer will be:
HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.

Note:

Elements of the given array are in the range of `0 ` to `10^9`

Length of the array will not exceed `10^4`.

【中文翻译】
两个整数的汉明距离是指它们对应二进制位不同的位置数目。

现在你的任务是计算给定数组中所有数字对之间的汉明距离总和。

示例：
    输入：4, 14, 2
    输出：6
    解释：二进制表示中，4 是 0100，14 是 1110，2 是 0010（仅展示相关的四位）。
    所以答案为：汉明距离(4,14) + 汉明距离(4,2) + 汉明距离(14,2) = 2 + 2 + 2 = 6。

注意：
    数组元素范围在 0 到 10^9 之间。
    数组长度不超过 10^4。
"""

from typing import List, Optional


class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0

        # Check each of the 32 bit positions (since nums[i] <= 10^9 < 2^30)
        for bit in range(31):
            # Count how many numbers have a 1 at this bit position
            ones = sum((num >> bit) & 1 for num in nums)
            zeros = n - ones

            # Each pair of (1, 0) contributes 1 to the total Hamming distance
            total += ones * zeros

        return total



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 按位独立计算。对于每一位（共 31 位，因为 10^9 < 2^30），统计所有数字在该位上为 1 的个数 ones。
# 该位上为 0 的个数即为 zeros = n - ones。在这一位上，每一对 (1, 0) 的组合都会产生 1 的汉明距离贡献。
# 因此该位的总贡献为 ones * zeros。将所有位的贡献累加即得答案。这样做避免了 O(n^2) 的两两比较。
#
# 时间复杂度: O(31 * N) = O(N)，其中 N 是数组长度。常数 31 是因为最多检查 31 个二进制位
# 空间复杂度: O(1) — 仅使用常数额外空间
#
# 关键点:
# - 逐位计算而非逐对计算，将 O(n^2) 优化到 O(n)
# - 每一位的贡献 = (该位为 1 的个数) * (该位为 0 的个数)
# - 数据范围 10^9 < 2^30，故需要检查 31 位（0-30 位，第 31 位为符号位不需要）
