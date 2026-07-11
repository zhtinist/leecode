"""
LeetCode #3217 - Delete Nodes From Linked List Present in Array
从链表中移除在数组中存在的节点
https://leetcode.cn/problems/delete-nodes-from-linked-list-present-in-array/

给你一个整数数组 `nums` 和一个链表的头节点 `head`。从链表中移除所有存在于 `nums` 中的节点后，返回修改后的链表的头节点。

示例 1：

输入： nums = [1,2,3], head = [1,2,3,4,5]
输出： [4,5]
解释：

移除数值为 1, 2 和 3 的节点。
示例 2：

输入： nums = [1], head = [1,2,1,2,1,2]
输出： [2,2,2]
解释：

移除数值为 1 的节点。
示例 3：

输入： nums = [5], head = [1,2,3,4]
输出： [1,2,3,4]
解释：

链表中不存在值为 5 的节点。

提示：
`1 <= nums.length <= 10^5`
`1 <= nums[i] <= 10^5`
`nums` 中的所有元素都是唯一的。
链表中的节点数在 `[1, 10^5]` 的范围内。
`1 <= Node.val <= 10^5`
输入保证链表中至少有一个值没有在 `nums` 中出现过。
"""

from typing import List, Optional


class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        num_set = set(nums)
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        while cur.next:
            if cur.next.val in num_set:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Hash Table, Linked List
#
# 解题思路:
# 将 nums 转换为哈希集合以实现 O(1) 查找。
# 使用虚拟头节点（dummy head）简化边界处理。
# 遍历链表，如果当前节点的值在集合中则跳过（cur.next = cur.next.next），
# 否则移动到下一个节点。
#
# 时间复杂度: O(n + m) — n 为链表长度，m 为 nums 长度
# 空间复杂度: O(m)
#
# 关键点:
# - 使用 set 而非 list 进行快速查找
# - 哑节点技巧避免处理头节点被删除的特殊情况
