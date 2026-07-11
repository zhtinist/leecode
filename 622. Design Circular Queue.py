"""
LeetCode #622 - Design Circular Queue
中文题名：设计循环队列
https://leetcode.com/problems/design-circular-queue/

Design your implementation of the circular queue. The circular queue is a linear data
structure in which the operations are performed based on FIFO (First In First Out) principle
and the last position is connected back to the first position to make a circle. It is also
called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces in front of
the queue. In a normal queue, once the queue becomes full, we cannot insert the next element
even if there is a space in front of the queue. But using the circular queue, we can use the
space to store new values.

Your implementation should support following operations:

`MyCircularQueue(k)`: Constructor, set the size of the queue to be k.

`Front`: Get the front item from the queue. If the queue is empty, return -1.

`Rear`: Get the last item from the queue. If the queue is empty, return -1.

`enQueue(value)`: Insert an element into the circular queue. Return true if
the operation is successful.

`deQueue()`: Delete an element from the circular queue. Return true if the
operation is successful.

`isEmpty()`: Checks whether the circular queue is empty or not.

`isFull()`: Checks whether the circular queue is full or not.

Example:

MyCircularQueue circularQueue = new MyCircularQueue(3); // set the size to be 3
circularQueue.enQueue(1);  // return true
circularQueue.enQueue(2);  // return true
circularQueue.enQueue(3);  // return true
circularQueue.enQueue(4);  // return false, the queue is full
circularQueue.Rear();  // return 3
circularQueue.isFull();  // return true
circularQueue.deQueue();  // return true
circularQueue.enQueue(4);  // return true
circularQueue.Rear();  // return 4

Note:

All values will be in the range of [0, 1000].

The number of operations will be in the range of [1, 1000].

Please do not use the built-in Queue library.

【中文翻译】
设计一个循环队列的完整实现。循环队列是一种线性数据结构，其操作基于 FIFO（先进先出）原则，
并且队尾位置连接到队首位置形成一个圆圈。它也被称为"环形缓冲区"。

循环队列的一个好处是我们可以利用队列前面的空间。在普通队列中，一旦队列满了，
即使队列前面有空间，我们也不能插入下一个元素。但使用循环队列，我们可以用这个空间来存储新值。

你的实现应该支持以下操作：

`MyCircularQueue(k)`：构造器，设置队列长度为 k。

`Front`：从队首获取元素。如果队列为空，返回 -1。

`Rear`：获取队尾元素。如果队列为空，返回 -1。

`enQueue(value)`：向循环队列插入一个元素。如果成功插入则返回 true。

`deQueue()`：从循环队列中删除一个元素。如果成功删除则返回 true。

`isEmpty()`：检查循环队列是否为空。

`isFull()`：检查循环队列是否已满。

示例：

MyCircularQueue circularQueue = new MyCircularQueue(3); // 设置长度为 3
circularQueue.enQueue(1);  // 返回 true
circularQueue.enQueue(2);  // 返回 true
circularQueue.enQueue(3);  // 返回 true
circularQueue.enQueue(4);  // 返回 false，队列已满
circularQueue.Rear();  // 返回 3
circularQueue.isFull();  // 返回 true
circularQueue.deQueue();  // 返回 true
circularQueue.enQueue(4);  // 返回 true
circularQueue.Rear();  // 返回 4

注意：

所有的值都在 [0, 1000] 范围内。

操作次数将在 [1, 1000] 范围内。

请不要使用内置的队列库。
"""

from typing import List


class MyCircularQueue:
    def __init__(self, k: int):
        self.queue: list[int] = [0] * k
        self.head: int = 0
        self.tail: int = 0
        self.size: int = 0
        self.capacity: int = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.queue[self.tail] = value
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[(self.tail - 1) % self.capacity]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用固定大小的数组 + 双指针（head 和 tail）模拟循环队列：
# - head 指向队首元素。
# - tail 指向下一个可插入的位置（队尾的下一个位置）。
# - size 记录当前元素个数，用于区分空和满的状态。
# - 入队操作：在 tail 处写入，tail = (tail + 1) % capacity，size++。
# - 出队操作：head = (head + 1) % capacity，size--。
# - Front 返回 queue[head]，Rear 返回 queue[(tail - 1) % capacity]。
#
# 时间复杂度: O(1) - 所有操作均为常数时间
# 空间复杂度: O(k) - k 为队列容量
#
# 关键点:
# - 使用 size 变量区分"空"和"满"状态（也可以用"浪费一个位置"的方式）
# - 取模运算实现环形：(index + 1) % capacity
# - Rear 是 (tail - 1 + capacity) % capacity，即队尾前一个位置
# - 注意处理空队列时 Front/Rear 返回 -1 的边界情况
