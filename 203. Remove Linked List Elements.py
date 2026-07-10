"""
LeetCode #203 - Remove Linked List Elements
中文题名：移除链表元素
https://leetcode.com/problems/remove-linked-list-elements/

Remove all elements from a linked list of integers that have value *val*.

Example:

Input:  1->2->6->3->4->5->6, *val* = 6
Output: 1->2->3->4->5

【中文翻译】
从链表中移除所有值等于 *val* 的节点。

示例：

输入：1->2->6->3->4->5->6，*val* = 6
输出：1->2->3->4->5
"""

from typing import List, Optional


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Dummy node to handle removal of head gracefully
        dummy = ListNode(0)
        dummy.next = head
        prev, curr = dummy, head

        while curr:
            if curr.val == val:
                prev.next = curr.next  # Skip the current node
            else:
                prev = curr  # Move prev forward only if no deletion
            curr = curr.next

        return dummy.next


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Easy
# Paid Only: No
#
# 解题思路:
# 使用哨兵节点（Dummy Node）简化链表删除操作。创建一个虚拟头节点 dummy，
# 其 next 指向原链表头。使用双指针 prev 和 curr：
# - curr 指向当前检查的节点
# - prev 指向 curr 的前一个节点（已确认不需要删除）
#
# 当 curr.val == val 时：prev.next = curr.next（跳过 curr）
# 当 curr.val != val 时：prev = curr（prev 前进）
# curr 总是前进到下一节点。
#
# 最后返回 dummy.next 即为新链表的头节点。
#
# 时间复杂度: O(N) — 一次遍历
# 空间复杂度: O(1) — 原地操作
#
# 关键点:
# - 哨兵节点避免单独处理头节点被删除的情况
# - prev 只有在不需要删除时才前进
# - curr 每次循环都前进
