"""
LeetCode #1105 - Filling Bookcase Shelves
中文题名：填充书架
https://leetcode.com/problems/filling-bookcase-shelves/

We have a sequence of `books`: the `i`-th book has thickness `books[i][0]`
and height `books[i][1]`.

We want to place these books in order onto bookcase shelves that have
total width `shelf_width`.

We choose some of the books to place on this shelf (such that the sum of their thickness
is `<= shelf_width`), then build another level of shelf of the bookcase so
that the total height of the bookcase has increased by the maximum height of the books we
just put down.  We repeat this process until there are no more books to place.

Note again that at each step of the above process, the order of the books we place is
the same order as the given sequence of books.  For example, if we have an ordered
list of 5 books, we might place the first and second book onto the first shelf, the
third book on the second shelf, and the fourth and fifth book on the last shelf.

Return the minimum possible height that the total bookshelf can be after placing shelves in
this manner.

Example 1:

Input: books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], shelf_width = 4
Output: 6
Explanation:
The sum of the heights of the 3 shelves are 1 + 3 + 2 = 6.
Notice that book number 2 does not have to be on the first shelf.

Constraints:

`1 <= books.length <= 1000`

`1 <= books[i][0] <= shelf_width <= 1000`

`1 <= books[i][1] <= 1000`

【中文翻译】
我们有一系列书 books：第 i 本书的厚度为 books[i][0]，高度为 books[i][1]。

我们想按顺序将这些书放到总宽度为 shelf_width 的书架上。

我们从这些书中选择一些放到当前层书架上（使得它们的厚度之和 <= shelf_width），然后构建下一层书架，此时书架的总高度增加了刚才放置的书中最大高度值。我们重复这个过程直到没有更多的书需要放置。

再次注意，在上述过程的每一步中，我们放置的书的顺序与给定的书的序列顺序相同。例如，如果我们有一个包含 5 本书的有序列表，我们可能把第一本和第二本书放在第一层，第三本书放在第二层，第四和第五本书放在最后一层。

返回按照这种方式放置后，整个书架可能达到的最小总高度。

示例 1：

输入：books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], shelf_width = 4
输出：6
解释：
3 层书架的高度之和为 1 + 3 + 2 = 6。
注意第二本书不必放在第一层书架上。

约束条件：

`1 <= books.length <= 1000`

`1 <= books[i][0] <= shelf_width <= 1000`

`1 <= books[i][1] <= 1000`
"""

from typing import List, Optional


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        n = len(books)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            width = 0
            height = 0
            for j in range(i - 1, -1, -1):
                width += books[j][0]
                if width > shelf_width:
                    break
                height = max(height, books[j][1])
                dp[i] = min(dp[i], dp[j] + height)

        return dp[n]










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用动态规划。定义 dp[i] 为放置前 i 本书（编号 0..i-1）所需的最小总高度。
# 初始条件：dp[0] = 0（没有书时高度为0）。
# 状态转移：对于每个 i，考虑将第 j 到第 i-1 本书放在同一层。
#   从 j = i-1 向前遍历，累加厚度 width 并记录最大高度 height。
#   若累计厚度超过 shelf_width 则停止，否则 dp[i] = min(dp[i], dp[j] + height)。
# 最终答案：dp[n]。
#
# 时间复杂度: O(n^2) - n 为书的数量，内层循环最多遍历 n 次
# 空间复杂度: O(n) - dp 数组大小为 n+1
#
# 关键点:
# - dp[i] 表示放置前 i 本书的最小高度，dp[0] = 0
# - 新的一层可以从任意位置 j < i 开始划分，包含 books[j..i-1]
