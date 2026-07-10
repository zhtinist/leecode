"""
LeetCode #237 - Delete Node in a Linked List
https://leetcode.com/problems/delete-node-in-a-linked-list/

Write a function to delete a node (except the tail) in a singly linked list, given only
access to that node.

Given linked list -- head = [4,5,1,9], which looks like following:

Example 1:

*

Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.

Example 2:

*

Input: head = [4,5,1,9], node = 1
Output: [4,5,9]
Explanation: You are given the third node with value 1, the linked list should become 4 -> 5 -> 9 after calling your function.

Note:

The linked list will have at least two elements.

All of the nodes' values will be unique.

The given node will not be the tail and it will always be a valid node of the
linked list.

Do not return anything from your function.
"""

from typing import List, Optional


class Solution:
    def deleteNode(self, node: ListNode) -> None:
        node.val = node.next.val
        node.next = node.next.next










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 由于只给了要删除的节点(无头节点)，无法访问前驱节点。
# 巧妙的做法是：将要删除节点的值替换为其下一个节点的值，
# 然后跳过下一个节点(将 next 指针指向下下个节点)。
# 例如删除值为 5 的节点 [4,5,1,9]：
#   - 将 5 替换为 1 → [4,1,1,9]
#   - 跳过原来的 1 → [4,1,9]
# 限制：节点不是尾节点（题目保证），否则无法操作。
#
# 时间复杂度: O(1) - 只修改当前节点
# 空间复杂度: O(1) - 不使用额外空间
#
# 关键点:
# - 无法访问前驱节点时，通过"值覆盖 + 跳过"模拟删除
# - 实际删除的是 node.next，node 本身留在链表中但值已变
# - 题目保证 node 不是尾节点，确保 node.next 存在
# - 这种删除方式的副作用：如果有外部引用指向原 node.next，会出问题
