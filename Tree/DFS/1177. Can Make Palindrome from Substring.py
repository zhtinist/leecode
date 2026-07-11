"""
LeetCode #1177 - Can Make Palindrome from Substring
中文题名：构建回文串检测
https://leetcode.com/problems/can-make-palindrome-from-substring/

Given a string `s`, we make queries on substrings of `s`.

For each query `queries[i] = [left, right, k]`, we may rearrange the
substring `s[left], ..., s[right]`, and then choose up to `k`
of them to replace with any lowercase English letter.

If the substring is possible to be a palindrome string after the operations above,
the result of the query is `true`. Otherwise, the result is
`false`.

Return an array `answer[]`, where `answer[i]` is the result of the
`i`-th query `queries[i]`.

Note that: Each letter is counted individually for replacement so if
for example `s[left..right] = "aaa"`, and `k = 2`, we
can only replace two of the letters.  (Also, note that the initial string
`s` is never modified by any query.)

Example :

Input: s = "abcda", queries = [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]
Output: [true,false,false,true,true]
Explanation:
queries[0] : substring = "d", is palidrome.
queries[1] : substring = "bc", is not palidrome.
queries[2] : substring = "abcd", is not palidrome after replacing only 1 character.
queries[3] : substring = "abcd", could be changed to "abba" which is palidrome. Also this can be changed to "baab" first rearrange it "bacd" then replace "cd" with "ab".
queries[4] : substring = "abcda", could be changed to "abcba" which is palidrome.

Constraints:

`1 <= s.length, queries.length <= 10^5`

`0 <= queries[i][0] <= queries[i][1] < s.length`

`0 <= queries[i][2] <= s.length`

`s` only contains lowercase English letters.

【中文翻译】
给你一个字符串 s，请你对 s 的子串进行检测。

每次检测的查询用 queries[i] = [left, right, k] 表示。我们可以重排子串 s[left], ..., s[right]，并从中选择最多 k 个字符替换为任何小写英文字母。

如果在上述操作后，子串可以变成回文串，那么查询结果为 true，否则为 false。

返回一个数组 answer[]，其中 answer[i] 是第 i 个查询 queries[i] 的结果。

注意：每个字母在替换时是单独计数的。例如 s[left..right] = "aaa" 且 k = 2，我们只能替换其中的两个字母。（另外，初始字符串 s 不会被任何查询修改。）

示例：

输入：s = "abcda", queries = [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]
输出：[true,false,false,true,true]
解释：
queries[0]：子串 = "d"，是回文。
queries[1]：子串 = "bc"，不是回文。
queries[2]：子串 = "abcd"，仅替换 1 个字符后不是回文。
queries[3]：子串 = "abcd"，可以变为 "abba"（回文），也可以先重排为 "bacd" 再将 "cd" 替换为 "ab"。
queries[4]：子串 = "abcda"，可以变为 "abcba"（回文）。

约束条件：

1 <= s.length, queries.length <= 10^5
0 <= queries[i][0] <= queries[i][1] < s.length
0 <= queries[i][2] <= s.length
s 只包含小写英文字母。

"""

from typing import List, Optional


class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        n = len(s)
        prefix = [0] * (n + 1)
        for i, ch in enumerate(s):
            prefix[i + 1] = prefix[i] ^ (1 << (ord(ch) - 97))

        res = []
        for l, r, k in queries:
            mask = prefix[r + 1] ^ prefix[l]
            odd_count = mask.bit_count()
            res.append(odd_count // 2 <= k)
        return res










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用前缀位掩码(Prefix Bitmask)高效统计子串中每个字符的出现次数奇偶性。
# 核心观察：一个字符串能否重排为回文串，取决于其中出现次数为奇数的字符个数。
# - 若奇数个数的字符 <= 1，则可以直接重排为回文串（无需替换）。
# - 每使用一次替换操作，可以改变一个字符，从而使两个奇数计数字符变为偶数（替换一个奇数计数字符为另一个字符）。因此，如果有 odd 个奇数字符，至少需要 odd // 2 次替换。
# 具体实现：
# 1. 用位掩码表示 26 个字母的奇偶状态：第 c 位为 1 表示字母 c 出现了奇数次。
# 2. 构建前缀异或数组 prefix[i+1] = prefix[i] ^ (1 << s[i])。
# 3. 子串 s[l..r] 的奇偶掩码 = prefix[r+1] ^ prefix[l]（异或抵消前缀部分）。
# 4. 计算掩码中 1 的个数 bit_count() 即为奇数计数字符数 odd。
# 5. 判断 odd // 2 <= k 即可。
#
# 时间复杂度: O(n + q) - O(n) 构建前缀数组，每个查询 O(1) 计算
# 空间复杂度: O(n) - 存储长度为 n+1 的前缀数组
#
# 关键点:
# - 利用位掩码的异或性质，子串掩码 = prefix[r+1] ^ prefix[l]，快速得到奇偶分布
# - 回文条件：奇数计数字符数 <= 1（可重排）。若需替换，每替换一次可减少两个奇数计数字符
# - bit_count() 或 bin(mask).count('1') 高效计算置位数量
# - 限制 10^5 级别，O(26*queries) 的暴力计数也可以，但位运算更优雅
