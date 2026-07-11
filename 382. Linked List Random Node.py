"""
LeetCode #382 - Linked List Random Node
中文题名：链表随机节点
https://leetcode.com/problems/linked-list-random-node/

Given a singly linked list, return a random node's value from the linked list. Each node must
have the same probability of being chosen.

Follow up:

What if the linked list is extremely large and its length is unknown to you? Could you solve
this efficiently without using extra space?

Example:

// Init a singly linked list [1,2,3].
ListNode head = new ListNode(1);
head.next = new ListNode(2);
head.next.next = new ListNode(3);
Solution solution = new Solution(head);

// getRandom() should return either 1, 2, or 3 randomly. Each element should have equal probability of returning.
solution.getRandom();

【中文翻译】
给定一个单链表，随机返回链表中的一个节点的值。每个节点必须具有相同的被选中的概率。

进阶：
如果链表非常大且长度未知呢？你能在不使用额外空间的情况下高效地解决这个问题吗？

示例：

// 初始化一个单链表 [1,2,3]。
ListNode head = new ListNode(1);
head.next = new ListNode(2);
head.next.next = new ListNode(3);
Solution solution = new Solution(head);

// getRandom() 应该随机返回 1、2 或 3。每个元素应该有相等的返回概率。
solution.getRandom();
"""

from typing import List, Optional


class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        import random
        count = 0
        chosen = 0
        curr = self.head
        while curr:
            count += 1
            # 以 1/count 的概率选择当前节点
            if random.randint(1, count) == 1:
                chosen = curr.val
            curr = curr.next
        return chosen











# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用水库抽样（Reservoir Sampling）算法。
# 遍历链表，维护一个计数器 count 表示当前已遍历的节点数。
# 对于第 count 个节点，以 1/count 的概率选择它作为当前结果。
# 这样每个节点最终被选中的概率都是 1/n（n 为链表总长度）。
# 证明：第 i 个节点被选中需要：当前步被选中（概率 1/i），且后续每一步都未被替换，
# 即 (1 - 1/(i+1)) * (1 - 1/(i+2)) * ... * (1 - 1/n) = 1/n。
# 此方法只需要一次遍历，且不需要预先知道链表长度，空间 O(1)，完美满足进阶要求。
#
# 时间复杂度: O(n) - 遍历链表一次
# 空间复杂度: O(1) - 只使用常数个变量
#
# 关键点:
# - 水库抽样算法的核心思想：以 1/i 的概率选择第 i 个元素
# - 不需要预先计算链表长度，一次遍历即可
# - 数学归纳法可证明每个节点被选中的概率相等
# - 使用 random.randint(1, count) 实现概率选择
