"""
LeetCode #641 - Design Circular Deque
中文题名：设计循环双端队列
https://leetcode.com/problems/design-circular-deque/

Design your implementation of the circular double-ended queue (deque).

Your implementation should support following operations:

`MyCircularDeque(k)`: Constructor, set the size of the deque to be k.

`insertFront()`: Adds an item at the front of Deque. Return true if the
operation is successful.

`insertLast()`: Adds an item at the rear of Deque. Return true if the
operation is successful.

`deleteFront()`: Deletes an item from the front of Deque. Return true if the
operation is successful.

`deleteLast()`: Deletes an item from the rear of Deque. Return true if the
operation is successful.

`getFront()`: Gets the front item from the Deque. If the deque is empty,
return -1.

`getRear()`: Gets the last item from Deque. If the deque is empty, return -1.

`isEmpty()`: Checks whether Deque is empty or not.

`isFull()`: Checks whether Deque is full or not.

Example:

MyCircularDeque circularDeque = new MycircularDeque(3); // set the size to be 3
circularDeque.insertLast(1);			// return true
circularDeque.insertLast(2);			// return true
circularDeque.insertFront(3);			// return true
circularDeque.insertFront(4);			// return false, the queue is full
circularDeque.getRear();  			// return 2
circularDeque.isFull();				// return true
circularDeque.deleteLast();			// return true
circularDeque.insertFront(4);			// return true
circularDeque.getFront();			// return 4

Note:

All values will be in the range of [0, 1000].

The number of operations will be in the range of [1, 1000].

Please do not use the built-in Deque library.

【中文翻译】
设计一个循环双端队列（deque）的完整实现。

你的实现应该支持以下操作：

`MyCircularDeque(k)`：构造器，设置双端队列的长度为 k。

`insertFront()`：将一个元素添加到双端队列头部。如果操作成功返回 true。

`insertLast()`：将一个元素添加到双端队列尾部。如果操作成功返回 true。

`deleteFront()`：从双端队列头部删除一个元素。如果操作成功返回 true。

`deleteLast()`：从双端队列尾部删除一个元素。如果操作成功返回 true。

`getFront()`：获取双端队列头部元素。如果双端队列为空，返回 -1。

`getRear()`：获取双端队列尾部元素。如果双端队列为空，返回 -1。

`isEmpty()`：检查双端队列是否为空。

`isFull()`：检查双端队列是否已满。

示例：

MyCircularDeque circularDeque = new MycircularDeque(3); // 设置长度为 3
circularDeque.insertLast(1);			// 返回 true
circularDeque.insertLast(2);			// 返回 true
circularDeque.insertFront(3);			// 返回 true
circularDeque.insertFront(4);			// 返回 false，队列已满
circularDeque.getRear();  			// 返回 2
circularDeque.isFull();				// 返回 true
circularDeque.deleteLast();			// 返回 true
circularDeque.insertFront(4);			// 返回 true
circularDeque.getFront();			// 返回 4

注意：

所有值都在 [0, 1000] 范围内。

操作次数将在 [1, 1000] 范围内。

请不要使用内置的双端队列库。
"""

from typing import List


class MyCircularDeque:
    def __init__(self, k: int):
        self.deque: list[int] = [0] * k
        self.head: int = 0
        self.tail: int = 0
        self.size: int = 0
        self.capacity: int = k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.head = (self.head - 1) % self.capacity
        self.deque[self.head] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.deque[self.tail] = value
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.tail = (self.tail - 1) % self.capacity
        self.size -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.deque[self.head]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.deque[(self.tail - 1) % self.capacity]

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
# 与 #622 循环队列类似，使用固定大小数组 + 双指针实现循环双端队列：
# - head 指向队首元素。
# - tail 指向下一个可插入的位置（尾部元素的下一个位置）。
# - size 记录当前元素个数，区分空/满状态。
# - insertFront：head 向左移动（取模），写入值。
# - insertLast：在 tail 处写入，tail 向右移动。
# - deleteFront：head 向右移动。
# - deleteLast：tail 向左移动。
# - getFront：返回 deque[head]。
# - getRear：返回 deque[(tail - 1) % capacity]。
#
# 时间复杂度: O(1) - 所有操作均为常数时间
# 空间复杂度: O(k) - k 为队列容量
#
# 关键点:
# - (index - 1) % capacity 实现向左循环移动
# - (index + 1) % capacity 实现向右循环移动
# - head 和 tail 的初始值都是 0，空队列时两者相等且 size == 0
# - 取模处理负数：Python 的 % 天生支持负数的正确取模
