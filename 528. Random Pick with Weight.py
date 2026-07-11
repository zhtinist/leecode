"""
LeetCode #528 - Random Pick with Weight
中文题名：按权重随机选择
https://leetcode.com/problems/random-pick-with-weight/

Given an array `w` of positive integers, where `w[i]` describes the
weight of index `i`, write a function `pickIndex` which
randomly picks an index in proportion to its weight.

Note:

`1 <= w.length <= 10000`

`1 <= w[i] <= 10^5`

`pickIndex` will be called at most `10000` times.

Example 1:

Input:
["Solution","pickIndex"]
[[[1]],[]]
Output: [null,0]

Example 2:

Input:
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output: [null,0,1,1,1,0]

【中文翻译】
给定一个正整数数组 w，其中 w[i] 描述下标 i 的权重。实现 pickIndex 方法，
根据权重按比例随机选择一个下标。即选中下标 i 的概率为 w[i] / sum(w)。

示例 1：
    输入：["Solution","pickIndex"]，[[[1]],[]]
    输出：[null,0]
    解释：只有一个元素，权重为 1，总是返回下标 0。

示例 2：
    输入：["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
         [[[1,3]],[],[],[],[],[]]
    输出：[null,0,1,1,1,0]
    解释：权重为 [1, 3]，选中下标 0 的概率为 1/4，选中下标 1 的概率为 3/4。
         pickIndex 总共调用 5 次。

说明：w.length <= 10000，w[i] <= 10^5，pickIndex 最多调用 10000 次。
"""

import random
from typing import List, Optional


class Solution:
    def __init__(self, w: List[int]):
        # Build prefix sum array
        self.prefix = []
        total = 0
        for weight in w:
            total += weight
            self.prefix.append(total)
        self.total = total

    def pickIndex(self) -> int:
        # Random number in [1, total]
        target = random.randint(1, self.total)
        # Binary search for the first prefix >= target
        left, right = 0, len(self.prefix) - 1
        while left < right:
            mid = (left + right) // 2
            if self.prefix[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 构建前缀和数组将权重映射到区间。例如 w = [1, 3]，前缀和为 [1, 4]，则区间 [1,1] 对应
# 下标 0，[2,4] 对应下标 1。每次 pickIndex 生成 [1, total] 间的随机整数，然后用二分查找
# 找到第一个前缀和 >= target 的下标。由于每个区间大小等于权重，选中概率与权重成正比。
#
# 时间复杂度: 构造函数 O(N)；pickIndex O(log N)
# 空间复杂度: O(N) — 前缀和数组
#
# 关键点:
# - 前缀和将权重问题转化为"按区间长度随机落点"问题
# - 二分查找找第一个 >= target 的前缀和就是答案下标
# - 可用 bisect_left 替代手动二分
