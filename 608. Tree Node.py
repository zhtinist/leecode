"""
LeetCode #608 - Tree Node
中文题名：树节点
https://leetcode.com/problems/tree-node/

Given a table `tree`, id is identifier of the tree node and p_id is
its parent node's id.

+----+------+
| id | p_id |
+----+------+
| 1  | null |
| 2  | 1    |
| 3  | 1    |
| 4  | 2    |
| 5  | 2    |
+----+------+

Each node in the tree can be one of three types:

Leaf: if the node is a leaf node.

Root: if the node is the root of the tree.

Inner: If the node is neither a leaf node nor a root node.

Write a query to print the node id and the type of the node. Sort your output by the node id.
The result for the above sample is:

+----+------+
| id | Type |
+----+------+
| 1  | Root |
| 2  | Inner|
| 3  | Leaf |
| 4  | Leaf |
| 5  | Leaf |
+----+------+

Explanation

Node '1' is root node, because its parent node is NULL and it has child node
'2' and '3'.

Node '2' is inner node, because it has parent node '1' and child node
'4' and '5'.

Node '3', '4' and '5' is Leaf node, because they have parent
node and they don't have child node.

And here is the image of the sample tree as below:

1
/   \
2       3
/   \
4       5

Note

If there is only one node on the tree, you only need to output its root
attributes.

【中文翻译】
给定一个表 `tree`，id 是树节点的标识，p_id 是其父节点的 id。

+----+------+
| id | p_id |
+----+------+
| 1  | null |
| 2  | 1    |
| 3  | 1    |
| 4  | 2    |
| 5  | 2    |
+----+------+

树中的每个节点可以是以下三种类型之一：

叶子节点（Leaf）：如果该节点是叶子节点。

根节点（Root）：如果该节点是树的根节点。

内部节点（Inner）：如果该节点既不是叶子节点也不是根节点。

编写一个查询来输出节点 id 和节点类型。按节点 id 排序。上述示例的结果应为：

+----+------+
| id | Type |
+----+------+
| 1  | Root |
| 2  | Inner|
| 3  | Leaf |
| 4  | Leaf |
| 5  | Leaf |
+----+------+

解释：

节点 '1' 是根节点，因为它的父节点为 NULL，且有子节点 '2' 和 '3'。

节点 '2' 是内部节点，因为它有父节点 '1'，且有子节点 '4' 和 '5'。

节点 '3'、'4' 和 '5' 是叶子节点，因为它们有父节点但没有子节点。

下面是示例树的图示：

			  1
			/   \
		   2     3
		  / \
		 4   5

注意：

如果树上只有一个节点，你只需要输出它的根属性。
"""

from typing import List, Optional


class Solution:
    """
    SQL Solution:

    SELECT
        id,
        CASE
            WHEN p_id IS NULL THEN 'Root'
            WHEN id IN (SELECT DISTINCT p_id FROM tree WHERE p_id IS NOT NULL) THEN 'Inner'
            ELSE 'Leaf'
        END AS Type
    FROM tree
    ORDER BY id;
    """
    pass



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用 CASE WHEN 判断每个节点的类型：
# - 如果 p_id IS NULL，则为根节点（Root）。
# - 如果 id 出现在 p_id 列中（即有人以该节点为父亲），则为内部节点（Inner）。
# - 否则为叶子节点（Leaf）。
# 然后按 id 升序排序即可。
#
# 时间复杂度: O(n log n) - n 为 tree 表的行数
# 空间复杂度: O(n) - 子查询存储中间结果
#
# 关键点:
# - 根节点的识别：p_id IS NULL
# - 内部节点的识别：id 在 p_id 列表中出现过
# - 使用子查询 SELECT DISTINCT p_id 来快速判断
# - 注意处理单节点的情况（既是根节点又是叶子节点，但按题目要求输出 Root）
