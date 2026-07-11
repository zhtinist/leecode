"""
LeetCode #973 - K Closest Points to Origin
中文题名：最接近原点的 K 个点
https://leetcode.com/problems/k-closest-points-to-origin/

我们有一个由平面上的点组成的列表 points。需要从中找出 K 个距离原点 (0, 0) 最近的点。

（这里，平面上两点之间的距离是欧几里德距离。）

你可以按任何顺序返回答案。除了点坐标的顺序之外，答案确保是唯一的。

示例 1：

输入：points = [[1,3],[-2,2]], K = 1
输出：[[-2,2]]
解释：
(1, 3) 和原点之间的距离为 sqrt(10)。
(-2, 2) 和原点之间的距离为 sqrt(8)。
由于 sqrt(8) < sqrt(10)，(-2, 2) 离原点更近。
我们只需要距离原点最近的 K = 1 个点，所以答案是 [[-2,2]]。

示例 2：

输入：points = [[3,3],[5,-1],[-2,4]], K = 2
输出：[[3,3],[-2,4]]
（答案 [[-2,4],[3,3]] 也会被接受。）

注意：

1 <= K <= points.length <= 10000
-10000 < points[i][0] < 10000
-10000 < points[i][1] < 10000

【中文翻译】
给定平面上的点列表，找出距离原点 (0,0) 最近的 K 个点。距离使用欧几里德距离。可以按任意顺序返回结果。

"""

from typing import List, Optional
import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Use a max-heap of size k, storing (-distance, x, y)
        # We keep the k closest points by pushing negative distances
        heap = []
        for x, y in points:
            dist = x * x + y * y  # no need for sqrt, comparison is same
            heapq.heappush(heap, (-dist, x, y))
            if len(heap) > k:
                heapq.heappop(heap)  # remove the farthest point
        return [[x, y] for _, x, y in heap]



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用最大堆（max-heap）维护 K 个最近的点的"门槛"：
# 1. 遍历所有点，计算每个点到原点的欧几里德距离的平方（x^2 + y^2）。
#    - 不需要开平方根，因为比较大小关系一致，节省计算量。
# 2. 将 (-距离的平方, x, y) 入最大堆（Python heapq 是最小堆，用负数模拟最大堆）。
# 3. 如果堆的大小超过 K，弹出堆顶元素（即当前堆中最远的点）。
# 4. 遍历结束后，堆中剩余的就是距离最近的 K 个点。
# 5. 返回堆中所有点的坐标。
#
# 时间复杂度: O(N log K)，遍历 N 个点，每次堆操作 O(log K)
# 空间复杂度: O(K)，堆中最多存储 K 个元素
#
# 关键点:
# - 使用最大堆维护"门槛"：堆顶始终是当前 K 个点中最远的那个
# - 不需要开平方根，x^2 + y^2 即可进行比较
# - Python heapq 是最小堆，用负数距离模拟最大堆
# - 也可以使用快速选择（QuickSelect）算法达到平均 O(N) 时间
