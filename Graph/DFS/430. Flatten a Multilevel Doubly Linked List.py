"""
LeetCode #430 - Flatten a Multilevel Doubly Linked List
中文题名：扁平化多级双向链表
https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/

You are given a doubly linked list which in addition to the next and previous pointers, it
could have a child pointer, which may or may not point to a separate doubly linked list.
These child lists may have one or more children of their own, and so on, to produce a
multilevel data structure, as shown in the example below.

Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are
given the head of the first level of the list.

Example:

Input:
1---2---3---4---5---6--NULL
|
7---8---9---10--NULL
|
11--12--NULL

Output:
1-2-3-7-8-11-12-9-10-4-5-6-NULL

Explanation for the above example:

Given the following multilevel doubly linked list:

We should return the following flattened doubly linked list:

【中文翻译】
给定一个双向链表，除了 next 和 prev 指针外，还可以有一个 child 指针，可能指向
另一个单独的双向链表。这些子链表可能还有自己的子链表，从而构成多级数据结构。
将链表扁平化，使所有节点出现在一个单级双向链表中。给定第一级链表的头节点。

示例：
    输入：
    1---2---3---4---5---6--NULL
    |
    7---8---9---10--NULL
    |
    11--12--NULL

    输出：
    1-2-3-7-8-11-12-9-10-4-5-6-NULL
"""

from typing import List, Optional


# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return None

        cur = head
        while cur:
            if cur.child:
                # Find the tail of the child list
                child_tail = cur.child
                while child_tail.next:
                    child_tail = child_tail.next

                # Connect child tail to cur.next (if cur.next exists)
                if cur.next:
                    cur.next.prev = child_tail
                child_tail.next = cur.next

                # Connect cur to child, and clear child pointer
                cur.next = cur.child
                cur.child.prev = cur
                cur.child = None

            cur = cur.next

        return head


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 迭代遍历。使用 cur 指针遍历主链表。当遇到有 child 的节点时：
# 1. 找到 child 链表的尾节点（顺着 next 走到头）
# 2. 将 child 尾节点的 next 指向 cur.next（保存主链表后续部分）
# 3. 如果 cur.next 存在，将它的 prev 指向 child 尾节点
# 4. 将 cur.next 指向 child 头节点（替代原来的 next）
# 5. 将 child 头节点的 prev 指向 cur
# 6. 将 cur.child 置为 None
#
# 这样处理相当于将 child 链表"插入"到 cur 和 cur.next 之间。
# 由于每次处理完 child 后会继续遍历（cur = cur.next，现在指向原来的 child 头节点），
# 所以嵌套的子链表也会被正确处理。
#
# 时间复杂度: O(N) — 每个节点访问常数次（寻找 child_tail 时可能需要遍历 child 链表，
#              但每个节点总体仍只被访问 O(1) 次）
# 空间复杂度: O(1) — 只使用指针变量
#
# 关键点:
# - 找到 child 链表的尾节点用于连接
# - 正确处理 prev 双向指针
# - 遍历时会自然进入 child 链表，因此嵌套子链表也被处理
# - 也可以用 DFS/栈的递归思路，但迭代方法空间更优
