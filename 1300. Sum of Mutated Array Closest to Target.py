"""
LeetCode #1300 - Sum of Mutated Array Closest to Target
中文题名：转变数组后最接近目标值的数组和
https://leetcode.com/problems/sum-of-mutated-array-closest-to-target/

Given an integer array `arr` and a target value `target`,
return the integer `value` such that when we change all the
integers larger than `value` in the given array to be equal to `value`, the
sum of the array gets as close as possible (in absolute difference) to `target`.

In case of a tie, return the minimum such integer.

Notice that the answer is not neccesarilly a number from `arr`.

Example 1:

Input: arr = [4,9,3], target = 10
Output: 3
Explanation: When using 3 arr converts to [3, 3, 3] which sums 9 and that's the optimal answer.

Example 2:

Input: arr = [2,3,5], target = 10
Output: 5

Example 3:

Input: arr = [60864,25176,27249,21296,20204], target = 56803
Output: 11361

Constraints:

`1 <= arr.length <= 10^4`

`1 <= arr[i], target <= 10^5`

【中文翻译】
给定一个整数数组 arr 和一个目标值 target，返回一个整数值 value，
使得将数组中所有大于 value 的值变成 value 后，数组的和最接近 target（绝对值差最小）。
如果有多个答案，返回最小的那个。注意答案不一定是 arr 中的数字。

示例 1：

输入：arr = [4,9,3], target = 10
输出：3
解释：当选择 value=3 时，数组变为 [3,3,3]，和为 9，这是最接近 10 的方案。

示例 2：

输入：arr = [2,3,5], target = 10
输出：5

示例 3：

输入：arr = [60864,25176,27249,21296,20204], target = 56803
输出：11361
"""

from typing import List, Optional


class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()
        n = len(arr)
        prefix = 0
        for i in range(n):
            # If we set value = arr[i], remaining (n-i) elements become arr[i]
            # Total = prefix + arr[i] * (n - i)
            # We want this >= target - (some threshold)
            remaining = n - i
            # The value x that makes prefix + x * remaining == target
            # x = (target - prefix) / remaining
            # If x <= arr[i], the optimal value is in this range
            ideal = (target - prefix) / remaining
            if ideal <= arr[i]:
                # Try floor and ceil of ideal
                lo = int(ideal)
                hi = lo + 1
                # But also consider arr[i] if ideal was larger than previous arr[i-1]
                candidates = []
                if lo >= (arr[i - 1] if i > 0 else 0):
                    candidates.append(lo)
                if hi <= arr[i]:
                    candidates.append(hi)
                # Also check arr[i] itself
                candidates.append(arr[i])
                best_val = -1
                best_diff = float('inf')
                for v in candidates:
                    s = prefix + v * remaining
                    diff = abs(s - target)
                    if diff < best_diff or (diff == best_diff and v < best_val):
                        best_diff = diff
                        best_val = v
                return best_val
            prefix += arr[i]
        # If target is larger than sum of all elements, return max element
        return arr[-1]










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 先对数组排序。遍历数组，计算前缀和。对于每个位置 i，假设我们选择 value 使得
# 前 i 个元素保持不变，后面 n-i 个元素变为 value。此时总和 = prefix + value * (n-i)。
# 令其等于 target，解得 ideal = (target - prefix) / (n-i)。
# 如果 ideal <= arr[i]，则最优值在 ideal 的 floor/ceil 以及 arr[i] 之间产生。
# 如果 target 大于所有元素的和，返回最大元素。
#
# 时间复杂度: O(N log N) — 排序主导
# 空间复杂度: O(1) 或 O(N) — 取决于排序是否原地
#
# 关键点:
# - 排序后，对于每个位置可以 O(1) 计算假设 value 在该区间的理想值
# - 最优值只需在 floor(ideal) 和 ceil(ideal) 之间选择
# - 注意边界：value 可以不是 arr 中的元素
