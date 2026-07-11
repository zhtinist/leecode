"""
LeetCode #1415 - The k-th Lexicographical String of All Happy Strings of Length n
中文题名：长度为 n 的开心字符串中字典序第 k 小的字符串
https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/

A happy string is a string that:

consists only of letters of the set `['a', 'b', 'c']`.

`s[i] != s[i + 1]` for all values of `i` from
`1` to `s.length - 1` (string is 1-indexed).

For example, strings "abc", "ac", "b" and
"abcbabcbcb" are all happy strings and strings "aa",
"baa" and "ababbc" are not happy strings.

Given two integers `n` and `k`, consider a list of all happy
strings of length `n` sorted in lexicographical order.

Return the kth string of this list or return an empty
string if there are less than `k` happy strings of length
`n`.

Example 1:

Input: n = 1, k = 3
Output: "c"
Explanation: The list ["a", "b", "c"] contains all happy strings of length 1. The third string is "c".

Example 2:

Input: n = 1, k = 4
Output: ""
Explanation: There are only 3 happy strings of length 1.

Example 3:

Input: n = 3, k = 9
Output: "cab"
Explanation: There are 12 different happy string of length 3 ["aba", "abc", "aca", "acb", "bab", "bac", "bca", "bcb", "cab", "cac", "cba", "cbc"]. You will find the 9th string = "cab"

Example 4:

Input: n = 2, k = 7
Output: ""

Example 5:

Input: n = 10, k = 100
Output: "abacbabacb"

Constraints:

`1 <= n <= 10`

`1 <= k <= 100`

【中文翻译】

一个「开心字符串」定义为：

仅由集合 `['a', 'b', 'c']` 中的字母组成。
对于 `1` 到 `s.length - 1` 中的所有 `i`（字符串下标从 1 开始），满足 `s[i] != s[i + 1]`。

例如，字符串 "abc"、"ac"、"b" 和 "abcbabcbcb" 都是开心字符串，而 "aa"、"baa" 和 "ababbc" 不是开心字符串。

给定两个整数 `n` 和 `k`，考虑一个包含所有长度为 `n` 的开心字符串的列表，按字典序排序。

返回该列表中第 k 个字符串，如果长度为 `n` 的开心字符串少于 `k` 个，则返回空字符串。

示例 1：
输入：n = 1, k = 3
输出："c"
解释：列表 ["a", "b", "c"] 包含所有长度为 1 的开心字符串。第三个字符串是 "c"。

示例 2：
输入：n = 1, k = 4
输出：""
解释：长度为 1 的开心字符串只有 3 个。

示例 3：
输入：n = 3, k = 9
输出："cab"
解释：有 12 个长度为 3 的不同开心字符串 ["aba", "abc", "aca", "acb", "bab", "bac", "bca", "bcb", "cab", "cac", "cba", "cbc"]。第 9 个字符串 = "cab"。

示例 4：
输入：n = 2, k = 7
输出：""

示例 5：
输入：n = 10, k = 100
输出："abacbabacb"

约束条件：
`1 <= n <= 10`
`1 <= k <= 100`

"""

from typing import List, Optional


class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        # 计算长度为 n 的开心字符串总数：3 * 2^(n-1)
        total = 3 * (1 << (n - 1))
        if k > total:
            return ""

        chars = ['a', 'b', 'c']
        result = []
        k -= 1  # 转换为 0-based 索引

        # 确定第一个字符
        # 每个第一字符有 2^(n-1) 个字符串
        group_size = 1 << (n - 1)
        first_idx = k // group_size
        result.append(chars[first_idx])
        k %= group_size

        # 确定后续字符
        for i in range(1, n):
            # 剩余长度：n - 1 - i 个字符，每个有 2 种选择
            # 当前剩余 n-1-i 个位置，每个位置有 2 种选择
            # 所以每个可用字符对应 2^(n-1-i) 个字符串
            group_size = 1 << (n - 1 - i)
            prev_char = result[-1]
            # 可选的字符：不同于前一个字符的两个字符
            options = [c for c in chars if c != prev_char]
            idx = k // group_size
            result.append(options[idx])
            k %= group_size

        return "".join(result)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 数学构造法（逐位确定）：
# 1. 首先计算总共有多少个长度为 n 的开心字符串：
#    第一个位置有 3 种选择（'a', 'b', 'c'），后续每个位置有 2 种选择（不能与前一个相同）。
#    总数 = 3 * 2^(n-1)。
#    如果 k > 总数，返回空字符串。
#
# 2. 将 k 转换为 0-based 索引（k -= 1）。
#
# 3. 确定第一个字符：每个第一字符对应 2^(n-1) 个字符串。
#    first_idx = k // 2^(n-1)，在 ['a','b','c'] 中选第 first_idx 个。
#    更新 k = k % 2^(n-1)。
#
# 4. 对于每个后续位置 i（从 1 到 n-1）：
#    剩余未确定的位置数是 (n-1-i)，每个位置有 2 种选择，
#    所以分组大小 = 2^(n-1-i)。
#    可选字符是两个不同于前一个字符的字符。
#    选择 idx = k // group_size。
#    更新 k = k % group_size。
#
# 5. 返回构造的字符串。
#
# 时间复杂度: O(N)，逐位构造长度为 n 的字符串。
# 空间复杂度: O(N)，存储结果字符串。
#
# 关键点:
# - 总数为 3 * 2^(n-1)，先判断 k 是否有效
# - 使用除法和取模逐位确定，无需回溯生成所有字符串
# - 剩余分组大小计算：剩余 (n-1-i) 个位置，每个有 2 种选择 => 2^(n-1-i)










