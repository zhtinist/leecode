"""
LeetCode #835 - Image Overlap
中文题名：图像重叠
https://leetcode.com/problems/image-overlap/

Two images `A` and `B` are given, represented as binary, square
matrices of the same size.  (A binary matrix has only 0s and 1s as values.)

We translate one image however we choose (sliding it left, right, up, or down any number of
units), and place it on top of the other image.  After, the overlap of this
translation is the number of positions that have a 1 in both images.

(Note also that a translation does not include any kind of rotation.)

What is the largest possible overlap?

Example 1:

Input: A = [[1,1,0],
[0,1,0],
[0,1,0]]
B = [[0,0,0],
[0,1,1],
[0,0,1]]
Output: 3
Explanation: We slide A to right by 1 unit and down by 1 unit.

Notes:

`1 <= A.length = A[0].length = B.length = B[0].length <= 30`

`0 <= A[i][j], B[i][j] <= 1`

【中文翻译】
给出两个图像 `A` 和 `B`，它们都是二值的、大小相同的方形矩阵。（二值矩阵中只有 0 和 1 作为值。）

我们可以以任意方式平移其中一个图像（向左、向右、向上或向下滑动任意单位），然后将其放在另一个图像的上面。然后，该平移的重叠数是两个图像中都是 1 的位置数。

（注意，平移不包括任何形式的旋转。）

最大可能的重叠数是多少？

示例 1：

输入：A = [[1,1,0],
           [0,1,0],
           [0,1,0]]
     B = [[0,0,0],
           [0,1,1],
           [0,0,1]]
输出：3
解释：我们将 A 向右移动 1 个单位，向下移动 1 个单位。

注意：

`1 <= A.length = A[0].length = B.length = B[0].length <= 30`

`0 <= A[i][j], B[i][j] <= 1`

"""

from typing import List, Optional


class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)

        # Collect coordinates of all 1's in both images
        ones1 = [(r, c) for r in range(n) for c in range(n) if img1[r][c] == 1]
        ones2 = [(r, c) for r in range(n) for c in range(n) if img2[r][c] == 1]

        # Count frequency of each translation vector (dr, dc)
        from collections import Counter
        vectors = Counter()
        for r1, c1 in ones1:
            for r2, c2 in ones2:
                # Translation vector that maps (r2,c2) in img2 to (r1,c1) in img1
                vectors[(r1 - r2, c1 - c2)] += 1

        # The most frequent vector gives max overlap
        return max(vectors.values()) if vectors else 0



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 向量计数法。
# 将两幅图中所有值为 1 的坐标分别收集到两个列表。
# 对于 img2 中的每个 1 (r2, c2) 和 img1 中的每个 1 (r1, c1)，
# 平移向量 (dr, dc) = (r1 - r2, c1 - c2) 表示将 img2 中的 (r2, c2)
# 平移到 img1 中的 (r1, c1) 所需的位移。
# 统计每个平移向量出现的次数，出现次数最多的向量对应的就是最大重叠。
# 因为：对于同一个平移向量 (dr, dc)，每个匹配的 (r1, r2, c1, c2) 对
# 就代表平移后 img2 的一个 1 落在 img1 的一个 1 上。
#
# 时间复杂度: O(N^4) 最坏 — N <= 30，最多 900 个 1，900^2 = 810,000 对
# 空间复杂度: O(K1 * K2) — 存储不同平移向量的计数
#
# 关键点:
# - 核心洞察：重叠数量 = 相同平移向量匹配的数量
# - 通过统计向量频率来找到最佳平移，而不是枚举所有平移位置
# - 不需要考虑平移后的边界，因为只要两个 1 对齐即可
# - 若没有 1，返回 0（max(vectors.values()) 会处理空的情况）
