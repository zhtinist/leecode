"""
LeetCode #3639 - Minimum Time to Activate String
变为活跃状态的最小时间
https://leetcode.cn/problems/minimum-time-to-activate-string/

给你一个长度为 `n` 的字符串 `s` 和一个整数数组 `order`，其中 `order` 是范围 `[0, n - 1]` 内数字的一个 排列。
从时间 `t = 0` 开始，在每个时间点，将字符串 `s` 中下标为 `order[t]` 的字符替换为 `'*'`。
如果 子字符串 包含 至少 一个 `'*'` ，则认为该子字符串有效。
如果字符串中 有效子字符串 的总数大于或等于 `k`，则称该字符串为 活跃 字符串。
返回字符串 `s` 变为 活跃 状态的最小时间 `t`。如果无法变为活跃状态，返回 -1。

示例 1:

输入: s = "abc", order = [1,0,2], k = 2
输出: 0
解释:   	 		 			`t` 			`order[t]` 			修改后的 `s` 			有效子字符串 			计数 			激活状态
(计数 >= k) 		 	 	 		 			0 			1 			`"a*c"` 			`"*"`, `"a*"`, `"*c"`, `"a*c"` 			4 			是
字符串 `s` 在 `t = 0` 时变为激活状态。因此，答案是 0。
示例 2:

输入: s = "cat", order = [0,2,1], k = 6
输出: 2
解释:   	 		 			`t` 			`order[t]` 			修改后的 `s` 			有效子字符串 			计数 			激活状态
(计数 >= k) 		 	 	 		 			0 			0 			`"*at"` 			`"*"`, `"*a"`, `"*at"` 			3 			否 		 		 			1 			2 			`"*a*"` 			`"*"`, `"*a"`, `"*a*"`, `"a*"`, `"*"` 			5 			否 		 		 			2 			1 			`"***"` 			所有子字符串(包含 `'*'`) 			6 			是
字符串 `s` 在 `t = 2` 时变为激活状态。因此，答案是 2。
示例 3:

输入: s = "xy", order = [0,1], k = 4
输出: -1
解释:
即使完成所有替换，也无法得到 `k = 4` 个有效子字符串。因此，答案是 -1。

提示:
`1 <= n == s.length <= 10^5`
`order.length == n`
`0 <= order[i] <= n - 1`
`s` 由小写英文字母组成。
`order` 是从 0 到 `n - 1` 的整数排列。
`1 <= k <= 10^9`
"""

from typing import List, Optional


class Solution:
    def minTime(self, s: str, order: List[int], k: int) -> int:
        n = len(s)
        total_substrings = n * (n + 1) // 2

        def count_valid(t: int) -> int:
            """返回时间 t (0-indexed) 时的有效子字符串数量"""
            activated = [False] * n
            for i in range(t + 1):
                activated[order[i]] = True

            invalid = 0
            seg_len = 0
            for i in range(n):
                if activated[i]:
                    invalid += seg_len * (seg_len + 1) // 2
                    seg_len = 0
                else:
                    seg_len += 1
            invalid += seg_len * (seg_len + 1) // 2

            return total_substrings - invalid

        lo, hi = 0, n - 1
        ans = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if count_valid(mid) >= k:
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1

        return ans










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Binary Search
#
# 解题思路:
# 对时间 t 进行二分查找（0 到 n-1）。对于给定的 t，将 order[0..t] 位置的字符
# 标记为 '*'，然后计算含至少一个 '*' 的子字符串数量。
# 计算方法：总数 = n*(n+1)/2；不合法子字符串 = 所有不含 '*' 的连续段中
# 长度为 L 的段贡献 L*(L+1)/2 个；有效 = 总数 - 不合法。
# 如果 count_valid(mid) >= k，记录答案并搜索左半区间，否则搜索右半区间。
#
# 时间复杂度: O(n log n) — 二分 log n 次，每次 O(n) 统计
# 空间复杂度: O(n) — 激活标记数组
#
# 关键点:
# - 有效子字符串 = 总子字符串 - 不含 '*' 的子字符串
# - 不含 '*' 的连续段长度为 L，其不含 '*' 的子字符串数为 L*(L+1)/2
# - 二分查找最小满足条件的 t
