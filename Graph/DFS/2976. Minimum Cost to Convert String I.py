"""
LeetCode #2976 - Minimum Cost to Convert String I
转换字符串的最小成本 I
https://leetcode.cn/problems/minimum-cost-to-convert-string-i/

给你两个下标从 0 开始的字符串 `source` 和 `target` ，它们的长度均为 `n` 并且由 小写 英文字母组成。
另给你两个下标从 0 开始的字符数组 `original` 和 `changed` ，以及一个整数数组 `cost` ，其中 `cost[i]` 代表将字符 `original[i]` 更改为字符 `changed[i]` 的成本。
你从字符串 `source` 开始。在一次操作中，如果 存在 任意 下标 `j` 满足 `cost[j] == z`  、`original[j] == x` 以及 `changed[j] == y` 。你就可以选择字符串中的一个字符 `x` 并以 `z` 的成本将其更改为字符 `y` 。
返回将字符串 `source` 转换为字符串 `target` 所需的 最小 成本。如果不可能完成转换，则返回 `-1` 。
注意，可能存在下标 `i` 、`j` 使得 `original[j] == original[i]` 且 `changed[j] == changed[i]` 。

示例 1：
输入：source = "abcd", target = "acbe", original = ["a","b","c","c","e","d"], changed = ["b","c","b","e","b","e"], cost = [2,5,5,1,2,20] 输出：28 解释：将字符串 "abcd" 转换为字符串 "acbe" ： - 更改下标 1 处的值 'b' 为 'c' ，成本为 5 。 - 更改下标 2 处的值 'c' 为 'e' ，成本为 1 。 - 更改下标 2 处的值 'e' 为 'b' ，成本为 2 。 - 更改下标 3 处的值 'd' 为 'e' ，成本为 20 。 产生的总成本是 5 + 1 + 2 + 20 = 28 。 可以证明这是可能的最小成本。
示例 2：
输入：source = "aaaa", target = "bbbb", original = ["a","c"], changed = ["c","b"], cost = [1,2] 输出：12 解释：要将字符 'a' 更改为 'b'： - 将字符 'a' 更改为 'c'，成本为 1  - 将字符 'c' 更改为 'b'，成本为 2  产生的总成本是 1 + 2 = 3。 将所有 'a' 更改为 'b'，产生的总成本是 3 * 4 = 12 。
示例 3：
输入：source = "abcd", target = "abce", original = ["a"], changed = ["e"], cost = [10000] 输出：-1 解释：无法将 source 字符串转换为 target 字符串，因为下标 3 处的值无法从 'd' 更改为 'e' 。

提示：
`1 <= source.length == target.length <= 10^5`
`source`、`target` 均由小写英文字母组成
`1 <= cost.length== original.length == changed.length <= 2000`
`original[i]`、`changed[i]` 是小写英文字母
`1 <= cost[i] <= 10^6`
`original[i] != changed[i]`
"""

from typing import List, Optional


class Solution:
    def minimumCost(
        self,
        source: str,
        target: str,
        original: List[str],
        changed: List[str],
        cost: List[int],
    ) -> int:
        """
        Floyd-Warshall all-pairs shortest path on 26 lowercase letters.
        Then sum the min cost to convert each source[i] to target[i].
        """
        INF = float('inf')
        # Distance matrix for 26 letters
        dist = [[INF] * 26 for _ in range(26)]
        for i in range(26):
            dist[i][i] = 0

        for o, c, w in zip(original, changed, cost):
            u = ord(o) - ord('a')
            v = ord(c) - ord('a')
            dist[u][v] = min(dist[u][v], w)

        # Floyd-Warshall
        for k in range(26):
            for i in range(26):
                if dist[i][k] == INF:
                    continue
                for j in range(26):
                    if dist[k][j] == INF:
                        continue
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        total = 0
        for s, t in zip(source, target):
            u = ord(s) - ord('a')
            v = ord(t) - ord('a')
            if dist[u][v] == INF:
                return -1
            total += dist[u][v]

        return total



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Graph, Array, String, Shortest Path
#
# 解题思路:
# 将 26 个小写字母视为图的节点，original[i] -> changed[i] 的转换成本为 cost[i]。
# 使用 Floyd-Warshall 算法计算所有字母对之间的最短转换成本（传递闭包）。
# 然后遍历 source 和 target，累加每个位置字符转换的最小成本，若不可达返回 -1。
#
# 时间复杂度: O(26^3 + N)，其中 N = source 长度，26^3 为 Floyd-Warshall 常数开销
# 空间复杂度: O(26^2) = O(1)，存储 26×26 的距离矩阵
#
# 关键点:
# - 字符转换具有传递性：a->b 和 b->c 意味着可以通过两次操作实现 a->c
# - Floyd-Warshall 全源最短路径适合 26 个节点的小规模图
# - 注意处理重复边（取最小成本）
