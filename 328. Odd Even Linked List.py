"""
LeetCode #328 - Odd Even Linked List
中文题名：奇偶链表
https://leetcode.com/problems/odd-even-linked-list/

Given a singly linked list, group all odd nodes together followed by the even nodes. Please
note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and
O(nodes) time complexity.

Example 1:

Input: `1->2->3->4->5->NULL`
Output: `1->3->5->2->4->NULL`

Example 2:

Input: 2`->1->3->5->6->4->7->NULL`
Output: `2->3->6->7->1->5->4->NULL`

Note:

The relative order inside both the even and odd groups should remain as it was in the
input.

The first node is considered odd, the second node even and so on ...

【中文翻译】
给定一个单链表，将所有奇数节点组合在一起，然后是所有偶数节点。这里说的奇偶是指节点编号
而非节点中的值。要求原地完成，时间复杂度 O(n)，空间复杂度 O(1)。

示例 1：
    输入：1->2->3->4->5->NULL
    输出：1->3->5->2->4->NULL

示例 2：
    输入：2->1->3->5->6->4->7->NULL
    输出：2->3->6->7->1->5->4->NULL

注意：
    奇数组和偶数组内部的相对顺序应与输入中的顺序保持一致。
    第一个节点被认为是奇数节点，第二个节点是偶数节点，以此类推。
"""

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        odd = head
        even = head.next
        even_head = even

        while even and even.next:
            odd.next = even.next      # Connect odd to next odd
            odd = odd.next            # Move odd forward
            even.next = odd.next      # Connect even to next even
            even = even.next          # Move even forward

        odd.next = even_head          # Connect end of odds to start of evens
        return head


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用两个指针 odd 和 even 分别跟踪奇数位置和偶数位置的节点。
# odd 从 head（第 1 个节点）开始，even 从 head.next（第 2 个节点）开始。
# 保存 even 的起始位置 even_head，用于最后连接。
#
# 每次迭代：
# 1. odd.next = even.next — 跳过偶数节点，直接指向下一个奇数节点
# 2. odd = odd.next — 奇数指针前移
# 3. even.next = odd.next — 跳过奇数节点（因为 odd 已经前移，odd.next 是下一个偶数节点）
# 4. even = even.next — 偶数指针前移
#
# 循环结束后，将奇数链表的尾部连接到偶数链表的头部（odd.next = even_head）。
#
# 时间复杂度: O(N) — 每个节点访问一次
# 空间复杂度: O(1) — 只使用几个指针变量
#
# 关键点:
# - 保存偶数链表头部 even_head，否则会丢失偶数链的起点
# - 循环条件是 even and even.next（因为 even 在 odd 之后，even.next为空说明没有更多奇数节点）
# - 原地操作，不需要额外空间
