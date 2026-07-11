"""
LeetCode #998 - Maximum Binary Tree II
中文题名：最大二叉树 II
https://leetcode.com/problems/maximum-binary-tree-ii/

给定一个最大树的根节点 root：最大树是指每个节点都有一个大于其子树中任何其他值的值。

和前面的问题一样，给定的树是从列表 A（root = Construct(A)）通过以下 Construct(A) 递归地构造的：

如果 A 为空，返回 null。
否则，令 A[i] 是 A 中的最大元素。创建一个值为 A[i] 的根节点 root。
root 的左子节点为 Construct([A[0], A[1], ..., A[i-1]])
root 的右子节点为 Construct([A[i+1], A[i+2], ..., A[A.length - 1]])
返回 root。

注意，我们没有直接给出 A，只有一个根节点 root = Construct(A)。

假设 B 是 A 的一个副本，并在末尾追加了值 val。保证 B 中的值是唯一的。

返回 Construct(B)。

示例 1：

输入：root = [4,1,3,null,null,2], val = 5
输出：[5,4,null,1,3,null,null,2]
解释：A = [1,4,2,3], B = [1,4,2,3,5]

示例 2：

输入：root = [5,2,4,null,1], val = 3
输出：[5,2,4,null,1,null,3]
解释：A = [2,1,5,4], B = [2,1,5,4,3]

示例 3：

输入：root = [5,2,3,null,1], val = 4
输出：[5,2,4,null,1,3]
解释：A = [2,1,5,3], B = [2,1,5,3,4]

【中文翻译】
已知一棵最大二叉树（根节点的值是整棵树的最大值，左子树是原数组左半部分的最大二叉树，右子树是原数组右半部分的最大二叉树）。现在在原数组末尾追加一个新值 val，要求返回更新后的最大二叉树。由于 val 是追加在末尾的，它应该出现在树的最右边。

"""

from typing import List, Optional


class Solution:
    def insertIntoMaxTree(self, root: Optional['TreeNode'], val: int) -> Optional['TreeNode']:
        new_node = TreeNode(val)
        if root is None:
            return new_node
        if val > root.val:
            # val becomes the new root, old root becomes left child
            new_node.left = root
            return new_node
        # val < root.val, it must go to the right subtree
        # Because val is appended at the end of the array
        root.right = self.insertIntoMaxTree(root.right, val)
        return root



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 递归插入：
# 1. 最大二叉树的性质：
#    - 根节点值是整棵树的最大值。
#    - 左子树由原数组中最大值左侧的元素构成。
#    - 右子树由原数组中最大值右侧的元素构成。
# 2. val 被追加在原数组末尾，意味着它只能出现在当前最大二叉树的"最右边"位置。
# 3. 递归逻辑：
#    - 如果 val > root.val，val 比当前根大，需要成为新的根。新根的左子树是原来的整棵树。
#      （因为 val 在数组末尾，其左侧所有元素构成左子树，右侧为空）
#    - 如果 val < root.val，val 必须插入到右子树中（因为它在数组中位于 root.val 的右侧）。
#      递归调用 insertIntoMaxTree(root.right, val)。
# 4. 由于 val 是唯一追加的值且所有值互不相同，不需要处理相等的情况。
#
# 时间复杂度: O(N)，最坏情况 val 比所有节点都小，遍历整条右链（链状树）
# 空间复杂度: O(H)，递归栈深度，最坏 O(N)，平均 O(log N)
#
# 关键点:
# - val 追加在数组末尾，意味着它在树中一定在右子树上
# - 如果 val 大于当前根，新值成为根，原树成为左子树
# - 如果 val 小于当前根，递归向右子树插入
# - 新值插入的位置一定在某条"纯右链"上
# - 因为数组中的位置决定：val 在原数组最大值右侧（即右子树方向）
