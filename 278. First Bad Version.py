"""
LeetCode #278 - First Bad Version
中文题名：第一个错误的版本
https://leetcode.com/problems/first-bad-version/

You are a product manager and currently leading a team to develop a new product.
Unfortunately, the latest version of your product fails the quality check. Since each
version is developed based on the previous version, all the versions after a bad version are
also bad.

Suppose you have `n` versions `[1, 2, ..., n]` and you want to find out
the first bad one, which causes all the following ones to be bad.

You are given an API `bool isBadVersion(version)` which will return whether `version`
is bad. Implement a function to find the first bad version. You should minimize the number
of calls to the API.

Example:

Given n = 5, and version = 4 is the first bad version.

`call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version. `

【中文翻译】
你是产品经理，正在带领一个团队开发新产品。不幸的是，产品的最新版本没有通过质量检测。由于每个版本都是基于之前的版本开发的，所以错误的版本之后的所有版本都是错误的。

假设你有 `n` 个版本 `[1, 2, ..., n]`，你想找出导致之后所有版本出错的第一个错误版本。

你会得到一个 API `bool isBadVersion(version)`，它会返回 `version` 是否为错误版本。实现一个函数来找到第一个错误的版本。你应该尽量减少对 API 的调用次数。

示例：

给定 n = 5，且 version 4 是第一个错误版本。

`call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version. `
"""

from typing import List, Optional


# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
#     """Return whether version is bad."""


class Solution:
    def firstBadVersion(self, n: int) -> int:
        """Find the first bad version using binary search.

        The versions range from 1 to n. All versions after the first bad one are bad.
        Binary search to find the leftmost bad version.
        """
        left, right = 1, n
        while left < right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid  # mid could be the first bad version
            else:
                left = mid + 1  # first bad version is after mid
        return left


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Easy
# Paid Only: No
#
# 解题思路:
# 标准二分查找找左边界。版本从 1 到 n，第一个坏版本之后的所有版本都是坏的。
# 可以使用二分查找定位第一个坏版本：
# - 如果 mid 是坏版本，那么第一个坏版本在 mid 或其左侧，right = mid
# - 如果 mid 是好版本，那么第一个坏版本在 mid 右侧，left = mid + 1
# - 当 left == right 时，找到了第一个坏版本
#
# 时间复杂度: O(log N) - 二分查找每次将搜索范围减半
# 空间复杂度: O(1) - 只使用常数个变量
#
# 关键点:
# - 使用 left < right 而非 left <= right（避免死循环）
# - mid = left + (right - left) // 2 防止整数溢出
# - 当 isBadVersion(mid) 为真时 right = mid（保留 mid 作为候选）
# - 当 isBadVersion(mid) 为假时 left = mid + 1（排除 mid）
