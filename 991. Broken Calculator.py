"""
LeetCode #991 - Broken Calculator
中文题名：坏了的计算器
https://leetcode.com/problems/broken-calculator/

在显示着数字的坏计算器上，我们可以执行以下两种操作：

双倍（Double）：将显示屏上的数字乘 2；
递减（Decrement）：将显示屏上的数字减 1。

最初，计算器显示数字 X。

返回显示数字 Y 所需的最小操作次数。

示例 1：

输入：X = 2, Y = 3
输出：2
解释：先进行双倍运算，再进行递减运算 {2 -> 4 -> 3}。

示例 2：

输入：X = 5, Y = 8
输出：2
解释：先递减，再双倍 {5 -> 4 -> 8}。

示例 3：

输入：X = 3, Y = 10
输出：3
解释：先双倍，再递减，再双倍 {3 -> 6 -> 5 -> 10}。

示例 4：

输入：X = 1024, Y = 1
输出：1023
解释：执行递减运算 1023 次。

注意：

1 <= X <= 10^9
1 <= Y <= 10^9

【中文翻译】
给定初始数字 X，目标数字 Y，每次操作可以将当前数字乘 2 或减 1，求从 X 到 Y 的最少操作次数。由于乘 2 增长很快，正向贪心不可行，需要反向思考：从 Y 出发，除以 2（当 Y 为偶数）或加 1（当 Y 为奇数），直到到达 X。

"""

from typing import List, Optional


class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        ops = 0
        # Work backwards from target to startValue
        while target > startValue:
            ops += 1
            if target % 2 == 1:
                # Odd number: the last operation must be decrement (inverse: increment)
                target += 1
            else:
                # Even number: the last operation could be double (inverse: divide by 2)
                target //= 2
        # When target <= startValue, only need decrement (inverse: increment) operations
        return ops + (startValue - target)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 反向贪心（从 Y 逆向回到 X）：
# 1. 正向操作（X -> Y）：可做乘 2 或减 1。
# 2. 逆向操作（Y -> X）：可做除 2 或加 1。
# 3. 核心贪心策略（反向）：
#    - 当 Y > X 时：
#      * 如果 Y 是偶数，最优操作是除以 2（因为除以 2 减少的幅度最大）。
#      * 如果 Y 是奇数，先加 1 使其变为偶数（逆向视角下只能先加 1）。
#    - 当 Y <= X 时，只需要不断加 1（逆向）即正向不断减 1。
# 4. 为什么反向贪心是正确的：
#    - 正向时减 1 操作应该在乘 2 之前（避免浪费乘法效果）。
#    - 逆向时，除 2 是最高效的减小方式，优先进行除 2。
#    - 奇数时不能直接除 2，需要先加 1 变成偶数。
#
# 时间复杂度: O(log Y)，每次 Y 至少减半（除 2 或接近除 2）
# 空间复杂度: O(1)，仅使用常量空间
#
# 关键点:
# - 正向 BFS/DP 会超时（数字范围到 10^9），必须逆向思维
# - 逆向操作选择：偶数直接除 2（最优），奇数加 1 变偶数
# - 当 Y <= X 时，剩余操作数 = X - Y（纯减 1）
# - 贪心正确性：除 2 比减 1 收敛快得多，优先使用
