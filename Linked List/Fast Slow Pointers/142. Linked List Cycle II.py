"""
LeetCode #142 - Linked List Cycle II
https://leetcode.com/problems/linked-list-cycle-ii/

Given the head of a linked list, return the node where the cycle begins. If
there is no cycle, return null.

Example 1:
    Input: head = [3,2,0,-4], pos = 1
    Output: tail connects to node index 1

Example 2:
    Input: head = [1,2], pos = 0
    Output: tail connects to node index 0

Example 3:
    Input: head = [1], pos = -1
    Output: no cycle

Constraints:
    The number of the nodes in the list is in the range [0, 10^4].
    -10^5 <= Node.val <= 10^5
    pos is -1 or a valid index in the linked-list.
"""

from typing import Optional


# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                break
        else:
            return None

        slow = head
        while slow is not fast:
            slow = slow.next
            fast = fast.next

        return slow
