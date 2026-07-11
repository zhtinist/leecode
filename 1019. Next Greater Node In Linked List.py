"""
LeetCode #1019 - Next Greater Node In Linked List
中文题名：链表中的下一个更大节点
https://leetcode.com/problems/next-greater-node-in-linked-list/

We are given a linked list with `head` as the first node.  Let's
number the nodes in the list: `node_1, node_2, node_3, ...` etc.

Each node may have a next larger value: for `node_i`, `next_larger(node_i)` is
the `node_j.val` such that `j > i`, `node_j.val >
node_i.val`, and `j` is the smallest possible choice.  If such a
`j` does not exist, the next larger value is `0`.

Return an array of integers `answer`, where `answer[i] =
next_larger(node_{i+1})`.

Note that in the example inputs (not outputs) below, arrays such as
`[2,1,5]` represent the serialization of a linked list with a head node
value of 2, second node value of 1, and third node value of 5.

Example 1:

Input: [2,1,5]
Output: [5,5,0]

Example 2:

Input: [2,7,4,3,5]
Output: [7,0,5,5,0]

Example 3:

Input: [1,7,5,1,9,2,5,1]
Output: [7,9,9,9,0,5,0,0]

Note:

`1 <= node.val <= 10^9` for each node in the linked list.

The given list has length in the range `[0, 10000]`.

【中文翻译】
给定一个以 `head` 为第一个节点的链表。让我们为链表中的节点编号：`node_1, node_2, node_3, ...` 等。

每个节点可能有一个下一个更大的值：对于 `node_i`，`next_larger(node_i)` 是 `node_j.val`，其中 `j > i`，`node_j.val > node_i.val`，且 `j` 是可能的最小选择。如果这样的 `j` 不存在，则下一个更大的值为 `0`。

返回一个整数数组 `answer`，其中 `answer[i] = next_larger(node_{i+1})`。

注意，在下面的示例输入（而非输出）中，诸如 `[2,1,5]` 的数组表示链表的序列化，头节点值为 2，第二个节点值为 1，第三个节点值为 5。

示例 1：

输入：[2,1,5]
输出：[5,5,0]

示例 2：

输入：[2,7,4,3,5]
输出：[7,0,5,5,0]

示例 3：

输入：[1,7,5,1,9,2,5,1]
输出：[7,9,9,9,0,5,0,0]

注意：

对于链表中的每个节点，`1 <= node.val <= 10^9`。

给定链表的长度在 `[0, 10000]` 范围内。

"""

from typing import List, Optional


class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next

        n = len(arr)
        res = [0] * n
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] < arr[i]:
                res[stack.pop()] = arr[i]
            stack.append(i)
        return res










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 先将链表转换为数组（便于随机访问），然后使用单调递减栈查找每个元素的下一个更大元素。
# 遍历数组，维护一个存储下标的单调递减栈（栈中下标对应的元素值严格递减）：
# - 对于当前元素 arr[i]，当栈非空且栈顶对应值小于 arr[i] 时，弹出栈顶下标，
#   并将 arr[i] 设为该下标位置的答案（因为 arr[i] 是右边第一个更大的值）。
# - 将当前下标 i 压入栈中。
# 遍历完成后，栈中剩余下标对应的位置没有下一个更大值，保持默认值 0。
#
# 时间复杂度: O(n) - 每个元素入栈出栈各一次
# 空间复杂度: O(n) - 数组和栈各需要 O(n) 空间
#
# 关键点:
# - 链表先转成数组，便于使用单调栈（需要随机访问和下标的对应关系）
# - 单调递减栈确保找到的是"下一个更大"（而非最大）
# - 栈中存储的是下标而非值，用于定位输出数组中的位置
