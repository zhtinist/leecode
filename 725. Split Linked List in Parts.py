"""
LeetCode #725 - Split Linked List in Parts
中文题名：分隔链表
https://leetcode.com/problems/split-linked-list-in-parts/

Given a (singly) linked list with head node `root`, write a function to split the
linked list into `k` consecutive linked list "parts".

The length of each part should be as equal as possible: no two parts should have a size
differing by more than 1. This may lead to some parts being null.

The parts should be in order of occurrence in the input list, and parts occurring earlier
should always have a size greater than or equal parts occurring later.

Return a List of ListNode's representing the linked list parts that are formed.

Examples
1->2->3->4, k = 5 // 5 equal parts
[ [1],
[2],
[3],
[4],
null ]

Example 1:

Input:
root = [1, 2, 3], k = 5
Output: [[1],[2],[3],[],[]]
Explanation:
The input and each element of the output are ListNodes, not arrays.
For example, the input root has root.val = 1, root.next.val = 2, \root.next.next.val = 3, and root.next.next.next = null.
The first element output[0] has output[0].val = 1, output[0].next = null.
The last element output[4] is null, but it's string representation as a ListNode is [].

Example 2:

Input:
root = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 3
Output: [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
Explanation:
The input has been split into consecutive parts with size difference at most 1, and earlier parts are a larger size than the later parts.

Note:

The length of `root` will be in the range `[0, 1000]`.

Each value of a node in the input will be an integer in the range `[0, 999]`.

`k` will be an integer in the range `[1, 50]`.

【中文翻译】
给定一个头结点为 root 的（单）链表，编写一个函数将链表分隔为 k 个连续的部分。

每部分的长度应该尽可能的相等：任意两部分的长度差距不能超过 1。这可能意味着有些部分为 null。

这 k 个部分应该按照在链表中出现的顺序进行输出，并且排在前面的部分的长度应该大于或等于后面的长度。

返回一个符合上述规则的链表的列表。

举例：1->2->3->4, k = 5 // 5 个相等部分
[ [1],
[2],
[3],
[4],
null ]

示例 1：

输入：
root = [1, 2, 3], k = 5
输出：[[1],[2],[3],[],[]]
解释：
输入和输出的每个元素都是 ListNode 类型，而非数组。
例如，输入的 root 中 root.val = 1, root.next.val = 2, \root.next.next.val = 3, 且 root.next.next.next = null。
第一个输出 output[0] 的 output[0].val = 1, output[0].next = null。
最后一个元素 output[4] 为 null，但它作为 ListNode 的字符串表示是 []。

示例 2：

输入：
root = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 3
输出：[[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
解释：
输入被分成了几个连续的部分，并且每部分的长度相差不超过 1。前面部分的长度大于等于后面部分的长度。

注意：

root 的长度范围在 [0, 1000]。

输入的每个节点的值都是一个在 [0, 999] 范围内的整数。

k 的取值范围为 [1, 50]。
"""

from typing import List, Optional


class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # Count length
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        # Calculate part sizes
        part_size = length // k
        extra = length % k

        result = []
        curr = head
        for i in range(k):
            result.append(curr)
            part_len = part_size + (1 if i < extra else 0)
            for j in range(part_len - 1):
                if curr:
                    curr = curr.next
            if curr:
                next_part = curr.next
                curr.next = None
                curr = next_part

        return result



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 首先遍历链表计算总长度 length。
# 每部分的基本大小为 part_size = length // k，前 extra = length % k 个部分多一个节点。
# 再次遍历链表，对于每个部分：
# - 确定该部分应有的长度（基本大小 + 是否在 extra 范围内）
# - 移动指针到该部分的最后一个节点，断开链表并记录下一部分的起始位置
# - 如果长度不够（链表已经遍历完），该部分为 None
#
# 时间复杂度: O(N + k) - N 为链表长度，k 为部分数
# 空间复杂度: O(k) - 存储 k 个部分的头节点引用（不包含已有链表节点）
#
# 关键点:
# - 两部分之间大小差最多为 1
# - 前面部分的长度 >= 后面部分的长度
# - 当 k > length 时，后面的部分为 None
# - 每个部分都需要断开链表（将最后一个节点的 next 设为 None）
