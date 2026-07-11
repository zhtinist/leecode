"""
LeetCode #1007 - Minimum Domino Rotations For Equal Row
中文题名：行相等的最少多米诺旋转
https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/

In a row of dominoes, `A[i]` and `B[i]` represent the top and bottom
halves of the `i`-th domino.  (A domino is a tile with two numbers from 1 to
6 - one on each half of the tile.)

We may rotate the `i`-th domino, so that `A[i]` and `B[i]`
swap values.

Return the minimum number of rotations so that all the values in `A` are the same,
or all the values in `B` are the same.

If it cannot be done, return `-1`.

Example 1:

Input: A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]
Output: 2
Explanation:
The first figure represents the dominoes as given by A and B: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.

Example 2:

Input: A = [3,5,1,2,3], B = [3,6,3,3,4]
Output: -1
Explanation:
In this case, it is not possible to rotate the dominoes to make one row of values equal.

Note:

`1 <= A[i], B[i] <= 6`

`2 <= A.length == B.length <= 20000`

【中文翻译】
在一排多米诺骨牌中，`A[i]` 和 `B[i]` 分别代表第 `i` 个多米诺骨牌的上半部分和下半部分。（多米诺骨牌是一种有两个数字（从 1 到 6）的牌——一面一个数字。）

我们可以旋转第 `i` 个多米诺骨牌，使得 `A[i]` 和 `B[i]` 的值交换。

返回使得 `A` 中所有值都相同，或 `B` 中所有值都相同所需的最少旋转次数。

如果无法做到，返回 `-1`。

示例 1：

输入：A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]
输出：2
解释：
第一个图表示按 A 和 B 给出的多米诺骨牌：在我们进行任何旋转之前。
如果我们旋转第二个和第四个多米诺骨牌，我们可以使顶部行中的每个值都等于 2，如第二个图所示。

示例 2：

输入：A = [3,5,1,2,3], B = [3,6,3,3,4]
输出：-1
解释：
在这种情况下，无法通过旋转多米诺骨牌来使一行值相同。

注意：

`1 <= A[i], B[i] <= 6`

`2 <= A.length == B.length <= 20000`

"""

from typing import List, Optional


class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        def check(x: int) -> int:
            rot_a = rot_b = 0
            for i in range(len(A)):
                if A[i] != x and B[i] != x:
                    return float('inf')
                if A[i] != x:
                    rot_a += 1
                if B[i] != x:
                    rot_b += 1
            return min(rot_a, rot_b)

        ans = min(check(A[0]), check(B[0]))
        return ans if ans != float('inf') else -1










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 要使一行中所有值相同，目标值必须是 A[0] 或 B[0]（因为第 0 个骨牌必须有一面等于目标值）。
# 定义辅助函数 check(x)，检查将所有骨牌的一面变为 x 所需的最小旋转次数：
# - 遍历每个骨牌 (A[i], B[i])，如果两面都不等于 x，则不可能实现，返回无穷大。
# - 如果 A[i] != x 则需要旋转使 A[i] 变成 x（rot_a++），同理如果 B[i] != x 需要 rot_b++。
# - 返回 min(rot_a, rot_b)：选择旋转上方还是下方的最小次数。
# 对 A[0] 和 B[0] 分别调用 check，取最小值。如果最小值为无穷大则返回 -1。
#
# 时间复杂度: O(n) - 最多遍历两次数组（check(A[0]) 和 check(B[0])）
# 空间复杂度: O(1) - 只使用常数额外空间
#
# 关键点:
# - 目标值只能是 A[0] 或 B[0]，因为第一个骨牌至少有一面等于目标值
# - rot_a 统计的是上方需要旋转的次数，rot_b 统计下方需要旋转的次数
# - 取 min(rot_a, rot_b) 是因为可以选择统一上方或统一下方
