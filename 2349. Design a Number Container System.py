"""
LeetCode #2349 - Design a Number Container System
设计数字容器系统
https://leetcode.cn/problems/design-a-number-container-system/

设计一个数字容器系统，可以实现以下功能：
在系统中给定下标处 插入 或者 替换 一个数字。
返回 系统中给定数字的最小下标。
请你实现一个 `NumberContainers` 类：
`NumberContainers()` 初始化数字容器系统。
`void change(int index, int number)` 在下标 `index` 处填入 `number` 。如果该下标 `index` 处已经有数字了，那么用 `number` 替换该数字。
`int find(int number)` 返回给定数字 `number` 在系统中的最小下标。如果系统中没有 `number` ，那么返回 `-1` 。

示例：
输入： ["NumberContainers", "find", "change", "change", "change", "change", "find", "change", "find"] [[], [10], [2, 10], [1, 10], [3, 10], [5, 10], [10], [1, 20], [10]] 输出： [null, -1, null, null, null, null, 1, null, 2]  解释： NumberContainers nc = new NumberContainers(); nc.find(10); // 没有数字 10 ，所以返回 -1 。 nc.change(2, 10); // 容器中下标为 2 处填入数字 10 。 nc.change(1, 10); // 容器中下标为 1 处填入数字 10 。 nc.change(3, 10); // 容器中下标为 3 处填入数字 10 。 nc.change(5, 10); // 容器中下标为 5 处填入数字 10 。 nc.find(10); // 数字 10 所在的下标为 1 ，2 ，3 和 5 。因为最小下标为 1 ，所以返回 1 。 nc.change(1, 20); // 容器中下标为 1 处填入数字 20 。注意，下标 1 处之前为 10 ，现在被替换为 20 。 nc.find(10); // 数字 10 所在下标为 2 ，3 和 5 。最小下标为 2 ，所以返回 2 。

提示：
`1 <= index, number <= 10^9`
调用 `change` 和 `find` 的 总次数 不超过 `10^5` 次。
"""

from typing import List, Optional


import heapq
from collections import defaultdict


class NumberContainers:
    def __init__(self):
        self.idx_to_num: dict = {}
        self.num_to_heap: dict = defaultdict(list)
        self.num_to_indices: dict = defaultdict(set)

    def change(self, index: int, number: int) -> None:
        if index in self.idx_to_num:
            old_num = self.idx_to_num[index]
            if old_num == number:
                return
            self.num_to_indices[old_num].discard(index)

        self.idx_to_num[index] = number
        self.num_to_indices[number].add(index)
        heapq.heappush(self.num_to_heap[number], index)

    def find(self, number: int) -> int:
        if number not in self.num_to_indices or not self.num_to_indices[number]:
            return -1
        heap = self.num_to_heap[number]
        # Lazy deletion: pop indices that are no longer valid
        while heap and heap[0] not in self.num_to_indices[number]:
            heapq.heappop(heap)
        return heap[0] if heap else -1



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Design, Hash Table, Ordered Set, Heap (Priority Queue)
#
# 解题思路:
# 使用三个数据结构：
# 1. idx_to_num: dict 记录 index -> number 的映射，用于 O(1) 查找和替换。
# 2. num_to_indices: defaultdict(set) 记录每个 number 对应的所有有效 index。
# 3. num_to_heap: defaultdict(list) 为每个 number 维护一个小顶堆，用于快速获取最小 index。
# change: 如果 index 已有旧数字，从旧数字的 set 中移除；更新映射，加入新数字的 set 和 heap。
# find: 对数字 number 的堆顶进行懒删除（如果堆顶不在有效 set 中则弹出），返回堆顶。
#
# 时间复杂度: change O(log N), find 均摊 O(log N)
# 空间复杂度: O(N) 其中 N 为 change 调用次数
#
# 关键点:
# - 懒删除策略：不直接从堆中删除旧 index，而是在 find 时跳过无效堆顶
# - set 用于 O(1) 验证 index 有效性
# - Python 没有内置 SortedSet，用 heap + set 组合代替
