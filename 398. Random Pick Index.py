"""
LeetCode #398 - Random Pick Index
中文题名：随机数索引
https://leetcode.com/problems/random-pick-index/

Given an array of integers with possible duplicates, randomly output the index of a given
target number. You can assume that the given target number must exist in the array.

Note:

The array size can be very large. Solution that uses too much extra space will not pass the
judge.

Example:

int[] nums = new int[] {1,2,3,3,3};
Solution solution = new Solution(nums);

// pick(3) should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
solution.pick(3);

// pick(1) should return 0. Since in the array only nums[0] is equal to 1.
solution.pick(1);

【中文翻译】
给定一个可能包含重复元素的整数数组，要求随机输出给定目标数字的索引。你可以假设给定的目标数字一定存在于数组中。

注意：

数组的大小可能非常大。使用过多额外空间的解决方案将无法通过评测。

示例：

int[] nums = new int[] {1, 2, 3, 3, 3};
Solution solution = new Solution(nums);

// pick(3) 应该返回索引 2、3 或 4，每个索引应有相等的返回概率。
solution.pick(3);

// pick(1) 应该返回 0，因为数组中只有 nums[0] 等于 1。
solution.pick(1);
"""

from typing import List, Optional
import random


class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        count = 0
        res = -1
        for i, num in enumerate(self.nums):
            if num == target:
                count += 1
                if random.randint(1, count) == 1:
                    res = i
        return res











# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用蓄水池抽样算法（Reservoir Sampling）。
# 遍历整个数组，当遇到目标数字时：
# - count 加 1（记录当前遇到了第几个目标数字）
# - 以 1/count 的概率选择当前索引作为结果
# 遍历结束后，每个目标数字的索引被选中的概率均为 1/总数。
# 这个算法保证了 O(1) 空间，不依赖哈希表存储所有索引。
#
# 时间复杂度: 初始化 O(1)；pick O(n) - 需要遍历整个数组
# 空间复杂度: O(1) - 不使用额外的数据结构存储索引
#
# 关键点:
# - 蓄水池抽样：每次以 1/count 的概率替换结果，保证等概率
# - 第 i 个目标索引被选中的概率 = 1/i * i/(i+1) * ... * (n-1)/n = 1/n
# - 无需预处理存储映射表，适合内存受限和大数据流场景
# - 每次 pick 都要遍历整个数组，如频繁调用可考虑哈希表预处理
