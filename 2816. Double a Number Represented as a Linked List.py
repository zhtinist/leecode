"""
LeetCode #2816 - Double a Number Represented as a Linked List
翻倍以链表形式表示的数字
https://leetcode.cn/problems/double-a-number-represented-as-a-linked-list/

给你一个 非空 链表的头节点 `head` ，表示一个不含前导零的非负数整数。
将链表 翻倍 后，返回头节点 `head` 。

示例 1：
输入：head = [1,8,9] 输出：[3,7,8] 解释：上图中给出的链表，表示数字 189 。返回的链表表示数字 189 * 2 = 378 。
示例 2：
输入：head = [9,9,9] 输出：[1,9,9,8] 解释：上图中给出的链表，表示数字 999 。返回的链表表示数字 999 * 2 = 1998 。

提示：
链表中节点的数目在范围 `[1, 10^4]` 内
`0 <= Node.val <= 9`
生成的输入满足：链表表示一个不含前导零的数字，除了数字 `0` 本身。
"""

from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Reverse the linked list
        prev = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        head = prev

        carry = 0
        cur = head
        while cur:
            val = cur.val * 2 + carry
            cur.val = val % 10
            carry = val // 10
            if not cur.next and carry:
                cur.next = ListNode(carry)
                break
            cur = cur.next

        # Reverse back
        prev = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Stack, Linked List, Math
#
# 解题思路:
# 链表表示的数字是正序的（最高位在头部），乘 2 需要从最低位开始（进位从低位向高位传播）。
# 先将链表反转，然后从头（原最低位）开始逐位乘以 2 并处理进位。
# 如果最后还有进位，在末尾添加新节点。最后再次反转恢复正序。
#
# 时间复杂度: O(n)
# 空间复杂度: O(1)
#
# 关键点:
# - 反转链表使得可以从最低位开始处理
# - 每位乘以 2 加上进位，更新值和进位
# - 处理完后再次反转恢复顺序
# - 注意最后可能产生新的最高位（如 999*2=1998 需要新增节点）
