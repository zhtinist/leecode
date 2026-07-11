"""
LeetCode #376 - Wiggle Subsequence
中文题名：摆动序列
https://leetcode.com/problems/wiggle-subsequence/

A sequence of numbers is called a wiggle sequence if the differences between
successive numbers strictly alternate between positive and negative. The first difference
(if one exists) may be either positive or negative. A sequence with fewer than two elements
is trivially a wiggle sequence.

For example, `[1,7,4,9,2,5]` is a wiggle sequence because the differences `(6,-3,5,-7,3)`
are alternately positive and negative. In contrast, `[1,4,7,2,5]` and `[1,7,4,5,5]`
are not wiggle sequences, the first because its first two differences are positive and the
second because its last difference is zero.

Given a sequence of integers, return the length of the longest subsequence that is a wiggle
sequence. A subsequence is obtained by deleting some number of elements (eventually, also
zero) from the original sequence, leaving the remaining elements in their original
order.

Example 1:

Input: [1,7,4,9,2,5]
Output: 6
Explanation: The entire sequence is a wiggle sequence.

Example 2:

Input: [1,17,5,10,13,15,10,5,16,8]
Output: 7
Explanation: There are several subsequences that achieve this length. One is [1,17,10,13,10,16,8].

Example 3:

Input: [1,2,3,4,5,6,7,8,9]
Output: 2

Follow up:

Can you do it in O(n) time?

【中文翻译】
如果连续数字之间的差严格地在正数和负数之间交替，则数字序列称为摆动序列。第一个差（如果存在）可以是正数或负数。少于两个元素的序列也是摆动序列。

例如，[1,7,4,9,2,5] 是一个摆动序列，因为差值 (6,-3,5,-7,3) 是正负交替的。相反，[1,4,7,2,5] 和 [1,7,4,5,5] 不是摆动序列，第一个是因为它的前两个差值都是正数，第二个是因为它的最后一个差值为零。

给定一个整数序列，返回作为摆动序列的最长子序列的长度。子序列可以通过从原始序列中删除一些元素（也可以不删除）来获得，剩下的元素保持其原始顺序。

示例 1：

输入：[1,7,4,9,2,5]
输出：6
解释：整个序列都是一个摆动序列。

示例 2：

输入：[1,17,5,10,13,15,10,5,16,8]
输出：7
解释：有几个子序列可以达到这个长度。其中一个是 [1,17,10,13,10,16,8]。

示例 3：

输入：[1,2,3,4,5,6,7,8,9]
输出：2

进阶：

你能用 O(n) 的时间复杂度完成此题吗？
"""

from typing import List, Optional


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # up: 以当前元素结尾且最后一步是"上升"的最长摆动子序列长度
        # down: 以当前元素结尾且最后一步是"下降"的最长摆动子序列长度
        up = down = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                # 当前元素比前一个大，可以在之前"下降"结尾的序列后加上当前元素
                up = down + 1
            elif nums[i] < nums[i - 1]:
                # 当前元素比前一个小，可以在之前"上升"结尾的序列后加上当前元素
                down = up + 1
            # 相等时忽略，不改变任何状态

        return max(up, down)











# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 本题要求找出给定数组中最长的摆动子序列（Wiggle Subsequence）。摆动序列的特点是相邻元素的
# 差值正负交替。子序列不要求连续，但需要保持原顺序。
#
# 使用动态规划（O(N) 时间）：
# - 维护两个状态变量 up 和 down
# - up 表示以当前元素结尾、最后一步为"上升"的最长摆动子序列长度
# - down 表示以当前元素结尾、最后一步为"下降"的最长摆动子序列长度
# - 遍历数组时：
#   * 如果 nums[i] > nums[i-1]（上升），可以接在"下降"序列后面，up = down + 1
#   * 如果 nums[i] < nums[i-1]（下降），可以接在"上升"序列后面，down = up + 1
#   * 如果相等，跳过（不需要改变状态）
# - 最终答案为 max(up, down)
#
# 也可以使用贪心思想：统计序列中的"峰"和"谷"的数量，本质相同。
#
# 时间复杂度: O(N) - 只需遍历数组一次
# 空间复杂度: O(1) - 只使用常量额外空间
#
# 关键点:
# - up 和 down 交替更新，体现了摆动序列"交替"的核心要求
# - 连续上升时 up 保持不变（等于最近的 down+1），意味着跳过中间非峰值的点
# - 此方法本质上等价于统计序列中极值点的数量
# - 相等元素不影响结果，直接跳过即可
