"""
LeetCode #1111 - Maximum Nesting Depth of Two Valid Parentheses Strings
中文题名：有效括号的嵌套深度
https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/

A string is a valid parentheses string (denoted VPS) if and only if it consists
of `"("` and `")"` characters only, and:

It is the empty string, or

It can be written as `AB` (`A` concatenated with `B`),
where `A` and `B` are VPS's, or

It can be written as `(A)`, where `A` is a VPS.

We can similarly define the nesting depth `depth(S)` of any VPS
`S` as follows:

`depth("") = 0`

`depth(A + B) = max(depth(A), depth(B))`, where `A` and
`B` are VPS's

`depth("(" + A + ")") = 1 + depth(A)`, where
`A` is a VPS.

For example,  `""`, `"()()"`,
and `"()(()())"` are VPS's (with nesting depths 0, 1, and
2), and `")("` and `"(()"` are not VPS's.

Given a VPS seq, split it into two disjoint subsequences `A`
and `B`, such that `A` and `B` are VPS's (and `A.length
+ B.length = seq.length`).

Now choose any such `A` and `B` such that `max(depth(A),
depth(B))` is the minimum possible value.

Return an `answer` array (of length `seq.length`) that encodes such a choice
of `A` and `B`:  `answer[i] = 0` if
`seq[i]` is part of `A`, else `answer[i] = 1`.  Note
that even though multiple answers may exist, you may return any of them.

Example 1:

Input: seq = "(()())"
Output: [0,1,1,1,1,0]

Example 2:

Input: seq = "()(())()"
Output: [0,0,0,1,1,0,1,1]

Constraints:

`1 <= seq.size <= 10000`

【中文翻译】
一个字符串是有效括号字符串（VPS）当且仅当它只由 '(' 和 ')' 字符组成，且满足以下条件之一：

- 它是空字符串，或
- 它可以写成 AB（A 与 B 连接），其中 A 和 B 都是 VPS，或
- 它可以写成 (A)，其中 A 是 VPS。

我们可以类似地定义任意 VPS S 的嵌套深度 depth(S) 如下：

depth("") = 0
depth(A + B) = max(depth(A), depth(B))，其中 A 和 B 是 VPS
depth("(" + A + ")") = 1 + depth(A)，其中 A 是 VPS。

例如，""、"()()" 和 "()(()())" 是 VPS（嵌套深度分别为 0、1 和 2），而 ")(" 和 "(()" 不是 VPS。

给定一个有效括号字符串 seq，将其分割成两个不相交的子序列 A 和 B，使得 A 和 B 都是 VPS（且 A.length + B.length = seq.length）。

现在选择任意这样的 A 和 B，使得 max(depth(A), depth(B)) 的值尽可能小。

返回一个长度为 seq.length 的 answer 数组，编码了对 A 和 B 的选择：answer[i] = 0 表示 seq[i] 属于 A，否则 answer[i] = 1。注意，即使可能存在多个答案，你只需要返回其中任意一个。

示例 1：

输入：seq = "(()())"
输出：[0,1,1,1,1,0]

示例 2：

输入：seq = "()(())()"
输出：[0,0,0,1,1,0,1,1]

约束条件：

`1 <= seq.size <= 10000`
"""

from typing import List, Optional


class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        result = []
        depth = 0
        for ch in seq:
            if ch == '(':
                result.append(depth % 2)
                depth += 1
            else:
                depth -= 1
                result.append(depth % 2)
        return result










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 核心思想：通过按嵌套深度的奇偶性来分配括号，将深度均匀分摊到两个子序列中。
# 1. 维护当前嵌套深度 depth。
# 2. 遍历字符串 seq：
#    - 遇到 '('：将当前深度 depth % 2 作为分组编号，然后 depth++。
#    - 遇到 ')'：先将 depth--，然后将当前深度 depth % 2 作为分组编号。
# 3. 这样，奇偶深度的括号分别分配给不同的组，最大嵌套深度被大致平分。
# 例如 "(()())" -> depth 变化: 0,1,2,1,2,1,0，按 depth%2 分配后为 [0,1,1,1,1,0]。
#
# 时间复杂度: O(n) - 遍历字符串一次
# 空间复杂度: O(n) - 结果数组
#
# 关键点:
# - 按深度奇偶性分配：将相邻深度的括号分到不同组，确保两组深度均衡
# - 对于 '('：先根据当前深度分配，再增加深度
# - 对于 ')'：先减少深度，再根据新深度分配
