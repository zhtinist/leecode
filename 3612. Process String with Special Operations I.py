"""
LeetCode #3612 - Process String with Special Operations I
用特殊操作处理字符串 I
https://leetcode.cn/problems/process-string-with-special-operations-i/

给你一个字符串 `s`，它由小写英文字母和特殊字符：`*`、`#` 和 `%` 组成。
请根据以下规则从左到右处理 `s` 中的字符，构造一个新的字符串 `result`：
如果字符是 小写 英文字母，则将其添加到 `result` 中。
字符 `'*'` 会 删除 `result` 中的最后一个字符（如果存在）。
字符 `'#'` 会 复制 当前的 `result` 并 追加 到其自身后面。
字符 `'%'` 会 反转 当前的 `result`。
在处理完 `s` 中的所有字符后，返回最终的字符串 `result`。

示例 1：

输入： s = "a#b%*"
输出： "ba"
解释：   	 		 			`i` 			`s[i]` 			操作 			当前 `result` 		 	 	 		 			0 			`'a'` 			添加 `'a'` 			`"a"` 		 		 			1 			`'#'` 			复制 `result` 			`"aa"` 		 		 			2 			`'b'` 			添加 `'b'` 			`"aab"` 		 		 			3 			`'%'` 			反转 `result` 			`"baa"` 		 		 			4 			`'*'` 			删除最后一个字符 			`"ba"`
因此，最终的 `result` 是 `"ba"`。
示例 2：

输入： s = "z*#"
输出： ""
解释：   	 		 			`i` 			`s[i]` 			操作 			当前 `result` 		 	 	 		 			0 			`'z'` 			添加 `'z'` 			`"z"` 		 		 			1 			`'*'` 			删除最后一个字符 			`""` 		 		 			2 			`'#'` 			复制字符串 			`""`
因此，最终的 `result` 是 `""`。

提示:
`1 <= s.length <= 20`
`s` 只包含小写英文字母和特殊字符 `*`、`#` 和 `%`。
"""

from typing import List, Optional


class Solution:
    def processString(self, s: str) -> str:
        result = []
        for ch in s:
            if 'a' <= ch <= 'z':  # lowercase letter
                result.append(ch)
            elif ch == '*':
                if result:
                    result.pop()
            elif ch == '#':
                result = result + result  # duplicate
            elif ch == '%':
                result.reverse()  # reverse in place
        return ''.join(result)










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: String, Simulation
#
# 解题思路:
# 按照题目规则从左到右模拟处理字符串：
# - 小写字母：直接追加到 result 列表末尾
# - '*'（退格）：删除 result 的最后一个字符（如果非空）
# - '#'（复制）：将当前 result 复制一份追加到自身后面（result = result + result）
# - '%'（反转）：将 result 原地反转
# 使用 list 处理而非字符串拼接，因为 list.pop() 和 list.reverse() 都是 O(1) 或 O(N) 的高效操作。
# 由于 s.length <= 20，最坏情况下 '#' 使字符串长度翻倍，最终长度不超过 2^20 ≈ 10^6，完全可处理。
#
# 时间复杂度: O(2^N) 最坏情况（全为 '#' 操作），N <= 20，上限约 10^6 次操作
# 空间复杂度: O(2^N) — result 列表的最大长度
#
# 关键点:
# - 使用 list 而非字符串拼接以获得 O(1) 的 pop 操作
# - '#' 复制操作：result = result + result 创建新列表
# - '%' 反转：list.reverse() 原地操作
# - 边界情况：'*' 在 result 为空时无效
