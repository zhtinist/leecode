"""
LeetCode #445 - Add Two Numbers II
中文题名：两数相加 II
https://leetcode.com/problems/add-two-numbers-ii/

You are given two non-empty linked lists representing two non-negative integers. The
most significant digit comes first and each of their nodes contain a single digit. Add the
two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0
itself.

Follow up:

What if you cannot modify the input lists? In other words, reversing the lists is not
allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7

【中文翻译】
给定两个非空链表，表示两个非负整数。最高位在最前面，每个节点包含一个数字。
将两数相加并返回其和（链表形式）。可假定两数不包含前导零，但数字 0 本身除外。

进阶：如果不能修改输入链表（即不允许翻转链表），该怎么做？

示例：
    输入：(7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
    输出：7 -> 8 -> 0 -> 7
"""

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1, stack2 = [], []

        # Push all digits onto stacks
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        carry = 0
        head = None

        # Pop from stacks (least significant first)
        while stack1 or stack2 or carry:
            val1 = stack1.pop() if stack1 else 0
            val2 = stack2.pop() if stack2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10

            # Prepend to result list
            new_node = ListNode(digit)
            new_node.next = head
            head = new_node

        return head


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用栈来反转链表（不修改原链表结构）。
# 1. 将两个链表的所有节点值分别压入栈 stack1 和 stack2
#    栈的特性（LIFO）自然实现了最低位先出（相当于链表反转的效果）
# 2. 依次从两个栈弹出数字相加，处理进位
# 3. 使用头插法构建结果链表（每次新节点插入头部），因为加法是从低位到高位，
#    头插法能保证高位在链表前面
#
# 头插法示例（处理 7243 + 564 = 7807）：
#   个位：3+4=7,  carry=0 → node(7) → 7
#   十位：4+6=10, carry=1 → node(0) → 0->7
#   百位：2+5+1=8,carry=0 → node(8) → 8->0->7
#   千位：7+0=7,  carry=0 → node(7) → 7->8->0->7
#
# 时间复杂度: O(M + N) — 分别遍历两个链表（M 和 N 为长度）
# 空间复杂度: O(M + N) — 两个栈的大小
#
# 关键点:
# - 使用栈代替翻转链表，不修改输入
# - 头插法构建结果链表（因为从低位向高位计算）
# - 循环条件要包含 carry，处理最后可能的进位
