"""
LeetCode #1845 - Seat Reservation Manager
中文题名：座位预约管理系统
https://leetcode.com/problems/seat-reservation-manager/

Design a system that manages the reservation state of `n` seats that are numbered from `1` to `n`.

Implement the `SeatManager` class:

`SeatManager(int n)` Initializes a `SeatManager` object that will manage `n` seats numbered from `1` to `n`. All seats are initially available.

`int reserve()` Fetches the smallest-numbered unreserved seat, reserves it, and returns its number.

`void unreserve(int seatNumber)` Unreserves the seat with the given `seatNumber`.

Example 1:

Input
["SeatManager", "reserve", "reserve", "unreserve", "reserve", "reserve", "reserve", "reserve", "unreserve"]
[[5], [], [], [2], [], [], [], [], [5]]
Output
[null, 1, 2, null, 2, 3, 4, 5, null]

Explanation
SeatManager seatManager = new SeatManager(5); // Initializes a SeatManager with 5 seats.
seatManager.reserve();    // All seats are available, so return the lowest numbered seat, which is 1.
seatManager.reserve();    // The available seats are [2,3,4,5], so return the lowest of them, which is 2.
seatManager.unreserve(2); // Unreserve seat 2, so now the available seats are [2,3,4,5].
seatManager.reserve();    // The available seats are [2,3,4,5], so return the lowest of them, which is 2.
seatManager.reserve();    // The available seats are [3,4,5], so return the lowest of them, which is 3.
seatManager.reserve();    // The available seats are [4,5], so return the lowest of them, which is 4.
seatManager.reserve();    // The only available seat is seat 5, so return 5.
seatManager.unreserve(5); // Unreserve seat 5, so now the available seats are [5].

Constraints:

`1 <= n <= 105`

`1 <= seatNumber <= n`

For each call to `reserve`, it is guaranteed that there will be at least one unreserved seat.

For each call to `unreserve`, it is guaranteed that `seatNumber` will be reserved.

At most `105` calls in total will be made to `reserve` and `unreserve`.

【中文翻译】

设计一个系统来管理编号从1到n的n个座位的预约状态。

实现 `SeatManager` 类：
- `SeatManager(int n)`：初始化管理n个座位的对象。
- `int reserve()`：获取编号最小的未预约座位并预约，返回其编号。
- `void unreserve(int seatNumber)`：取消预约给定编号的座位。

示例：
输入：["SeatManager", "reserve", "reserve", "unreserve", "reserve", "reserve", "reserve", "reserve", "unreserve"]
[[5], [], [], [2], [], [], [], [], [5]]
输出：[null, 1, 2, null, 2, 3, 4, 5, null]

"""

from typing import List, Optional


class SeatManager:

    def __init__(self, n: int):
        import heapq
        self.available = list(range(1, n + 1))
        heapq.heapify(self.available)

    def reserve(self) -> int:
        import heapq
        return heapq.heappop(self.available)

    def unreserve(self, seatNumber: int) -> None:
        import heapq
        heapq.heappush(self.available, seatNumber)










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用最小堆维护所有可预约的座位。初始化时将1到n全部入堆。
# reserve()直接从堆顶取出最小座位号。unreserve(seatNumber)将座位号重新入堆。
# 最小堆保证每次reserve都返回当前最小的可用座位号。
#
# 时间复杂度: O(log N) per reserve/unreserve，初始化为O(N)
# 空间复杂度: O(N)，堆的大小
#
# 关键点:
# - 最小堆自动维护最小的可用座位号
# - 不需要额外的"已预约"集合，因为unreserve的座位一定是之前预约过的
# - 注意这里是SeatManager类而不是Solution类
