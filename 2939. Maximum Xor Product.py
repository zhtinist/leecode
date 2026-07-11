"""
LeetCode #2939 - Maximum Xor Product
最大异或乘积
https://leetcode.cn/problems/maximum-xor-product/

给你三个整数 `a` ，`b` 和 `n` ，请你返回 `(a XOR x) * (b XOR x)` 的 最大值 且 `x` 需要满足 `0 <= x < 2^n`。
由于答案可能会很大，返回它对 `10^9 + 7` 取余 后的结果。
注意，`XOR` 是按位异或操作。

示例 1：
输入：a = 12, b = 5, n = 4 输出：98 解释：当 x = 2 时，(a XOR x) = 14 且 (b XOR x) = 7 。所以，(a XOR x) * (b XOR x) = 98 。 98 是所有满足 0 <= x < 2^n 中 (a XOR x) * (b XOR x) 的最大值。
示例 2：
输入：a = 6, b = 7 , n = 5 输出：930 解释：当 x = 25 时，(a XOR x) = 31 且 (b XOR x) = 30 。所以，(a XOR x) * (b XOR x) = 930 。 930 是所有满足 0 <= x < 2^n 中 (a XOR x) * (b XOR x) 的最大值。
示例 3：
输入：a = 1, b = 6, n = 3 输出：12 解释： 当 x = 5 时，(a XOR x) = 4 且 (b XOR x) = 3 。所以，(a XOR x) * (b XOR x) = 12 。 12 是所有满足 0 <= x < 2^n 中 (a XOR x) * (b XOR x) 的最大值。

提示：
`0 <= a, b < 2^50`
`0 <= n <= 50`
"""

from typing import List, Optional


class Solution:
    def maximumXorProduct(self, a: int, b: int, n: int) -> int:
        MOD = 10**9 + 7
        av, bv = 0, 0  # running values of a^x and b^x

        # Process bits from high to low (up to bit 50 since a,b < 2^50, n <= 50)
        for i in range(50, -1, -1):
            ai = (a >> i) & 1
            bi = (b >> i) & 1

            if i >= n:
                # x_i must be 0
                av |= (ai << i)
                bv |= (bi << i)
            else:
                if ai == bi:
                    # Set x_i to make both bits 1 (x_i = 1 - ai)
                    av |= (1 << i)
                    bv |= (1 << i)
                else:
                    # ai != bi: decide who gets the 1
                    # x_i = 0 keeps ai,bi as-is; x_i = 1 flips both
                    # To give 1 to av: if ai=1 keep (x=0), if ai=0 flip (x=1) => x = 1-ai
                    # To give 1 to bv: x = 1-bi
                    give_to_a = (av <= bv)
                    if give_to_a:
                        # give 1 to av, 0 to bv: x_i = 1 - ai
                        av |= (1 << i)
                    else:
                        # give 1 to bv: x_i = 1 - bi
                        bv |= (1 << i)

        return (av % MOD) * (bv % MOD) % MOD



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Bit Manipulation, Math
#
# 解题思路:
# 按位从高到低贪心处理。对于可控位（i < n）：
# - 若 a 和 b 在该位相同，设置 x_i 使两者该位均为1（最大化两者的值）
# - 若不同，该位的1只能给其中一个数，将1分配给当前值较小的数以最大化乘积
# 对于不可控位（i >= n），x_i 固定为0，保持原值。最后乘积取模。
#
# 时间复杂度: O(50) = O(1)
# 空间复杂度: O(1)
#
# 关键点:
# - 高位优先：高位对乘积影响远大于低位
# - 同位相同→双赢（都设为1）；不同→让较小者变大
# - 处理位范围：n只控制低n位，高位x_i固定为0
