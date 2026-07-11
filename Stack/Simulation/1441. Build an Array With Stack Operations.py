"""
LeetCode #1441 - Build an Array With Stack Operations
中文题名：用栈操作构建数组
https://leetcode.com/problems/build-an-array-with-stack-operations/

Given an array `target` and an integer `n`. In each
iteration, you will read a number from  `list = {1,2,3..., n}`.

Build the `target` array using the following operations:

Push: Read a new element from the
beginning `list`, and push it in the array.

Pop: delete the last element of the array.

If the target array is already built, stop reading more elements.

You are guaranteed that the target array is strictly increasing, only containing numbers
between 1 to `n` inclusive.

Return the operations to build the target array.

You are guaranteed that the answer is unique.

Example 1:

Input: target = [1,3], n = 3
Output: ["Push","Push","Pop","Push"]
Explanation:
Read number 1 and automatically push in the array -> [1]
Read number 2 and automatically push in the array then Pop it -> [1]
Read number 3 and automatically push in the array -> [1,3]

Example 2:

Input: target = [1,2,3], n = 3
Output: ["Push","Push","Push"]

Example 3:

Input: target = [1,2], n = 4
Output: ["Push","Push"]
Explanation: You only need to read the first 2 numbers and stop.

Example 4:

Input: target = [2,3,4], n = 4
Output: ["Push","Pop","Push","Push","Push"]

Constraints:

`1 <= target.length <= 100`

`1 <= target[i] <= 100`

`1 <= n <= 100`

`target` is strictly increasing.

【中文翻译】
给定一个数组 `target` 和一个整数 `n`。每次迭代，你将从 `list = {1,2,3..., n}` 中读取一个数字。

使用以下操作构建 `target` 数组：

Push（推入）：从列表开头读取一个新元素，并将其推入数组中。

Pop（弹出）：删除数组的最后一个元素。

如果目标数组已经构建完成，则停止读取更多元素。

保证目标数组是严格递增的，且只包含 1 到 `n`（含）之间的数字。

返回构建目标数组所使用的操作。

保证答案是唯一的。

示例 1：

输入：target = [1,3], n = 3
输出：["Push","Push","Pop","Push"]
解释：
读取数字 1 并自动推入数组 -> [1]
读取数字 2 并自动推入数组然后弹出 -> [1]
读取数字 3 并自动推入数组 -> [1,3]

示例 2：

输入：target = [1,2,3], n = 3
输出：["Push","Push","Push"]

示例 3：

输入：target = [1,2], n = 4
输出：["Push","Push"]
解释：只需要读取前 2 个数字并停止。

示例 4：

输入：target = [2,3,4], n = 4
输出：["Push","Pop","Push","Push","Push"]

约束条件：

`1 <= target.length <= 100`

`1 <= target[i] <= 100`

`1 <= n <= 100`

`target` 严格递增。
"""

from typing import List, Optional


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        j = 0
        for num in range(1, n + 1):
            ans.append("Push")
            if j < len(target) and target[j] == num:
                j += 1
            else:
                ans.append("Pop")
            if j == len(target):
                break
        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# target 是严格递增的，因此可以用一个指针 j 遍历 target。
# 从 1 到 n 依次处理每个数字 num：
#   - 总是先执行 "Push"
#   - 如果 num == target[j]，说明该数字在 target 中，移动 j 指针
#   - 否则该数字不在 target 中，需要再执行 "Pop" 将其移除
# 当 j 到达 target 末尾时提前结束。
#
# 时间复杂度: O(N)  -- 遍历 1 到 n 每个数字一次
# 空间复杂度: O(1)  -- 不计结果数组，仅用常数额外空间
#
# 关键点:
# - 利用 target 严格递增的性质，按顺序匹配数字
# - 不在 target 中的数字需要 Push + Pop 两个操作
# - 全部匹配完成后即可提前返回，不需要处理剩余数字









