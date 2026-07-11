"""
LeetCode #1061 - Lexicographically Smallest Equivalent String
中文题名：按字典序排列最小的等效字符串
https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

Given strings `A` and `B` of the same length, we say A[i] and B[i] are
equivalent characters. For example, if `A = "abc"` and `B = "cde"`,
then we have `'a' == 'c', 'b' == 'd', 'c' ==
'e'`.

Equivalent characters follow the usual rules of any equivalence relation:

Reflexivity: 'a' == 'a'

Symmetry: 'a' == 'b' implies 'b' == 'a'

Transitivity: 'a' == 'b' and 'b' == 'c' implies 'a'
== 'c'

For example, given the equivalency information from `A` and `B` above,
`S = "eed"`, `"acd"`, and
`"aab"` are equivalent strings, and `"aab"` is the
lexicographically smallest equivalent string of `S`.

Return the lexicographically smallest equivalent string of `S` by using the
equivalency information from `A` and `B`.

Example 1:

Input: A = "parker", B = "morris", S = "parser"
Output: "makkek"
Explanation: Based on the equivalency information in `A` and `B`, we can group their characters as `[m,p]`, `[a,o]`, `[k,r,s]`, `[e,i]`. The characters in each group are equivalent and sorted in lexicographical order. So the answer is `"makkek"`.

Example 2:

Input: A = "hello", B = "world", S = "hold"
Output: "hdld"
Explanation:  Based on the equivalency information in `A` and `B`, we can group their characters as `[h,w]`, `[d,e,o]`, `[l,r]`. So only the second letter `'o'` in `S` is changed to `'d'`, the answer is `"hdld"`.

Example 3:

Input: A = "leetcode", B = "programs", S = "sourcecode"
Output: "aauaaaaada"
Explanation:  We group the equivalent characters in `A` and `B` as `[a,o,e,r,s,c]`, `[l,p]`, `[g,t]` and `[d,m]`, thus all letters in `S` except `'u'` and `'d'` are transformed to `'a'`, the answer is `"aauaaaaada"`.

Note:

String `A`, `B` and `S` consist of only lowercase
English letters from `'a'` - `'z'`.

The lengths of string `A`, `B` and `S` are between
`1` and `1000`.

String `A` and `B` are of the same length.

【中文翻译】
给出长度相同的两个字符串 A 和 B，A[i] 和 B[i] 是一组等价字符。例如，如果 A = "abc" 且 B = "cde"，那么就有 'a' == 'c', 'b' == 'd', 'c' == 'e'。

等价字符遵循任何等价关系的常规规则：

自反性：'a' == 'a'
对称性：'a' == 'b' 意味着 'b' == 'a'
传递性：'a' == 'b' 且 'b' == 'c' 意味着 'a' == 'c'

例如，A 和 B 的等价信息和之前的例子一样，那么 S = "eed"、"acd" 和 "aab" 都是等效字符串，其中 "aab" 是 S 的按字典序排列最小的等效字符串。

利用 A 和 B 的等价信息，找出并返回 S 的按字典序排列最小的等效字符串。

示例 1：

输入：A = "parker", B = "morris", S = "parser"
输出："makkek"
解释：根据 A 和 B 中的等价信息，可以将这些字符分为 [m,p]、[a,o]、[k,r,s]、[e,i]。共四组。每组中的字符是等价的，并按字典序排列。所以答案是 "makkek"。

示例 2：

输入：A = "hello", B = "world", S = "hold"
输出："hdld"
解释：根据 A 和 B 中的等价信息，可以将这些字符分为 [h,w]、[d,e,o]、[l,r]。所以只在 S 中的第二个字母 'o' 变为 'd'，答案是 "hdld"。

示例 3：

输入：A = "leetcode", B = "programs", S = "sourcecode"
输出："aauaaaaada"
解释：将 A 和 B 中的等效字符分组为 [a,o,e,r,s,c]、[l,p]、[g,t] 和 [d,m]，因此 S 中除了 'u' 和 'd' 之外的所有字母都转化为了 'a'，答案是 "aauaaaaada"。

注意：

字符串 A、B 和 S 仅由从 'a' 到 'z' 的小写英文字母组成。
字符串 A、B 和 S 的长度在 1 到 1000 之间。
字符串 A 和 B 长度相同。

"""

from typing import List, Optional


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = list(range(26))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px < py:
                parent[py] = px
            else:
                parent[px] = py

        for a, b in zip(s1, s2):
            union(ord(a) - 97, ord(b) - 97)

        result = []
        for ch in baseStr:
            root = find(ord(ch) - 97)
            result.append(chr(root + 97))

        return ''.join(result)










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用并查集（Union-Find）解决等价关系问题。
# 1. 初始化 26 个字母各自的父节点为自己（parent[i] = i）。
# 2. 遍历 A 和 B 的每对字符，将它们合并到同一集合中。
#    合并时，将字典序较大的字母的根指向字典序较小的字母的根，这样每个集合的根始终是其中最小的字母。
# 3. 对于 S 中的每个字符，找到它所在集合的根（最小的等价字母），替换为根字母。
#
# 时间复杂度: O((n + m) * α(26)) - n 为 A/B 长度，m 为 S 长度，α 为阿克曼反函数（近似常数）
# 空间复杂度: O(1) - parent 数组固定大小为 26
#
# 关键点:
# - 并查集处理等价关系的传递性
# - 合并时始终让字典序较小的作为根（parent[py] = px 当 px < py）
# - 路径压缩优化查找效率
# - 直接映射字母到 0-25 的整数
