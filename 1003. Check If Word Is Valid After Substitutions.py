"""
LeetCode #1003 - Check If Word Is Valid After Substitutions
中文题名：检查替换后的词是否有效
https://leetcode.com/problems/check-if-word-is-valid-after-substitutions/

We are given that the string `"abc"` is valid.

From any valid string `V`, we may split `V` into two pieces `X`
and `Y` such that `X + Y` (`X` concatenated with
`Y`) is equal to `V`.  (`X` or `Y` may be
empty.)  Then, `X + "abc" + Y` is also valid.

If for example `S = "abc"`, then examples of valid strings are: `"abc",
"aabcbc", "abcabc", "abcabcababcc"`.  Examples of
invalid strings are: `"abccba"`, `"ab"`,
`"cababc"`, `"bac"`.

Return `true` if and only if the given string `S` is valid.

Example 1:

Input: "aabcbc"
Output: true
Explanation:
We start with the valid string "abc".
Then we can insert another "abc" between "a" and "bc", resulting in "a" + "abc" + "bc" which is "aabcbc".

Example 2:

Input: "abcabcababcc"
Output: true
Explanation:
"abcabcabc" is valid after consecutive insertings of "abc".
Then we can insert "abc" before the last letter, resulting in "abcabcab" + "abc" + "c" which is "abcabcababcc".

Example 3:

Input: "abccba"
Output: false

Example 4:

Input: "cababc"
Output: false

【中文翻译】
给定一个字符串 `"abc"` 是有效的。

从任何有效的字符串 `V` 开始，我们可以将 `V` 分成两部分 `X` 和 `Y`，使得 `X + Y`（`X` 与 `Y` 连接）等于 `V`。（`X` 或 `Y` 可以为空。）那么，`X + "abc" + Y` 也是有效的。

例如，如果 `S = "abc"`，则有效字符串的示例包括：`"abc"`、`"aabcbc"`、`"abcabc"`、`"abcabcababcc"`。无效字符串的示例包括：`"abccba"`、`"ab"`、`"cababc"`、`"bac"`。

当且仅当给定的字符串 `S` 有效时返回 `true`。

示例 1：

输入："aabcbc"
输出：true
解释：
我们从有效字符串 "abc" 开始。
然后我们可以在 "a" 和 "bc" 之间插入另一个 "abc"，得到 "a" + "abc" + "bc"，即 "aabcbc"。

示例 2：

输入："abcabcababcc"
输出：true
解释：
连续插入 "abc" 后 "abcabcabc" 是有效的。
然后我们可以在最后一个字母之前插入 "abc"，得到 "abcabcab" + "abc" + "c"，即 "abcabcababcc"。

示例 3：

输入："abccba"
输出：false

示例 4：

输入："cababc"
输出：false

"""

from typing import List, Optional


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            stack.append(ch)
            if len(stack) >= 3 and stack[-3:] == ['a', 'b', 'c']:
                stack.pop()
                stack.pop()
                stack.pop()
        return len(stack) == 0










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用栈来模拟字符串的构建过程。遍历字符串中的每个字符，将其压入栈中。
# 每当栈顶的三个字符依次为 'a'、'b'、'c' 时，说明形成了一个有效的 "abc" 单元，
# 将其弹出（相当于消去）。这模拟了从有效字符串中不断插入 "abc" 的逆过程。
# 最后检查栈是否为空：如果为空说明整个字符串可以通过反复插入 "abc" 构建，即有效。
#
# 时间复杂度: O(n) - 每个字符最多入栈一次、出栈一次
# 空间复杂度: O(n) - 栈最多存储全部字符
#
# 关键点:
# - 每次遇到 'c' 时检查栈顶是否为 'b' 和 'a'（用 stack[-3:] 统一判断）
# - 栈模拟的是不断消除 "abc" 的过程，类似括号匹配
# - 不能简单地替换 "abc" 为空（O(n^2)），栈方法只需一次遍历
