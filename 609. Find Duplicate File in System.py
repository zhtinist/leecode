"""
LeetCode #609 - Find Duplicate File in System
中文题名：在系统中查找重复文件
https://leetcode.com/problems/find-duplicate-file-in-system/

Given a list of directory info including directory path, and all the files with contents in
this directory, you need to find out all the groups of duplicate files in the file system in
terms of their paths.

A group of duplicate files consists of at least two files that have exactly the same
content.

A single directory info string in the input list has the following format:

`"root/d1/d2/.../dm f1.txt(f1_content) f2.txt(f2_content) ... fn.txt(fn_content)"`

It means there are n files (`f1.txt`, `f2.txt` ...
`fn.txt` with content `f1_content`, `f2_content` ... `fn_content`,
respectively) in directory `root/d1/d2/.../dm`. Note that n >= 1 and m >=
0. If m = 0, it means the directory is just the root directory.

The output is a list of group of duplicate file paths. For each group, it contains all
the file paths of the files that have the same content. A file path is a string that has the
following format:

`"directory_path/file_name.txt"`

Example 1:

Input:
["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]
Output:
[["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]]

Note:

No order is required for the final output.

You may assume the directory name, file name and file content only has letters and
digits, and the length of file content is in the range of [1,50].

The number of files given is in the range of [1,20000].

You may assume no files or directories share the same name in the same directory.

You may assume each given directory info represents a unique directory. Directory path
and file info are separated by a single blank space.

Follow-up beyond contest:

Imagine you are given a real file system, how will you search files? DFS or BFS?

If the file content is very large (GB level), how will you modify your solution?

If you can only read the file by 1kb each time, how will you modify your solution?

What is the time complexity of your modified solution? What is the most time-consuming
part and memory consuming part of it? How to optimize?

How to make sure the duplicated files you find are not false positive?

【中文翻译】
给定一个包含目录信息的列表，其中包括目录路径以及该目录下所有文件及其内容，
你需要找出文件系统中所有重复文件组（根据其路径）。

一组重复文件由至少两个内容完全相同的文件组成。

输入列表中的单个目录信息字符串格式如下：

`"root/d1/d2/.../dm f1.txt(f1_content) f2.txt(f2_content) ... fn.txt(fn_content)"`

这意味着在目录 `root/d1/d2/.../dm` 中有 n 个文件（`f1.txt`、`f2.txt` ...
`fn.txt`，内容分别为 `f1_content`、`f2_content` ... `fn_content`）。
注意 n >= 1，m >= 0。如果 m = 0，表示该目录就是根目录。

输出是一组重复文件路径的列表。对于每个组，包含所有具有相同内容的文件路径。文件路径的格式为：

`"directory_path/file_name.txt"`

示例 1：

输入：
["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]
输出：
[["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]]

注意：

最终输出不需要遵循某种顺序。

你可以假设目录名、文件名和文件内容只包含字母和数字，文件内容的长度在 [1,50] 范围内。

给定的文件数量在 [1,20000] 范围内。

你可以假设没有文件或目录在同一目录中共享相同的名称。

你可以假设每个给定的目录信息代表一个唯一的目录。目录路径和文件信息由单个空格分隔。

Follow-up（超越竞赛）：
假想你被给定一个真实的文件系统，你将如何搜索文件？DFS 还是 BFS？
如果文件内容非常大（GB 级别），你将如何修改你的解决方案？
如果你每次只能读取 1KB 的文件，你将如何修改你的解决方案？
你修改后的解决方案的时间复杂度是多少？其中最耗时和最占内存的部分是什么？如何优化？
如何确保你找到的重复文件不是假阳性？
"""

from collections import defaultdict


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_to_paths: dict[str, list[str]] = defaultdict(list)

        for path in paths:
            parts = path.split()
            directory = parts[0]

            for file_info in parts[1:]:
                # file_info format: "filename(content)"
                name, content_with_paren = file_info.split('(')
                content = content_with_paren[:-1]  # remove trailing ')'
                full_path = f"{directory}/{name}"
                content_to_paths[content].append(full_path)

        # Return only groups with at least 2 files (duplicates)
        return [group for group in content_to_paths.values() if len(group) > 1]



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用哈希表（defaultdict）将文件内容作为键，完整路径列表作为值：
# 1. 遍历每个目录信息字符串。
# 2. 对每个字符串，用空格分割：第一部分是目录路径，后续部分是文件名(内容)。
# 3. 将文件名和内容分离（以 '(' 分割并去掉 ')'）。
# 4. 将完整路径（目录/文件名）添加到该内容对应的列表中。
# 5. 最后筛选出长度大于 1 的组（即存在重复文件）。
#
# 时间复杂度: O(N * L) - N 为文件总数，L 为平均文件内容长度
# 空间复杂度: O(N * L) - 存储所有文件的内容和路径映射
#
# 关键点:
# - 以文件内容为键进行分组，自然找出重复文件
# - 字符串解析：注意文件名和内容用 ( ) 包围
# - 路径拼接：directory + "/" + filename
# - Follow-up 涉及大文件场景，需用文件哈希（MD5/SHA）进行增量比较
