"""
LeetCode #655 - Print Binary Tree
中文题名：输出二叉树
https://leetcode.com/problems/print-binary-tree/

Print a binary tree in an m*n 2D string array following these rules:

The row number `m` should be equal to the height of the given binary tree.

The column number `n` should always be an odd number.

The root node's value (in string format) should be put in the exactly middle of the
first row it can be put. The column and the row where the root node belongs will
separate the rest space into two parts (left-bottom part and right-bottom part).
You should print the left subtree in the left-bottom part and print the right subtree in
the right-bottom part. The left-bottom part and the right-bottom part should have the
same size. Even if one subtree is none while the other is not, you don't need to print
anything for the none subtree but still need to leave the space as large as that for the
other subtree. However, if two subtrees are none, then you don't need to leave space for
both of them.

Each unused space should contain an empty string `""`.

Print the subtrees following the same rules.

Example 1:

Input:
1
/
2
Output:
[["", "1", ""],
["2", "", ""]]

Example 2:

Input:
1
/ \
2   3
\
4
Output:
[["", "", "", "1", "", "", ""],
["", "2", "", "", "", "3", ""],
["", "", "4", "", "", "", ""]]

Example 3:

Input:
1
/ \
2   5
/
3
/
4
Output:

[["",  "",  "", "",  "", "", "", "1", "",  "",  "",  "",  "", "", ""]
["",  "",  "", "2", "", "", "", "",  "",  "",  "",  "5", "", "", ""]
["",  "3", "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]
["4", "",  "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]]

Note:
The height of binary tree is in the range of [1, 10].

【中文翻译】
在一个 m*n 的二维字符串数组中输出二叉树，遵循以下规则：

行数 `m` 应等于给定二叉树的高度。

列数 `n` 应始终为奇数。

根节点的值（以字符串格式）应放在第一行的正中间位置。根节点所在的行和列将剩余空间分成两部分（左下部分和右下部分）。你应该在左下部分输出左子树，在右下部分输出右子树。左下部分和右下部分应具有相同的大小。即使一个子树为空而另一个非空，你不需要为空的子树输出任何内容，但仍需要为另一个子树保留同样大小的空间。但是，如果两个子树都为空，则不需要为它们保留空间。

每个未使用的空间应包含空字符串 `""`。

以相同的规则输出子树。

示例 1：

输入：
     1
    /
   2
输出：
[["", "1", ""],
 ["2", "", ""]]

示例 2：

输入：
     1
    / \
   2   3
    \
     4
输出：
[["", "", "", "1", "", "", ""],
 ["", "2", "", "", "", "3", ""],
 ["", "", "4", "", "", "", ""]]

注意：
二叉树的高度在 [1, 10] 范围内。
"""

from typing import List, Optional


class Solution:
    def printTree(self, root: Optional['TreeNode']) -> List[List[str]]:
        def get_height(node: Optional['TreeNode']) -> int:
            if not node:
                return 0
            return 1 + max(get_height(node.left), get_height(node.right))

        height = get_height(root)
        width = (1 << height) - 1  # 2^height - 1
        res = [[""] * width for _ in range(height)]

        def fill(node: Optional['TreeNode'], row: int, left: int, right: int) -> None:
            if not node:
                return
            mid = (left + right) // 2
            res[row][mid] = str(node.val)
            fill(node.left, row + 1, left, mid - 1)
            fill(node.right, row + 1, mid + 1, right)

        fill(root, 0, 0, width - 1)
        return res











# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 分两步：
# 1. 计算树的高度 height，确定矩阵维度：
#    - 行数 m = height
#    - 列数 n = 2^height - 1
# 2. 递归填充矩阵：
#    - 根节点放在当前区间 [left, right] 的中间位置 mid = (left + right) // 2
#    - 左子树填充到 [left, mid-1]，右子树填充到 [mid+1, right]
#    - 当节点为空时，不填充任何内容（保持 ""）
# 初始化时用 "" 填充所有位置，然后递归覆盖需要的位置。
#
# 时间复杂度: O(h * 2^h) - 需要填充整个矩阵，矩阵大小为 height * (2^height - 1)
# 空间复杂度: O(h * 2^h) - 结果矩阵的大小
#
# 关键点:
# - 列宽 = 2^height - 1（满二叉树性质）
# - 根节点始终在子区间正中间
# - 递归参数同时传递行号（row）和列区间（left, right）
# - h <= 10，所以 2^10 = 1024，矩阵大小可控
