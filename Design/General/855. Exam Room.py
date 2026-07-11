"""
LeetCode #855 - Exam Room
中文题名：考场就座
https://leetcode.com/problems/exam-room/

In an exam room, there are `N` seats in a single row, numbered `0, 1, 2, ...,
N-1`.

When a student enters the room, they must sit in the seat that maximizes the distance to the
closest person.  If there are multiple such seats, they sit in the seat with the lowest
number.  (Also, if no one is in the room, then the student sits at seat number 0.)

Return a class `ExamRoom(int N)` that exposes two functions: `ExamRoom.seat()` returning
an `int` representing what seat the student sat in, and `ExamRoom.leave(int
p)` representing that the student in seat number `p` now
leaves the room.  It is guaranteed that any calls to `ExamRoom.leave(p)`
have a student sitting in seat `p`.

Example 1:

Input: ["ExamRoom","seat","seat","seat","seat","leave","seat"], [[10],[],[],[],[],[4],[]]
Output: [null,0,9,4,2,null,5]
Explanation:
ExamRoom(10) -> null
seat() -> 0, no one is in the room, then the student sits at seat number 0.
seat() -> 9, the student sits at the last seat number 9.
seat() -> 4, the student sits at the last seat number 4.
seat() -> 2, the student sits at the last seat number 2.
leave(4) -> null
seat() -> 5, the student sits at the last seat number 5.

​​​​​​​

Note:

`1 <= N <= 10^9`

`ExamRoom.seat()` and `ExamRoom.leave()` will be called at most
`10^4` times across all test cases.

Calls to `ExamRoom.leave(p)` are guaranteed to have a student currently
sitting in seat number `p`.

【中文翻译】
在考场中，有 N 个座位排成一行，编号为 0, 1, 2, ..., N-1。

当一个学生进入考场时，他必须坐在能最大化与他最近的人距离的座位上。如果有多个这样的座位，他坐在编号最小的座位上。（另外，如果考场没人，则学生坐在 0 号座位。）

实现一个 ExamRoom 类，暴露两个函数：
- ExamRoom.seat() 返回一个整数，表示学生所坐的座位编号。
- ExamRoom.leave(p) 表示坐在座位 p 的学生离开考场。
保证任何 ExamRoom.leave(p) 的调用都确实有一个学生坐在座位 p 上。

"""

from typing import List, Optional


class ExamRoom:

    def __init__(self, n: int):
        self.n = n
        self.seats = []  # sorted list of occupied seat numbers

    def seat(self) -> int:
        if not self.seats:
            self.seats.append(0)
            return 0

        # Maximum distance found so far and the corresponding seat
        max_dist = self.seats[0]  # from 0 to first occupied seat
        best_seat = 0

        # Check gaps between adjacent occupied seats
        for i in range(1, len(self.seats)):
            left = self.seats[i - 1]
            right = self.seats[i]
            # Candidate seat in the middle of the gap
            mid = (left + right) // 2
            dist = mid - left  # distance to closest person
            if dist > max_dist:
                max_dist = dist
                best_seat = mid

        # Check the gap from the last occupied seat to the end
        last = self.seats[-1]
        if self.n - 1 - last > max_dist:
            best_seat = self.n - 1

        # Insert the chosen seat into the sorted list
        import bisect
        idx = bisect.bisect_left(self.seats, best_seat)
        self.seats.insert(idx, best_seat)
        return best_seat

    def leave(self, p: int) -> None:
        self.seats.remove(p)


# LeetCode expects class ExamRoom directly for this design problem.
# The Solution alias is provided for local testing convenience.
class Solution:
    def __init__(self, n: int):
        self.room = ExamRoom(n)
    def seat(self) -> int:
        return self.room.seat()
    def leave(self, p: int) -> None:
        self.room.leave(p)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 维护一个有序列表 self.seats 存储已占用的座位编号。
# seat() 方法：
# - 如果列表为空，学生坐 0 号座位。
# - 遍历相邻座位对 (left, right)，计算中间位置 mid = (left+right)//2，
#   距离最近的人是 mid-left。记录距离最大的座位。
# - 还需要检查两个边界：从 0 到第一个座位、从最后一个座位到 N-1。
# - 使用 bisect 将新座位插入有序列表保持升序。
# leave(p) 方法：直接从列表中移除 p。
# 注意：N 可达 10^9，不能遍历所有座位，但调用次数最多 10^4，所以遍历已占用的座位是可行的。
#
# 时间复杂度: seat() O(K) 其中 K 是当前已占座位数；leave() O(K)
# 空间复杂度: O(K) 存储已占座位列表
#
# 关键点:
# - 维护有序的已占座位列表（使用 bisect 插入）
# - 选择座位时需要检查三种情况：第一个座位到0、两座位之间、最后一个座位到N-1
# - 距离最近的"人" = 座位之间距离的一半（向左取整，因为要选编号最小的）
# - 注意边界条件：考场空时坐0号；以及最后到 N-1 的距离不需要除以2
