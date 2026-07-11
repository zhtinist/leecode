"""
LeetCode #1261 - Find Elements in a Contaminated Binary Tree
中文题名：在受污染的二叉树中查找元素
https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/

Given a binary tree with the following rules:

`root.val == 0`

If `treeNode.val == x` and `treeNode.left != null`, then
`treeNode.left.val == 2 * x + 1`

If `treeNode.val == x` and `treeNode.right != null`, then
`treeNode.right.val == 2 * x + 2`

Now the binary tree is contaminated, which means all `treeNode.val` have been
changed to `-1`.

You need to first recover the binary tree and then implement the
`FindElements` class:

`FindElements(TreeNode* root)` Initializes the object with a contamined
binary tree, you need to recover it first.

`bool find(int target)` Return if the `target` value
exists in the recovered binary tree.

Example 1:

Input
["FindElements","find","find"]
[[[-1,null,-1]],[1],[2]]
Output
[null,false,true]
Explanation
FindElements findElements = new FindElements([-1,null,-1]);
findElements.find(1); // return False
findElements.find(2); // return True

Example 2:

Input
["FindElements","find","find","find"]
[[[-1,-1,-1,-1,-1]],[1],[3],[5]]
Output
[null,true,true,false]
Explanation
FindElements findElements = new FindElements([-1,-1,-1,-1,-1]);
findElements.find(1); // return True
findElements.find(3); // return True
findElements.find(5); // return False

Example 3:

Input
["FindElements","find","find","find","find"]
[[[-1,null,-1,-1,null,-1]],[2],[3],[4],[5]]
Output
[null,true,false,false,true]
Explanation
FindElements findElements = new FindElements([-1,null,-1,-1,null,-1]);
findElements.find(2); // return True
findElements.find(3); // return False
findElements.find(4); // return False
findElements.find(5); // return True

Constraints:

`TreeNode.val == -1`

The height of the binary tree is less than or equal to `20`

The total number of nodes is between `[1, 10^4]`

Total calls of `find()` is between `[1, 10^4]`

`0 <= target <= 10^6`

【中文翻译】
给出一个满足以下规则的二叉树：

- `root.val == 0`
- 如果 `treeNode.val == x` 且 `treeNode.left != null`，那么 `treeNode.left.val == 2 * x + 1`
- 如果 `treeNode.val == x` 且 `treeNode.right != null`，那么 `treeNode.right.val == 2 * x + 2`

现在这个二叉树受到「污染」，所有的 `treeNode.val` 都变成了 `-1`。

请先还原二叉树，然后实现 `FindElements` 类：

- `FindElements(TreeNode* root)` 用受污染的二叉树初始化对象，你需要先把它还原。
- `bool find(int target)` 判断目标值 `target` 是否存在于还原后的二叉树中。

示例 1：

输入
["FindElements","find","find"]
[[[-1,null,-1]],[1],[2]]
输出
[null,false,true]
解释
FindElements findElements = new FindElements([-1,null,-1]);
findElements.find(1); // 返回 False
findElements.find(2); // 返回 True

示例 2：

输入
["FindElements","find","find","find"]
[[[-1,-1,-1,-1,-1]],[1],[3],[5]]
输出
[null,true,true,false]
解释
FindElements findElements = new FindElements([-1,-1,-1,-1,-1]);
findElements.find(1); // 返回 True
findElements.find(3); // 返回 True
findElements.find(5); // 返回 False

示例 3：

输入
["FindElements","find","find","find","find"]
[[[-1,null,-1,-1,null,-1]],[2],[3],[4],[5]]
输出
[null,true,false,false,true]
解释
FindElements findElements = new FindElements([-1,null,-1,-1,null,-1]);
findElements.find(2); // 返回 True
findElements.find(3); // 返回 False
findElements.find(4); // 返回 False
findElements.find(5); // 返回 True

约束条件：

`TreeNode.val == -1`

二叉树的高度小于或等于 `20`

节点的总数在 `[1, 10^4]` 之间

`find()` 的总调用次数在 `[1, 10^4]` 之间

`0 <= target <= 10^6`
"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        self.values = set()
        if root:
            root.val = 0
            self._recover(root)

    def _recover(self, node: TreeNode):
        self.values.add(node.val)
        if node.left:
            node.left.val = 2 * node.val + 1
            self._recover(node.left)
        if node.right:
            node.right.val = 2 * node.val + 2
            self._recover(node.right)

    def find(self, target: int) -> bool:
        return target in self.values










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# DFS 恢复树 + 哈希集合查找。
# 1. 构造函数中，将根节点的值设为 0，然后从根开始 DFS 遍历整棵树。
# 2. 对于每个节点：
#    - 将当前节点的值存入哈希集合 `self.values` 中。
#    - 如果存在左子节点，根据规则 `left.val = 2 * node.val + 1` 恢复其值，然后递归处理左子树。
#    - 如果存在右子节点，根据规则 `right.val = 2 * node.val + 2` 恢复其值，然后递归处理右子树。
# 3. `find(target)` 只需 O(1) 时间在哈希集合中查找 target 是否存在。
# 另一种方法：不需要恢复整棵树。给定 target，可以反向推导其父节点路径，
# 检查该路径在树中是否存在。公式：父节点值 = (target - 1) // 2（验证奇偶性决定左右方向）。
#
# 时间复杂度: 初始化 O(N)，find O(1)，其中 N 是节点数
# 空间复杂度: O(N)，哈希集合存储所有节点的值
#
# 关键点:
# - 恢复规则：left = 2*val+1，right = 2*val+2
# - 用集合存储所有值使 find 达到 O(1)
# - 也可以用数学方法逆推：从 target 反推到根路径，在原树上验证路径是否存在
# - 逆推方法空间 O(1) 但 find 为 O(h)，这里 N <= 10^4，O(N) 空间完全可行
