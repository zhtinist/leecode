"""
LeetCode #1130 - Minimum Cost Tree From Leaf Values
中文题名：叶值的最小代价生成树
https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/

Given an array `arr` of positive integers, consider all binary trees such that:

Each node has either 0 or 2 children;

The values of `arr` correspond to the values of
each leaf in an in-order traversal of the tree.  (Recall
that a node is a leaf if and only if it has 0 children.)

The value of each non-leaf node is equal to the product of the largest leaf value
in its left and right subtree respectively.

Among all possible binary trees considered, return the smallest possible sum of the
values of each non-leaf node.  It is guaranteed this sum fits into a 32-bit
integer.

Example 1:

Input: arr = [6,2,4]
Output: 32
Explanation:
There are two possible trees.  The first has non-leaf node sum 36, and the second has non-leaf node sum 32.

    24            24
   / \\          / \\
  12   4        6    8
 / \\               / \\
6    2             2   4

Constraints:

`2 <= arr.length <= 40`

`1 <= arr[i] <= 15`

It is guaranteed that the answer fits into a 32-bit signed integer (ie. it is less
than `2^31`).

【中文翻译】
给定一个正整数数组 arr，考虑所有满足以下条件的二叉树：

每个节点要么有 0 个孩子要么有 2 个孩子；

数组 arr 中的值与树的中序遍历中每个叶节点的值一一对应。（回忆一下，如果一个节点有 0 个子节点，那么该节点是叶节点。）

每个非叶节点的值等于其左子树和右子树中各自最大叶节点值的乘积。

在所有可能的二叉树中，返回所有非叶节点值之和的最小可能值。保证这个和在一个 32 位整数范围内。

示例 1：

输入：arr = [6,2,4]
输出：32
解释：
有两种可能的树。第一种的非叶节点值之和为 36，第二种的非叶节点值之和为 32。

    24            24
   / \\          / \\
  12   4        6    8
 / \\               / \\
6    2             2   4

约束条件：

`2 <= arr.length <= 40`

`1 <= arr[i] <= 15`

保证答案适合 32 位有符号整数（即小于 2^31）。
"""

from typing import List, Optional


class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        stack = []
        result = 0
        for num in arr:
            while stack and stack[-1] <= num:
                mid = stack.pop()
                if stack:
                    result += mid * min(stack[-1], num)
                else:
                    result += mid * num
            stack.append(num)

        while len(stack) > 1:
            result += stack.pop() * stack[-1]

        return result










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用单调递减栈（Monotonic Stack）。问题等价于：每次合并两个相邻的元素，代价为两个元素中
# 较大的那个（因为较大的会成为父节点值的一部分），合并后保留较大的元素。
# 我们需要最小化总代价。
# 1. 维护一个单调递减栈。
# 2. 遍历 arr 中的每个元素 num：
#    - 当栈不为空且栈顶 <= num 时，弹出栈顶元素 mid。
#      mid 是一个"谷底"值，它需要与左右邻居中较小的那个相乘并计入结果。
#      如果栈不为空，说明 mid 左边有更大的值 stack[-1]，
#      代价 = mid * min(stack[-1], num)。
#      如果栈为空，代价 = mid * num。
#    - 将 num 入栈。
# 3. 遍历结束后，栈中剩余的元素从大到小。依次弹出，代价 = 弹出值 * 新的栈顶。
# 4. 返回累计的 result。
#
# 时间复杂度: O(n) - 每个元素入栈出栈各一次
# 空间复杂度: O(n) - 栈的空间
#
# 关键点:
# - 贪心思想：最小的叶节点应该尽早合并（与较小的邻居相乘）
# - 单调栈帮助找到每个"谷底"值及其左右邻居
# - 本题也可用区间 DP 解决，O(n^3)，单调栈解法更优
