"""
LeetCode #160 - Intersection of Two Linked Lists
https://leetcode.com/problems/intersection-of-two-linked-lists/

Given the heads of two singly linked-lists headA and headB, return the node at
which the two lists intersect. If the two linked lists have no intersection at
all, return null.

Example 1:
    Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5]
    Output: Intersected at '8'

Example 2:
    Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4]
    Output: Intersected at '2'

Example 3:
    Input: intersectVal = 0, listA = [2,6,4], listB = [1,5]
    Output: No intersection

Constraints:
    The number of nodes of listA is in the m.
    The number of nodes of listB is in the n.
    1 <= m, n <= 3 * 10^4
    1 <= Node.val <= 10^5
    0 <= skipA <= m
    0 <= skipB <= n
    intersectVal is 0 if listA and listB do not intersect.
    intersectVal == listA[skipA] == listB[skipB] if listA and listB intersect.
"""

from typing import Optional


# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(
        self, headA: Optional[ListNode], headB: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not headA or not headB:
            return None

        a, b = headA, headB

        while a is not b:
            a = a.next if a else headB
            b = b.next if b else headA

        return a
