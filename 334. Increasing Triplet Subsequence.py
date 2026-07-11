"""
LeetCode #334 - Increasing Triplet Subsequence
中文题名：递增的三元子序列
https://leetcode.com/problems/increasing-triplet-subsequence/

Given an unsorted array return whether an increasing subsequence of length 3 exists or not in
the array.

Formally the function should:

Return true if there exists i, j, k

such that arr[i] < arr[j] < arr[k] given 0 <= i < j
< k <= n-1 else return false.

Note: Your algorithm should run in O(n) time complexity and
O(1) space complexity.

Example 1:

Input: [1,2,3,4,5]
Output: true

Example 2:

Input: [5,4,3,2,1]
Output: false

【中文翻译】
给定一个未排序的数组，判断该数组中是否存在长度为 3 的递增子序列。

数学表达式如下：

如果存在 i, j, k，满足 0 <= i < j < k <= n-1，使得 arr[i] < arr[j] < arr[k]，返回 true；否则返回 false。

注意：你的算法应该具有 O(n) 时间复杂度和 O(1) 空间复杂度。

示例 1：

输入：[1,2,3,4,5]
输出：true

示例 2：

输入：[5,4,3,2,1]
输出：false
"""

from typing import List, Optional


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float('inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False











# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 维护 first 和 second 两个变量，分别表示当前找到的最小值和次小值。
# 遍历数组：
# - 如果 n <= first：更新 first = n
# - 否则如果 n <= second：更新 second = n
# - 否则（n > first 且 n > second）：找到了第三个大于前两个的数，返回 True
# 注意：用 <= 而不是 <，确保严格递增且处理重复值。
# 即使 first 和 second 不是真正的子序列（可能顺序不严格），但只要存在 third > second > first，
# 就一定存在递增三元组（因为 first 的值一定在 second 之前出现）。
#
# 时间复杂度: O(n)
# 空间复杂度: O(1)
#
# 关键点:
# - 贪心维护最小的两个候选值
# - 使用 <= 处理重复元素
# - 不需要维护索引，因为值的大小关系已经足够保证存在性
