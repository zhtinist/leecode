"""
LeetCode #907 - Sum of Subarray Minimums
中文题名：子数组的最小值之和
https://leetcode.com/problems/sum-of-subarray-minimums/

Given an array of integers `A`, find the sum of `min(B)`, where
`B` ranges over every (contiguous) subarray of `A`.

Since the answer may be large, return the answer modulo `10^9 +
7`.

Example 1:

Input: [3,1,2,4]
Output: 17
Explanation: Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4].
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.  Sum is 17.

Note:

`1 <= A.length <= 30000`

`1 <= A[i] <= 30000`

【中文翻译】
给定整数数组 `A`，求 `min(B)` 的总和，其中 `B` 为 `A` 的每个（连续）子数组。

由于答案可能很大，因此返回答案模 `10^9 + 7` 的结果。

示例 1：

输入：[3,1,2,4]
输出：17
解释：子数组为 [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]。
最小值为 3, 1, 2, 4, 1, 1, 2, 1, 1, 1。和为 17。

"""

from typing import List, Optional


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)

        # left[i] = 以 i 结尾向左延伸，有多少个连续元素 >= arr[i]（包含 arr[i] 自身）
        left = [1] * n
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            left[i] = i - stack[-1] if stack else i + 1
            stack.append(i)

        # right[i] = 以 i 开头向右延伸，有多少个连续元素 >= arr[i]（包含 arr[i] 自身）
        # 注意：用 >= 而非 >，避免重复计算相等元素
        right = [1] * n
        stack.clear()
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            right[i] = stack[-1] - i if stack else n - i
            stack.append(i)

        ans = 0
        for i in range(n):
            ans = (ans + arr[i] * left[i] * right[i]) % MOD

        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用单调栈（Monotonic Stack）计算每个元素作为"子数组最小值"的贡献次数。
# 对于每个 arr[i]，找到：
# - left[i]：以 i 结尾向左延伸，有多少个连续元素 >= arr[i]
#   （即上一个严格小于 arr[i] 的位置到 i 的距离）
# - right[i]：以 i 开头向右延伸，有多少个连续元素 >= arr[i]
#   （即下一个小于等于 arr[i] 的位置到 i 的距离）
#
# 注意左右两侧一个用 strict less `>`，一个用 non-strict `>=`，避免重复计算。
# 那么 arr[i] 作为最小值的子数组个数 = left[i] * right[i]。
# arr[i] 的总贡献 = arr[i] * left[i] * right[i]。
# 最终答案 = sum(贡献) % MOD。
#
# 例如 arr = [3,1,2,4]：
# i=0(arr=3): left=1, right=1 → 贡献 3
# i=1(arr=1): left=2, right=3 → 贡献 6
# i=2(arr=2): left=1, right=2 → 贡献 4
# i=3(arr=4): left=1, right=1 → 贡献 4
# 总和 = 17
#
# 时间复杂度: O(N) — 三次遍历，单调栈均摊 O(1)
# 空间复杂度: O(N) — left/right/stack 均为 O(N)
#
# 关键点:
# - 使用贡献法（Contribution Method）：不枚举子数组，而是计算每个元素贡献多少次
# - 单调栈两边严格/非严格的处理是消除重复计数的关键
# - 注意大数取模 MOD = 10^9 + 7
