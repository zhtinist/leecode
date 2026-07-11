"""
LeetCode #2074 - Reverse Nodes in Even Length Groups
反转偶数长度组的节点
https://leetcode.cn/problems/reverse-nodes-in-even-length-groups/

给你一个链表的头节点 `head` 。
链表中的节点 按顺序 划分成若干 非空 组，这些非空组的长度构成一个自然数序列（`1, 2, 3, 4, ...`）。一个组的 长度 就是组中分配到的节点数目。换句话说：
节点 `1` 分配给第一组
节点 `2` 和 `3` 分配给第二组
节点 `4`、`5` 和 `6` 分配给第三组，以此类推
注意，最后一组的长度可能小于或者等于 `1 + 倒数第二组的长度` 。
反转 每个 偶数 长度组中的节点，并返回修改后链表的头节点 `head` 。

示例 1：

输入：head = [5,2,6,3,9,1,7,3,8,4] 输出：[5,6,2,3,9,1,4,8,3,7] 解释： - 第一组长度为 1 ，奇数，没有发生反转。 - 第二组长度为 2 ，偶数，节点反转。 - 第三组长度为 3 ，奇数，没有发生反转。 - 最后一组长度为 4 ，偶数，节点反转。
示例 2：

输入：head = [1,1,0,6] 输出：[1,0,1,6] 解释： - 第一组长度为 1 ，没有发生反转。 - 第二组长度为 2 ，节点反转。 - 最后一组长度为 1 ，没有发生反转。
示例 3：

输入：head = [2,1] 输出：[2,1] 解释： - 第一组长度为 1 ，没有发生反转。 - 最后一组长度为 1 ，没有发生反转。

提示：
链表中节点数目范围是 `[1, 10^5]`
`0 <= Node.val <= 10^5`
"""

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseEvenLengthGroups(self, head: Optional['ListNode']) -> Optional['ListNode']:
        # Helper to reverse a linked list segment
        def reverse_list(node, count):
            prev = None
            curr = node
            for _ in range(count):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            # prev is new head, node (original head) is new tail
            node.next = curr  # connect to remaining list
            return prev

        dummy = ListNode(0)
        dummy.next = head
        prev_tail = dummy
        group_len = 1
        curr = head

        while curr:
            # Count nodes remaining in current group
            count = 0
            temp = curr
            while temp and count < group_len:
                temp = temp.next
                count += 1

            if count == 0:
                break

            if count % 2 == 0:
                # Reverse this group
                new_head = reverse_list(curr, count)
                prev_tail.next = new_head
                prev_tail = curr  # curr is now the tail after reversal
            else:
                # Skip this group
                for _ in range(count):
                    prev_tail = prev_tail.next

            curr = prev_tail.next
            group_len += 1

        return dummy.next



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Linked List
#
# 解题思路:
# 使用dummy节点简化边界处理。按组遍历链表：第k组的预期长度为k，
# 实际长度可能小于k（最后一组）。计算当前组实际节点数：
# 如果为偶数则反转该组；如果为奇数则不操作。
# 反转操作使用标准的链表反转。
#
# 时间复杂度: O(n)
# 空间复杂度: O(1)
#
# 关键点:
# - 组长度从1递增
# - 最后一组长度可能不足
# - 仅反转偶数长度组
# - dummy节点简化处理
