"""
LeetCode #34 - Find First and Last Position of Element in Sorted Array
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

Given an array of integers nums sorted in non-decreasing order, find the starting
and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1:
    Input: nums = [5,7,7,8,8,10], target = 8
    Output: [3,4]

Example 2:
    Input: nums = [5,7,7,8,8,10], target = 6
    Output: [-1,-1]

Example 3:
    Input: nums = [], target = 0
    Output: [-1,-1]

Constraints:
    0 <= nums.length <= 10^5
    -10^9 <= nums[i], target <= 10^9
    nums is a non-decreasing array.
"""

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        left = self._lower_bound(nums, target)
        if left == len(nums) or nums[left] != target:
            return [-1, -1]

        right = self._upper_bound(nums, target)
        return [left, right]

    def _lower_bound(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        ans = len(nums)
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans

    def _upper_bound(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans


# --- 二分法易错点总结 ---
#
# 1. 循环条件 left <= right vs left < right
#    - left <= right：闭区间 [left, right]，mid 命中时可继续收缩，适合找边界/精确值
#    - left < right：开区间写法，结束时 left == right 即答案，别混用两种风格
#
# 2. 边界初始化
#    - 普通二分：left=0, right=len(nums)-1
#    - lower_bound 常设 ans=len(nums) 表示「不存在」；upper_bound 常设 ans=-1
#    - 空数组要单独处理，否则 right=-1 时循环行为容易错
#
# 3. mid 计算溢出（其他语言）
#    - Python 无溢出问题，但 Java/C++ 应写 mid = left + (right - left) // 2
#
# 4. 收缩方向写反
#    - 找左边界：nums[mid] >= target → right = mid - 1（往左缩）
#    - 找右边界：nums[mid] <= target → left = mid + 1（往右缩）
#    - 普通查找：nums[mid] < target → left = mid + 1，否则 right = mid - 1
#
# 5. 找到 target 时不能立刻 return
#    - 找「第一个/最后一个」位置时，命中只是候选，还要继续往左/右搜
#    - 本题 lower_bound 用 ans=mid + right=mid-1，upper_bound 用 ans=mid + left=mid+1
#
# 6. 死循环
#    - 必须保证每次循环区间严格变小：left=mid+1 或 right=mid-1
#    - 错误写法：right=mid（当 left==right 时不变）在某些模板下会死循环
#
# 7. 返回值含义搞混
#    - lower_bound 返回第一个 >= target 的下标，还需检查 nums[ans]==target
#    - upper_bound 返回最后一个 <= target 的下标（或第一个 > target 的前一位）
#    - 找不到时 lower_bound 可能返回 len(nums)，访问前必须判界
#
# 8. 重复元素
#    - 普通二分只找一个位置；找区间端点必须两次二分或统一 bound 模板
#
# 9. 旋转/循环数组
#    - 不能直接用全局有序假设；先判断哪半边有序，再决定往哪边搜
#
# 10. 记忆口诀
#     - 找左：>= 时往左（right = mid - 1）
#     - 找右：<= 时往右（left = mid + 1）
#     - 找值：小了往右，大了往左
