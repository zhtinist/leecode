"""
LeetCode #990 - Satisfiability of Equality Equations
中文题名：等式方程的可满足性
https://leetcode.com/problems/satisfiability-of-equality-equations/

给定一个由表示变量之间关系的字符串方程组成的数组，每个字符串 equations[i] 的长度为 4，并采用两种不同的形式之一："a==b" 或 "a!=b"。在这里，a 和 b 是小写字母（不一定不同），表示单字母变量名。

只有当可以将整数分配给变量名，以便满足所有给定的方程时才返回 true，否则返回 false。

示例 1：

输入：["a==b","b!=a"]
输出：false
解释：如果我们指定 a = 1 且 b = 1，那么可以满足第一个方程，但无法满足第二个方程。没有办法分配变量同时满足这两个方程。

示例 2：

输入：["b==a","a==b"]
输出：true
解释：我们可以指定 a = 1 且 b = 1 以满足满足这两个方程。

示例 3：

输入：["a==b","b==c","a==c"]
输出：true

示例 4：

输入：["a==b","b!=c","c==a"]
输出：false

示例 5：

输入：["c==c","b==d","x!=z"]
输出：true

注意：

1 <= equations.length <= 500
equations[i].length == 4
equations[i][0] 和 equations[i][3] 是小写字母
equations[i][1] 是 '=' 或 '!'
equations[i][2] 是 '='

【中文翻译】
给定一组等式和不等式方程（如 "a==b" 和 "a!=b"），判断是否存在一组整数赋值使得所有方程同时成立。可以先处理所有等式建立连通关系（并查集），再检查不等式中变量是否属于同一连通分量。

"""

from typing import List, Optional


class UnionFind:
    def __init__(self):
        self.parent = list(range(26))

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> None:
        px, py = self.find(x), self.find(y)
        if px != py:
            self.parent[px] = py


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UnionFind()
        # First pass: process all equality equations
        for eq in equations:
            if eq[1] == '=':
                x = ord(eq[0]) - ord('a')
                y = ord(eq[3]) - ord('a')
                uf.union(x, y)
        # Second pass: check inequality equations
        for eq in equations:
            if eq[1] == '!':
                x = ord(eq[0]) - ord('a')
                y = ord(eq[3]) - ord('a')
                if uf.find(x) == uf.find(y):
                    return False
        return True



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 并查集（Union-Find）：
# 1. 核心思想：等式形成等价关系（自反、对称、传递），所有通过等式相连的变量必须属于同一集合。
# 2. 两个步骤：
#    - 第一步：遍历所有 "==" 方程，将两个变量合并到同一集合（union 操作）。
#    - 第二步：遍历所有 "!=" 方程，检查两个变量是否在同一集合中。
#      * 如果在同一集合，说明之前有等式将它们连接，与不等式矛盾，返回 False。
#      * 如果不在同一集合，不矛盾，继续。
# 3. 如果所有不等式都不矛盾，返回 True。
# 4. 变量只有 26 个小写字母，并查集可以用大小为 26 的数组实现。
#
# 时间复杂度: O(N * α(26)) ≈ O(N)，N 为方程数量。α 为阿克曼函数的反函数，近似常数。
#   - 实际上每次 find/union 操作近乎 O(1)，因为只有 26 个元素。
# 空间复杂度: O(1)，并查集数组大小为常数 26。
#
# 关键点:
# - 等式具有传递性，适合用并查集建模
# - 先处理所有等式建立连通关系，再检查不等式
# - 不等式检查：如果两个变量属于同一连通分量则矛盾
# - 路径压缩优化 find 操作（虽然 26 个元素下优化不明显）
# - 字符转索引：ord(ch) - ord('a')
