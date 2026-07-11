"""
LeetCode #1721 - Swapping Nodes in a Linked List
中文题名：交换链表中的节点
https://leetcode.com/problems/swapping-nodes-in-a-linked-list/

You are given the `head` of a linked list, and an integer `k`.

Return the head of the linked list after swapping the values of
the `kth` node from the beginning and the `kth`
node from the end (the list is 1-indexed).

Example 1:

Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]

Example 2:

Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
Output: [7,9,6,6,8,7,3,0,9,5]

Example 3:

Input: head = [1], k = 1
Output: [1]

Example 4:

Input: head = [1,2], k = 1
Output: [2,1]

Example 5:

Input: head = [1,2,3], k = 2
Output: [1,2,3]

Constraints:

The number of nodes in the list is `n`.

`1 <= k <= n <= 105`

`0 <= Node.val <= 100`

【中文翻译】
给定链表的头节点 head 和整数 k。交换链表中第 k 个节点和倒数第 k 个节点的值，返回交换后的链表头。

示例 1：
输入: head = [1,2,3,4,5], k = 2
输出: [1,4,3,2,5]
解释: 正数第2个节点值为2，倒数第2个节点值为4，交换后得到 [1,4,3,2,5]。
"""

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 找到第 k 个节点
        first = head
        for _ in range(k - 1):
            first = first.next

        # 找到倒数第 k 个节点（快慢指针）
        fast = first
        second = head
        while fast.next:
            fast = fast.next
            second = second.next

        # 交换值
        first.val, second.val = second.val, first.val
        return head
# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用快慢指针找倒数第 k 个节点。
# 1. 先走 k-1 步找到正数第 k 个节点（first）
# 2. 让 fast 从 first 出发，slow 从 head 出发，同步移动直到 fast 到链表末尾
# 3. 此时 slow 指向倒数第 k 个节点
# 4. 交换 first 和 second 的值（题目只需交换值，不用交换节点本身）
#
# 时间复杂度: O(N) — 一次遍历
# 空间复杂度: O(1)
#
# 关键点:
# - 快慢指针只需一次遍历就能找到倒数第 k 个节点
# - 交换节点的值即可，无需交换节点引用
