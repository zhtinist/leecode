"""
LeetCode #2271 - Maximum White Tiles Covered by a Carpet
毯子覆盖的最多白色砖块数
https://leetcode.cn/problems/maximum-white-tiles-covered-by-a-carpet/

给你一个二维整数数组 `tiles` ，其中 `tiles[i] = [l_i, r_i]` ，表示所有在 `l_i <= j <= r_i` 之间的每个瓷砖位置 `j` 都被涂成了白色。
同时给你一个整数 `carpetLen` ，表示可以放在 任何位置 的一块毯子的长度。
请你返回使用这块毯子，最多 可以盖住多少块白色瓷砖。

示例 1：

输入：tiles = [[1,5],[10,11],[12,18],[20,25],[30,32]], carpetLen = 10 输出：9 解释：将毯子从瓷砖 10 开始放置。 总共覆盖 9 块瓷砖，所以返回 9 。 注意可能有其他方案也可以覆盖 9 块瓷砖。 可以看出，瓷砖无法覆盖超过 9 块瓷砖。
示例 2：

输入：tiles = [[10,11],[1,1]], carpetLen = 2 输出：2 解释：将毯子从瓷砖 10 开始放置。 总共覆盖 2 块瓷砖，所以我们返回 2 。

提示：
`1 <= tiles.length <= 5 * 10^4`
`tiles[i].length == 2`
`1 <= l_i <= r_i <= 10^9`
`1 <= carpetLen <= 10^9`
`tiles` 互相 不会重叠 。
"""

from typing import List, Optional
import bisect


class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        """
        Find the maximum number of white tiles that can be covered by a carpet
        of given length placed anywhere.
        """
        tiles.sort(key=lambda x: x[0])
        n = len(tiles)

        # prefix[i] = total tiles covered from tiles[0] to tiles[i-1] (inclusive)
        prefix = [0] * (n + 1)
        starts = [0] * n
        for i, (l, r) in enumerate(tiles):
            prefix[i + 1] = prefix[i] + (r - l + 1)
            starts[i] = l

        ans = 0
        for i, (l, r) in enumerate(tiles):
            # carpet starts at tile[i].l
            carpet_end = l + carpetLen - 1
            # find the rightmost tile whose start <= carpet_end
            j = bisect.bisect_right(starts, carpet_end) - 1

            # total tiles from i to j (fully covered tiles)
            covered = prefix[j + 1] - prefix[i]
            # partial coverage of the tile at j+1 if carpet extends into it
            if j + 1 < n:
                covered += max(0, carpet_end - tiles[j + 1][0] + 1)

            ans = max(ans, covered)

        return ans


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Array, Binary Search, Prefix Sum, Sorting, Sliding Window
#
# 解题思路:
# 最优情况下，毯子的左边界应该与某个瓷砖区间的左边界对齐（可以通过反证法证明：
# 如果不对齐，向右微调使左边界对齐而不减少覆盖）。因此，枚举每个瓷砖区间的左边界
# 作为毯子的起始位置，毯子覆盖范围是 [l, l+carpetLen-1]。使用前缀和数组快速
# 计算覆盖的瓷砖数：二分查找毯子右边界覆盖到了哪个瓷砖区间，被完全包含的区间
# 用前缀和计算，部分覆盖的最后一个区间单独加上。取所有起始位置的最大值。
#
# 时间复杂度: O(N log N)，N 为 tiles 长度。排序 O(N log N)，对每个区间
# 二分查找 O(log N)，总 O(N log N)。
# 空间复杂度: O(N)，用于存储前缀和数组和起始位置数组。
#
# 关键点:
# - 最优起始位置一定是某个瓷砖区间的左边界
# - 使用 bisect_right 找毯子覆盖的最右区间（完全或部分覆盖）
# - 前缀和快速计算完全覆盖区间的总瓷砖数
# - 注意部分覆盖的区间：即使毯子右边界小于该区间的左边界，覆盖数为 0
# - 地毯长度可能跨越多个不连续的瓷砖区间，但只覆盖白色瓷砖
