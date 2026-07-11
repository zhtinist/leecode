"""
LeetCode #1004 - Max Consecutive Ones III
中文题名：最大连续1的个数 III
https://leetcode.com/problems/max-consecutive-ones-iii/

Given an array `A` of 0s and 1s, we may change up to `K` values
from 0 to 1.

Return the length of the longest (contiguous) subarray that contains only 1s.

Example 1:

Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
Output: 6
Explanation:
[1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.

Example 2:

Input: A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
Output: 10
Explanation:
[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.

Note:

`1 <= A.length <= 20000`

`0 <= K <= A.length`

`A[i]` is `0` or `1`

【中文翻译】
给定一个由 `0` 和 `1` 组成的数组 `A`，我们可以最多将 `K` 个 `0` 翻转为 `1`。

返回包含最多连续 `1` 的最长（连续）子数组的长度。

示例 1：

输入：A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
输出：6
解释：
[1,1,1,0,0,1,1,1,1,1,1]
粗体数字是从 0 翻转为 1 的数字。最长的子数组已用下划线标出。

示例 2：

输入：A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
输出：10
解释：
[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
粗体数字是从 0 翻转为 1 的数字。最长的子数组已用下划线标出。

注意：

`1 <= A.length <= 20000`

`0 <= K <= A.length`

`A[i]` 是 `0` 或 `1`

"""

from typing import List, Optional


class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        left = 0
        for right in range(len(A)):
            if A[right] == 0:
                K -= 1
            if K < 0:
                if A[left] == 0:
                    K += 1
                left += 1
        return len(A) - left










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用滑动窗口技巧。维护一个窗口 [left, right]，窗口内最多允许 K 个 0。
# 用变量 K 直接记录当前窗口内还能翻转的 0 的个数：
# - 右指针 right 遍历数组，遇到 0 时 K 减 1。
# - 当 K < 0（窗口内 0 的个数超过允许值），需要收缩左指针 left。
#   如果左指针指向的是 0，则 K 加 1（恢复一次翻转机会），left 右移一位。
# - 最终窗口的长度（right - left + 1 或 len(A) - left）就是答案。
# 窗口只会增大不会缩小，因此最终返回 len(A) - left。
#
# 时间复杂度: O(n) - 每个元素最多被 left 和 right 各访问一次
# 空间复杂度: O(1) - 只使用了常数额外空间
#
# 关键点:
# - 将 K 直接用作"剩余翻转配额"，简化了代码逻辑
# - 窗口只增不减：用 len(A) - left 计算最终长度，无需额外变量记录最大值
# - 收缩条件：K < 0 时移动 left，保证窗口内始终满足条件
