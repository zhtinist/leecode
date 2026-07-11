"""
LeetCode #406 - Queue Reconstruction by Height
中文题名：根据身高重建队列
https://leetcode.com/problems/queue-reconstruction-by-height/

Suppose you have a random list of people standing in a queue. Each person is described by a
pair of integers `(h, k)`, where `h` is the height of the person and
`k` is the number of people in front of this person who have a height greater
than or equal to `h`. Write an algorithm to reconstruct the queue.

Note:

The number of people is less than 1,100.

Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

【中文翻译】
假设有一群按随机顺序排队的人。每个人由一对整数 (h, k) 描述，其中 h 是这个人的身高，
k 是排在这个人前面且身高大于或等于 h 的人数。编写算法重建这个队列。

注意：
    总人数小于 1,100。

示例：
    输入：[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
    输出：[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
"""

from typing import List, Optional


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # Sort by height descending; for same height, sort by k ascending
        people.sort(key=lambda x: (-x[0], x[1]))

        result = []
        for p in people:
            result.insert(p[1], p)  # Insert at index k

        return result


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 贪心 + 插入排序。
# 1. 按身高 h 降序排列；身高相同时按 k 升序排列。
#    这样保证先处理高的人，后处理矮的人。
# 2. 遍历排序后的数组，将每个人插入到结果数组的第 k 个位置。
#
# 原理：因为先插入的都是身高更高（或相等）的人，插入时已经存在于结果数组中的人
# 身高都 >= 当前人的身高。把当前人插入到第 k 个位置，正好满足他前面有 k 个
# 身高 >= 他的人。后续插入的矮个子不会影响高个子的 k 值（因为矮个子插在任何位置
# 都不会增加高个子前面 >= 自己身高的人数）。
#
# 时间复杂度: O(N^2) — 每次 insert 最坏 O(N)，共 N 次
# 空间复杂度: O(N) — 结果数组
#
# 关键点:
# - 排序策略：身高降序，同身高时 k 升序
# - 贪心思想：先处理高的，矮的插入不影响高者的 k 值
# - insert(index, value) 将元素插入到指定索引位置
