"""
LeetCode #86 - Partition List
https://leetcode.com/problems/partition-list/

Given the head of a linked list and a value x, partition it such that all nodes
less than x come before nodes greater than or equal to x.

Example 1:
    Input: head = [1,4,3,2,5,2], x = 3
    Output: [1,2,2,4,3,5]

Example 2:
    Input: head = [2,1], x = 2
    Output: [1,2]

Constraints:
    The number of nodes in the list is in the range [0, 200].
    -100 <= Node.val <= 100
    -200 <= x <= 200
"""

from typing import Optional


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        small_dummy = ListNode()
        large_dummy = ListNode()
        small = small_dummy
        large = large_dummy

        while head:
            if head.val < x:
                small.next = head
                small = small.next
            else:
                large.next = head
                large = large.next
            head = head.next

        large.next = None
        small.next = large_dummy.next
        return small_dummy.next
