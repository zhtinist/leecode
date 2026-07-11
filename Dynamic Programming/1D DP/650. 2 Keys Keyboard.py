"""
LeetCode #650 - 2 Keys Keyboard
中文题名：只有两个键的键盘
https://leetcode.com/problems/2-keys-keyboard/

Initially on a notepad only one character 'A' is present. You can perform two
operations on this notepad for each step:

`Copy All`: You can copy all the characters present on the notepad (partial
copy is not allowed).

`Paste`: You can paste the characters which are copied last time.

Given a number `n`. You have to get exactly `n` 'A' on
the notepad by performing the minimum number of steps permitted. Output the minimum number
of steps to get `n` 'A'.

Example 1:

Input: 3
Output: 3
Explanation:
Intitally, we have one character 'A'.
In step 1, we use Copy All operation.
In step 2, we use Paste operation to get 'AA'.
In step 3, we use Paste operation to get 'AAA'.

Note:

The `n` will be in the range [1, 1000].

【中文翻译】
最初在一个记事本上只有一个字符 'A'。你每次可以对这个记事本执行两种操作：

「全选复制」(Copy All)：你可以复制记事本上当前所有的字符（不允许部分复制）。

「粘贴」(Paste)：你可以粘贴上一次复制的字符。

给定一个数字 `n`。你需要使用最少的操作次数，在记事本上恰好得到 `n` 个 'A'。输出得到 `n` 个 'A' 的最少操作次数。

示例 1：

输入：3
输出：3
解释：
最初，我们只有一个字符 'A'。
在第 1 步，我们使用「全选复制」操作。
在第 2 步，我们使用「粘贴」操作得到 'AA'。
在第 3 步，我们使用「粘贴」操作得到 'AAA'。

注意：

`n` 的取值范围是 [1, 1000]。
"""

from typing import List, Optional


class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0

        steps = 0
        factor = 2

        while n > 1:
            while n % factor == 0:
                steps += factor
                n //= factor
            factor += 1

        return steps











# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 问题本质是求 n 的质因数之和。可以通过分解质因数来理解：
# 当 n > 1 时，如果要得到 n 个 A，需要先有 n/factor 个 A（其中 factor 是 n 的一个因子），
# 然后执行"全选复制"(1步) 和 (factor-1) 次"粘贴"，共 factor 步。
# 因此，n 的最小步数等于所有质因数之和。
# 证明：假设一次复制粘贴序列生成 k 个 A，则总共需要 1 + (k-1) = k 步。
# 所以最优策略是将 n 分解为质因数，每个质因数 p 贡献 p 步。
# 本质上是一个质因数分解问题。
#
# 时间复杂度: O(sqrt(n)) - 质因数分解的最坏情况
# 空间复杂度: O(1) - 仅使用常数额外空间
#
# 关键点:
# - 将问题转化为质因数分解：最少步数 = 所有质因数之和
# - 例如 n=12: 分解为 2*2*3, 步数 = 2+2+3 = 7
# - 动态规划也可解：dp[i] = min(dp[j] + i/j) for j dividing i
# - 质因数分解法是 O(sqrt(n))，比 DP 的 O(n^2) 或 O(n*sqrt(n)) 更优
