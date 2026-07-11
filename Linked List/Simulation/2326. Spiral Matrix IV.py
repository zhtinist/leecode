"""
LeetCode #2326 - Spiral Matrix IV
螺旋矩阵 IV
https://leetcode.cn/problems/spiral-matrix-iv/

给你两个整数：`m` 和 `n` ，表示矩阵的维数。
另给你一个整数链表的头节点 `head` 。
请你生成一个大小为 `m x n` 的螺旋矩阵，矩阵包含链表中的所有整数。链表中的整数从矩阵 左上角 开始、顺时针 按 螺旋 顺序填充。如果还存在剩余的空格，则用 `-1` 填充。
返回生成的矩阵。

示例 1：
输入：m = 3, n = 5, head = [3,0,2,6,8,1,7,9,4,2,5,5,0] 输出：[[3,0,2,6,8],[5,0,-1,-1,1],[5,2,4,9,7]] 解释：上图展示了链表中的整数在矩阵中是如何排布的。 注意，矩阵中剩下的空格用 -1 填充。
示例 2：
输入：m = 1, n = 4, head = [0,1,2] 输出：[[0,1,2,-1]] 解释：上图展示了链表中的整数在矩阵中是如何从左到右排布的。  注意，矩阵中剩下的空格用 -1 填充。

提示：
`1 <= m, n <= 10^5`
`1 <= m * n <= 10^5`
链表中节点数目在范围 `[1, m * n]` 内
`0 <= Node.val <= 1000`
"""

from typing import List, Optional


class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional['ListNode']) -> List[List[int]]:
        # 初始化矩阵，全部填充 -1
        matrix = [[-1] * n for _ in range(m)]

        top, bottom = 0, m - 1
        left, right = 0, n - 1

        curr = head
        while curr:
            # 从左到右填充顶部行
            for col in range(left, right + 1):
                if not curr:
                    break
                matrix[top][col] = curr.val
                curr = curr.next
            top += 1
            if top > bottom or not curr:
                break

            # 从上到下填充右侧列
            for row in range(top, bottom + 1):
                if not curr:
                    break
                matrix[row][right] = curr.val
                curr = curr.next
            right -= 1
            if left > right or not curr:
                break

            # 从右到左填充底部行
            for col in range(right, left - 1, -1):
                if not curr:
                    break
                matrix[bottom][col] = curr.val
                curr = curr.next
            bottom -= 1
            if top > bottom or not curr:
                break

            # 从下到上填充左侧列
            for row in range(bottom, top - 1, -1):
                if not curr:
                    break
                matrix[row][left] = curr.val
                curr = curr.next
            left += 1

        return matrix


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Linked List, Matrix, Simulation
#
# 解题思路:
# 这是经典的螺旋矩阵填充问题。矩阵初始全部填充 -1，然后按顺时针螺旋顺序
# 依次将链表节点值填入矩阵：
#   1. 从左到右填充 top 行，top 下移
#   2. 从上到下填充 right 列，right 左移
#   3. 从右到左填充 bottom 行，bottom 上移
#   4. 从下到上填充 left 列，left 右移
# 每完成一个方向后检查边界是否越界或链表是否已遍历完，如果是则提前退出。
# 链表遍历完后，剩余位置自动保持初始值 -1，无需额外处理。
#
# 时间复杂度: O(m×n)，每个矩阵单元格最多被访问一次。链表遍历也是 O(L)，
#            其中 L ≤ m×n 是链表长度。总体 O(m×n)。
# 空间复杂度: O(1)，除输出矩阵外只使用常数级额外变量。
#            （输出矩阵不计入空间复杂度分析）
#
# 关键点:
# - 先初始化为 -1，之后链表节点值会覆盖对应位置，剩余位置自然保留 -1。
# - 四个边界变量 (top, bottom, left, right) 控制螺旋范围，每次完成一行/列后收缩。
# - 每步都检查链表节点是否用完，用完立即终止避免空指针访问。
