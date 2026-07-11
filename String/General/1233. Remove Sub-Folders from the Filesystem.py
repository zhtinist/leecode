"""
LeetCode #1233 - Remove Sub-Folders from the Filesystem
中文题名：删除子文件夹
https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/

Given a list of folders, remove all sub-folders in those folders and return in any
order the folders after removing.

If a `folder[i]` is located within another `folder[j]`, it is
called a sub-folder of it.

The format of a path is one or more concatenated strings of the
form: `/` followed by one or more lowercase English letters. For
example, `/leetcode` and `/leetcode/problems` are
valid paths while an empty string and `/` are not.

Example 1:

Input: folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
Output: ["/a","/c/d","/c/f"]
Explanation: Folders "/a/b/" is a subfolder of "/a" and "/c/d/e" is inside of folder "/c/d" in our filesystem.

Example 2:

Input: folder = ["/a","/a/b/c","/a/b/d"]
Output: ["/a"]
Explanation: Folders "/a/b/c" and "/a/b/d/" will be removed because they are subfolders of "/a".

Example 3:

Input: folder = ["/a/b/c","/a/b/ca","/a/b/d"]
Output: ["/a/b/c","/a/b/ca","/a/b/d"]

Constraints:

`1 <= folder.length <= 4 * 10^4`

`2 <= folder[i].length <= 100`

`folder[i]` contains only lowercase letters and '/'

`folder[i]` always starts with character '/'

Each folder name is unique.

【中文翻译】
给你一个文件夹列表，请你删除其中的所有子文件夹，并以任意顺序返回剩下的文件夹。

如果一个文件夹 `folder[i]` 位于另一个文件夹 `folder[j]` 下，那么 `folder[i]` 就是 `folder[j]` 的子文件夹。

路径的格式是一个或多个连接起来的字符串，形式为：`/` 后跟一个或多个小写英文字母。例如，`/leetcode` 和 `/leetcode/problems` 是有效路径，而空字符串和 `/` 不是。

示例 1：

输入：folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
输出：["/a","/c/d","/c/f"]
解释：文件夹 "/a/b/" 是 "/a" 的子文件夹，"/c/d/e" 是 "/c/d" 的子文件夹。

示例 2：

输入：folder = ["/a","/a/b/c","/a/b/d"]
输出：["/a"]
解释：文件夹 "/a/b/c" 和 "/a/b/d/" 将被删除，因为它们都是 "/a" 的子文件夹。

示例 3：

输入：folder = ["/a/b/c","/a/b/ca","/a/b/d"]
输出：["/a/b/c","/a/b/ca","/a/b/d"]

约束条件：

`1 <= folder.length <= 4 * 10^4`

`2 <= folder[i].length <= 100`

`folder[i]` 仅包含小写英文字母和 '/'

`folder[i]` 始终以字符 '/' 开头

每个文件夹名称都是唯一的。
"""

from typing import List, Optional


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        res = []

        for f in folder:
            if not res or not f.startswith(res[-1] + "/"):
                res.append(f)

        return res










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 1. 将文件夹列表按字典序排序。排序后，如果 A 是 B 的父文件夹，A 一定排在 B 前面。
# 2. 遍历排序后的列表，维护结果数组 res。
# 3. 对于当前文件夹 f，如果 res 为空或者 f 不以 res[-1] + "/" 为前缀，
#    则说明 f 不是已添加的最后一个文件夹的子文件夹，将 f 加入 res。
# 4. 关键是加 "/" 防止误判：如 "/a" 和 "/ab"，"/ab" 以 "/a" 开头但不是子文件夹，
#    而 "/a/b" 以 "/a/" 开头，确实是子文件夹。
#
# 时间复杂度: O(N * log N * L)，其中 N 是文件夹数量，L 是文件夹路径的平均长度。排序需要 O(N * log N * L)，遍历需要 O(N * L)。
# 空间复杂度: O(N * L)，用于排序和存储结果。
#
# 关键点:
# - 排序是关键预处理步骤，确保父文件夹在子文件夹之前出现
# - 用 `startswith(res[-1] + "/")` 而非 `startswith(res[-1])`，防止将 "/a/bc" 误判为 "/a/b" 的子文件夹
# - 只需要与结果数组中最后一个元素比较，因为排序保证了顺序
