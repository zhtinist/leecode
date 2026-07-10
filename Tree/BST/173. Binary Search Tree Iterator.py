"""
LeetCode #173 - Binary Search Tree Iterator
https://leetcode.com/problems/binary-search-tree-iterator/

Implement the BSTIterator class that represents an iterator over the in-order
traversal of a binary search tree (BST):
- BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The
  root of the BST is given as part of the constructor.
- boolean hasNext() Returns true if there exists a number in the traversal to
  the right of the pointer, otherwise returns false.
- int next() Moves the pointer to the right, then returns the number at the
  pointer.

Notice that by initializing the pointer to a nonexistent smallest number, the
first call to next() will return the smallest element in the BST.

You may assume that next() calls will always be valid. That is, there will be
at least a next number in the in-order traversal when next() is called.

Example 1:
    Input: ["BSTIterator","next","next","hasNext","next","hasNext","next",
            "hasNext","next","hasNext"]
           [[[7,3,15,null,null,9,20]],[],[],[],[],[],[],[],[],[]]
    Output: [null,3,7,true,9,true,15,true,20,false]

Constraints:
    The number of nodes in the tree is in the range [1, 10^5].
    0 <= Node.val <= 10^6
    At most 10^5 calls will be made to hasNext and next.
"""

from typing import Optional


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self._push_left(root)

    def _push_left(self, node: Optional[TreeNode]) -> None:
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        node = self.stack.pop()
        self._push_left(node.right)
        return node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0
