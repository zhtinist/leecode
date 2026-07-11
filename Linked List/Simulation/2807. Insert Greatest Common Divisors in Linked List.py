"""
LeetCode #2807 - Insert Greatest Common Divisors in Linked List
在链表中插入最大公约数
https://leetcode.cn/problems/insert-greatest-common-divisors-in-linked-list/

给你一个链表的头 `head` ，每个结点包含一个整数值。
在相邻结点之间，请你插入一个新的结点，结点值为这两个相邻结点值的 最大公约数 。
请你返回插入之后的链表。
两个数的 最大公约数 是可以被两个数字整除的最大正整数。

示例 1：

输入：head = [18,6,10,3] 输出：[18,6,6,2,10,1,3] 解释：第一幅图是一开始的链表，第二幅图是插入新结点后的图（蓝色结点为新插入结点）。 - 18 和 6 的最大公约数为 6 ，插入第一和第二个结点之间。 - 6 和 10 的最大公约数为 2 ，插入第二和第三个结点之间。 - 10 和 3 的最大公约数为 1 ，插入第三和第四个结点之间。 所有相邻结点之间都插入完毕，返回链表。
示例 2：

输入：head = [7] 输出：[7] 解释：第一幅图是一开始的链表，第二幅图是插入新结点后的图（蓝色结点为新插入结点）。 没有相邻结点，所以返回初始链表。

提示：
链表中结点数目在 `[1, 5000]` 之间。
`1 <= Node.val <= 1000`
"""

from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        import math
        cur = head
        while cur and cur.next:
            gcd_val = math.gcd(cur.val, cur.next.val)
            new_node = ListNode(gcd_val)
            new_node.next = cur.next
            cur.next = new_node
            cur = new_node.next
        return head



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Linked List, Math, Number Theory
#
# 解题思路:
# 遍历链表，对每一对相邻节点 (cur, cur.next)，计算它们的最大公约数（GCD）。
# 创建一个新节点值为 GCD，插入到两个节点之间。注意更新遍历指针跳过新插入的节点（cur = new_node.next）。
# 当 cur.next 为 None 时停止。
#
# 时间复杂度: O(n * log M) 其中 M 是节点值的最大值，n 是节点数
# 空间复杂度: O(1) 仅使用额外指针
#
# 关键点:
# - 使用 math.gcd 计算最大公约数
# - 插入新节点后，cur 需要跳过新插入的节点（即 cur = new_node.next）
# - 注意 ListNode 类的定义（LeetCode 环境已预定义，这里也定义了方便测试）
