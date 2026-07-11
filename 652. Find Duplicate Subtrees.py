"""
LeetCode #652 - Find Duplicate Subtrees
中文题名：寻找重复的子树
https://leetcode.com/problems/find-duplicate-subtrees/

Given a binary tree, return all duplicate subtrees. For each kind of duplicate subtrees, you
only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with same node values.

Example 1:

1
/ \
2   3
/   / \
4   2   4
/
4

The following are two duplicate subtrees:

2
/
4

and

4

Therefore, you need to return above trees' root in the form of a list.

【中文翻译】
给定一棵二叉树，返回所有重复的子树。对于每种重复的子树，你只需要返回其中任意一棵的根节点。

如果两棵树具有相同的结构和相同的节点值，则认为它们是重复的。

示例 1：

        1
       / \
      2   3
     /   / \
    4   2   4
       /
      4

以下是两棵重复的子树：

      2
     /
    4

和

    4

因此，你需要以列表形式返回上述子树的根节点。
"""

from typing import List, Optional


class Solution:
    def findDuplicateSubtrees(self, root: Optional['TreeNode']) -> List[Optional['TreeNode']]:
        from collections import defaultdict

        count: dict[str, int] = defaultdict(int)
        result: list[Optional['TreeNode']] = []

        def serialize(node: Optional['TreeNode']) -> str:
            if not node:
                return "#"
            key = f"{node.val},{serialize(node.left)},{serialize(node.right)}"
            count[key] += 1
            if count[key] == 2:
                result.append(node)
            return key

        serialize(root)
        return result











# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用后序遍历将每棵子树序列化为唯一的字符串标识。
# 序列化格式："节点值,左子树序列化,右子树序列化"，空节点用 "#" 表示。
# 用哈希表统计每种序列化字符串出现的次数：
# - 当某序列化串第一次出现（count == 1），继续
# - 当某序列化串第二次出现（count == 2），将该子树的根节点加入结果
# - 第三次及以后不再重复添加（题目要求每种重复只返回一个）
# 后序遍历保证在检查当前节点之前，其左右子树的序列化已经完成。
#
# 时间复杂度: O(n^2) - 每个节点遍历一次，但字符串拼接在最坏情况下（斜树）每次产生 O(n) 字符串
# 空间复杂度: O(n^2) - 存储所有序列化字符串，每串长度可能为 O(n)
#
# 关键点:
# - 后序遍历序列化每棵子树
# - 用哈希表计数去重
# - count == 2 时添加（确保重复的只记录一次）
# - 可优化为用 uid 代替字符串来降低到 O(n)：
#   给每个 (val, left_uid, right_uid) 三元组分配唯一 ID
