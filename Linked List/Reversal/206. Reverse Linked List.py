"""
LeetCode #206 - Reverse Linked List
中文题名：反转链表
https://leetcode.com/problems/reverse-linked-list/

Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement
both?

【中文翻译】
反转一个单链表。

示例：
    输入：1->2->3->4->5->NULL
    输出：5->4->3->2->1->NULL

进阶：
    链表可以迭代或递归地反转，你能否用两种方法实现？
"""

from typing import List, Optional


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next_temp = curr.next  # Save the next node
            curr.next = prev       # Reverse the pointer
            prev = curr            # Move prev forward
            curr = next_temp       # Move curr forward

        return prev  # prev is the new head


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Easy
# Paid Only: No
#
# 解题思路:
# 迭代法反转链表。使用三个指针（实际上是操作两个指针 + 一个临时变量）：
# - prev：已反转部分的头节点（初始为 None）
# - curr：当前待处理的节点（初始为 head）
# - next_temp：保存 curr.next 防止断链
#
# 每次迭代：
# 1. next_temp = curr.next（保存下一个节点）
# 2. curr.next = prev（反转当前节点的指针）
# 3. prev = curr（prev 前进）
# 4. curr = next_temp（curr 前进）
#
# 循环结束后，prev 指向原链表的最后一个节点（即新链表的头）。
#
# 时间复杂度: O(N) — 一次遍历
# 空间复杂度: O(1) — 原地操作
#
# 关键点:
# - 保存 curr.next 防止丢失后续节点
# - 最后返回 prev 而非 curr（循环结束时 curr 为 None）
# - 也可用递归实现（理解和迭代不同但逻辑等价）
