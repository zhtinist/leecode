"""
LeetCode #230 - Kth Smallest Element in a BST
https://leetcode.com/problems/kth-smallest-element-in-a-bst/

Given a binary search tree, write a function `kthSmallest` to find the kth
smallest element in it.

Note:

You may assume k is always valid, 1 <= k <= BST's total elements.

Example 1:

Input: root = [3,1,4,null,2], k = 1
3
/ \
1   4
\
2
Output: 1

Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
5
/ \
3   6
/ \
2   4
/
1
Output: 3

Follow up:

What if the BST is modified (insert/delete operations) often and you need to find the kth
smallest frequently? How would you optimize the kthSmallest routine?
"""

from typing import List, Optional


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right

        return -1


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 利用 BST 的中序遍历是升序序列这一性质。使用迭代方式(显式栈)进行中序遍历:
# - 从根节点开始，将所有左子节点入栈(一路向左走到最左边)
# - 弹出栈顶节点(当前最小值)，k 减 1
# - 如果 k == 0，当前节点就是第 k 小的元素，直接返回
# - 否则转向右子树继续遍历
# 迭代方式避免递归栈溢出，且可以在找到第 k 个元素时提前终止，
# 不需要遍历整棵树。
#
# 时间复杂度: O(H + k) - 其中 H 是树高，需要先走到最左节点，然后依次弹出 k 个元素
#   最坏情况 O(n) (树退化成链表且 k=n)
# 空间复杂度: O(H) - 栈中存储的节点数等于树高，最坏 O(n)
#
# 关键点:
# - BST 中序遍历 = 升序序列，这是核心性质
# - 找到第 k 个后立即返回，不需要完成整个遍历
# - 迭代方式比递归更可控，避免递归深度问题
# - 进阶: 如果频繁查询，可以在节点中维护左子树大小，将查询优化到 O(log n)
