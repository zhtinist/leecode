"""
LeetCode #1171 - Remove Zero Sum Consecutive Nodes from Linked List
中文题名：从链表中删去总和值为零的连续节点
https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/

Given the `head` of a linked list, we repeatedly delete consecutive sequences of
nodes that sum to `0` until there are no such sequences.

After doing so, return the head of the final linked list.  You may return any such
answer.

(Note that in the examples below, all sequences are serializations of `ListNode`
objects.)

Example 1:

Input: head = [1,2,-3,3,1]
Output: [3,1]
Note: The answer [1,2,1] would also be accepted.

Example 2:

Input: head = [1,2,3,-3,4]
Output: [1,2,4]

Example 3:

Input: head = [1,2,3,-3,-2]
Output: [1]

Constraints:

The given linked list will contain between `1` and `1000` nodes.

Each node in the linked list has `-1000 <= node.val <= 1000`.

【中文翻译】
给定一个链表的头节点 head，我们反复删除链表中总和为 0 的连续节点序列，直到不存在这样的序列。

完成后，返回最终链表的头节点。你可以返回任意满足条件的答案。

（注意，下面示例中的所有序列都是 ListNode 对象的序列化表示。）

示例 1：

输入：head = [1,2,-3,3,1]
输出：[3,1]
注意：答案 [1,2,1] 也会被接受。

示例 2：

输入：head = [1,2,3,-3,4]
输出：[1,2,4]

示例 3：

输入：head = [1,2,3,-3,-2]
输出：[1]

约束条件：

给定的链表将包含 1 到 1000 个节点。

链表中的每个节点值为 `-1000 <= node.val <= 1000`。
"""

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        # Dummy node to handle cases where head itself is removed
        dummy = ListNode(0)
        dummy.next = head

        prefix_sum = 0
        # Map from prefix_sum to the node right before the sum-to-zero segment
        seen = {0: dummy}

        # First pass: record the LAST occurrence of each prefix sum
        # This naturally handles nested zero-sum segments
        cur = dummy
        while cur:
            prefix_sum += cur.val if cur != dummy else 0
            seen[prefix_sum] = cur
            cur = cur.next

        # Second pass: skip zero-sum segments
        prefix_sum = 0
        cur = dummy
        while cur:
            prefix_sum += cur.val if cur != dummy else 0
            cur.next = seen[prefix_sum].next
            cur = cur.next

        return dummy.next










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用前缀和 + 哈希表的两遍扫描法：
#
# 关键洞察：如果两个位置的前缀和相同，说明这两个位置之间的子数组和为 0。
# 例如 prefix[0] = 0, prefix[3] = 0，则 [1],[2],[3] 的和为 0。
#
# 第一遍扫描（记录最后一次出现）：
# 1. 使用虚拟头节点 dummy 简化边界处理。
# 2. 遍历链表计算前缀和，对于每个前缀和，记录该前缀和对应的最后一个节点。
#    这样如果有多个相同的前缀和，最后出现的会覆盖前面的，
#    从而自然跳过被包含的内部零和段。
#
# 第二遍扫描（跳过零和段）：
# 1. 再次遍历链表，对于当前节点的前缀和，将 cur.next 直接指向
#    seen[prefix_sum].next，即跳到该前缀和最后出现位置的下一个节点。
# 2. 这一步就删除了所有零和段。
#
# 时间复杂度: O(n) - 两遍扫描链表，每遍 O(n)
# 空间复杂度: O(n) - 哈希表存储前缀和映射
#
# 关键点:
# - 前缀和相等意味着中间段和为 0，这是核心数学性质
# - 记录最后出现的位置（而非第一次），可以自然处理嵌套/重叠的零和段
# - 虚拟头节点处理头部被删除的情况
# - 两次遍历策略简洁优雅，避免了复杂的区间删除操作
