"""
LeetCode #375 - Guess Number Higher or Lower II
中文题名：猜数字大小 II
https://leetcode.com/problems/guess-number-higher-or-lower-ii/

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number
I picked.

Every time you guess wrong, I'll tell you whether the number I picked is higher or
lower.

However, when you guess a particular number x, and you guess wrong, you pay $x. You
win the game when you guess the number I picked.

Example:

n = 10, I pick 8.

First round:  You guess 5, I tell you that it's higher. You pay $5.
Second round: You guess 7, I tell you that it's higher. You pay $7.
Third round:  You guess 9, I tell you that it's lower. You pay $9.

Game over. 8 is the number I picked.

You end up paying $5 + $7 + $9 = $21.

Given a particular n &ge; 1, find out how much money you need to have to
guarantee a win.

【中文翻译】
我们正在玩一个猜谜游戏。游戏规则如下：

我从 1 到 n 中挑选一个数字。你需要猜出我挑选的数字。

每次你猜错时，我会告诉你，我挑选的数字是更高还是更低。

然而，当你猜某个数字 x 并且猜错时，你需要支付 $x。当你猜中我挑选的数字时，游戏胜利。

示例：

n = 10，我挑选了 8。

第一轮：你猜 5，我告诉你更高。你支付 $5。
第二轮：你猜 7，我告诉你更高。你支付 $7。
第三轮：你猜 9，我告诉你更低。你支付 $9。

游戏结束。8 是我挑选的数字。

你最终支付了 $5 + $7 + $9 = $21。

给定一个 n >= 1，求出你需要准备多少钱才能确保获胜。
"""

from typing import List, Optional


class Solution:
    def getMoneyAmount(self, n: int) -> int:
        # dp[i][j] = 在区间 [i, j] 内保证猜中数字所需的最小金额
        dp = [[0] * (n + 2) for _ in range(n + 2)]

        # 按区间长度从小到大计算
        for length in range(2, n + 1):
            for i in range(1, n - length + 2):
                j = i + length - 1
                dp[i][j] = float('inf')
                # 尝试区间 [i, j] 内的每一个数字作为第一次猜测
                for k in range(i, j + 1):
                    # 猜 k：如果猜小了需要准备的金额是 dp[i][k-1]
                    # 如果猜大了需要准备的金额是 dp[k+1][j]
                    # 为保险起见，取最坏情况（max），加上本次猜错的代价 k
                    cost = k + max(dp[i][k - 1], dp[k + 1][j])
                    dp[i][j] = min(dp[i][j], cost)

        return dp[1][n]











# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 本题是极小化极大（Minimax）动态规划问题，目标是在最坏情况下花最少的钱保证猜中。
# 对于区间 [i, j]，我们不知道目标数字是什么，需要找到一种策略使得无论目标数字是多少，
# 所需的总花费尽可能小。
#
# 定义 dp[i][j] = 在区间 [i, j] 内保证猜中所需的最小金额。
# 状态转移：对于每个可能的猜测 k（i <= k <= j）：
# - 如果猜小了，目标数字在 [i, k-1]，我们需要 dp[i][k-1] 的金额
# - 如果猜大了，目标数字在 [k+1, j]，我们需要 dp[k+1][j] 的金额
# - 为保险起见，我们要取两者的最大值（最坏情况）
# - 加上本次猜错支付的金额 k
# - 在所有可能的 k 中，我们选择总花费最小的策略
# 即 dp[i][j] = min(k + max(dp[i][k-1], dp[k+1][j])) for all k in [i, j]
#
# 按区间长度从小到大计算，最终答案为 dp[1][n]。
#
# 时间复杂度: O(N^3) - N 最大为 200，三层循环共约 1.3M 次运算，可以接受
# 空间复杂度: O(N^2) - 二维 DP 数组
#
# 关键点:
# - Minimax 思想：在最坏情况下选择最优策略
# - dp[i][k-1] 和 dp[k+1][j] 取 max 是"最坏情况"，外层 min 是"最优策略"
# - 区间长度为 1 时不需要猜，dp[i][i] = 0（base case）
# - dp 数组多开两列（n+2）以避免 k-1 或 k+1 越界
