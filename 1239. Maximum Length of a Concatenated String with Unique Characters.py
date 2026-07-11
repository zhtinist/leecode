"""
LeetCode #1239 - Maximum Length of a Concatenated String with Unique Characters
中文题名：串联字符串的最大长度
https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/

Given an array of strings `arr`. String `s` is a concatenation of a
sub-sequence of `arr` which have unique characters.

Return the maximum possible length of `s`.

Example 1:

Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All possible concatenations are "","un","iq","ue","uniq" and "ique".
Maximum length is 4.

Example 2:

Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible solutions are "chaers" and "acters".

Example 3:

Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26

Constraints:

`1 <= arr.length <= 16`

`1 <= arr[i].length <= 26`

`arr[i]` contains only lower case English letters.

【中文翻译】
给定一个字符串数组 `arr`。字符串 `s` 是将 `arr` 的某个子序列中的字符串连接所得的字符串，且 `s` 中的每个字符都只出现一次。

返回 `s` 的最大可能长度。

示例 1：

输入：arr = ["un","iq","ue"]
输出：4
解释：所有可能的串联是 ""、"un"、"iq"、"ue"、"uniq" 和 "ique"。最大长度为 4。

示例 2：

输入：arr = ["cha","r","act","ers"]
输出：6
解释：可能的答案是 "chaers" 和 "acters"。

示例 3：

输入：arr = ["abcdefghijklmnopqrstuvwxyz"]
输出：26

约束条件：

`1 <= arr.length <= 16`

`1 <= arr[i].length <= 26`

`arr[i]` 仅包含小写英文字母。
"""

from typing import List, Optional


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        self.res = 0

        # Preprocess: convert each string to a bitmask, skip strings with duplicate chars
        masks = []
        for s in arr:
            mask = 0
            for ch in s:
                bit = 1 << (ord(ch) - ord('a'))
                if mask & bit:
                    mask = 0
                    break
                mask |= bit
            if mask:
                masks.append(mask)

        def dfs(idx: int, cur_mask: int):
            self.res = max(self.res, bin(cur_mask).count("1"))
            for i in range(idx, len(masks)):
                if cur_mask & masks[i] == 0:
                    dfs(i + 1, cur_mask | masks[i])

        dfs(0, 0)
        return self.res










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 回溯法（DFS）+ 位运算优化。由于 arr 长度最多为 16，可以枚举所有子序列。
# 1. 预处理：将每个字符串转为位掩码（bitmask），用 26 位表示出现了哪些字母。
#    如果字符串本身有重复字符（如 "aa"），直接丢弃，因为它不可能被包含在结果中。
# 2. 回溯：从索引 idx 开始，对于每个还未考虑过的掩码，如果它与当前掩码无交集
#    （cur_mask & masks[i] == 0），则可以选择连接它。
# 3. 每次递归都更新最大长度：当前掩码中 1 的个数（bin(cur_mask).count("1")）。
# 4. 剪枝：arr.length <= 16，最坏 2^16 = 65536 种组合，完全可以接受。
#
# 时间复杂度: O(2^N)，其中 N = len(arr) <= 16，最多 65536 种组合
# 空间复杂度: O(N)，递归栈深度最多 N
#
# 关键点:
# - 用位掩码表示字符集合，检查交集只需 `mask1 & mask2 == 0`
# - 预处理过滤掉自身有重复字符的字符串，减少分支
# - 长度用 `bin(mask).count("1")` 计算，即掩码中 1 的位数
# - N 很小（<= 16），回溯是最直接的做法；也可以用 DP 或迭代方式
