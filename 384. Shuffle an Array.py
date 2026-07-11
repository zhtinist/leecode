"""
LeetCode #384 - Shuffle an Array
中文题名：打乱数组
https://leetcode.com/problems/shuffle-an-array/

Shuffle a set of numbers without duplicates.

Example:

// Init an array with set 1, 2, and 3.
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
solution.shuffle();

// Resets the array back to its original configuration [1,2,3].
solution.reset();

// Returns the random shuffling of array [1,2,3].
solution.shuffle();

【中文翻译】
打乱一个没有重复元素的数组。

示例：

// 用集合 1、2 和 3 初始化数组。
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// 打乱数组 [1,2,3] 并返回结果。任何 [1,2,3] 的排列都应该有相同的返回概率。
solution.shuffle();

// 将数组重置回原始配置 [1,2,3]。
solution.reset();

// 返回数组 [1,2,3] 的随机打乱结果。
solution.shuffle();
"""

from typing import List, Optional


class Solution:

    def __init__(self, nums: List[int]):
        self.original = nums[:]
        self.arr = nums[:]

    def reset(self) -> List[int]:
        self.arr = self.original[:]
        return self.arr

    def shuffle(self) -> List[int]:
        import random
        for i in range(len(self.arr) - 1, 0, -1):
            j = random.randint(0, i)
            self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
        return self.arr











# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用 Fisher-Yates 洗牌算法（Knuth Shuffle）。
# 1. __init__：保存原始数组的副本和当前数组的副本。
# 2. reset：将当前数组恢复为原始数组的副本，并返回。
# 3. shuffle：从后向前遍历数组，对于每个位置 i，随机选择一个 [0, i] 范围内的索引 j，
#    交换 arr[i] 和 arr[j]。这样保证了每种排列的概率都是 1/n!。
# Fisher-Yates 算法的正确性：第一个位置有 n 种选择，第二个有 n-1 种，...，
# 总共 n! 种等可能结果。
#
# 时间复杂度: O(n) - 初始化和洗牌都是 O(n)，重置也是 O(n)
# 空间复杂度: O(n) - 需要存储原始数组和当前数组的副本
#
# 关键点:
# - Fisher-Yates 算法是均匀随机的洗牌算法
# - 从后向前遍历，每次随机选择 [0, i] 中的一个索引交换
# - 保存原始数组副本以支持 reset 操作
# - random.randint(0, i) 可以选中自身（即不交换），保证均匀分布
