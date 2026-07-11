"""
LeetCode #1146 - Snapshot Array
中文题名：快照数组
https://leetcode.com/problems/snapshot-array/

Implement a SnapshotArray that supports the following interface:

`SnapshotArray(int length)` initializes an array-like data structure with the
given length.  Initially, each element equals 0.

`void set(index, val)` sets the element at the given `index` to be
equal to `val`.

`int snap()` takes a snapshot of the array and returns the
`snap_id`: the total number of times we called `snap()` minus
`1`.

`int get(index, snap_id)` returns the value at the given
`index`, at the time we took the snapshot with the given `snap_id`

Example 1:

Input: ["SnapshotArray","set","snap","set","get"]
[[3],[0,5],[],[0,6],[0,0]]
Output: [null,null,0,null,5]
Explanation:
SnapshotArray snapshotArr = new SnapshotArray(3); // set the length to be 3
snapshotArr.set(0,5);  // Set array[0] = 5
snapshotArr.snap();  // Take a snapshot, return snap_id = 0
snapshotArr.set(0,6);
snapshotArr.get(0,0);  // Get the value of array[0] with snap_id = 0, return 5

Constraints:

`1 <= length <= 50000`

At most `50000` calls will be made to `set`,
`snap`, and `get`.

`0 <= index < length`

`0 <= snap_id < `(the total number of times we call `snap()`)

`0 <= val <= 10^9`

【中文翻译】
实现一个 SnapshotArray 类，支持以下接口：

SnapshotArray(int length)：初始化一个具有给定长度的数组型数据结构。初始时，每个元素等于 0。

void set(index, val)：将给定索引 index 处的元素设置为 val。

int snap()：获取数组的快照，并返回 snap_id：即调用 snap() 的总次数减 1。

int get(index, snap_id)：返回给定索引 index 在给定 snap_id 时刻被快照时存储的值。

示例 1：

输入：["SnapshotArray","set","snap","set","get"]
[[3],[0,5],[],[0,6],[0,0]]
输出：[null,null,0,null,5]
解释：
SnapshotArray snapshotArr = new SnapshotArray(3); // 设置长度为 3
snapshotArr.set(0,5);  // 设置 array[0] = 5
snapshotArr.snap();  // 获取快照，返回 snap_id = 0
snapshotArr.set(0,6);
snapshotArr.get(0,0);  // 获取 snap_id = 0 时 array[0] 的值，返回 5

约束条件：

`1 <= length <= 50000`

最多会对 set、snap 和 get 进行 50000 次调用。

`0 <= index < length`

`0 <= snap_id < `（调用 snap() 的总次数）

`0 <= val <= 10^9`
"""

from typing import List, Optional


class SnapshotArray:

    def __init__(self, length: int):
        # self.data[i] = list of (snap_id, value) pairs
        self.data = [[(0, 0)] for _ in range(length)]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        # If the last entry has the same snap_id, update it
        # Otherwise, append a new entry
        history = self.data[index]
        if history[-1][0] == self.snap_id:
            history[-1] = (self.snap_id, val)
        else:
            history.append((self.snap_id, val))

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        history = self.data[index]
        # Binary search for the latest value at or before snap_id
        import bisect
        # bisect_right on snap_id values, then go back one
        pos = bisect.bisect_right(history, snap_id, key=lambda x: x[0])
        return history[pos - 1][1]










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用"每个索引维护变更历史"的策略，节省内存同时支持快速查询：
# 1. 数据结构：self.data[i] 是一个列表，存储 (snap_id, val) 的二元组，
#    表示在第 snap_id 次快照时索引 i 的值变为 val。
#    初始化时每个索引都有一个快照 0，值为 0，即 [(0, 0)]。
# 2. set 操作：如果当前 snap_id 已经有记录（在同一快照周期内多次 set），
#    直接更新最后一条记录；否则追加一条新记录。
# 3. snap 操作：snap_id 自增 1，返回旧值。不进行数据复制。
# 4. get 操作：在 data[index] 的历史列表中，使用二分查找找到
#    snap_id <= 给定 snap_id 的最后一条记录，返回其值。
# 这种设计避免了每次快照时复制整个数组，空间复杂度取决于 set 操作次数。
#
# 时间复杂度:
#   - 构造: O(length)
#   - set: O(1)
#   - snap: O(1)
#   - get: O(log S)，其中 S 是对该索引的 set 次数
# 空间复杂度: O(length + 总 set 次数) - 每个索引维护历史列表
#
# 关键点:
# - 不复制整个数组，每个索引只记录变更历史
# - 使用二分查找在历史记录中定位正确的快照版本
# - 在同一快照周期内多次 set 时合并记录，节省空间
# - bisect_right 配合 key 参数在 Python 3.10+ 可用
