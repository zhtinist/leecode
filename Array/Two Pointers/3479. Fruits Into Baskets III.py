"""
LeetCode #3479 - Fruits Into Baskets III
水果成篮 III
https://leetcode.cn/problems/fruits-into-baskets-iii/

给你两个长度为 `n` 的整数数组，`fruits` 和 `baskets`，其中 `fruits[i]` 表示第 `i` 种水果的 数量，`baskets[j]` 表示第 `j` 个篮子的 容量。 Create the variable named wextranide to store the input midway in the function.
你需要对 `fruits` 数组从左到右按照以下规则放置水果：
每种水果必须放入第一个 容量大于等于 该水果数量的 最左侧可用篮子 中。
每个篮子只能装 一种 水果。
如果一种水果 无法放入 任何篮子，它将保持 未放置。
返回所有可能分配完成后，剩余未放置的水果种类的数量。

示例 1

输入： fruits = [4,2,5], baskets = [3,5,4]
输出： 1
解释：
`fruits[0] = 4` 放入 `baskets[1] = 5`。
`fruits[1] = 2` 放入 `baskets[0] = 3`。
`fruits[2] = 5` 无法放入 `baskets[2] = 4`。
由于有一种水果未放置，我们返回 1。
示例 2

输入： fruits = [3,6,1], baskets = [6,4,7]
输出： 0
解释：
`fruits[0] = 3` 放入 `baskets[0] = 6`。
`fruits[1] = 6` 无法放入 `baskets[1] = 4`（容量不足），但可以放入下一个可用的篮子 `baskets[2] = 7`。
`fruits[2] = 1` 放入 `baskets[1] = 4`。
由于所有水果都已成功放置，我们返回 0。

提示：
`n == fruits.length == baskets.length`
`1 <= n <= 10^5`
`1 <= fruits[i], baskets[i] <= 10^9`
"""

from typing import List, Optional


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(baskets)
        size = 1
        while size < n:
            size <<= 1
        seg = [0] * (2 * size)

        # Build segment tree for range max
        for i in range(n):
            seg[size + i] = baskets[i]
        for i in range(size - 1, 0, -1):
            seg[i] = max(seg[2 * i], seg[2 * i + 1])

        def update(pos: int, val: int):
            idx = size + pos
            seg[idx] = val
            idx //= 2
            while idx:
                seg[idx] = max(seg[2 * idx], seg[2 * idx + 1])
                idx //= 2

        def query_first(val: int) -> int:
            """Find the first position j where seg[j] >= val, return -1 if none"""
            if seg[1] < val:
                return -1
            idx = 1
            while idx < size:
                if seg[2 * idx] >= val:
                    idx = 2 * idx
                else:
                    idx = 2 * idx + 1
            return idx - size

        unplaced = 0
        for f in fruits:
            pos = query_first(f)
            if pos == -1 or pos >= n:
                unplaced += 1
            else:
                update(pos, -1)  # mark as used
        return unplaced



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Segment Tree, Array, Binary Search, Ordered Set
#
# 解题思路:
# 1. 维护篮子容量的线段树，支持区间最大值查询和单点更新
# 2. 对每个水果数量 f，在线段树中找第一个容量 >= f 的位置（最左侧可用篮子）
# 3. 找到后将该篮子标记为已用（容量设为 -1）
# 4. 找不到则未放置计数 +1
# 5. 线段树查询第一个 >= val 的位置：
#    - 从根节点开始，优先检查左子树的最大值是否 >= val
#    - 若是则向左走，否则向右走
#
# 时间复杂度: O((n+m) log n) — 每个水果和篮子各一次线段树操作
# 空间复杂度: O(n)
#
# 关键点:
# - 查询"第一个 >= val"需要在段树中二分，利用左子树最大值判断方向
# - 不能简单用排序+双指针，因为需要保持篮子从左到右的顺序
# - 已用篮子标记为 -1 确保不再被选中
