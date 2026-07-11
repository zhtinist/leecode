"""
LeetCode #1493 - Longest Subarray of 1's After Deleting One Element
中文题名：删掉一个元素以后全为 1 的最长子数组
https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/

Given a binary array `nums`, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the
resulting array.

Return 0 if there is no such subarray.

Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.

Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].

Example 3:

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.

Example 4:

Input: nums = [1,1,0,0,1,1,1,0,1]
Output: 4

Example 5:

Input: nums = [0,0,0]
Output: 0

Constraints:

`1 <= nums.length <= 10^5`

`nums[i]` is
either `0` or `1`.

【中文翻译】

给定一个二进制数组 `nums`，你需要从中删除一个元素。

返回结果数组中仅包含 1 的最长非空子数组的大小。

如果不存在这样的子数组，返回 0。

示例 1：
输入：nums = [1,1,0,1]
输出：3
解释：删除位置 2 的数字后，[1,1,1] 包含 3 个值为 1 的数字。

示例 2：
输入：nums = [0,1,1,1,0,1,1,0,1]
输出：5
解释：删除位置 4 的数字后，[0,1,1,1,1,1,0,1] 中最长的值为 1 的子数组是 [1,1,1,1,1]。

示例 3：
输入：nums = [1,1,1]
输出：2
解释：必须删除一个元素。

示例 4：
输入：nums = [1,1,0,0,1,1,1,0,1]
输出：4

示例 5：
输入：nums = [0,0,0]
输出：0

约束条件：
1 <= nums.length <= 10^5
nums[i] 是 0 或 1。

"""

from typing import List, Optional


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        zero_count = 0
        max_len = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1

            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            # Window size minus the one deleted element
            max_len = max(max_len, right - left)

        return max_len



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 1. 使用滑动窗口，窗口中最多允许包含一个 0（因为允许删除一个元素）。
# 2. 遍历数组，right 指针向右扩展：
#    - 如果 nums[right] == 0，zero_count++
#    - 当 zero_count > 1 时，收缩 left 指针直到 zero_count <= 1
#    - 更新最大长度：max_len = max(max_len, right - left)
#      （窗口长度减 1，因为必须删除一个元素；如果窗口中没有 0，
#       也必须删除一个元素，所以结果也是窗口长度减 1）
# 3. 注意：窗口尺寸 right - left + 1 包含了窗口中的所有元素，
#    但因为必须删除一个元素，所以有效 1 的长度是 right - left。
#
# 时间复杂度: O(N)
# 空间复杂度: O(1)
#
# 关键点:
# - 滑动窗口最多允许一个 0
# - 窗口大小 - 1 = 有效 1 的数量（因为必须删除一个元素）
# - 当整个数组都是 1 时，也需要删除一个，返回 n-1
# - 当整个数组都是 0 时，返回 0










