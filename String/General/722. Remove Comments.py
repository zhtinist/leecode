"""
LeetCode #722 - Remove Comments
中文题名：删除注释
https://leetcode.com/problems/remove-comments/

Given a C++ program, remove comments from it. The program `source` is an array
where `source[i]` is the `i`-th line of the source code. This
represents the result of splitting the original source code string by the newline character
`\n`.

In C++, there are two types of comments, line comments, and block comments.

The string `//` denotes a line comment, which represents that it and rest of the
characters to the right of it in the same line should be ignored.

The string `/*` denotes a block comment, which represents that all characters
until the next (non-overlapping) occurrence of `*/` should be ignored. (Here,
occurrences happen in reading order: line by line from left to right.) To be clear, the
string `/*/` does not yet end the block comment, as the ending would be
overlapping the beginning.

The first effective comment takes precedence over others: if the string `//`
occurs in a block comment, it is ignored. Similarly, if the string `/*` occurs in
a line or block comment, it is also ignored.

If a certain line of code is empty after removing comments, you must not output that line:
each string in the answer list will be non-empty.

There will be no control characters, single quote, or double quote characters. For example,
`source = "string s = "/* Not a comment. */";"` will not be a test case. (Also,
nothing else such as defines or macros will interfere with the comments.)

It is guaranteed that every open block comment will eventually be closed, so `/*`
outside of a line or block comment always starts a new comment.

Finally, implicit newline characters can be deleted by block comments. Please see the
examples below for details.

After removing the comments from the source code, return the source code in the same
format.

Example 1:

Input:
source = ["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]

The line by line code is visualized as below:
/*Test program */
int main()
{
// variable declaration
int a, b, c;
/* This is a test
multiline
comment for
testing */
a = b + c;
}

Output: ["int main()","{ ","  ","int a, b, c;","a = b + c;","}"]

The line by line code is visualized as below:
int main()
{

int a, b, c;
a = b + c;
}

Explanation:
The string `/*` denotes a block comment, including line 1 and lines 6-9. The string `//` denotes line 4 as comments.

Example 2:

Input:
source = ["a/*comment", "line", "more_comment*/b"]
Output: ["ab"]
Explanation: The original source string is "a/*comment\nline\nmore_comment*/b", where we have bolded the newline characters.  After deletion, the implicit newline characters are deleted, leaving the string "ab", which when delimited by newline characters becomes ["ab"].

Note:

The length of `source` is in the range `[1, 100]`.

The length of `source[i]` is in the range `[0, 80]`.

Every open block comment is eventually closed.

There are no single-quote, double-quote, or control characters in the source code.

【中文翻译】
给一个 C++ 程序，删除程序中的注释。这个程序 source 是一个数组，其中 source[i] 表示第 i 行源代码。这表示将原始源代码字符串按换行符 \n 分隔的结果。

在 C++ 中有两种注释风格，行内注释和块注释。

字符串 // 表示行注释，表示 // 和其右侧的其余字符在所在行中应该被忽略。

字符串 /* 表示一个块注释，它表示直到下一个（非重叠的）出现的 */ 之间的所有字符都应该被忽略。（阅读顺序为从左到右，逐行读取。）需要明确的是，字符串 /*/ 并不结束块注释，因为注释的结束与开始重叠。

第一个有效注释优先于其他注释：如果字符串 // 出现在块注释中，则它被忽略。同样，如果字符串 /* 出现在行注释或块注释中，它也被忽略。

如果某一行在删除注释后变为空字符串，那么不要输出该行。即，答案列表中的每个字符串都是非空的。

样例中没有控制字符，单引号或双引号字符。例如，source = "string s = "/* Not a comment. */";" 不会作为测试样例。（此外，没有其他诸如 define 或 macros 之类会干扰注释的内容。）

保证每一个打开的块注释最终都会被关闭。所以在行注释或块注释之外的 /* 总是会开始一个新的注释。

最后，隐式换行符可以被块注释删除。有关详细信息，请参阅下面的示例。

从源代码中删除注释后，需要以相同的格式返回源代码。

示例 1：

输入：
source = ["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]

逐行代码可视化如下：
/*Test program */
int main()
{
// variable declaration
int a, b, c;
/* This is a test
multiline
comment for
testing */
a = b + c;
}

输出：["int main()","{ ","  ","int a, b, c;","a = b + c;","}"]

逐行代码可视化如下：
int main()
{

int a, b, c;
a = b + c;
}

解释：
字符串 /* 表示块注释，包括第 1 行和第 6-9 行。字符串 // 表示第 4 行是注释。

示例 2：

输入：
source = ["a/*comment", "line", "more_comment*/b"]
输出：["ab"]
解释：原始 source 字符串是 "a/*comment\nline\nmore_comment*/b"，其中我们用粗体标注了换行符。删除注释后，隐式换行符被删除，留下字符串 "ab"，用换行符分隔后变为 ["ab"]。

注意：

source 的长度在 [1, 100] 范围内。

source[i] 的长度在 [0, 80] 范围内。

每个打开的块注释最终都会被关闭。

源代码中没有单引号、双引号或控制字符。
"""

from typing import List, Optional


class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        result = []
        in_block = False
        new_line = []

        for line in source:
            i = 0
            while i < len(line):
                if not in_block and i + 1 < len(line) and line[i:i + 2] == "/*":
                    in_block = True
                    i += 2
                elif in_block and i + 1 < len(line) and line[i:i + 2] == "*/":
                    in_block = False
                    i += 2
                elif not in_block and i + 1 < len(line) and line[i:i + 2] == "//":
                    break
                elif not in_block:
                    new_line.append(line[i])
                    i += 1
                else:
                    i += 1

            if not in_block and new_line:
                result.append("".join(new_line))
                new_line = []

        return result



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用状态机模拟注释的解析过程。维护一个布尔变量 in_block 表示当前是否处于块注释中。
# 逐行逐字符遍历 source：
# - 不在块注释中遇到 "/*" → 进入块注释模式
# - 在块注释中遇到 "*/" → 退出块注释模式
# - 不在块注释中遇到 "//" → 忽略该行剩余部分
# - 不在块注释中的普通字符 → 加入当前行结果
# - 在块注释中的字符 → 跳过
# 每行结束后，如果不在块注释中且当前行有内容，加入结果。
#
# 时间复杂度: O(N * L) - N 为行数，L 为每行最大长度
# 空间复杂度: O(N * L) - 存储输出结果
#
# 关键点:
# - 块注释可以跨越多行，需要维护 in_block 状态
# - 行注释 // 在块注释中不生效
# - 块注释 /* 在行注释中不生效（因为 // 已经让该行剩余部分被忽略）
# - 删除注释后如果某行为空，不能输出该行
# - 块注释中的隐式换行符也要被删除（示例 2）
