"""
LeetCode #234 - Palindrome Linked List
中文题名：回文链表
https://leetcode.com/problems/palindrome-linked-list/

Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false

Example 2:

Input: 1->2->2->1
Output: true

Follow up:

Could you do it in O(n) time and O(1) space?

【中文翻译】
请判断一个链表是否为回文链表。

示例 1：

输入：1->2
输出：false

示例 2：

输入：1->2->2->1
输出：true

进阶：

你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
"""

from typing import List, Optional


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt

        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Easy
# Paid Only: No
#
# 解题思路:
# 使用快慢指针找中点 + 反转后半部分 + 比较，O(1) 额外空间。
# 1. 快慢指针定位中点：slow 每次走一步，fast 每次走两步。
#    当 fast 到达末尾时，slow 正好在中点(奇数长度)或中点的后一个(偶数长度)。
# 2. 反转链表后半部分：从中点(slow)开始，使用 prev/curr 指针反转链表。
#    反转后 prev 指向后半部分的头节点。
# 3. 双指针比较：left 从头节点开始，right 从反转后的后半部分头节点开始，
#    逐个比较节点的值。若全部相等则为回文链表。
# 4. (可选)恢复链表：再次反转后半部分恢复原链表结构。
#
# 时间复杂度: O(n) - 找中点 O(n)，反转 O(n)，比较 O(n)
# 空间复杂度: O(1) - 只使用几个指针，不开辟新链表
#
# 关键点:
# - 快慢指针是找链表中点的标准技巧
# - 反转链表只需 O(1) 额外空间
# - 比较时以 right 指针为终止条件(后半部分可能比前半部分短 1 个节点)
# - 满足进阶要求: O(n) 时间 + O(1) 空间
