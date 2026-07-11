"""
LeetCode #665 - Non-decreasing Array
中文题名：非递减数列
https://leetcode.com/problems/non-decreasing-array/

Given an array with `n` integers, your task is to check if it could become
non-decreasing by modifying at most `1` element.

We define an array is non-decreasing if `array[i] <= array[i + 1]` holds for
every `i` (1 <= i < n).

Example 1:

Input: [4,2,3]
Output: True
Explanation: You could modify the first `4` to `1` to get a non-decreasing array.

Example 2:

Input: [4,2,1]
Output: False
Explanation: You can't get a non-decreasing array by modify at most one element.

Note:
The `n` belongs to [1, 10,000].

【中文翻译】
给定一个包含 `n` 个整数的数组，你的任务是检查它是否可以通过最多修改 `1` 个元素变成非递减数组。

我们定义一个数组是非递减的，如果对于每个 `i`（1 <= i < n），都有 `array[i] <= array[i + 1]` 成立。

示例 1：

输入：[4,2,3]
输出：True
解释：你可以将第一个 `4` 修改为 `1`，得到一个非递减数组。

示例 2：

输入：[4,2,1]
输出：False
解释：你无法通过最多修改一个元素得到非递减数组。

注意：
`n` 的取值范围是 [1, 10,000]。
"""

from typing import List, Optional


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        modified = False

        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                if modified:
                    return False
                modified = True
                if i >= 2 and nums[i] < nums[i - 2]:
                    nums[i] = nums[i - 1]
                else:
                    nums[i - 1] = nums[i]

        return True











# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 一次遍历数组，当发现 nums[i] < nums[i-1]（违反非递减）时：
# 如果之前已经修改过一次（modified == True），直接返回 False。
# 否则，需要决定如何修改：
# - 如果 i >= 2 且 nums[i] < nums[i-2]：
#   说明 nums[i] 太小了（比前前个还小），需要将 nums[i] 抬高到 nums[i-1]
#   即：nums[i] = nums[i-1]
# - 否则（i == 1 或 nums[i] >= nums[i-2]）：
#   说明是 nums[i-1] 太大了，将 nums[i-1] 降低到 nums[i]
#   即：nums[i-1] = nums[i]
# 这样保证局部修改后不影响前面已检查的非递减性质。
#
# 时间复杂度: O(n) - 一次遍历
# 空间复杂度: O(1) - 仅使用常数额外空间
#
# 关键点:
# - 贪心策略：优先降低前一个数（nums[i-1] = nums[i]）以最小化对后续的影响
# - 但当前前个数比 nums[i] 还大时（nums[i] < nums[i-2]），只能抬高 nums[i]
# - 只允许修改一次，用 modified 标志跟踪
# - 经典贪心题，很容易写错边界条件（特别是 nums[i] < nums[i-2] 的判断）
