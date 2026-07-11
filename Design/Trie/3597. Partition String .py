"""
LeetCode #3597 - Partition String 
分割字符串
https://leetcode.cn/problems/partition-string/

给你一个字符串 `s`，按照以下步骤将其分割为 互不相同的段 ：
从下标 0 开始构建一个段。
逐字符扩展当前段，直到该段之前未曾出现过。
只要当前段是唯一的，就将其加入段列表，标记为已经出现过，并从下一个下标开始构建新的段。
重复上述步骤，直到处理完整个字符串 `s`。
返回字符串数组 `segments`，其中 `segments[i]` 表示创建的第 `i` 段。

示例 1：

输入： s = "abbccccd"
输出： ["a","b","bc","c","cc","d"]
解释：   	 		 			下标 			添加后的段 			已经出现过的段 			当前段是否已经出现过？ 			新段 			更新后已经出现过的段 		 		 			0 			"a" 			[] 			否 			"" 			["a"] 		 		 			1 			"b" 			["a"] 			否 			"" 			["a", "b"] 		 		 			2 			"b" 			["a", "b"] 			是 			"b" 			["a", "b"] 		 		 			3 			"bc" 			["a", "b"] 			否 			"" 			["a", "b", "bc"] 		 		 			4 			"c" 			["a", "b", "bc"] 			否 			"" 			["a", "b", "bc", "c"] 		 		 			5 			"c" 			["a", "b", "bc", "c"] 			是 			"c" 			["a", "b", "bc", "c"] 		 		 			6 			"cc" 			["a", "b", "bc", "c"] 			否 			"" 			["a", "b", "bc", "c", "cc"] 		 		 			7 			"d" 			["a", "b", "bc", "c", "cc"] 			否 			"" 			["a", "b", "bc", "c", "cc", "d"]
因此，最终输出为 `["a", "b", "bc", "c", "cc", "d"]`。
示例 2：

输入： s = "aaaa"
输出： ["a","aa"]
解释：   	 		 			下标 			添加后的段 			已经出现过的段 			当前段是否已经出现过？ 			新段 			更新后已经出现过的段 		 		 			0 			"a" 			[] 			否 			"" 			["a"] 		 		 			1 			"a" 			["a"] 			是 			"a" 			["a"] 		 		 			2 			"aa" 			["a"] 			否 			"" 			["a", "aa"] 		 		 			3 			"a" 			["a", "aa"] 			是 			"a" 			["a", "aa"]
因此，最终输出为 `["a", "aa"]`。

提示：
`1 <= s.length <= 10^5`
`s` 仅包含小写英文字母。
"""

from typing import List, Optional


class Solution:
    def partitionString(self, s: str) -> List[str]:
        segments = []
        seen = set()
        i = 0
        n = len(s)

        while i < n:
            # Build segment starting at i, extending character by character
            j = i
            while j < n:
                current = s[i:j + 1]
                if current not in seen:
                    # Unique segment found
                    segments.append(current)
                    seen.add(current)
                    i = j + 1
                    break
                j += 1
            else:
                # Reached end of string but the last segment
                # has been seen before; just stop
                break

        return segments











# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Trie, Hash Table, String, Simulation
#
# 解题思路:
# 按照题目描述的步骤直接模拟分割过程：
# 1. 从下标 0 开始构建当前段。
# 2. 逐字符扩展当前段，检查是否已经出现过（在 seen 集合中）。
# 3. 如果当前段未曾出现过，将其加入结果列表和 seen 集合，
#    然后从下一个下标开始构建新的段。
# 4. 如果当前段已经出现过，继续扩展（加入下一个字符）再检查。
# 5. 重复直到处理完整个字符串。如果遍历结束时仍无法形成新段，则停止。
#
# 时间复杂度: O(N * sqrt(N))，最坏情况下（全相同字符如 "aaaa..."）
#   段的数量约为 O(sqrt(N))，每段形成的子串总长度也为 O(sqrt(N))
# 空间复杂度: O(N)，存储 seen 集合中的段和结果列表
#
# 关键点:
# - 模拟过程严格按照题目要求：逐字符扩展，首次遇到未见过的段就截断
# - 使用集合存储已出现的段，O(1) 查找
# - 当剩余字符构成的段都已出现过且无法再扩展时，自然结束
