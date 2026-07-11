"""
LeetCode #817 - Linked List Components
中文题名：链表组件
https://leetcode.com/problems/linked-list-components/

We are given `head`, the head node of a linked list
containing unique integer values.

We are also given the list `G`, a subset of the values in the linked list.

Return the number of connected components in `G`, where two values are connected
if they appear consecutively in the linked list.

Example 1:

Input:
head: 0->1->2->3
G = [0, 1, 3]
Output: 2
Explanation:
0 and 1 are connected, so [0, 1] and [3] are the two connected components.

Example 2:

Input:
head: 0->1->2->3->4
G = [0, 3, 1, 4]
Output: 2
Explanation:
0 and 1 are connected, 3 and 4 are connected, so [0, 1] and [3, 4] are the two connected components.

Note:

If `N` is the length of the linked list given by `head`, `1
<= N <= 10000`.

The value of each node in the linked list will be in the range` [0, N - 1]`.

`1 <= G.length <= 10000`.

`G` is a subset of all values in the linked list.

【中文翻译】
给定一个包含唯一整数值的链表的头节点 `head`。
同时给定列表 `G`，它是链表中值的子集。

返回 `G` 中连通分量的数量。如果两个值在链表中连续出现，则它们是连通的。

示例 1：
输入：head: 0->1->2->3, G = [0, 1, 3]
输出：2
解释：0 和 1 是连通的，所以 [0, 1] 和 [3] 是两个连通分量。

示例 2：
输入：head: 0->1->2->3->4, G = [0, 3, 1, 4]
输出：2
解释：0 和 1 是连通的，3 和 4 是连通的，所以 [0, 1] 和 [3, 4] 是两个连通分量。

注意：
如果 `N` 是由 `head` 给出的链表长度，`1 <= N <= 10000`。
链表中每个节点的值在范围 `[0, N - 1]` 内。
`1 <= G.length <= 10000`。
`G` 是链表中所有值的子集。
"""

from typing import List, Optional


class Solution:
    def numComponents(self, head: Optional['ListNode'], nums: List[int]) -> int:
        g_set = set(nums)
        count = 0
        cur = head
        in_component = False
        while cur:
            if cur.val in g_set:
                if not in_component:
                    count += 1
                    in_component = True
            else:
                in_component = False
            cur = cur.next
        return count



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 将 G 转换为集合以便 O(1) 查找。遍历链表，
# 用一个布尔标志 `in_component` 跟踪是否当前处于一个连通分量中。
# 当遇到在 G 中的节点且之前不在分量中时，说明发现了新的分量，
# 计数加 1 并设置标志为 True。
# 当遇到不在 G 中的节点时，结束当前分量，设置标志为 False。
#
# 时间复杂度: O(N) - 遍历链表一次
# 空间复杂度: O(M) - 存储 G 的哈希集合，M = len(G)
#
# 关键点:
# - 用集合加速查找
# - 计数分量的开始（从"不在 G"到"在 G"的转换）
# - 不需要存储节点之间的实际连接关系，
#   因为链表顺序就是连接关系的定义
