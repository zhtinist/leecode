"""
LeetCode #1268 - Search Suggestions System
中文题名：搜索推荐系统
https://leetcode.com/problems/search-suggestions-system/

Given an array of strings `products` and a string `searchWord`.
We want to design a system that suggests at most three product names from
`products` after each character of `searchWord` is
typed. Suggested products should have common prefix with the searchWord. If there are more
than three products with a common prefix return the three lexicographically
minimums products.

Return list of lists of the suggested `products` after each
character of `searchWord` is typed.

Example 1:

Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [
["mobile","moneypot","monitor"],
["mobile","moneypot","monitor"],
["mouse","mousepad"],
["mouse","mousepad"],
["mouse","mousepad"]
]
Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
After typing mou, mous and mouse the system suggests ["mouse","mousepad"]

Example 2:

Input: products = ["havana"], searchWord = "havana"
Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]

Example 3:

Input: products = ["bags","baggage","banner","box","cloths"], searchWord = "bags"
Output: [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]

Example 4:

Input: products = ["havana"], searchWord = "tatiana"
Output: [[],[],[],[],[],[],[]]

Constraints:

`1 <= products.length <= 1000`

There are no repeated elements in `products`.

`1 <= Σ products[i].length <= 2 * 10^4`

All characters of `products[i]` are lower-case English letters.

`1 <= searchWord.length <= 1000`

All characters of `searchWord` are lower-case English letters.

【中文翻译】
给定一个字符串数组 `products` 和一个字符串 `searchWord`。我们想要设计一个系统，在输入 `searchWord` 的每个字符后，从 `products` 中推荐最多三个产品名称。推荐的产品应该与 `searchWord` 有相同的前缀。如果超过三个产品拥有相同前缀，请返回字典序最小的三个产品。

请返回输入 `searchWord` 每个字符后所推荐产品的列表的列表。

示例 1：

输入：products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
输出：[
["mobile","moneypot","monitor"],
["mobile","moneypot","monitor"],
["mouse","mousepad"],
["mouse","mousepad"],
["mouse","mousepad"]
]
解释：按字典序排序后的 products = ["mobile","moneypot","monitor","mouse","mousepad"]
输入 m 和 mo 后，所有产品都匹配，向用户显示 ["mobile","moneypot","monitor"]
输入 mou、mous 和 mouse 后，系统推荐 ["mouse","mousepad"]

示例 2：

输入：products = ["havana"], searchWord = "havana"
输出：[["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]

示例 3：

输入：products = ["bags","baggage","banner","box","cloths"], searchWord = "bags"
输出：[["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]

示例 4：

输入：products = ["havana"], searchWord = "tatiana"
输出：[[],[],[],[],[],[],[]]

约束条件：

`1 <= products.length <= 1000`

`products` 中没有重复的元素。

`1 <= Σ products[i].length <= 2 * 10^4`

`products[i]` 的所有字符都是小写英文字母。

`1 <= searchWord.length <= 1000`

`searchWord` 的所有字符都是小写英文字母。
"""

from typing import List, Optional


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        res = []

        prefix = ""
        for ch in searchWord:
            prefix += ch
            suggestions = []
            for p in products:
                if p.startswith(prefix):
                    suggestions.append(p)
                    if len(suggestions) == 3:
                        break
            res.append(suggestions)

        return res










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 排序 + 线性扫描（或二分查找）。
# 1. 将 products 按字典序排序。
# 2. 逐字符构建前缀 prefix，对于每个 prefix：
#    - 遍历排序后的 products，找到所有以 prefix 为前缀的字符串。
#    - 由于已排序，匹配的字符串会连续出现。
#    - 收集前 3 个匹配的字符串作为推荐结果。
# 3. 优化：使用二分查找找到第一个匹配的起始位置（bisect_left），然后取后续最多 3 个
#    仍然匹配前缀的字符串，可将每次查询优化到 O(log N + 3)。
#    更高级的方案是使用 Trie（前缀树），但排序 + 线性扫描对本题的数据规模已经足够。
#
# 时间复杂度: O(N * log N + M * N)，其中 N = len(products)，M = len(searchWord)。
#            二分优化后可达到 O(N * log N + M * log N)。
# 空间复杂度: O(1)，不计结果数组
#
# 关键点:
# - 排序是关键预处理：匹配前缀的字符串在排序后连续排列
# - 可以使用 bisect_left 定位起始位置加速
# - 也可以使用 Trie 树，但代码更复杂，对 N <= 1000 的规模没必要
# - 每次只需要最多 3 个结果，及时 break 可以优化常数项
