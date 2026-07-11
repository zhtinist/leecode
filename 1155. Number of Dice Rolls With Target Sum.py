"""
LeetCode #1155 - Number of Dice Rolls With Target Sum
中文题名：掷骰子的N种方法
https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/

You have `d` dice, and each die has `f` faces numbered `1, 2, ...,
f`.

Return the number of possible ways (out of `fd` total ways)
modulo `10^9 + 7` to roll the dice so the sum of the face up
numbers equals `target`.

Example 1:

Input: d = 1, f = 6, target = 3
Output: 1
Explanation:
You throw one die with 6 faces.  There is only one way to get a sum of 3.

Example 2:

Input: d = 2, f = 6, target = 7
Output: 6
Explanation:
You throw two dice, each with 6 faces.  There are 6 ways to get a sum of 7:
1+6, 2+5, 3+4, 4+3, 5+2, 6+1.

Example 3:

Input: d = 2, f = 5, target = 10
Output: 1
Explanation:
You throw two dice, each with 5 faces.  There is only one way to get a sum of 10: 5+5.

Example 4:

Input: d = 1, f = 2, target = 3
Output: 0
Explanation:
You throw one die with 2 faces.  There is no way to get a sum of 3.

Example 5:

Input: d = 30, f = 30, target = 500
Output: 222616187
Explanation:
The answer must be returned modulo 10^9 + 7.

Constraints:

`1 <= d, f <= 30`

`1 <= target <= 1000`

【中文翻译】
你有 d 个骰子，每个骰子有 f 个面，分别标有 1, 2, ..., f。

返回投掷骰子的所有可能方法（共 f^d 种）中，使得骰子正面朝上的数字总和等于 target 的方法数目，结果对 10^9 + 7 取模。

示例 1：

输入：d = 1, f = 6, target = 3
输出：1
解释：你掷一个有 6 个面的骰子。只有一种方法得到和为 3。

示例 2：

输入：d = 2, f = 6, target = 7
输出：6
解释：你掷两个骰子，每个有 6 个面。有 6 种方法得到和为 7：1+6, 2+5, 3+4, 4+3, 5+2, 6+1。

示例 3：

输入：d = 2, f = 5, target = 10
输出：1
解释：你掷两个骰子，每个有 5 个面。只有一种方法得到和为 10：5+5。

示例 4：

输入：d = 1, f = 2, target = 3
输出：0
解释：你掷一个有 2 个面的骰子。无法得到和为 3。

示例 5：

输入：d = 30, f = 30, target = 500
输出：222616187
解释：答案需要对 10^9 + 7 取模。

约束条件：

`1 <= d, f <= 30`

`1 <= target <= 1000`
"""

from typing import List, Optional


class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        MOD = 10 ** 9 + 7

        # dp[i][j] = number of ways to get sum j using i dice
        dp = [[0] * (target + 1) for _ in range(d + 1)]
        dp[0][0] = 1  # 0 dice, sum 0 = 1 way

        for i in range(1, d + 1):
            for j in range(1, target + 1):
                # Sum over face values 1..f
                for k in range(1, f + 1):
                    if j >= k:
                        dp[i][j] = (dp[i][j] + dp[i - 1][j - k]) % MOD

        return dp[d][target]










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 经典背包类动态规划问题。定义 dp[i][j] 表示用 i 个骰子投掷出总和为 j 的方法数：
# 1. 初始状态：dp[0][0] = 1（0 个骰子总和为 0 有 1 种方法）
# 2. 状态转移：对于第 i 个骰子，它可以投出 1 到 f 的任意值 k。
#    如果当前目标总和 j >= k，则 dp[i][j] += dp[i-1][j-k]。
#    即用 i-1 个骰子投出 j-k 的方法数，加上第 i 个骰子投出 k。
# 3. 最终答案：dp[d][target] % MOD。
#
# 可以空间优化为 O(target)：使用两个一维数组交替（滚动数组），
# 因为 dp[i] 只依赖于 dp[i-1]。
#
# 时间复杂度: O(d * target * f) - 三重循环
# 空间复杂度: O(d * target) - DP 表格（可优化至 O(target)）
#
# 关键点:
# - MOD = 10^9 + 7，每次加法后取模防止溢出
# - dp 表行数为 d+1（骰子数量），列数为 target+1（目标总和）
# - 这是一个正向递推的 DP，从少到多骰子逐步构建
# - 提前剪枝：如果 target < d 或 target > d*f，可直接返回 0
