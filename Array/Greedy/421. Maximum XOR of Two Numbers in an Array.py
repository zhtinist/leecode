"""
LeetCode #421 - Maximum XOR of Two Numbers in an Array
中文题名：数组中两个数的最大异或值
https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

Given a non-empty array of numbers, a0, a1, a2,
&hellip; , an-1, where 0 <= ai < 231.

Find the maximum result of ai XOR aj, where 0 <= i, j
< n.

Could you do this in O(n) runtime?

Example:

Input: [3, 10, 5, 25, 2, 8]

Output: 28

Explanation: The maximum result is 5 ^ 25 = 28.

【中文翻译】
给定一个非空数组，包含数字 a0, a1, a2, …, an-1，其中 0 <= ai < 2^31。
求出 ai XOR aj 的最大结果，其中 0 <= i, j < n。
能否以 O(n) 时间复杂度完成？

示例：
    输入：[3, 10, 5, 25, 2, 8]
    输出：28
    解释：最大结果是 5 ^ 25 = 28。
"""

from typing import List, Optional


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        max_result = 0
        mask = 0

        # Build answer bit by bit from MSB to LSB (31 bits)
        for bit in range(30, -1, -1):
            mask |= (1 << bit)
            prefixes = set()

            # Collect all prefixes (top bits) with current mask
            for num in nums:
                prefixes.add(num & mask)

            # Greedy: try to set this bit to 1 in the answer
            candidate = max_result | (1 << bit)

            for prefix in prefixes:
                # If prefix ^ candidate exists in the set, this bit can be 1
                if (prefix ^ candidate) in prefixes:
                    max_result = candidate
                    break

        return max_result


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 位运算 + 贪心 + 哈希集合。从最高位到最低位逐位构建答案。
#
# 核心原理：a ^ b = c 等价于 a ^ c = b。
# 对于每一位，我们尝试让结果的这一位为 1，然后检查是否存在两个数的前缀异或等于
# 这个候选值。
#
# 具体步骤：
# 1. 维护 mask（当前考虑的高位部分）和 max_result（当前能得到的最大异或值）
# 2. 对于每一位（从第 30 位到第 0 位，最高位为符号位不考虑）：
#    - 更新 mask，加入当前位
#    - 收集所有数的当前前缀（num & mask）
#    - 假设结果这一位可以为 1：candidate = max_result | (1 << bit)
#    - 遍历前缀集合，检查 (prefix ^ candidate) 是否也在集合中
#      若存在，说明有两个数的前缀异或等于 candidate，这一位可以设为 1
#
# 时间复杂度: O(N * 31) ≈ O(N) — 固定 31 次遍历
# 空间复杂度: O(N) — 哈希集合存储 N 个前缀
#
# 关键点:
# - a ^ b = c => a ^ c = b，这是判断的关键恒等式
# - 从高位向低位贪心构建，保证结果最大
# - mask 用于截取高位前缀
# - 也可用 Trie 解决，但 Hash Set 方法更简洁
