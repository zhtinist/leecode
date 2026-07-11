"""
LeetCode #1410 - HTML Entity Parser
中文题名：HTML 实体解析器
https://leetcode.com/problems/html-entity-parser/

HTML entity parser is the parser that takes HTML code as input and
replace all the entities of the special characters by the characters itself.

The special characters and their entities for HTML are:

Quotation Mark: the entity is `&quot;` and symbol
character is `"`.

Single Quote Mark: the entity is
`&apos;` and symbol character is `'`.

Ampersand: the entity is `&amp;` and symbol
character is `&`.

Greater Than Sign: the entity is `&gt;` and
symbol character is `>`.

Less Than Sign: the entity is `&lt;` and
symbol character is `<`.

Slash: the entity is `&frasl;` and symbol
character is `/`.

Given the input `text` string to the HTML parser, you have to implement
the entity parser.

Return the text after replacing the entities by the special characters.

Example 1:

Input: text = "&amp; is an HTML entity but &ambassador; is not."
Output: "& is an HTML entity but &ambassador; is not."
Explanation: The parser will replace the &amp; entity by &

Example 2:

Input: text = "and I quote: &quot;...&quot;"
Output: "and I quote: \"...\""

Example 3:

Input: text = "Stay home! Practice on Leetcode :)"
Output: "Stay home! Practice on Leetcode :)"

Example 4:

Input: text = "x &gt; y &amp;&amp; x &lt; y is always false"
Output: "x > y && x < y is always false"

Example 5:

Input: text = "leetcode.com&frasl;problemset&frasl;all"
Output: "leetcode.com/problemset/all"

Constraints:

`1 <= text.length <= 10^5`

The string may contain any possible characters out of all the 256 ASCII
characters.

【中文翻译】

HTML 实体解析器是一种解析器，它接受 HTML 代码作为输入，并用字符本身替换所有特殊字符的实体。

HTML 的特殊字符及其对应的实体如下：

引号：实体为 `&quot;`，符号字符为 `"`。
单引号：实体为 `&apos;`，符号字符为 `'`。
与号：实体为 `&amp;`，符号字符为 `&`。
大于号：实体为 `&gt;`，符号字符为 `>`。
小于号：实体为 `&lt;`，符号字符为 `<`。
斜线：实体为 `&frasl;`，符号字符为 `/`。

给定输入 `text` 字符串，你需要实现实体解析器。

返回将实体替换为特殊字符后的文本。

示例 1：
输入：text = "&amp; is an HTML entity but &ambassador; is not."
输出："& is an HTML entity but &ambassador; is not."
解释：解析器会将 &amp; 实体替换为 &。

示例 2：
输入：text = "and I quote: &quot;...&quot;"
输出："and I quote: \"...\""

示例 3：
输入：text = "Stay home! Practice on Leetcode :)"
输出："Stay home! Practice on Leetcode :)"

示例 4：
输入：text = "x &gt; y &amp;&amp; x &lt; y is always false"
输出："x > y && x < y is always false"

示例 5：
输入：text = "leetcode.com&frasl;problemset&frasl;all"
输出："leetcode.com/problemset/all"

约束条件：
`1 <= text.length <= 10^5`
字符串可能包含所有 256 个 ASCII 字符中的任意字符。

"""

from typing import List, Optional


class Solution:
    def entityParser(self, text: str) -> str:
        # 使用字典存储所有 HTML 实体及其对应字符
        entities = {
            "&quot;": '"',
            "&apos;": "'",
            "&amp;": "&",
            "&gt;": ">",
            "&lt;": "<",
            "&frasl;": "/",
        }

        # 遍历每个实体，依次替换
        for entity, char in entities.items():
            text = text.replace(entity, char)

        return text



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 直接替换法：
# 1. 创建一个字典，将所有 HTML 实体映射到对应的字符。
# 2. 遍历字典中的每个键值对，使用 str.replace() 替换文本中的实体。
# 3. 注意：&amp; 应首先或最后替换以确保正确性。因为 & 在其他实体中被使用，
#    如果先替换 &amp; -> &，后续 &quot; 中的 & 可能会被污染。
#    但在这个实现中，我们使用字典的键直接替换完整实体字符串，不会出现这个问题，
#    因为 replace 是精确匹配整个实体字符串。
# 4. 最后返回替换完成的文本。
#
# 时间复杂度: O(N * K)，其中 N 是文本长度，K 是实体数量（常数 6）。实际每次 replace 扫描整个字符串。
# 空间复杂度: O(N)，用于存储替换后的结果字符串。
#
# 关键点:
# - HTML 实体以 & 开头，以 ; 结尾
# - 直接字符串替换即可，无需处理复杂的解析逻辑
# - 注意替换顺序（先换 &amp; 或最后换 &amp; 都可以，因为我们是精确匹配整个实体字符串）










