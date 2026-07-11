"""
LeetCode #3234 - Count the Number of Substrings With Dominant Ones
统计 1 显著的字符串的数量
https://leetcode.cn/problems/count-the-number-of-substrings-with-dominant-ones/

给你一个二进制字符串 `s`。
请你统计并返回其中 1 显著  的 子字符串 的数量。
如果字符串中 1 的数量 大于或等于 0 的数量的 平方，则认为该字符串是一个 1 显著 的字符串 。

示例 1：

输入：s = "00011"
输出：5
解释：
1 显著的子字符串如下表所示。    	 		 			i 			j 			s[i..j] 			0 的数量 			1 的数量 		 	 	 		 			3 			3 			1 			0 			1 		 		 			4 			4 			1 			0 			1 		 		 			2 			3 			01 			1 			1 		 		 			3 			4 			11 			0 			2 		 		 			2 			4 			011 			1 			2
示例 2：

输入：s = "101101"
输出：16
解释：
1 不显著的子字符串如下表所示。
总共有 21 个子字符串，其中 5 个是 1 不显著字符串，因此有 16 个 1 显著子字符串。    	 		 			i 			j 			s[i..j] 			0 的数量 			1 的数量 		 	 	 		 			1 			1 			0 			1 			0 		 		 			4 			4 			0 			1 			0 		 		 			1 			4 			0110 			2 			2 		 		 			0 			4 			10110 			2 			3 		 		 			1 			5 			01101 			2 			3

提示：
`1 <= s.length <= 4 * 10^4`
`s` 仅包含字符 `'0'` 和 `'1'`。
"""

from typing import List, Optional


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        import math
        import bisect
        n = len(s)
        zeros = [i for i, ch in enumerate(s) if ch == '0']
        # 前缀和：pref[i] = s[0..i-1] 中 1 的个数
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + (1 if s[i] == '1' else 0)

        ans = 0
        max_k = int(math.isqrt(n))  # 最大需要考虑的 0 的数量

        for i in range(n):
            # 找到 i 及之后第一个 0 的位置
            idx = bisect.bisect_left(zeros, i)
            # k = 0：不含 0 的子串，只要 ones >= 0 即可（恒成立）
            r_max = zeros[idx] - 1 if idx < len(zeros) else n - 1
            if r_max >= i:
                ans += r_max - i + 1

            # k = 1..max_k
            for k in range(1, max_k + 1):
                if idx + k - 1 >= len(zeros):
                    break
                need_ones = k * k
                # 第 k 个 0 的位置（从 i 开始数）
                kth_zero = zeros[idx + k - 1]
                # 右边界最大为下一个 0 之前
                if idx + k < len(zeros):
                    r_max = zeros[idx + k] - 1
                else:
                    r_max = n - 1
                # 需要 ones[i..r] >= need_ones
                # pref[r+1] - pref[i] >= need_ones
                need = pref[i] + need_ones
                lo, hi = kth_zero, r_max
                r_min = r_max + 1  # 默认无解
                while lo <= hi:
                    mid = (lo + hi) // 2
                    if pref[mid + 1] >= need:
                        r_min = mid
                        hi = mid - 1
                    else:
                        lo = mid + 1
                if r_min <= r_max:
                    ans += r_max - r_min + 1

        return ans










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: String, Enumeration
#
# 解题思路:
# 核心条件 ones >= zeros^2。由于 zeros^2 增长很快，任何有效子串中 zeros <= sqrt(n)。
# 因此可以枚举子串中 0 的个数 k（0 到 sqrt(n)）。
# 对每个左边界 i，找到其后第 k 个 0 的位置：
# - 右边界必须 >= 第 k 个 0（确保恰好包含 k 个零）
# - 右边界必须 < 第 k+1 个 0（确保不包含更多零）
# - 同时需要 ones[i..r] >= k^2，二分查找满足条件的最小 r
# 满足条件的 r 的数量 = r_max - r_min + 1，累加到答案。
#
# 时间复杂度: O(n * sqrt(n) * log n)
# 空间复杂度: O(n)
#
# 关键点:
# - 0 的个数被限制在 sqrt(n) 以内，大幅减少需要枚举的范围
# - 使用前缀和 + 二分查找快速定位满足 ones 条件的右边界
