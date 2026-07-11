"""
LeetCode #1669 - Merge In Between Linked Lists
中文题名：合并两个链表
https://leetcode.com/problems/merge-in-between-linked-lists/

You are given two linked lists: `list1` and `list2` of sizes
`n` and `m` respectively.

Remove `list1`'s nodes from the `ath` node to the
`bth` node, and put `list2` in their place.

The blue edges and nodes in the following figure incidate the result:

Build the result list and return its head.

Example 1:

Input: list1 = [0,1,2,3,4,5], a = 3, b = 4, list2 = [1000000,1000001,1000002]
Output: [0,1,2,1000000,1000001,1000002,5]
Explanation: We remove the nodes 3 and 4 and put the entire list2 in their place. The blue edges and nodes in the above figure indicate the result.

Example 2:

Input: list1 = [0,1,2,3,4,5,6], a = 2, b = 5, list2 = [1000000,1000001,1000002,1000003,1000004]
Output: [0,1,1000000,1000001,1000002,1000003,1000004,6]
Explanation: The blue edges and nodes in the above figure indicate the result.

Constraints:

`3 <= list1.length <= 104`

`1 <= a <= b < list1.length - 1`

`1 <= list2.length <= 104`

【中文翻译】
给定两个链表list1和list2，大小分别为n和m。

移除list1中从第a个节点到第b个节点的部分，并将list2插入该位置。

构建结果链表并返回其头节点。

示例1：

输入：list1 = [0,1,2,3,4,5], a = 3, b = 4, list2 = [1000000,1000001,1000002]
输出：[0,1,2,1000000,1000001,1000002,5]
解释：移除节点3和4，将整个list2插入它们的位置。

示例2：

输入：list1 = [0,1,2,3,4,5,6], a = 2, b = 5, list2 = [1000000,1000001,1000002,1000003,1000004]
输出：[0,1,1000000,1000001,1000002,1000003,1000004,6]

约束条件：

3 <= list1.length <= 10^4
1 <= a <= b < list1.length - 1
1 <= list2.length <= 10^4

"""

from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # 找到第 a-1 个节点（a的前驱）
        before_a = list1
        for _ in range(a - 1):
            before_a = before_a.next

        # 找到第 b 个节点
        node_b = before_a
        for _ in range(b - a + 2):
            node_b = node_b.next

        # 找到 list2 的尾节点
        tail2 = list2
        while tail2.next:
            tail2 = tail2.next

        # 连接：before_a -> list2 -> node_b.next
        before_a.next = list2
        tail2.next = node_b.next

        return list1










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 链表操作。分三步：
# 1. 遍历list1找到第a-1个节点（before_a）
# 2. 从before_a继续遍历找到第b个节点（node_b），然后取node_b.next作为后半段起点
# 3. 遍历list2找到尾节点（tail2）
# 最后连接：before_a.next = list2, tail2.next = node_b.next
#
# 时间复杂度: O(n + m)，其中n是list1长度，m是list2长度
# 空间复杂度: O(1)，只使用几个指针
#
# 关键点:
# - 定位a的前驱节点（第a-1个）
# - 定位b节点，保存b.next作为后续
# - 找到list2的尾节点完成连接
