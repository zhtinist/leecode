"""
LeetCode #377 - Combination Sum IV
中文题名：组合总和 Ⅳ
https://leetcode.com/problems/combination-sum-iv/

Given an integer array with all positive numbers and no duplicates, find the number of
possible combinations that add up to a positive integer target.

Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.

Follow up:

What if negative numbers are allowed in the given array?

How does it change the problem?

What limitation we need to add to the question to allow negative numbers?

Credits:

Special thanks to @pbrother for adding this
problem and creating all test cases.

【中文翻译】
给定一个由正整数组成且不存在重复数字的数组，找出所有可能组合的个数，使得这些组合中的数字相加等于一个给定的正整数 target。

示例：

nums = [1, 2, 3]
target = 4

所有可能的组合方式有：
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

请注意，顺序不同的序列被视为不同的组合。

因此输出为 7。

进阶：

如果给定的数组中含有负数会怎么样？

问题将如何变化？

我们需要在题目中添加什么限制来允许负数出现？

致谢：

特别感谢 @pbrother 添加此问题并创建所有测试用例。
"""

from typing import List, Optional


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # dp[i] = 和为 i 的组合数（顺序不同的序列视为不同组合）
        dp = [0] * (target + 1)
        dp[0] = 1  # 和为 0 的组合只有一种：空序列（不选任何数字）

        for i in range(1, target + 1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i - num]

        return dp[target]











# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 本题名为"组合总和"，但实际上计算的是"排列数"（顺序不同的序列视为不同组合）。
# 属于完全背包问题中"求排列数"的变体。
#
# 使用动态规划：
# - 定义 dp[i] = 和为 i 的不同序列（排列）的数量
# - 初始化 dp[0] = 1，表示和为 0 的空序列有一种
# - 对于每个和 i（从 1 到 target）：
#   遍历所有数字 num，如果 i >= num，则 dp[i] += dp[i - num]
#   这表示在所有和为 (i-num) 的序列末尾添加 num，形成和为 i 的新序列
#
# 注意循环顺序：
# - 外层循环 target（和的值），内层循环 nums（可选数字）
# - 这种顺序保证考虑了元素的顺序（排列）
# - 如果反过来（外层 nums，内层 target），则只计算组合（不考虑顺序）
#
# 时间复杂度: O(N * target) - N 是 nums 的长度
# 空间复杂度: O(target) - 一维 DP 数组
#
# 关键点:
# - 外层 target / 内层 nums 的循环顺序 = 求排列数（顺序有关）
# - 外层 nums / 内层 target 的循环顺序 = 求组合数（顺序无关）
# - dp[0] = 1 是这类背包问题的标准 base case
# - 进阶问题：如果允许负数，可能出现无限种组合（因为可以无限抵消），
#   需要限制每个数字的使用次数或最大序列长度
