"""
LeetCode #988 - Smallest String Starting From Leaf
中文题名：从叶节点开始的最小字符串
https://leetcode.com/problems/smallest-string-starting-from-leaf/

给定一个二叉树的根节点 root，每个节点的值在 0 到 25 之间，分别代表字母 'a' 到 'z'：值 0 代表 'a'，值 1 代表 'b'，依此类推。

找出按字典序最小的字符串，该字符串从这棵树的一个叶节点开始，到根节点结束。

（作为提示，字符串中任何较短的前缀在字典序上都是较小的：例如，按字典序 "ab" 比 "aba" 要小。叶节点是没有子节点的节点。）

【中文翻译】
给定一棵二叉树，每个节点的值 0-25 对应字母 a-z。找出从某个叶子节点到根节点路径形成的字符串中，字典序最小的那个。注意字符串方向是从叶子到根（从下到上）。

"""

from typing import List, Optional


class Solution:
    def smallestFromLeaf(self, root: Optional['TreeNode']) -> str:
        self.ans = None

        def dfs(node: Optional['TreeNode'], path: List[str]) -> None:
            if node is None:
                return
            # Prepend current character (build from leaf to root)
            path.append(chr(ord('a') + node.val))
            if node.left is None and node.right is None:
                # Leaf node: form string from leaf to root (reverse of path)
                cur = ''.join(reversed(path))
                if self.ans is None or cur < self.ans:
                    self.ans = cur
            dfs(node.left, path)
            dfs(node.right, path)
            path.pop()

        dfs(root, [])
        return self.ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# DFS 回溯法：
# 1. 使用深度优先搜索遍历二叉树，维护从根到当前节点的路径（用列表存储字符）。
# 2. 到达叶节点时，将路径反转得到从叶到根的字符串，与当前最优解比较，保留字典序更小的。
# 3. 关键技巧：
#    - 构建字符串时，先从根向下收集字符，到叶节点时再反转得到"叶子到根"的字符串。
#    - 也可以使用自底向上的递归，直接在叶节点返回字符串。
# 4. 字典序比较：Python 字符串可以直接比较，按字母顺序。
#
# 时间复杂度: O(N * H)，N 为节点数，H 为树高。每个叶节点构造一个长度为 H 的字符串进行比较。
#   - 更优的实现可以达到 O(N^2) 最坏，但通常 O(N log N)。
# 空间复杂度: O(H)，递归栈深度 + 路径列表
#
# 关键点:
# - 字符串方向是从叶子到根（不是根到叶子）
# - 需要在叶节点处将路径反转再比较字典序
# - 使用回溯（path.pop()）恢复状态，避免路径污染其他分支
# - 字典序比较：Python 字符串直接比较，但注意 "ab" < "aba"（短前缀更小）
