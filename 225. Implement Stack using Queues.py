"""
LeetCode #225 - Implement Stack using Queues
中文题名：用队列实现栈
https://leetcode.com/problems/implement-stack-using-queues/

Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.

pop() -- Removes the element on top of the stack.

top() -- Get the top element.

empty() -- Return whether the stack is empty.

Example:

MyStack stack = new MyStack();

stack.push(1);
stack.push(2);
stack.top();   // returns 2
stack.pop();   // returns 2
stack.empty(); // returns false

Notes:

You must use *only* standard operations of a queue -- which means only `push
to back`, `peek/pop from front`, `size`, and `is
empty` operations are valid.

Depending on your language, queue may not be supported natively. You may simulate a
queue by using a list or deque (double-ended queue), as long as you use only standard
operations of a queue.

You may assume that all operations are valid (for example, no pop or top operations will
be called on an empty stack).

【中文翻译】
使用队列实现栈的下列操作：

push(x) -- 元素 x 入栈

pop() -- 移除栈顶元素

top() -- 获取栈顶元素

empty() -- 返回栈是否为空

示例：

MyStack stack = new MyStack();

stack.push(1);
stack.push(2);
stack.top();   // 返回 2
stack.pop();   // 返回 2
stack.empty(); // 返回 false

注意：

你只能使用队列的标准操作——这意味着只有 `push to back`、`peek/pop from front`、`size` 和 `is empty` 操作是有效的。

根据你的语言，队列可能没有原生支持。你可以使用 list 或 deque（双端队列）来模拟一个队列，只要你只使用队列的标准操作即可。

你可以假设所有操作都是有效的（例如，不会对空栈调用 pop 或 top 操作）。
"""

from typing import List, Optional


class MyStack:
    def __init__(self):
        self.q = []

    def push(self, x: int) -> None:
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.pop(0))

    def pop(self) -> int:
        return self.q.pop(0)

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Easy
# Paid Only: No
#
# 解题思路:
# 用一个队列模拟栈，采用 push O(n), pop/top O(1) 的策略。
# push(x): 将 x 加入队列尾部，然后将队列中在 x 之前的所有元素依次出队再入队
# (即把前面的元素移到 x 后面)。这样 x 就变成了队首元素，模拟了栈顶。
# pop(): 直接从队首弹出元素 (O(1))
# top(): 返回队首元素 (O(1))
# empty(): 判断队列是否为空
# 只使用队列的标准操作: push to back(append), pop from front(pop(0)), peek front([0]),
# size(len), is empty(len==0)
#
# 时间复杂度: push O(n), pop O(1), top O(1), empty O(1)
# 空间复杂度: O(n) - 存储所有元素
#
# 关键点:
# - push 时通过循环旋转队列，将新元素置于队首(栈顶)
# - 只使用队列的 FIFO 标准操作，不用列表的随机访问
# - 另一种实现: push O(1), pop O(n) 也可以
