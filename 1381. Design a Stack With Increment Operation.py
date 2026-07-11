"""
LeetCode #1381 - Design a Stack With Increment Operation
中文题名：设计一个支持增量操作的栈
https://leetcode.com/problems/design-a-stack-with-increment-operation/

Design a stack which supports the following operations.

Implement the `CustomStack` class:

`CustomStack(int maxSize)` Initializes the object with
`maxSize` which is the maximum number of elements in the stack or do
nothing if the stack reached the `maxSize`.

`void push(int x)` Adds `x` to the top of the stack
if the stack hasn't reached the `maxSize`.

`int pop()` Pops and returns the top of stack or
-1 if the stack is empty.

`void inc(int k, int val)` Increments the bottom `k`
elements of the stack by `val`. If there are less than `k`
elements in the stack, just increment all the elements in the stack.

Example 1:

Input
["CustomStack","push","push","pop","push","push","push","increment","increment","pop","pop","pop","pop"]
[[3],[1],[2],[],[2],[3],[4],[5,100],[2,100],[],[],[],[]]
Output
[null,null,null,2,null,null,null,null,null,103,202,201,-1]
Explanation
CustomStack customStack = new CustomStack(3); // Stack is Empty []
customStack.push(1);                          // stack becomes [1]
customStack.push(2);                          // stack becomes [1, 2]
customStack.pop();                            // return 2 --> Return top of the stack 2, stack becomes [1]
customStack.push(2);                          // stack becomes [1, 2]
customStack.push(3);                          // stack becomes [1, 2, 3]
customStack.push(4);                          // stack still [1, 2, 3], Don't add another elements as size is 4
customStack.increment(5, 100);                // stack becomes [101, 102, 103]
customStack.increment(2, 100);                // stack becomes [201, 202, 103]
customStack.pop();                            // return 103 --> Return top of the stack 103, stack becomes [201, 202]
customStack.pop();                            // return 202 --> Return top of the stack 102, stack becomes [201]
customStack.pop();                            // return 201 --> Return top of the stack 101, stack becomes []
customStack.pop();                            // return -1 --> Stack is empty return -1.

Constraints:

`1 <= maxSize <= 1000`

`1 <= x <= 1000`

`1 <= k <= 1000`

`0 <= val <= 100`

At most `1000` calls will be made to each method of `increment`,
`push` and `pop` each separately.

【中文翻译】

设计一个支持以下操作的栈。

实现 CustomStack 类：

CustomStack(int maxSize) 用 maxSize 初始化对象，maxSize 是栈中元素的最大数量，栈在达到 maxSize 时不应增长。
void push(int x) 如果栈未达到 maxSize，将 x 添加到栈顶。
int pop() 弹出并返回栈顶，如果栈为空则返回 -1。
void inc(int k, int val) 将栈底 k 个元素的值增加 val。如果栈中元素少于 k 个，则增加栈中的所有元素。

示例 1：

输入：
["CustomStack","push","push","pop","push","push","push","increment","increment","pop","pop","pop","pop"]
[[3],[1],[2],[],[2],[3],[4],[5,100],[2,100],[],[],[],[]]
输出：
[null,null,null,2,null,null,null,null,null,103,202,201,-1]
解释：
CustomStack customStack = new CustomStack(3); // 栈为空 []
customStack.push(1);                          // 栈变为 [1]
customStack.push(2);                          // 栈变为 [1, 2]
customStack.pop();                            // 返回 2 --> 返回栈顶 2，栈变为 [1]
customStack.push(2);                          // 栈变为 [1, 2]
customStack.push(3);                          // 栈变为 [1, 2, 3]
customStack.push(4);                          // 栈仍为 [1, 2, 3]，不添加任何元素，因为大小为 4
customStack.increment(5, 100);                // 栈变为 [101, 102, 103]
customStack.increment(2, 100);                // 栈变为 [201, 202, 103]
customStack.pop();                            // 返回 103 --> 返回栈顶 103，栈变为 [201, 202]
customStack.pop();                            // 返回 202 --> 返回栈顶 202，栈变为 [201]
customStack.pop();                            // 返回 201 --> 返回栈顶 201，栈变为 []
customStack.pop();                            // 返回 -1 --> 栈为空返回 -1

约束条件：
1 <= maxSize <= 1000
1 <= x <= 1000
1 <= k <= 1000
0 <= val <= 100
每个方法 increment、push 和 pop 最多调用 1000 次。
"""

from typing import List, Optional


class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.inc = []
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)
            self.inc.append(0)

    def pop(self) -> int:
        if not self.stack:
            return -1
        i = len(self.stack) - 1
        result = self.stack[i] + self.inc[i]
        if i > 0:
            self.inc[i - 1] += self.inc[i]
        self.stack.pop()
        self.inc.pop()
        return result

    def increment(self, k: int, val: int) -> None:
        i = min(k, len(self.inc)) - 1
        if i >= 0:
            self.inc[i] += val



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用一个列表作为栈，配合一个"增量数组"实现惰性增量。
# push: 将值加入栈，并在增量数组末尾加0。
# pop: 如果栈为空返回 -1；否则取栈顶元素加上对应增量。
#   在弹出之前，将当前增量向下传递（传递给前一个元素），实现 O(1) 延迟增量。
# increment(k, val): 将增量数组的第 min(k, n)-1 个元素加上 val。
#   弹出时才将增量传播，避免每次 inc 遍历前 k 个元素。
#
# 时间复杂度: O(1)  所有操作均为 O(1)
# 空间复杂度: O(N)  N 为栈的最大容量
#
# 关键点:
# - 惰性增量法：在 increment 时只记录增量值，在 pop 时才向前传播
# - 使用辅助数组 inc 保存每个位置待增加的基准值
# - 弹出时向下传递增量到前一个位置










