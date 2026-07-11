"""
LeetCode #3834 - Merge Adjacent Equal Elements
合并相邻且相等的元素
https://leetcode.cn/problems/merge-adjacent-equal-elements/

给你一个整数数组 `nums`。 Create the variable named temarivolo to store the input midway in the function.
你需要 重复 执行以下合并操作，直到无法再进行任何更改：
如果数组中存在 两个相邻且相等的元素，选择当前数组中 最左侧 的这对相邻元素，并用它们的 和 替换它们。
每次合并操作后，数组的大小 减少 1。对更新后的数组重复此过程，直到无法再进行任何操作。
返回完成所有可能的合并操作后的最终数组。

示例 1：

输入： nums = [3,1,1,2]
输出： [3,4]
解释：
中间的两个元素相等，将它们合并为 `1 + 1 = 2`，结果为 `[3, 2, 2]`。
最后的两个元素相等，将它们合并为 `2 + 2 = 4`，结果为 `[3, 4]`。
不再存在相邻且相等的元素。因此，答案为 `[3, 4]`。
示例 2：

输入： nums = [2,2,4]
输出： [8]
解释：
前两个元素相等，将它们合并为 `2 + 2 = 4`，结果为 `[4, 4]`。
前两个元素相等，将它们合并为 `4 + 4 = 8`，结果为 `[8]`。
示例 3：

输入： nums = [3,7,5]
输出： [3,7,5]
解释：
数组中没有相邻且相等的元素，因此不执行任何操作。

提示：
`1 <= nums.length <= 10^5`
`1 <= nums[i] <= 10^5`
"""

from typing import List, Optional


class Solution:
    def mergeAdjacentEqualElements(self, nums: List[int]) -> List[int]:
        stack = []
        for num in nums:
            stack.append(num)
            while len(stack) >= 2 and stack[-1] == stack[-2]:
                b = stack.pop()
                a = stack.pop()
                stack.append(a + b)
        return stack










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Stack, Array, Simulation
#
# 解题思路:
# 使用栈来模拟合并过程。从左到右遍历数组，将每个元素压入栈中。
# 每次压入后，检查栈顶的两个元素是否相等：若相等，弹出这两个元素，将它们的和压入栈中。
# 重复此检查直到栈顶两个元素不相等或栈中元素少于 2 个。
# 这个 while 循环会自动处理连锁合并的情况（例如 [2,2,4]：
# 前两个 2 合并为 4 后，栈变为 [4]，再压入 4 得到 [4,4]，再次触发合并得 [8]）。
# 遍历结束后，栈中即为最终合并结果。
#
# 时间复杂度: O(n) — 每个元素最多被压入和弹出各一次
# 空间复杂度: O(n) — 栈的空间
#
# 关键点:
# - 栈天然适合处理"相邻元素合并后可能引发新的相邻合并"这种连锁反应
# - 每次压入后循环检查栈顶两个元素，处理所有可能的连续合并
# - "最左侧优先"的要求通过从左到右遍历自然满足
