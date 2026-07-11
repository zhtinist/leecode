"""
LeetCode #1670 - Design Front Middle Back Queue
中文题名：设计前中后队列
https://leetcode.com/problems/design-front-middle-back-queue/

Design a queue that supports `push` and `pop` operations in
the front, middle, and back.

Implement the `FrontMiddleBack` class:

`FrontMiddleBack()` Initializes the queue.

`void pushFront(int val)` Adds `val` to the
front of the queue.

`void pushMiddle(int val)` Adds `val` to the middle
of the queue.

`void pushBack(int val)` Adds `val` to the
back of the queue.

`int popFront()` Removes the front element of the
queue and returns it. If the queue is empty, return `-1`.

`int popMiddle()` Removes the middle element of the
queue and returns it. If the queue is empty, return `-1`.

`int popBack()` Removes the back element of the
queue and returns it. If the queue is empty, return `-1`.

Notice that when there are two middle position choices, the
operation is performed on the frontmost middle position choice. For
example:

Pushing `6` into the middle of `[1, 2, 3, 4, 5]` results
in `[1, 2, 6, 3, 4, 5]`.

Popping the middle from `[1, 2, 3, 4, 5, 6]` returns
`3` and results in `[1, 2, 4, 5, 6]`.

Example 1:

Input:
["FrontMiddleBackQueue", "pushFront", "pushBack", "pushMiddle", "pushMiddle", "popFront", "popMiddle", "popMiddle", "popBack", "popFront"]
[[], [1], [2], [3], [4], [], [], [], [], []]
Output:
[null, null, null, null, null, 1, 3, 4, 2, -1]

Explanation:
FrontMiddleBackQueue q = new FrontMiddleBackQueue();
q.pushFront(1);   // [1]
q.pushBack(2);    // [1, 2]
q.pushMiddle(3);  // [1, 3, 2]
q.pushMiddle(4);  // [1, 4, 3, 2]
q.popFront();     // return 1 -> [4, 3, 2]
q.popMiddle();    // return 3 -> [4, 2]
q.popMiddle();    // return 4 -> [2]
q.popBack();      // return 2 -> []
q.popFront();     // return -1 -> [] (The queue is empty)

Constraints:

`1 <= val <= 109`

At most `1000` calls will be made
to `pushFront`, `pushMiddle`, `pushBack`,
`popFront`, `popMiddle`, and `popBack`.

【中文翻译】
设计一个支持在前端、中间和后端进行push和pop操作的队列。

实现FrontMiddleBack类：

- FrontMiddleBack() 初始化队列。
- void pushFront(int val) 将val添加到队列的前端。
- void pushMiddle(int val) 将val添加到队列的中间。
- void pushBack(int val) 将val添加到队列的后端。
- int popFront() 移除队列的前端元素并返回它。如果队列为空，返回-1。
- int popMiddle() 移除队列的中间元素并返回它。如果队列为空，返回-1。
- int popBack() 移除队列的后端元素并返回它。如果队列为空，返回-1。

注意当有两个中间位置时，操作会在更靠前的中间位置上执行。例如：
向[1,2,3,4,5]的中间插入6，得到[1,2,6,3,4,5]。
从[1,2,3,4,5,6]的中间弹出，返回3，得到[1,2,4,5,6]。

示例1：

输入：
["FrontMiddleBackQueue", "pushFront", "pushBack", "pushMiddle", "pushMiddle", "popFront", "popMiddle", "popMiddle", "popBack", "popFront"]
[[], [1], [2], [3], [4], [], [], [], [], []]
输出：
[null, null, null, null, null, 1, 3, 4, 2, -1]

解释：
FrontMiddleBackQueue q = new FrontMiddleBackQueue();
q.pushFront(1);   // [1]
q.pushBack(2);    // [1, 2]
q.pushMiddle(3);  // [1, 3, 2]
q.pushMiddle(4);  // [1, 4, 3, 2]
q.popFront();     // 返回 1 -> [4, 3, 2]
q.popMiddle();    // 返回 3 -> [4, 2]
q.popMiddle();    // 返回 4 -> [2]
q.popBack();      // 返回 2 -> []
q.popFront();     // 返回 -1 -> [] (队列为空)

约束条件：

1 <= val <= 10^9
最多调用1000次pushFront、pushMiddle、pushBack、popFront、popMiddle和popBack。

"""

from typing import List, Optional


from collections import deque


class FrontMiddleBackQueue:

    def __init__(self):
        # left和right是两个双端队列
        # 始终保持：len(left) == len(right) 或 len(left) == len(right) + 1
        self.left = deque()
        self.right = deque()

    def _balance(self):
        """调整两个队列的大小使之满足不变量"""
        # left 过多
        if len(self.left) > len(self.right) + 1:
            self.right.appendleft(self.left.pop())
        # right 过多
        if len(self.right) > len(self.left):
            self.left.append(self.right.popleft())

    def pushFront(self, val: int) -> None:
        self.left.appendleft(val)
        self._balance()

    def pushMiddle(self, val: int) -> None:
        # 中间位置在 left 的末尾（当前 left 数量比 right 相等或多一个时，中间是 left 的最后一个）
        if len(self.left) > len(self.right):
            # left比right多一个，中间在left末尾和right开头之间
            # 先把left最后一个移到right开头，然后新值放在left末尾
            self.right.appendleft(self.left.pop())
        self.left.append(val)
        self._balance()

    def pushBack(self, val: int) -> None:
        self.right.append(val)
        self._balance()

    def popFront(self) -> int:
        if not self.left and not self.right:
            return -1
        if self.left:
            val = self.left.popleft()
        else:
            val = self.right.popleft()
        self._balance()
        return val

    def popMiddle(self) -> int:
        if not self.left and not self.right:
            return -1
        # 中间位置：如果len(left)==len(right)，中间是left的最后一个
        # 如果len(left)==len(right)+1，中间也是left的最后一个
        if len(self.left) == len(self.right):
            # 中间在 left 末尾
            val = self.left.pop()
        else:
            # len(left) > len(right)，中间在 left 末尾
            val = self.left.pop()
        self._balance()
        return val

    def popBack(self) -> int:
        if not self.left and not self.right:
            return -1
        if self.right:
            val = self.right.pop()
        else:
            val = self.left.pop()
        self._balance()
        return val


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用两个双端队列（left和right）来维护前中后队列。
# 保持不变量：len(left) == len(right) 或 len(left) == len(right) + 1。
# 这样中间位置总是left的最后一个元素。
# 每次操作后调用_balance()进行再平衡。
# - pushFront: 添加到left的左端
# - pushMiddle: 如果left比right多一个，先将left末尾移到right开头，再添加到left末尾
# - pushBack: 添加到right的右端
# - popFront/popMiddle/popBack: 根据两个队列的状态从相应位置弹出
#
# 时间复杂度: O(1) 平均每次操作
# 空间复杂度: O(n)，n为队列中的元素数量
#
# 关键点:
# - 两个deque的不变量：left始终有相等或多一个元素
# - 中间位置始终是left的最后一个元素
# - 每次操作后调用_balance保持不变量
# - pushMiddle时特殊的处理逻辑
