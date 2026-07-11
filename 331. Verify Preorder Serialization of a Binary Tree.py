"""
LeetCode #331 - Verify Preorder Serialization of a Binary Tree
中文题名：验证二叉树的前序序列化
https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/

One way to serialize a binary tree is to use pre-order traversal. When we encounter a
non-null node, we record the node's value. If it is a null node, we record using a
sentinel value such as `#`.

_9_
/   \
3     2
/ \   / \
4   1  #  6
/ \ / \   / \
# # # #   # #

For example, the above binary tree can be serialized to the string `"9,3,4,#,#,1,#,#,2,#,6,#,#"`,
where `#` represents a null node.

Given a string of comma separated values, verify whether it is a correct preorder traversal
serialization of a binary tree. Find an algorithm without reconstructing the tree.

Each comma separated value in the string must be either an integer or a character `'#'`
representing `null` pointer.

You may assume that the input format is always valid, for example it could never contain two
consecutive commas such as `"1,,3"`.

Example 1:

Input: `"9,3,4,#,#,1,#,#,2,#,6,#,#"`
Output: `true`

Example 2:

Input: `"1,#"`
Output: `false`

Example 3:

Input: `"9,#,#,1"`
Output: `false`

【中文翻译】
序列化二叉树的一种方法是使用前序遍历。当我们遇到一个非空节点时，记录该节点的值。如果是一个空节点，则使用标记值（如 '#'）来记录。

     _9_
    /   \
   3     2
  / \   / \
 4   1  #  6
/ \ / \   / \
# # # #   # #

例如，上面的二叉树可以被序列化为字符串 "9,3,4,#,#,1,#,#,2,#,6,#,#"，其中 '#' 代表一个空节点。

给定一串以逗号分隔的值，验证它是否是正确的二叉树的前序序列化。请找到一种不重建树的算法。

字符串中每个以逗号分隔的值必须是整数或表示 null 指针的字符 '#'。

你可以假设输入格式始终有效，例如它永远不会包含两个连续的逗号，如 "1,,3"。

示例 1：

输入："9,3,4,#,#,1,#,#,2,#,6,#,#"
输出：true

示例 2：

输入："1,#"
输出：false

示例 3：

输入："9,#,#,1"
输出：false
"""

from typing import List, Optional


class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        slots = 1
        for node in preorder.split(','):
            slots -= 1
            if slots < 0:
                return False
            if node != '#':
                slots += 2
        return slots == 0











# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用"槽位"思想：初始化槽位 slots = 1（根节点需要一个槽位）。
# 遍历每个节点：
# - 每遇到一个节点，消耗一个槽位（slots -= 1）
# - 如果 slots < 0，说明序列无效，返回 False
# - 如果节点不是 '#'（非空节点），则新增两个槽位（slots += 2），因为非空节点有两个子节点
# 遍历结束后，slots 必须等于 0，说明所有槽位恰好被填满。
# 这本质上是利用二叉树的性质：对于任意二叉树，空节点的数量 = 非空节点数量 + 1。
#
# 时间复杂度: O(n)，n 为序列长度
# 空间复杂度: O(n) —— split 操作产生的列表；可优化至 O(1) 不拆分
#
# 关键点:
# - 槽位（容量）的概念：每个非空节点消耗 1 个槽但产生 2 个槽
# - 空节点只消耗槽不产生槽
# - 遍历过程中槽位不应为负，最终必须归零
# - 类似问题也可以用"出度 = 入度"的图论角度理解
