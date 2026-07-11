"""
LeetCode #2109 - Adding Spaces to a String
向字符串添加空格
https://leetcode.cn/problems/adding-spaces-to-a-string/

给你一个下标从 0 开始的字符串 `s` ，以及一个下标从 0 开始的整数数组 `spaces` 。
数组 `spaces` 描述原字符串中需要添加空格的下标。每个空格都应该插入到给定索引处的字符值 之前 。
例如，`s = "EnjoyYourCoffee"` 且 `spaces = [5, 9]` ，那么我们需要在 `'Y'` 和 `'C'` 之前添加空格，这两个字符分别位于下标 `5` 和下标 `9` 。因此，最终得到 `"Enjoy Your Coffee"` 。
请你添加空格，并返回修改后的字符串。

示例 1：
输入：s = "LeetcodeHelpsMeLearn", spaces = [8,13,15] 输出："Leetcode Helps Me Learn" 解释： 下标 8、13 和 15 对应 "LeetcodeHelpsMeLearn" 中加粗斜体字符。 接着在这些字符前添加空格。
示例 2：
输入：s = "icodeinpython", spaces = [1,5,7,9] 输出："i code in py thon" 解释： 下标 1、5、7 和 9 对应 "icodeinpython" 中加粗斜体字符。 接着在这些字符前添加空格。
示例 3：
输入：s = "spacing", spaces = [0,1,2,3,4,5,6] 输出：" s p a c i n g" 解释： 字符串的第一个字符前可以添加空格。

提示：
`1 <= s.length <= 3 * 10^5`
`s` 仅由大小写英文字母组成
`1 <= spaces.length <= 3 * 10^5`
`0 <= spaces[i] <= s.length - 1`
`spaces` 中的所有值 严格递增
"""

from typing import List, Optional


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = []
        space_idx = 0
        for i, ch in enumerate(s):
            if space_idx < len(spaces) and i == spaces[space_idx]:
                result.append(' ')
                space_idx += 1
            result.append(ch)
        return ''.join(result)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Two Pointers, String, Simulation
#
# 解题思路:
# 遍历字符串s的每个字符，同时维护一个指针 space_idx 指向 spaces 数组中下一个要插入空格的位置。
# 当遍历到的索引 i 等于 spaces[space_idx] 时，先在结果中插入一个空格，再添加当前字符。
# 由于 spaces 数组严格递增，可以线性单次遍历完成。
# 使用列表收集结果字符最后 join，避免多次字符串拼接带来的 O(N^2) 开销。
#
# 时间复杂度: O(N + M)，其中N为字符串长度，M为spaces数组长度。一次遍历即可。
# 空间复杂度: O(N + M)，结果字符串和中间列表的长度。
#
# 关键点:
# - spaces数组严格递增，因此可以用单指针顺序匹配。
# - 使用列表 append 而非字符串拼接，提高效率。
# - 空格插入在指定索引的字符之前。
