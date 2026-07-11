"""
LeetCode #3889 - Mirror Frequency Distance
镜像频次距离
https://leetcode.cn/problems/mirror-frequency-distance/

给你一个由小写英文字母和数字组成的字符串 `s`。
对于每个字符，其 镜像字符 根据逆序定义其字符集合：
对于字母，某字符的镜像字符是字母表中从末尾与其位置相同的字母。
例如，`'a'` 的镜像字符是 `'z'`，`'b'` 的镜像字符是 `'y'`，以此类推。
对于数字，某字符的镜像字符是范围 `'0'` 到 `'9'` 中从末尾与其位置相同的数字。
例如，`'0'` 的镜像字符是 `'9'`，`'1'` 的镜像字符是 `'8'`，以此类推。
对于字符串中每个 唯一 字符 `c`：
设 `m` 为其 镜像字符 。
设 `freq(x)` 表示字符 `x` 在字符串中出现的次数。
计算其与镜像字符出现次数之间的 绝对差，定义为：`|freq(c) - freq(m)|`
镜像对 `(c, m)` 和 `(m, c)` 被视为相同，只能被计算 一次 。
返回一个整数，表示所有这些 不同的镜像对 的绝对差之和。

示例 1：

输入： s = "ab1z9"
输出： 3
解释：
对于每个镜像对：   	 		 			`c` 			`m` 			`freq(c)` 			`freq(m)` 			`|freq(c) - freq(m)|` 		 	 	 		 			a 			z 			1 			1 			0 		 		 			b 			y 			1 			0 			1 		 		 			1 			8 			1 			0 			1 		 		 			9 			0 			1 			0 			1
因此，答案是 `0 + 1 + 1 + 1 = 3`。
示例 2：

输入： s = "4m7n"
输出： 2
解释：   	 		 			`c` 			`m` 			`freq(c)` 			`freq(m)` 			`|freq(c) - freq(m)|` 		 	 	 		 			4 			5 			1 			0 			1 		 		 			m 			n 			1 			1 			0 		 		 			7 			2 			1 			0 			1
因此，答案是 `1 + 0 + 1 = 2`。
示例 3：

输入：s = "byby"
输出：0
解释：   	 		 			`c` 			`m` 			`freq(c)` 			`freq(m)` 			`|freq(c) - freq(m)|` 		 	 	 		 			b 			y 			2 			2 			0
因此，答案是 0 。

提示:
`1 <= s.length <= 5 * 10^5`
`s` 仅由小写英文字母和数字组成。
"""

from typing import List, Optional


class Solution:
    def mirrorFrequencyDistance(self, s: str) -> int:
        from collections import Counter

        freq = Counter(s)

        def mirror(ch: str) -> str:
            if 'a' <= ch <= 'z':
                # 字母镜像: a<->z, b<->y, ...
                return chr(ord('a') + ord('z') - ord(ch))
            else:
                # 数字镜像: 0<->9, 1<->8, ...
                return chr(ord('0') + ord('9') - ord(ch))

        ans = 0
        seen = set()
        for c in freq:
            m = mirror(c)
            # 使用有序对 (min, max) 去重，确保每个镜像对只计算一次
            # 不能仅用 c <= m 去重：例如 '9' 的镜像是 '0'，'9'>'0' 会被跳过，
            # 若 '0' 不在字符串中则 (9,0) 永远不被计算
            pair = (c, m) if c <= m else (m, c)
            if pair not in seen:
                seen.add(pair)
                ans += abs(freq[c] - freq.get(m, 0))

        return ans










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Hash Table, String, Counting
#
# 解题思路:
# 1. 使用哈希表 Counter 统计字符串中每个字符的出现频次。
# 2. 定义镜像函数 mirror(ch)：
#    - 字母：a<->z, b<->y, ...，满足 ord(c) + ord(m) = ord('a') + ord('z')
#    - 数字：0<->9, 1<->8, ...，满足 ord(c) + ord(m) = ord('0') + ord('9')
# 3. 遍历所有出现过的唯一字符 c，找到其镜像字符 m = mirror(c)。
# 4. 去重条件：使用 seen 集合存储已处理的有序对 (min(c,m), max(c,m))，
#    确保 (c, m) 和 (m, c) 只被计算一次。不能仅用 c <= m 字典序去重，
#    因为当镜像字符不在字符串中时，较大的字符会被错误跳过（如 '9'>'0'，'0'不在串中则丢失）。
# 5. 计算 |freq[c] - freq[m]|，若镜像字符不在字符串中则频次视为 0。
# 6. 累加所有差值，返回总和。
#
# 时间复杂度: O(n) — 遍历字符串统计频次 O(n)，遍历唯一字符集 O(1)（最多 36 种字符）
# 空间复杂度: O(1) — 字符集仅包含 26 个小写字母和 10 个数字，Counter 大小恒定
#
# 关键点:
# - 镜像映射的核心公式：ord(镜像字符) = ord(基准起点) + ord(基准终点) - ord(原字符)
# - 去重技巧：使用 seen 集合存储有序对 (min(c,m), max(c,m))，确保不重不漏
# - 简单地用 c <= mirror(c) 判断去重存在缺陷：当镜像字符不在字符串中时，字典序较大的字符会被错误跳过
# - 未出现的镜像字符频次为 0，使用 freq.get(m, 0) 处理
