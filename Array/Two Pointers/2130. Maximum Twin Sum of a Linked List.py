"""
LeetCode #2130 - Maximum Twin Sum of a Linked List
链表最大孪生和
https://leetcode.cn/problems/maximum-twin-sum-of-a-linked-list/

在一个大小为 `n` 且 `n` 为 偶数 的链表中，对于 `0 <= i <= (n / 2) - 1` 的 `i` ，第 `i` 个节点（下标从 0 开始）的孪生节点为第 `(n-1-i)` 个节点 。
比方说，`n = 4` 那么节点 `0` 是节点 `3` 的孪生节点，节点 `1` 是节点 `2` 的孪生节点。这是长度为 `n = 4` 的链表中所有的孪生节点。
孪生和 定义为一个节点和它孪生节点两者值之和。
给你一个长度为偶数的链表的头节点 `head` ，请你返回链表的 最大孪生和 。

示例 1：

输入：head = [5,4,2,1] 输出：6 解释： 节点 0 和节点 1 分别是节点 3 和 2 的孪生节点。孪生和都为 6 。 链表中没有其他孪生节点。 所以，链表的最大孪生和是 6 。
示例 2：

输入：head = [4,2,2,3] 输出：7 解释： 链表中的孪生节点为： - 节点 0 是节点 3 的孪生节点，孪生和为 4 + 3 = 7 。 - 节点 1 是节点 2 的孪生节点，孪生和为 2 + 2 = 4 。 所以，最大孪生和为 max(7, 4) = 7 。
示例 3：

输入：head = [1,100000] 输出：100001 解释： 链表中只有一对孪生节点，孪生和为 1 + 100000 = 100001 。

提示：
链表的节点数目是 `[2, 10^5]` 中的 偶数 。
`1 <= Node.val <= 10^5`
"""

from typing import List, Optional


class Solution:
    def pairSum(self, head: Optional['ListNode']) -> int:
        # Find middle
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse second half
        prev = None
        curr = slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Find max twin sum
        max_sum = 0
        first = head
        second = prev
        while second:
            max_sum = max(max_sum, first.val + second.val)
            first = first.next
            second = second.next

        return max_sum



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Stack, Linked List, Two Pointers
#
# 解题思路:
# 三步法：
# 1. 快慢指针找到链表中点：slow 每次走一步，fast 每次走两步。fast 到达末尾时，slow 位于中点。
# 2. 反转链表后半部分：从中点开始反转链表，得到反转后的头节点 prev。
# 3. 双指针求最大孪生和：head 从头开始，prev 从反转后的头开始，同时遍历并计算 head.val + prev.val 的最大值。
# 由于 n 为偶数，孪生节点恰好是 (0, n-1), (1, n-2), ... 即前后对应的节点。
#
# 时间复杂度: O(n)
# 空间复杂度: O(1)
#
# 关键点:
# - 快慢指针定位中点
# - 原地反转后半部分链表
# - 孪生节点是前后对称位置，反转后恰好对齐
