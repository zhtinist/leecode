"""
LeetCode #457 - Circular Array Loop
中文题名：环形数组循环
https://leetcode.com/problems/circular-array-loop/

You are given a circular array `nums` of positive and negative integers. If
a number k at an index is positive, then move forward k steps. Conversely, if
it's negative (-k), move backward k steps. Since the array is
circular, you may assume that the last element's next element is the first element, and
the first element's previous element is the last element.

Determine if there is a loop (or a cycle) in `nums`. A cycle must start and end at
the same index and the cycle's length > 1. Furthermore, movements in a cycle must all
follow a single direction. In other words, a cycle must not consist of both forward and
backward movements.

Example 1:

Input: [2,-1,1,2,2]
Output: true
Explanation: There is a cycle, from index 0 -> 2 -> 3 -> 0. The cycle's length is 3.

Example 2:

Input: [-1,2]
Output: false
Explanation: The movement from index 1 -> 1 -> 1 ... is not a cycle, because the cycle's length is 1. By definition the cycle's length must be greater than 1.

Example 3:

Input: [-2,1,-1,-2,-2]
Output: false
Explanation: The movement from index 1 -> 2 -> 1 -> ... is not a cycle, because movement from index 1 -> 2 is a forward movement, but movement from index 2 -> 1 is a backward movement. All movements in a cycle must follow a single direction.

Note:

-1000 <= nums[i] <= 1000

nums[i] != 0

1 <= nums.length <= 5000

Follow up:

Could you solve it in O(n) time complexity and O(1) extra space
complexity?

【中文翻译】
给定一个包含正整数和负整数的环形数组 nums。如果索引处的数字 k 为正数，则向前移动 k 步；
如果是负数 (-k)，则向后移动 k 步。由于数组是环形的，最后一个元素的下一个元素是第一个元素，
第一个元素的前一个元素是最后一个元素。

判断 nums 中是否存在循环。循环必须从同一索引开始和结束，且循环长度 > 1。
此外，循环中的所有移动必须沿同一方向，不能同时包含向前和向后移动。

示例 1：
输入：[2,-1,1,2,2]
输出：true
解释：存在循环，从索引 0 -> 2 -> 3 -> 0。循环长度为 3。

示例 2：
输入：[-1,2]
输出：false
解释：从索引 1 -> 1 -> 1 ... 不是循环，因为循环长度为 1。根据定义，循环长度必须大于 1。

示例 3：
输入：[-2,1,-1,-2,-2]
输出：false
解释：从索引 1 -> 2 -> 1 -> ... 不是循环，因为从索引 1 -> 2 是向前移动，
但从索引 2 -> 1 是向后移动。循环中的所有移动必须沿同一方向。

进阶：能否用 O(n) 时间复杂度和 O(1) 额外空间解决？
"""

from typing import List, Optional


class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)

        def next_index(i: int) -> int:
            return (i + nums[i]) % n

        for i in range(n):
            if nums[i] == 0:
                continue

            # Use two pointers to detect cycle
            slow = i
            fast = next_index(i)

            # All elements in the cycle must have the same direction
            # nums[i] > 0 means forward, nums[i] < 0 means backward
            direction = nums[i] > 0

            while True:
                # Check if fast pointer is still valid (same direction, not self-loop)
                if nums[fast] == 0:
                    break
                if (nums[fast] > 0) != direction:
                    break

                slow = next_index(slow)
                fast = next_index(next_index(fast))

                # Check fast pointer again after advancing
                if nums[fast] == 0:
                    break
                if (nums[fast] > 0) != direction:
                    break

                if slow == fast:
                    # Check cycle length > 1 (self-loop case)
                    if slow == next_index(slow):
                        break
                    return True

            # Mark all visited elements in this failed path as 0 (visited)
            # to achieve O(n) time
            idx = i
            while nums[idx] != 0:
                nxt = next_index(idx)
                # Check direction consistency before marking
                if (nums[idx] > 0) != direction:
                    break
                nums[idx] = 0
                idx = nxt

        return False



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用快慢指针（Floyd 判圈法）检测循环。遍历每个未访问的索引作为起点，使用快慢指针判断是否存在环。
# 关键约束：(1) 所有移动方向必须一致（全正或全负）；(2) 循环长度必须大于 1（不能是自环）。
# 访问过的无效路径标记为 0，避免重复检查，实现 O(N) 时间。
#
# 时间复杂度: O(N) — 每个元素最多被访问一次（标记为 0 后跳过）
# 空间复杂度: O(1) — 原地修改数组作为访问标记
#
# 关键点:
# - 快速判断同方向：用 (nums[i] > 0) 布尔值比较
# - 自循环检测：slow == next_index(slow) 即循环长度为 1
# - 原地标记访问过的元素为 0（因为题目中 nums[i] != 0）
# - 计算下一索引：((i + nums[i]) % n + n) % n 处理负数取模（Python 中 (i + nums[i]) % n 即可）
