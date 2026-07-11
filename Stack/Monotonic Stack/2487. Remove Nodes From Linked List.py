"""
LeetCode #2487 - Remove Nodes From Linked List
从链表中移除节点
https://leetcode.cn/problems/remove-nodes-from-linked-list/

给你一个链表的头节点 `head` 。
移除每个右侧有一个更大数值的节点。
返回修改后链表的头节点 `head` 。

示例 1：

输入：head = [5,2,13,3,8] 输出：[13,8] 解释：需要移除的节点是 5 ，2 和 3 。 - 节点 13 在节点 5 右侧。 - 节点 13 在节点 2 右侧。 - 节点 8 在节点 3 右侧。
示例 2：
输入：head = [1,1,1,1] 输出：[1,1,1,1] 解释：每个节点的值都是 1 ，所以没有需要移除的节点。

提示：
给定列表中的节点数目在范围 `[1, 10^5]` 内
`1 <= Node.val <= 10^5`
"""

from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        反转链表 + 过滤：
        1. 先将链表反转
        2. 从反转后的头部开始遍历，维护当前遇到的最大值 cur_max
        3. 如果节点值 >= cur_max，保留该节点并更新 cur_max；否则跳过
        4. 再次反转得到最终结果
        """
        def reverse(node: Optional[ListNode]) -> Optional[ListNode]:
            prev = None
            curr = node
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev

        # 第一次反转
        reversed_head = reverse(head)

        # 过滤：只保留值 >= 右侧最大值的节点
        dummy = ListNode(0)
        tail = dummy
        cur_max = float('-inf')
        curr = reversed_head
        while curr:
            if curr.val >= cur_max:
                cur_max = curr.val
                tail.next = curr
                tail = tail.next
            curr = curr.next
        tail.next = None  # 切断尾部

        # 第二次反转，恢复原始顺序
        return reverse(dummy.next)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Stack, Recursion, Linked List, Monotonic Stack
#
# 解题思路:
# 采用"两次反转"的迭代方法。首先将链表完全反转，这样原本在"右侧"的节点就变成了
# "左侧"。然后遍历反转后的链表，维护当前遇到的最大值 cur_max，遇到值 >= cur_max
# 的节点就保留并更新 cur_max，否则移除。过滤完成后再次反转链表恢复原始顺序。
# 这样等同于移除了所有"右侧有更大值"的节点。
#
# 时间复杂度: O(n) — 两次反转各 O(n)，一次过滤遍历 O(n)
# 空间复杂度: O(1) — 只使用常数个指针变量，不依赖额外数据结构
#
# 关键点:
# - 反转链表使得"右侧"变成"左侧"，简化了比较逻辑
# - 过滤时使用虚拟头节点 dummy 简化链表重建
# - 过滤结束后必须将 tail.next 置为 None，切断与旧链表的连接
# - 如果节点值相等（>=），保留该节点（处理重复值的情况）
