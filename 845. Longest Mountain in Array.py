"""
LeetCode #845 - Longest Mountain in Array
中文题名：数组中的最长山脉
https://leetcode.com/problems/longest-mountain-in-array/

Let's call any (contiguous) subarray B (of A) a mountain if the following
properties hold:

`B.length >= 3`

There exists some `0 < i < B.length - 1` such that `B[0] <
B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]`

(Note that B could be any subarray of A, including the entire array A.)

Given an array `A` of integers, return the length of the
longest mountain.

Return `0` if there is no mountain.

Example 1:

Input: [2,1,4,7,3,2,5]
Output: 5
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.

Example 2:

Input: [2,2,2]
Output: 0
Explanation: There is no mountain.

Note:

`0 <= A.length <= 10000`

`0 <= A[i] <= 10000`

Follow up:

Can you solve it using only one pass?

Can you solve it in `O(1)` space?

【中文翻译】
我们把数组 A 中符合下列属性的任意连续子数组 B 称为"山脉"：

`B.length >= 3`

存在某个 `0 < i < B.length - 1` 使得 `B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]`

（注意：B 可以是 A 的任意子数组，包括整个数组 A。）

给定一个整数数组 `A`，返回最长"山脉"的长度。

如果没有山脉，返回 `0`。

示例 1：

输入：[2,1,4,7,3,2,5]
输出：5
解释：最长山脉是 [1,4,7,3,2]，长度为 5。

示例 2：

输入：[2,2,2]
输出：0
解释：没有山脉。

注意：

`0 <= A.length <= 10000`

`0 <= A[i] <= 10000`

进阶：

你能仅用一次遍历解决吗？

你能用 `O(1)` 空间解决吗？

"""

from typing import List, Optional


class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 3:
            return 0

        max_len = 0
        i = 1  # Start from second element
        while i < n - 1:
            # Check if arr[i] is a peak (strictly greater than neighbors)
            if arr[i - 1] < arr[i] > arr[i + 1]:
                # Expand left
                left = i - 1
                while left > 0 and arr[left - 1] < arr[left]:
                    left -= 1
                # Expand right
                right = i + 1
                while right < n - 1 and arr[right] > arr[right + 1]:
                    right += 1
                # Update max
                length = right - left + 1
                if length > max_len:
                    max_len = length
                # Skip past this mountain
                i = right
            else:
                i += 1

        return max_len



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 一次遍历（找峰顶法）。
# 山脉的核心是峰顶（peek），即同时大于左右邻居的元素。
# 遍历数组，当找到峰顶时：
#   1. 向左扩展：找到严格递增的最长序列
#   2. 向右扩展：找到严格递减的最长序列
#   3. 计算山脉长度 = right - left + 1
#   4. 跳转到当前山脉的右端点继续搜索（因为重叠不会更长）
# 没有峰顶时直接前进。
#
# 时间复杂度: O(n) — 每个元素最多被访问两次（左扩展和右扩展各一次）
# 空间复杂度: O(1) — 只使用常数变量
#
# 关键点:
# - 峰顶条件：arr[i-1] < arr[i] > arr[i+1]
# - 左右扩展法确保每个山脉被完整测量
# - 跳过已处理的区域（i = right），避免重复遍历
# - 边界检查：山脉至少需要 3 个元素（`n >= 3` 的检查）
