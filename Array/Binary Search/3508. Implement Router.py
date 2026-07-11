"""
LeetCode #3508 - Implement Router
设计路由器
https://leetcode.cn/problems/implement-router/

请你设计一个数据结构来高效管理网络路由器中的数据包。每个数据包包含以下属性：
`source`：生成该数据包的机器的唯一标识符。
`destination`：目标机器的唯一标识符。
`timestamp`：该数据包到达路由器的时间戳。
实现 `Router` 类：
`Router(int memoryLimit)`：初始化路由器对象，并设置固定的内存限制。
`memoryLimit` 是路由器在任意时间点可以存储的 最大 数据包数量。
如果添加一个新数据包会超过这个限制，则必须移除 最旧的 数据包以腾出空间。
`bool addPacket(int source, int destination, int timestamp)`：将具有给定属性的数据包添加到路由器。
如果路由器中已经存在一个具有相同 `source`、`destination` 和 `timestamp` 的数据包，则视为重复数据包。
如果数据包成功添加（即不是重复数据包），返回 `true`；否则返回 `false`。
`int[] forwardPacket()`：以 FIFO（先进先出）顺序转发下一个数据包。
从存储中移除该数据包。
以数组 `[source, destination, timestamp]` 的形式返回该数据包。
如果没有数据包可以转发，则返回空数组。
`int getCount(int destination, int startTime, int endTime)`：
返回当前存储在路由器中（即尚未转发）的，且目标地址为指定 `destination` 且时间戳在范围 `[startTime, endTime]`（包括两端）内的数据包数量。
注意：对于 `addPacket` 的查询会按照 `timestamp` 的非递减顺序进行。

示例 1：

输入：
["Router", "addPacket", "addPacket", "addPacket", "addPacket", "addPacket", "forwardPacket", "addPacket", "getCount"]
[[3], [1, 4, 90], [2, 5, 90], [1, 4, 90], [3, 5, 95], [4, 5, 105], [], [5, 2, 110], [5, 100, 110]]
输出：
[null, true, true, false, true, true, [2, 5, 90], true, 1]
解释： `Router router = new Router(3);` // 初始化路由器，内存限制为 3。
`router.addPacket(1, 4, 90);` // 数据包被添加，返回 True。
`router.addPacket(2, 5, 90);` // 数据包被添加，返回 True。
`router.addPacket(1, 4, 90);` // 这是一个重复数据包，返回 False。
`router.addPacket(3, 5, 95);` // 数据包被添加，返回 True。
`router.addPacket(4, 5, 105);` // 数据包被添加，`[1, 4, 90]` 被移除，因为数据包数量超过限制，返回 True。
`router.forwardPacket();` // 转发数据包 `[2, 5, 90]` 并将其从路由器中移除。
`router.addPacket(5, 2, 110);` // 数据包被添加，返回 True。
`router.getCount(5, 100, 110);` // 唯一目标地址为 5 且时间在 `[100, 110]` 范围内的数据包是 `[4, 5, 105]`，返回 1。
示例 2：

输入：
["Router", "addPacket", "forwardPacket", "forwardPacket"]
[[2], [7, 4, 90], [], []]
输出：
[null, true, [7, 4, 90], []]
解释： `Router router = new Router(2);` // 初始化路由器，内存限制为 2。
`router.addPacket(7, 4, 90);` // 返回 True。
`router.forwardPacket();` // 返回 `[7, 4, 90]`。
`router.forwardPacket();` // 没有数据包可以转发，返回 `[]`。

提示：
`2 <= memoryLimit <= 10^5`
`1 <= source, destination <= 2 * 10^5`
`1 <= timestamp <= 10^9`
`1 <= startTime <= endTime <= 10^9`
`addPacket`、`forwardPacket` 和 `getCount` 方法的总调用次数最多为 `10^5`。
对于 `addPacket` 的查询，`timestamp` 按非递减顺序给出。
"""

from typing import List, Optional


class Router:

    def __init__(self, memoryLimit: int):
        from collections import deque
        self.limit = memoryLimit
        self.queue = deque()            # (source, dest, timestamp)
        self.seen = set()               # (source, dest, timestamp) for dedup
        # For each destination: list of timestamps + head pointer for lazy deletion
        self.dest_lists = {}            # dest -> list of timestamps
        self.dest_heads = {}            # dest -> head index

    def _evict_one(self):
        src, dst, ts = self.queue.popleft()
        self.seen.discard((src, dst, ts))
        self.dest_heads[dst] += 1

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        key = (source, destination, timestamp)
        if key in self.seen:
            return False
        self.seen.add(key)
        self.queue.append(key)

        if destination not in self.dest_lists:
            self.dest_lists[destination] = []
            self.dest_heads[destination] = 0
        self.dest_lists[destination].append(timestamp)

        if len(self.queue) > self.limit:
            self._evict_one()
        return True

    def forwardPacket(self) -> List[int]:
        if not self.queue:
            return []
        src, dst, ts = self.queue.popleft()
        self.seen.discard((src, dst, ts))
        self.dest_heads[dst] += 1
        return [src, dst, ts]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        if destination not in self.dest_lists:
            return 0
        from bisect import bisect_left, bisect_right
        lst = self.dest_lists[destination]
        head = self.dest_heads[destination]
        left = bisect_left(lst, startTime, head)
        right = bisect_right(lst, endTime, left)
        return right - left



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Design, Queue, Array, Hash Table, Binary Search, Ordered Set
#
# 解题思路:
# 1. 使用 deque 维护 FIFO 队列，set 进行去重
# 2. 对于 getCount(dest, start, end)：
#    - 每个 destination 维护一个按时间戳排序的列表
#    - 由于 addPacket 的 timestamp 非递减，列表自然有序
#    - 使用 head 指针进行延迟删除（forwardPacket 时只需 head++）
#    - 查询时在 [head:] 范围内二分查找 start 和 end
# 3. 当队列超 memoryLimit 时，evict 最旧数据包
#
# 时间复杂度: addPacket O(1), forwardPacket O(1), getCount O(log N)
# 空间复杂度: O(N) where N = memoryLimit
#
# 关键点:
# - timestamp 非递减顺序保证列表有序
# - head 指针延迟删除避免 O(N) 删除开销
# - bisect_left/bisect_right 计算范围计数
