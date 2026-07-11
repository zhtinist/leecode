"""
LeetCode #1202 - Smallest String With Swaps
中文题名：交换字符串中的元素
https://leetcode.com/problems/smallest-string-with-swaps/

You are given a string `s`, and an array of pairs of indices in the
string `pairs` where `pairs[i] = [a, b]` indicates
2 indices(0-indexed) of the string.

You can swap the characters at any pair of indices in the given `pairs` any
number of times.

Return the lexicographically smallest string that `s` can be changed to
after using the swaps.

Example 1:

Input: s = "dcab", pairs = [[0,3],[1,2]]
Output: "bacd"
Explaination:
Swap s[0] and s[3], s = "bcad"
Swap s[1] and s[2], s = "bacd"

Example 2:

Input: s = "dcab", pairs = [[0,3],[1,2],[0,2]]
Output: "abcd"
Explaination:
Swap s[0] and s[3], s = "bcad"
Swap s[0] and s[2], s = "acbd"
Swap s[1] and s[2], s = "abcd"

Example 3:

Input: s = "cba", pairs = [[0,1],[1,2]]
Output: "abc"
Explaination:
Swap s[0] and s[1], s = "bca"
Swap s[1] and s[2], s = "bac"
Swap s[0] and s[1], s = "abc"

Constraints:

`1 <= s.length <= 10^5`

`0 <= pairs.length <= 10^5`

`0 <= pairs[i][0], pairs[i][1] < s.length`

`s` only contains lower case English letters.

【中文翻译】
给你一个字符串 s，以及该字符串中的一些索引对数组 pairs，其中 pairs[i] = [a, b] 表示字符串中的两个索引（从 0 开始）。

你可以交换任意索引对中的字符，交换次数不限。

返回经过若干次交换后，s 可以变成的按字典序最小的字符串。

示例 1：

输入：s = "dcab", pairs = [[0,3],[1,2]]
输出："bacd"
解释：
交换 s[0] 和 s[3]，s = "bcad"
交换 s[1] 和 s[2]，s = "bacd"

示例 2：

输入：s = "dcab", pairs = [[0,3],[1,2],[0,2]]
输出："abcd"
解释：
交换 s[0] 和 s[3]，s = "bcad"
交换 s[0] 和 s[2]，s = "acbd"
交换 s[1] 和 s[2]，s = "abcd"

示例 3：

输入：s = "cba", pairs = [[0,1],[1,2]]
输出："abc"
解释：
交换 s[0] 和 s[1]，s = "bca"
交换 s[1] 和 s[2]，s = "bac"
交换 s[0] 和 s[1]，s = "abc"

约束条件：

1 <= s.length <= 10^5
0 <= pairs.length <= 10^5
0 <= pairs[i][0], pairs[i][1] < s.length
s 只包含小写英文字母。

"""

from typing import List, Optional


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        parent = list(range(n))

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x: int, y: int) -> None:
            px, py = find(x), find(y)
            if px != py:
                parent[px] = py

        for a, b in pairs:
            union(a, b)

        from collections import defaultdict
        groups = defaultdict(list)
        for i in range(n):
            groups[find(i)].append(i)

        res = list(s)
        for indices in groups.values():
            chars = sorted(res[i] for i in indices)
            for idx, ch in zip(sorted(indices), chars):
                res[idx] = ch

        return ''.join(res)










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用并查集(Union-Find)将可交换的索引分组。
# 关键洞察：如果索引 a 和 b 可以交换，b 和 c 可以交换，则 a、b、c 形成一个连通分量，
# 通过多次交换可以实现连通分量内任意排列。因此每个连通分量内的字符可以排成字典序最小。
#
# 具体步骤：
# 1. 使用并查集将 pairs 中的索引对合并到同一连通分量。
# 2. 收集每个连通分量中的所有索引及其对应的字符。
# 3. 对每个连通分量：将对应的字符排序，按索引升序放回，得到该分量内的最小字典序排列。
# 4. 拼接所有字符得到最终字符串。
#
# 时间复杂度: O(n * α(n) + n log n) ≈ O(n log n)
#   - 并查集操作近似 O(n * α(n))（近乎常数）
#   - 对每个连通分量的字符排序，总排序代价 O(n log n)（每个字符最多参与一次排序）
# 空间复杂度: O(n) - 存储 parent 数组和 groups 字典
#
# 关键点:
# - 并查集的核心作用：识别"交换可达"的连通分量
# - 路径压缩（parent[x] = parent[parent[x]]）提升查找效率
# - 每个连通分量内的字符排序后按索引放回，保证局部字典序最小等效于全局最小
# - 使用 defaultdict(list) 高效收集分组信息
