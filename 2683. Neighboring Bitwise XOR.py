"""
LeetCode #2683 - Neighboring Bitwise XOR
相邻值的按位异或
https://leetcode.cn/problems/neighboring-bitwise-xor/

下标从 0 开始、长度为 `n` 的数组 `derived` 是由同样长度为 `n` 的原始 二进制数组 `original` 通过计算相邻值的 按位异或（⊕）派生而来。
特别地，对于范围 `[0, n - 1]` 内的每个下标 `i` ：
如果 `i = n - 1` ，那么 `derived[i] = original[i] ⊕ original[0]`
否则 `derived[i] = original[i] ⊕ original[i + 1]`
给你一个数组 `derived` ，请判断是否存在一个能够派生得到 `derived` 的 有效原始二进制数组 `original` 。
如果存在满足要求的原始二进制数组，返回 true ；否则，返回 false 。
二进制数组是仅由 0 和 1 组成的数组。

示例 1：
输入：derived = [1,1,0] 输出：true 解释：能够派生得到 [1,1,0] 的有效原始二进制数组是 [0,1,0] ： derived[0] = original[0] ⊕ original[1] = 0 ⊕ 1 = 1  derived[1] = original[1] ⊕ original[2] = 1 ⊕ 0 = 1 derived[2] = original[2] ⊕ original[0] = 0 ⊕ 0 = 0
示例 2：
输入：derived = [1,1] 输出：true 解释：能够派生得到 [1,1] 的有效原始二进制数组是 [0,1] ： derived[0] = original[0] ⊕ original[1] = 1 derived[1] = original[1] ⊕ original[0] = 1
示例 3：
输入：derived = [1,0] 输出：false 解释：不存在能够派生得到 [1,0] 的有效原始二进制数组。

提示：
`n == derived.length`
`1 <= n <= 10^5`
`derived` 中的值不是 0 就是 1 。
"""

from typing import List, Optional


class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        # XOR all elements of derived.
        # derived[0] = original[0] ^ original[1]
        # derived[1] = original[1] ^ original[2]
        # ...
        # derived[n-1] = original[n-1] ^ original[0]
        # XOR all: derived[0] ^ derived[1] ^ ... ^ derived[n-1]
        # = (original[0]^original[1]) ^ (original[1]^original[2]) ^ ... ^ (original[n-1]^original[0])
        # = 0 (each original[i] appears twice)
        # So total XOR of derived must be 0.
        xor_sum = 0
        for x in derived:
            xor_sum ^= x
        return xor_sum == 0



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Bit Manipulation, Array
#
# 解题思路:
# 将所有derived元素异或起来。由于derived[i]=original[i]^original[(i+1)%n]，
# 所有derived的异或 = 每个original[i]异或两次 = 0。因此如果derived全部异或结果为0则存在有效original。
# 也可以通过构造来验证：设original[0]=0，然后递推original[1..n-1]，最终检查一致性。
#
# 时间复杂度: O(n)
# 空间复杂度: O(1)
#
# 关键点:
# - 核心数学性质：所有derived元素的异或必须为0
# - 每个original元素在derived中出现两次，异或抵消
# - 必要条件也是充分条件
