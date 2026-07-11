"""
LeetCode #606 - Construct String from Binary Tree
中文题名：根据二叉树创建字符串
https://leetcode.com/problems/construct-string-from-binary-tree/

You need to construct a string consists of parenthesis and integers from a binary tree with
the preorder traversing way.

The null node needs to be represented by empty parenthesis pair "()". And you need to omit
all the empty parenthesis pairs that don't affect the one-to-one mapping relationship
between the string and the original binary tree.

Example 1:

Input: Binary tree: [1,2,3,4]
1
/   \
2     3
/
4

Output: "1(2(4))(3)"

Explanation: Originallay it needs to be "1(2(4)())(3()())",
but you need to omit all the unnecessary empty parenthesis pairs.
And it will be "1(2(4))(3)".

Example 2:

Input: Binary tree: [1,2,3,null,4]
1
/   \
2     3
\
4

Output: "1(2()(4))(3)"

Explanation: Almost the same as the first example,
except we can't omit the first parenthesis pair to break the one-to-one mapping relationship between the input and the output.

【中文翻译】
你需要根据一棵二叉树，通过前序遍历的方式构造一个由括号和整数组成的字符串。

空节点需要用一对空括号对 "()" 来表示。而且你需要省略所有不影响字符串与原始二叉树
之间一一映射关系的空括号对。

示例 1：

输入：二叉树：[1,2,3,4]
       1
     /   \
    2     3
   /
  4

输出："1(2(4))(3)"

解释：原本应为 "1(2(4)())(3()())"，
但你需要省略所有不必要的空括号对。
结果将是 "1(2(4))(3)"。

示例 2：

输入：二叉树：[1,2,3,null,4]
       1
     /   \
    2     3
     \
      4

输出："1(2()(4))(3)"

解释：和第一个示例几乎相同，
除了我们无法省略第一对括号来保持输入和输出之间的一一映射关系。
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""

        left = self.tree2str(root.left)
        right = self.tree2str(root.right)

        # Case 1: No children
        if not left and not right:
            return str(root.val)

        # Case 2: Right child only -> left must show as "()"
        if not left:
            return f"{root.val}()({right})"

        # Case 3: Left child only -> omit empty right
        if not right:
            return f"{root.val}({left})"

        # Case 4: Both children
        return f"{root.val}({left})({right})"



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 递归地进行前序遍历，根节点值直接追加到字符串，然后递归处理左右子树：
# - 如果左右子树都为空，只需输出节点值本身。
# - 如果仅左子树非空（右子树空），需要括上左子树但省略右子树，即 val(left)。
# - 如果仅右子树非空（左子树空），不能省略左子树的空括号（保持唯一映射），即 val()(right)。
# - 如果左右子树都非空，两边都括起来，即 val(left)(right)。
#
# 时间复杂度: O(n) - 每个节点访问一次
# 空间复杂度: O(H) - H 为树的高度，递归栈空间，最坏 O(n)
#
# 关键点:
# - 核心规则：左子树空但右子树非空时，左子树的 "()" 不能省略
# - 左子树非空而右子树空时，右子树的 "()" 可以省略
# - 递归或迭代都可行，递归写法更直观
