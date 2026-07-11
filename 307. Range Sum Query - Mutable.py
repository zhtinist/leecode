"""
LeetCode #307 - Range Sum Query - Mutable
中文题名：区域和检索 - 数组可修改
https://leetcode.com/problems/range-sum-query-mutable/

Given an integer array nums, find the sum of the elements between indices i and
j (i <= j), inclusive.

The update(i, val) function modifies nums by updating the element at index
i to val.

Example:

Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8

Note:

The array is only modifiable by the update function.

You may assume the number of calls to update and sumRange function is
distributed evenly.

【中文翻译】
给定一个整数数组 nums，求出数组中从索引 i 到 j（i <= j）范围内元素的总和，包含 i、j 两点。

update(i, val) 函数可以通过将下标为 i 的值更新为 val，从而对数组进行修改。

示例：

给定 nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8

注意：

数组仅能通过 update 函数进行修改。

你可以假设 update 函数和 sumRange 函数的调用次数是均匀分布的。
"""

from typing import List, Optional


class NumArray:
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.nums = nums[:]
        self.bit = [0] * (self.n + 1)
        for i, val in enumerate(nums):
            self._add(i + 1, val)

    def _add(self, idx: int, delta: int) -> None:
        """在 BIT 的 idx 位置增加 delta"""
        while idx <= self.n:
            self.bit[idx] += delta
            idx += idx & -idx

    def _prefix_sum(self, idx: int) -> int:
        """查询前缀和 [1, idx]"""
        s = 0
        while idx > 0:
            s += self.bit[idx]
            idx -= idx & -idx
        return s

    def update(self, index: int, val: int) -> None:
        """将 nums[index] 更新为 val"""
        delta = val - self.nums[index]
        self.nums[index] = val
        self._add(index + 1, delta)

    def sumRange(self, left: int, right: int) -> int:
        """查询 [left, right] 的区间和"""
        return self._prefix_sum(right + 1) - self._prefix_sum(left)










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用树状数组（Binary Indexed Tree / Fenwick Tree）。
# BIT 支持 O(log n) 单点更新和 O(log n) 区间前缀和查询。
# 核心操作：
# - 构建：对每个元素调用 add 建立 BIT，共 O(n log n)
# - add(idx, delta)：将 delta 累加到 idx 及其所有祖先节点，通过 idx += idx & -idx 向上传播
# - prefix_sum(idx)：查询 [1, idx] 的前缀和，通过 idx -= idx & -idx 向下累加
# - update(index, val)：计算差值 delta = val - nums[index]，更新原数组和 BIT
# - sumRange(left, right)：right 的前缀和减去 left-1 的前缀和
# BIT 下标从 1 开始，所以原数组索引需要 +1 映射。
#
# 时间复杂度: 构造 O(n log n)，update O(log n)，sumRange O(log n)
# 空间复杂度: O(n)
#
# 关键点:
# - 树状数组 vs 线段树：BIT 代码更简洁，适用于单点更新 + 区间求和
# - lowbit 运算 x & -x：获取 x 二进制表示中最低位的 1
# - BIT 下标从 1 开始，注意索引转换（index + 1）
# - 线段树也可解此题，但 BIT 更轻量
