"""
LeetCode #247 - Strobogrammatic Number II
中文题名：中心对称数 II
https://leetcode.com/problems/strobogrammatic-number-ii/

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at
upside down).

Find all strobogrammatic numbers that are of length = n.

Example:

Input:  n = 2
Output: `["11","69","88","96"]`

【中文翻译】
中心对称数是指一个数字在 180 度旋转（上下颠倒）后，看起来和原数字一样。

找出所有长度为 n 的中心对称数。

示例：

输入：n = 2
输出：`["11","69","88","96"]`
"""

from typing import List, Optional


class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        # 可用的旋转数字对
        pairs = [('0', '0'), ('1', '1'), ('6', '9'), ('8', '8'), ('9', '6')]

        def helper(m: int) -> List[str]:
            """生成长度为 m 的所有 strobogrammatic 数"""
            if m == 0:
                return [""]
            if m == 1:
                return ["0", "1", "8"]

            # 递归生成长度为 m-2 的内部结果
            inner = helper(m - 2)
            res = []
            for left, right in pairs:
                for mid in inner:
                    # 首尾不能为 '0'（除非 n==1，已在上面处理）
                    res.append(left + mid + right)
            return res

        if n == 1:
            return ["0", "1", "8"]

        # 排除以 '0' 开头的结果（长度 > 1 时）
        all_nums = helper(n)
        return [s for s in all_nums if s[0] != '0']


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: Yes
#
# 解题思路：
# 使用递归构造。对于长度为 n，在两端对称地添加有效的数字对
# (0,0), (1,1), (6,9), (8,8), (9,6)，中间递归构造长度为 n-2 的结果。
# 基础情况: n=0 返回 [""]，n=1 返回 ["0","1","8"]。
# 最后过滤掉以 '0' 开头的结果（长度 > 1 时不允许前导零）。
#
# 时间复杂度: O(5^(n/2)) — 每一步有 5 种配对选择
# 空间复杂度: O(n * 5^(n/2)) — 存储所有结果，每串长 n
#
# 关键点：
# - 递归构造，每次在两端添加对称字符
# - n=0 返回空字符串作为递归基础
# - 最后排除前导零
