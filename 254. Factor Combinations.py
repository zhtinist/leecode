"""
LeetCode #254 - Factor Combinations
中文题名：因子的组合
https://leetcode.com/problems/factor-combinations/

Numbers can be regarded as product of its factors. For example,

8 = 2 x 2 x 2;
= 2 x 4.

Write a function that takes an integer *n* and return all possible combinations of its
factors.

Note:

You may assume that *n* is always positive.

Factors should be greater than 1 and less than *n*.

Example 1:

Input: `1`
Output: []

Example 2:

Input: `37`
Output:[]

Example 3:

Input: `12`
Output:
[
[2, 6],
[2, 2, 3],
[3, 4]
]

Example 4:

Input: `32`
Output:
[
[2, 16],
[2, 2, 8],
[2, 2, 2, 4],
[2, 2, 2, 2, 2],
[2, 4, 4],
[4, 8]
]

【中文翻译】
数字可以看作是其因子的乘积。例如，

8 = 2 x 2 x 2;
= 2 x 4.

编写一个函数，接收整数 *n*，返回所有可能的因子组合。

注意：

你可以假设 *n* 始终为正整数。

因子应大于 1 且小于 *n*。

示例 1：

输入：`1`
输出：[]

示例 2：

输入：`37`
输出：[]

示例 3：

输入：`12`
输出：
[
[2, 6],
[2, 2, 3],
[3, 4]
]

示例 4：

输入：`32`
输出：
[
[2, 16],
[2, 2, 8],
[2, 2, 2, 4],
[2, 2, 2, 2, 2],
[2, 4, 4],
[4, 8]
]
"""

from typing import List, Optional


class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        res = []

        def backtrack(start: int, target: int, path: List[int]):
            # 从 start 开始尝试因子，避免重复
            # 因子的范围是 [start, sqrt(target)]
            i = start
            while i * i <= target:
                if target % i == 0:
                    # 找到一组因子分解
                    res.append(path + [i, target // i])
                    # 继续递归分解 target // i
                    backtrack(i, target // i, path + [i])
                i += 1

        backtrack(2, n, [])
        return res


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: Yes
#
# 解题思路：
# 使用回溯法（DFS）。从因子 2 开始，尝试所有可能的因子组合。
# 对于每个可被整除的因子 i，先记录当前组合 [..., i, n//i]，
# 然后继续递归分解 n//i。关键是用 start 参数保证因子序列非递减，
# 从而避免生成重复组合（如 [2,2,3] 和 [2,3,2]）。
#
# 时间复杂度: O(n^(log n)) — 与因子的数量有关，较难精确表达
# 空间复杂度: O(log n) — 递归栈深度
#
# 关键点：
# - start 参数确保因子非递减，避免重复
# - 遍历上限为 sqrt(target)
# - 收集当前 i 和 n//i 作为一组分解，再递归分解 n//i
