"""
LeetCode #232 - Implement Queue using Stacks
中文题名：用栈实现队列
https://leetcode.com/problems/implement-queue-using-stacks/

Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.

pop() -- Removes the element from in front of queue.

peek() -- Get the front element.

empty() -- Return whether the queue is empty.

Example:

MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);
queue.peek();  // returns 1
queue.pop();   // returns 1
queue.empty(); // returns false

Notes:

You must use *only* standard operations of a stack -- which means only `push
to top`, `peek/pop from top`, `size`, and `is
empty` operations are valid.

Depending on your language, stack may not be supported natively. You may simulate a
stack by using a list or deque (double-ended queue), as long as you use only standard
operations of a stack.

You may assume that all operations are valid (for example, no pop or peek operations
will be called on an empty queue).

【中文翻译】
使用栈实现队列的下列操作：

push(x) -- 将一个元素放入队列的尾部。

pop() -- 从队列首部移除元素。

peek() -- 返回队列首部的元素。

empty() -- 返回队列是否为空。

示例：

MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);
queue.peek();  // 返回 1
queue.pop();   // 返回 1
queue.empty(); // 返回 false

注意：

你只能使用栈的标准操作——这意味着只有 `push to top`、`peek/pop from top`、`size` 和 `is empty` 操作是有效的。

根据你的语言，栈可能没有原生支持。你可以使用 list 或 deque（双端队列）来模拟一个栈，只要你只使用栈的标准操作即可。

你可以假设所有操作都是有效的（例如，不会对空队列调用 pop 或 peek 操作）。
"""

from typing import List, Optional


class MyQueue:

    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x: int) -> None:
        self.input.append(x)

    def pop(self) -> int:
        self.peek()
        return self.output.pop()

    def peek(self) -> int:
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self) -> bool:
        return not self.input and not self.output










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Easy
# Paid Only: No
#
# 解题思路:
# 使用两个栈(input 和 output)来模拟队列的 FIFO 行为。
# - push(x): 直接将元素压入 input 栈 (O(1))
# - pop(): 如果 output 栈为空，将 input 栈中所有元素逐个弹出并压入 output 栈，
#   从而反转元素顺序，使得 input 栈底的元素(最早入队)出现在 output 栈顶。
#   然后从 output 栈弹出栈顶元素。摊还时间复杂度 O(1)。
# - peek(): 与 pop 类似，先确保 output 栈顶有元素(必要时从 input 转移)，
#   返回 output 栈顶元素而不弹出。
# - empty(): 当两个栈都为空时队列为空。
# 摊还分析: 每个元素最多被 push 和 pop 各两次，
# 平均每次操作 O(1)。
#
# 时间复杂度: push O(1), pop 摊还 O(1), peek 摊还 O(1), empty O(1)
# 空间复杂度: O(n) - 两个栈共存储 n 个元素
#
# 关键点:
# - input 栈负责接收新元素(LIFO)，output 栈负责输出元素(FIFO)
# - 转移只在 output 为空时发生，确保元素顺序正确
# - 每个元素从 input 到 output 最多转移一次，摊还 O(1)
# - 只使用栈的标准操作: append(push), pop(pop), [-1](peek)
