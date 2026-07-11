"""
LeetCode #788 - Rotated Digits
中文题名：旋转数字
https://leetcode.com/problems/rotated-digits/

X is a good number if after rotating each digit individually by 180 degrees, we get a valid
number that is different from X.  Each digit must be rotated - we cannot choose to
leave it alone.

A number is valid if each digit remains a digit after rotation. 0, 1, and 8 rotate to
themselves; 2 and 5 rotate to each other; 6 and 9 rotate to each other, and the rest of the
numbers do not rotate to any other number and become invalid.

Now given a positive number `N`, how many numbers X from `1` to
`N` are good?

Example:
Input: 10
Output: 4
Explanation:
There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.

Note:

N  will be in range `[1, 10000]`.

【中文翻译】
如果将一个数的每个数字分别旋转 180 度后，我们能得到一个有效且不同于 X 的数，则 X 是一个好数。每个数字都必须旋转，不能选择不旋转。

如果一个数字旋转后仍是一个数字，则它是有效的。0、1 和 8 旋转后仍是自身；2 和 5 互相旋转；6 和 9 互相旋转，其余数字旋转后不是任何数字，因此无效。

现在给定一个正整数 `N`，从 `1` 到 `N` 中有多少个好数？

示例：
输入：10
输出：4
解释：[1, 10] 范围内有四个好数：2, 5, 6, 9。
注意 1 和 10 不是好数，因为它们在旋转后保持不变。

注意：

N 的范围是 `[1, 10000]`。
"""

from typing import List, Optional


class Solution:
    def rotatedDigits(self, N: int) -> int:
        count = 0
        for num in range(1, N + 1):
            s = str(num)
            valid = True
            has_different = False
            for ch in s:
                if ch in '347':
                    valid = False
                    break
                if ch in '2569':
                    has_different = True
            if valid and has_different:
                count += 1
        return count



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 暴力枚举。
# 遍历 1 到 N 的每个数，判断是否是好数：
# - 如果数字中包含 3、4、7 中任意一个，旋转后无效，不是好数。
# - 如果数字中只包含 0、1、8（自旋转数字），旋转后与原数相同，不是好数。
# - 如果数字中包含至少一个 2、5、6、9（会变化的数字），且不包含 3、4、7，则是好数。
# 也可以使用动态规划（数位 DP），但 N <= 10000 时暴力法足够高效。
#
# 时间复杂度: O(N * L)，其中 L 是数字的位数（最多 5），实际为 O(N)
# 空间复杂度: O(1)
#
# 关键点:
# - 好数的两个条件：旋转后有效 AND 旋转后不同于原数
# - 无效数字：3、4、7（旋转后不是数字）
# - 自旋数字：0、1、8（旋转后不变）
# - 变换数字：2、5、6、9（旋转后改变但有效）
# - 必须至少有一个变换数字 + 全部为有效数字
