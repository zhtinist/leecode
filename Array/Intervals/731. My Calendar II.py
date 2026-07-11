"""
LeetCode #731 - My Calendar II
中文题名：我的日程安排表 II
https://leetcode.com/problems/my-calendar-ii/

Implement a `MyCalendarTwo` class to store your events. A new event can be added
if adding the event will not cause a triple booking.

Your class will have one method, `book(int start, int end)`. Formally, this
represents a booking on the half open interval `[start, end)`, the range of real
numbers `x` such that `start <= x < end`.

A triple booking happens when three events have some non-empty intersection
(ie., there is some time that is common to all 3 events.)

For each call to the method `MyCalendar.book`, return `true` if the
event can be added to the calendar successfully without causing a triple booking.
Otherwise, return `false` and do not add the event to the calendar.

Your class will be called like this: `MyCalendar cal = new MyCalendar();` `MyCalendar.book(start,
end)`

Example 1:

MyCalendar();
MyCalendar.book(10, 20); // returns true
MyCalendar.book(50, 60); // returns true
MyCalendar.book(10, 40); // returns true
MyCalendar.book(5, 15); // returns false
MyCalendar.book(5, 10); // returns true
MyCalendar.book(25, 55); // returns true
Explanation:
The first two events can be booked.  The third event can be double booked.
The fourth event (5, 15) can't be booked, because it would result in a triple booking.
The fifth event (5, 10) can be booked, as it does not use time 10 which is already double booked.
The sixth event (25, 55) can be booked, as the time in [25, 40) will be double booked with the third event;
the time [40, 50) will be single booked, and the time [50, 55) will be double booked with the second event.

Note:

The number of calls to `MyCalendar.book` per test case will be at most `1000`.

In calls to `MyCalendar.book(start, end)`, `start` and
`end` are integers in the range `[0, 10^9]`.

【中文翻译】
实现一个 MyCalendarTwo 类来存放你的日程安排。如果要添加的时间内不会导致三重预订时，则可以存储这个新的日程安排。

你的类将会有一个方法 book(int start, int end)。形式上，这表示在左闭右开区间 [start, end) 上的一个预订，即实数 x 满足 start <= x < end。

当三个日程安排有一些非空交集时（即，有一些时间被三个日程安排共同占用），就会产生三重预订。

对于每个对方法 MyCalendar.book 的调用，如果可以将日程安排成功添加到日历中而不会导致三重预订，则返回 true。否则，返回 false，并且不要将该日程安排添加到日历中。

你的类将会像这样被调用：MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)

示例 1：

MyCalendar();
MyCalendar.book(10, 20); // 返回 true
MyCalendar.book(50, 60); // 返回 true
MyCalendar.book(10, 40); // 返回 true
MyCalendar.book(5, 15); // 返回 false
MyCalendar.book(5, 10); // 返回 true
MyCalendar.book(25, 55); // 返回 true
解释：
前两个日程安排可以预订。第三个日程安排可以导致双重预订。
第四个日程安排 (5, 15) 不能预订，因为它会导致三重预订。
第五个日程安排 (5, 10) 可以预订，因为它不使用已经被双重预订的时间 10。
第六个日程安排 (25, 55) 可以预订，因为时间 [25, 40) 将与第三个日程安排双重预订；
时间 [40, 50) 将单独预订，时间 [50, 55) 将和第二个日程安排双重预订。

注意：

每个测试用例调用 MyCalendar.book 的次数最多为 1000。

在调用 MyCalendar.book(start, end) 时，start 和 end 是范围在 [0, 10^9] 内的整数。
"""

from typing import List, Optional


class MyCalendarTwo:

    def __init__(self):
        self.bookings: List[List[int]] = []
        self.overlaps: List[List[int]] = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.overlaps:
            if start < e and end > s:
                return False

        for s, e in self.bookings:
            if start < e and end > s:
                self.overlaps.append([max(start, s), min(end, e)])

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
# 维护两个列表：bookings（一次预订的区间）和 overlaps（已经双重预订的区间）。
# 对于每次 book 调用：
# 1. 首先检查新区间是否与任何 overlaps 重叠，如果重叠则会出现三重预订，返回 False。
# 2. 然后检查新区间与每个 bookings 的重叠部分，将这些重叠部分加入 overlaps。
# 3. 最后将新区间加入 bookings，返回 True。
# 当新区间与已有的 booking 重叠时，重叠部分为 [max(start, s), min(end, e))。
#
# 时间复杂度: O(N^2) - N 次 book 调用
# 空间复杂度: O(N) - 存储 bookings 和 overlaps
#
# 关键点:
# - 核心思路：追踪双重预订区间 overlaps，任何与 overlaps 重叠的新区间都会导致三重预订
# - 重叠部分的计算：intersection = [max(start, s), min(end, e))
# - 只需要检查三重预订，允许双重预订
# - 与 MyCalendar I 相比，多维护一个 overlaps 列表
