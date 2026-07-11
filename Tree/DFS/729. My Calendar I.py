"""
LeetCode #729 - My Calendar I
中文题名：我的日程安排表 I
https://leetcode.com/problems/my-calendar-i/

Implement a `MyCalendar` class to store your events. A new event can be added if
adding the event will not cause a double booking.

Your class will have the method, `book(int start, int end)`. Formally, this
represents a booking on the half open interval `[start, end)`, the range of real
numbers `x` such that `start <= x < end`.

A double booking happens when two events have some non-empty intersection (ie., there
is some time that is common to both events.)

For each call to the method `MyCalendar.book`, return `true` if the
event can be added to the calendar successfully without causing a double booking. Otherwise,
return `false` and do not add the event to the calendar.

Your class will be called like this: `MyCalendar cal = new MyCalendar();` `MyCalendar.book(start,
end)`

Example 1:

MyCalendar();
MyCalendar.book(10, 20); // returns true
MyCalendar.book(15, 25); // returns false
MyCalendar.book(20, 30); // returns true
Explanation:
The first event can be booked.  The second can't because time 15 is already booked by another event.
The third event can be booked, as the first event takes every time less than 20, but not including 20.

Note:

The number of calls to `MyCalendar.book` per test case will be at most `1000`.

In calls to `MyCalendar.book(start, end)`, `start` and
`end` are integers in the range `[0, 10^9]`.

【中文翻译】
实现一个 MyCalendar 类来存放你的日程安排。如果要添加的时间内没有其他安排，则可以存储这个新的日程安排。

你的类将会有一个方法 book(int start, int end)。形式上，这表示在左闭右开区间 [start, end) 上的一个预订，即实数 x 满足 start <= x < end。

当两个日程安排有一些非空交集时（即，有一些时间被两个日程安排共同占用），就会产生重复预订。

对于每个对方法 MyCalendar.book 的调用，如果可以将日程安排成功添加到日历中而不会导致重复预订，则返回 true。否则，返回 false，并且不要将该日程安排添加到日历中。

你的类将会像这样被调用：MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)

示例 1：

MyCalendar();
MyCalendar.book(10, 20); // 返回 true
MyCalendar.book(15, 25); // 返回 false
MyCalendar.book(20, 30); // 返回 true
解释：
第一个日程安排可以预订。第二个不能预订，因为时间 15 已经被另一个日程安排预订了。
第三个日程安排可以预订，因为第一个日程安排预订了每个小于 20 的时间，但不包括 20。

注意：

每个测试用例调用 MyCalendar.book 的次数最多为 1000。

在调用 MyCalendar.book(start, end) 时，start 和 end 是范围在 [0, 10^9] 内的整数。
"""

from typing import List, Optional


class MyCalendar:

    def __init__(self):
        self.bookings: List[List[int]] = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.bookings:
            if start < e and end > s:
                return False
        self.bookings.append([start, end])
        return True



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 维护一个已预订区间的列表。对于每次 book 调用，遍历所有已有预订：
# 检查新区间 [start, end) 是否与已有区间 [s, e) 重叠。
# 重叠条件：start < e and end > s（两个半开区间的交集非空）。
# 如果没有重叠，将新区间加入列表并返回 True；否则返回 False。
# 也可以使用平衡二叉搜索树（如 sortedcontainers 或自实现）将查询优化到 O(log N)。
#
# 时间复杂度: O(N^2) - N 次 book 调用，每次遍历已有预订 O(N)；使用 BST 可优化到 O(N log N)
# 空间复杂度: O(N) - 存储所有已预订区间
#
# 关键点:
# - 区间是左闭右开 [start, end)，重叠判断需要考虑边界相等不重叠的情况
# - 重叠条件：start < e and end > s（而非 start <= e and end >= s）
# - 数据规模不大 (最多 1000 次调用)，线性扫描足够
# - 进阶：使用线段树或平衡树优化到大范围数据
