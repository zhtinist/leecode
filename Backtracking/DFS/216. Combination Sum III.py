"""
LeetCode #216 - Combination Sum III
中文题名：组合总和 III
https://leetcode.com/problems/combination-sum-iii/

Find all possible combinations of *k* numbers that add up to a number
*n*, given that only numbers from 1 to 9 can be used and each combination
should be a unique set of numbers.

Note:

All numbers will be positive integers.

The solution set must not contain duplicate combinations.

Example 1:

Input: *k* = 3, *n* = 7
Output: [[1,2,4]]

Example 2:

Input: *k* = 3, *n* = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]

【中文翻译】
找出所有相加之和为 *n* 的 *k* 个数的组合，且满足下列条件：

注意：

所有数字均为正整数。

解集不能包含重复的组合。

示例 1：

输入：*k* = 3，*n* = 7
输出：[[1,2,4]]

示例 2：

输入：*k* = 3，*n* = 9
输出：[[1,2,6], [1,3,5], [2,3,4]]
"""

from typing import List, Optional


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []

        def backtrack(start, remaining, path):
            if len(path) == k:
                if remaining == 0:
                    result.append(path[:])
                return
            if remaining < 0:
                return

            for num in range(start, 10):
                # Pruning: if the smallest possible sum exceeds remaining
                if remaining < num * (k - len(path)):
                    break
                path.append(num)
                backtrack(num + 1, remaining - num, path)
                path.pop()

        backtrack(1, n, [])
        return result


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用回溯法（Backtracking）在 1-9 中选择 k 个不重复的数字，使其和等于 n。
# 1. 从 start=1 开始，每次选择一个数字 num 加入当前组合 path。
# 2. 递归时 start 设为 num+1，确保数字不重复且组合递增（自动去重）。
# 3. 当 path 长度达到 k 时：
#    - 若 remaining == 0，找到一个有效组合，加入结果。
#    - 否则直接返回。
# 4. 若 remaining < 0，说明当前和已超过 n，剪枝返回。
# 5. 剪枝优化：若剩余数字即使全取最小值 num 仍超过 remaining，
#    则后续数字更大更不可能，提前 break 结束循环。
#
# 时间复杂度: O(C(9,k) * k)，即组合数乘以复制路径的开销
# 空间复杂度: O(k)，递归栈深度和 path 存储
#
# 关键点:
# - 候选集固定为 1-9，规模很小（最多 C(9,4)=126 种），回溯完全可行
# - start 递增确保组合内部递增，无需额外去重逻辑
# - 剪枝条件 remaining < num * (k - len(path)) 可大幅减少无效搜索
