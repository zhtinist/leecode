"""
LeetCode #71 - Simplify Path
https://leetcode.com/problems/simplify-path/

You are given an absolute path for a Unix-style file system, which begins with a
slash '/'. Your task is to transform this absolute path into its simplified canonical
path.

The rules of a Unix-style file system are as follows:

- A single period '.' represents the current directory.
- A double period '..' represents the previous directory.
- Multiple consecutive slashes such as '//' or '///' are treated as a single slash '/'.
- Any sequence of periods that does not match the rules above should be treated as a
  valid directory or file name. For example, '...' and '....' are valid directory
  or file names.
- The simplified canonical path should follow these rules:
    - The path starts with a single slash '/'.
    - Directories in the path are separated by a single slash '/'.
    - The path does not end with a trailing slash '/', unless it is the root directory.
    - The path only contains single periods '.', not double periods '..'.

Example 1:
    Input: path = "/home/"
    Output: "/home"
    Explanation: The trailing slash should be removed.

Example 2:
    Input: path = "/home//foo/"
    Output: "/home/foo"
    Explanation: Multiple consecutive slashes are replaced by a single one.

Example 3:
    Input: path = "/home/user/Documents/../Pictures"
    Output: "/home/user/Pictures"
    Explanation: A double period ".." refers to the directory up a level.

Example 4:
    Input: path = "/../"
    Output: "/"
    Explanation: Going one level up from the root directory is not possible.

Example 5:
    Input: path = "/.../a/../b/c/../d/./"
    Output: "/.../b/d"
    Explanation: "..." is a valid name for a directory in this problem.

Constraints:
    1 <= path.length <= 3000
    path consists of English letters, digits, period '.', slash '/', or '_'.
    path is a valid absolute Unix path.
"""


class Solution:
    def simplifyPath(self, path: str) -> str:
        pass
