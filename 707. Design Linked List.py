"""
LeetCode #707 - Design Linked List
中文题名：设计链表
https://leetcode.com/problems/design-linked-list/

Design your implementation of the linked list. You can choose to use the singly linked
list or the doubly linked list. A node in a singly linked list should have two
attributes: `val` and `next`. `val` is the value of
the current node, and `next` is a pointer/reference to the next
node. If you want to use the doubly linked list, you will need one more attribute
`prev` to indicate the previous node in the linked list. Assume all nodes in the
linked list are 0-indexed.

Implement these functions in your linked list class:

get(index) : Get the value of the `index`-th node in the linked
list. If the index is invalid, return `-1`.

addAtHead(val) : Add a node of value `val` before the first element of
the linked list. After the insertion, the new node will be the first node of the linked
list.

addAtTail(val) : Append a node of value `val` to the last element of the
linked list.

addAtIndex(index, val) : Add a node of value `val` before the `index`-th node
in the linked list. If `index` equals to the length of linked
list, the node will be appended to the end of linked list. If index is greater than the
length, the node will not be inserted. If index is negative, the node will be inserted
at the head of the list.

deleteAtIndex(index) : Delete the `index`-th node in the linked
list, if the index is valid.

Example:

MyLinkedList linkedList = new MyLinkedList();
linkedList.addAtHead(1);
linkedList.addAtTail(3);
linkedList.addAtIndex(1, 2);  // linked list becomes 1->2->3
linkedList.get(1);            // returns 2
linkedList.deleteAtIndex(1);  // now the linked list is 1->3
linkedList.get(1);            // returns 3

Note:

All values will be in the range of `[1, 1000]`.

The number of operations will be in the range of `[1, 1000]`.

Please do not use the built-in LinkedList library.

【中文翻译】
设计你的链表实现。你可以选择使用单向链表或双向链表。单向链表中的节点应有两个属性：`val` 和 `next`。`val` 是当前节点的值，`next` 是指向下一个节点的指针/引用。如果要使用双向链表，则还需要一个属性 `prev` 来指示链表中的前一个节点。假设链表中的所有节点都是 0 索引的。

在你的链表类中实现以下方法：

get(index)：获取链表中第 `index` 个节点的值。如果索引无效，则返回 `-1`。

addAtHead(val)：在链表的第一个元素之前添加一个值为 `val` 的节点。插入后，新节点将成为链表的第一个节点。

addAtTail(val)：将值为 `val` 的节点追加为链表的最后一个元素。

addAtIndex(index, val)：在链表的第 `index` 个节点之前添加值为 `val` 的节点。如果 `index` 等于链表的长度，则该节点将附加在链表的末尾。如果 index 大于链表长度，则不会插入节点。如果 index 为负数，则会在头部插入节点。

deleteAtIndex(index)：如果索引有效，则删除链表中第 `index` 个节点。

示例：

MyLinkedList linkedList = new MyLinkedList();
linkedList.addAtHead(1);
linkedList.addAtTail(3);
linkedList.addAtIndex(1, 2);  // 链表变为 1->2->3
linkedList.get(1);            // 返回 2
linkedList.deleteAtIndex(1);  // 现在链表变为 1->3
linkedList.get(1);            // 返回 3

注意：

所有值将在 `[1, 1000]` 范围内。

操作次数将在 `[1, 1000]` 范围内。

请不要使用内置的 LinkedList 库。
"""

from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        cur = self.head
        for _ in range(index):
            cur = cur.next
        return cur.val

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val, self.head)
        self.head = new_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        if not self.head:
            self.head = ListNode(val)
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = ListNode(val)
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            if index < 0:
                self.addAtHead(val)
            return
        if index == 0:
            self.addAtHead(val)
            return
        cur = self.head
        for _ in range(index - 1):
            cur = cur.next
        new_node = ListNode(val, cur.next)
        cur.next = new_node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        if index == 0:
            self.head = self.head.next
        else:
            cur = self.head
            for _ in range(index - 1):
                cur = cur.next
            cur.next = cur.next.next
        self.size -= 1









# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用单向链表实现，维护 head 指针和 size 变量。
# - get(index): 遍历到第 index 个节点，返回其值。O(index)。
# - addAtHead(val): 创建新节点，指向当前 head，更新 head。O(1)。
# - addAtTail(val): 遍历到尾部后追加。O(n)；可用 tail 指针优化到 O(1)。
# - addAtIndex(index, val): 遍历到 index-1 位置后插入。O(index)。
# - deleteAtIndex(index): 遍历到 index-1 位置后删除。O(index)。
# size 变量用于快速判断 index 是否有效。
#
# 时间复杂度: 各操作 O(k) 其中 k = index；addAtHead O(1)
# 空间复杂度: O(n) - n 个节点的存储
#
# 关键点:
# - size 变量避免每次遍历计算长度
# - 注意 index 边界条件（负数、等于 size、超出）
# - 使用哨兵节点（dummy head）可以简化头部操作（可选优化）
