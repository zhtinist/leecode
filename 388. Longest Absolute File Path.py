"""
LeetCode #388 - Longest Absolute File Path
中文题名：文件的最长绝对路径
https://leetcode.com/problems/longest-absolute-file-path/

Suppose we abstract our file system by a string in the following manner:

The string `"dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"` represents:

dir
subdir1
subdir2
file.ext

The directory `dir` contains an empty sub-directory `subdir1` and a
sub-directory `subdir2` containing a file `file.ext`.

The string `"dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"`
represents:

dir
subdir1
file1.ext
subsubdir1
subdir2
subsubdir2
file2.ext

The directory `dir` contains two sub-directories `subdir1` and `subdir2`.
`subdir1` contains a file `file1.ext` and an empty second-level
sub-directory `subsubdir1`. `subdir2` contains a second-level
sub-directory `subsubdir2` containing a file `file2.ext`.

We are interested in finding the longest (number of characters) absolute path to a file
within our file system. For example, in the second example above, the longest absolute path
is `"dir/subdir2/subsubdir2/file2.ext"`, and its length is `32` (not
including the double quotes).

Given a string representing the file system in the above format, return the length of the
longest absolute path to file in the abstracted file system. If there is no file in the
system, return `0`.

Note:

The name of a file contains at least a `.` and an extension.

The name of a directory or sub-directory will not contain a `.`.

Time complexity required: `O(n)` where `n` is the size of the input
string.

Notice that `a/aa/aaa/file1.txt` is not the longest file path, if there is another
path `aaaaaaaaaaaaaaaaaaaaa/sth.png`.

【中文翻译】
假设我们通过以下方式将文件系统抽象为一个字符串：

字符串 `"dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"` 表示：

dir
    subdir1
    subdir2
        file.ext

目录 `dir` 包含一个空的子目录 `subdir1` 和一个包含文件 `file.ext` 的子目录 `subdir2`。

字符串 `"dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"` 表示：

dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext

目录 `dir` 包含两个子目录 `subdir1` 和 `subdir2`。`subdir1` 包含一个文件 `file1.ext` 和一个空的二级子目录 `subsubdir1`。`subdir2` 包含一个二级子目录 `subsubdir2`，其中包含一个文件 `file2.ext`。

我们希望找出文件系统中文件的最长绝对路径（字符数）。例如，在上面的第二个例子中，最长的绝对路径是 `"dir/subdir2/subsubdir2/file2.ext"`，其长度为 `32`（不包括双引号）。

给定一个以上述格式表示文件系统的字符串，返回抽象文件系统中文件的最长绝对路径的长度。如果系统中没有文件，返回 `0`。

注意：

文件名至少包含一个 `.` 和一个扩展名。

目录名或子目录名不会包含 `.`。

要求时间复杂度：`O(n)`，其中 `n` 是输入字符串的长度。

请注意，如果存在另一个路径 `aaaaaaaaaaaaaaaaaaaaa/sth.png`，则 `a/aa/aaa/file1.txt` 不是最长的文件路径。
"""

from typing import List, Optional


class Solution:
    def lengthLongestPath(self, input: str) -> int:
        max_len = 0
        # path_len[depth] = 从根到当前深度目录的累积路径长度（不含末尾的 '/'）
        path_len = {0: 0}

        for line in input.split('\n'):
            # 去掉制表符，得到纯名称；统计 '\t' 的数量得到深度
            name = line.lstrip('\t')
            depth = len(line) - len(name)

            if '.' in name:
                # 这是一个文件：计算完整路径长度
                max_len = max(max_len, path_len[depth] + len(name))
            else:
                # 这是一个目录：记录当前深度的累积路径长度（加 1 是为了后面的 '/'）
                path_len[depth + 1] = path_len[depth] + len(name) + 1

        return max_len











# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用栈/哈希表记录每一级目录的累积路径长度。
# 1. 用换行符 '\n' 分割输入字符串，得到每一行。
# 2. 对于每一行，通过统计 '\t' 的数量确定其所在的深度（层级）。
# 3. 去掉 '\t' 后得到文件/目录的纯名称。
# 4. 如果是文件（名称含 '.'），计算完整路径长度 = 父目录累积长度 + 文件名长度，
#    更新全局最大值。
# 5. 如果是目录，记录当前深度的累积路径长度 = 父目录累积长度 + 目录名长度 + 1
#    （+1 是因为目录后面要加 '/'）。
# 使用字典 path_len 记录每个深度对应的累积路径长度，只需要一次遍历。
#
# 时间复杂度: O(n) - 遍历输入字符串一次
# 空间复杂度: O(d) - d 为目录树的最大深度，用于存储 path_len 字典
#
# 关键点:
# - 用 '\t' 的数量确定深度，天然适配题目输入格式
# - 分开处理文件和目录：文件更新 max_len，目录更新 path_len
# - path_len[depth] 存储从根到当前深度目录的累积路径长度（包含路径分隔符）
# - 用字典而非数组存储深度信息，更灵活
# - 使用 split('\n') 和 lstrip('\t') 高效解析每一行
