"""
LeetCode #2181 - Merge Nodes in Between Zeros
合并零之间的节点
https://leetcode.cn/problems/merge-nodes-in-between-zeros/

给你一个链表的头节点 `head` ，该链表包含由 `0` 分隔开的一连串整数。链表的 开端 和 末尾 的节点都满足 `Node.val == 0` 。
对于每两个相邻的 `0` ，请你将它们之间的所有节点合并成一个节点，其值是所有已合并节点的值之和。然后将所有 `0` 移除，修改后的链表不应该含有任何 `0` 。
返回修改后链表的头节点 `head` 。

示例 1：

输入：head = [0,3,1,0,4,5,2,0] 输出：[4,11] 解释： 上图表示输入的链表。修改后的链表包含： - 标记为绿色的节点之和：3 + 1 = 4 - 标记为红色的节点之和：4 + 5 + 2 = 11
示例 2：

输入：head = [0,1,0,3,0,2,2,0] 输出：[1,3,4] 解释： 上图表示输入的链表。修改后的链表包含： - 标记为绿色的节点之和：1 = 1 - 标记为红色的节点之和：3 = 3 - 标记为黄色的节点之和：2 + 2 = 4

提示：
列表中的节点数目在范围 `[3, 2 * 10^5]` 内
`0 <= Node.val <= 1000`
不 存在连续两个 `Node.val == 0` 的节点
链表的 开端 和 末尾 节点都满足 `Node.val == 0`
"""

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        遍历链表，跳过开头的 0。对每两个 0 之间的节点值累加求和，
        遇到下一个 0 时创建一个新节点并把累加和写入，然后重置累加和。
        最后返回新链表的头节点。
        """
        dummy = ListNode(0)      # 哨兵节点，简化头节点处理
        tail = dummy             # 新链表的尾指针
        curr = head.next         # 跳过开头的 0
        segment_sum = 0

        while curr:
            if curr.val == 0:
                # 遇到分隔 0，将当前段的和创建为新节点
                tail.next = ListNode(segment_sum)
                tail = tail.next
                segment_sum = 0
            else:
                segment_sum += curr.val
            curr = curr.next

        return dummy.next


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Linked List, Simulation
#
# 解题思路:
# 1. 使用哨兵节点 dummy 简化新链表头节点的处理。
# 2. 从 head.next 开始遍历（跳过开头的 0）。
# 3. 维护一个 segment_sum 变量，累加当前段（两个 0 之间）的所有节点值。
# 4. 当遇到值为 0 的节点时，用 segment_sum 创建一个新节点，接到新链表尾部，
#    然后重置 segment_sum = 0。
# 5. 遍历结束后返回 dummy.next 即为合并后的链表头。
#
# 时间复杂度: O(n)
# - 遍历链表一次，n 为链表节点数。
#
# 空间复杂度: O(1)
# - 只使用常数额外空间（不计输出链表）。
#
# 关键点:
# - 跳过第一个 0 节点。
# - 遇到 0 时将累加和写入新节点并重置。
# - 使用哨兵节点简化链表构建。
