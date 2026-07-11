"""
LeetCode #889 - Construct Binary Tree from Preorder and Postorder Traversal
中文题名：根据前序和后序遍历构造二叉树
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/

Return any binary tree that matches the given preorder and postorder traversals.

Values in the traversals `pre` and `post` are distinct positive
integers.

Example 1:

Input: pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
Output: [1,2,3,4,5,6,7]

Note:

`1 <= pre.length == post.length <= 30`

`pre[]` and `post[]` are both permutations of `1, 2,
..., pre.length`.

It is guaranteed an answer exists. If there exists multiple answers, you can return
any of them.

【中文翻译】

返回任意一个与前序和后序遍历匹配的二叉树。

遍历中的值 `pre` 和 `post` 是不同的正整数。

示例 1：

输入：pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
输出：[1,2,3,4,5,6,7]

注意：

`1 <= pre.length == post.length <= 30`

`pre[]` 和 `post[]` 都是 `1, 2, ..., pre.length` 的排列。

保证答案存在。如果存在多个答案，可以返回任意一个。

"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructFromPrePost(
        self, pre: List[int], post: List[int]
    ) -> Optional[TreeNode]:
        if not pre:
            return None

        root = TreeNode(pre[0])
        if len(pre) == 1:
            return root

        # 前序第二个元素是左子树的根节点
        left_root_val = pre[1]
        # 在后序中找到左子树根节点的位置，确定左子树大小
        left_size = post.index(left_root_val) + 1

        root.left = self.constructFromPrePost(
            pre[1:1 + left_size], post[:left_size]
        )
        root.right = self.constructFromPrePost(
            pre[1 + left_size:], post[left_size:-1]
        )

        return root



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 递归构造。前序遍历(pre)的第一个元素是根节点。
# 第二个元素是左子树的根节点。在后序遍历(post)中找到左子树根节点的位置，
# 即可确定左子树的节点数量（左子树大小 = post中左根位置 + 1）。
# 然后递归构建左右子树：
# - 左子树：pre[1:1+left_size], post[:left_size]
# - 右子树：pre[1+left_size:], post[left_size:-1]（去掉最后一个根节点）
#
# 时间复杂度: O(N^2) — 每次递归中 post.index() 需要 O(N)
# 空间复杂度: O(N) — 递归栈深度
#
# 关键点:
# - 答案不唯一，任意一种合法构造均可
# - 通过前序第二个元素定位左子树是关键
# - 当 pre 长度为 1 时直接返回叶子节点
# - 可以用哈希表预先存储 post 值的索引，优化到 O(N)
