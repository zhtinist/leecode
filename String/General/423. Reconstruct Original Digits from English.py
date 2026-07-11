"""
LeetCode #423 - Reconstruct Original Digits from English
中文题名：从英文中重建数字
https://leetcode.com/problems/reconstruct-original-digits-from-english/

Given a non-empty string containing an out-of-order English representation of digits
`0-9`, output the digits in ascending order.

Note:

Input contains only lowercase English letters.

Input is guaranteed to be valid and can be transformed to its original digits. That
means invalid inputs such as "abc" or "zerone" are not permitted.

Input length is less than 50,000.

Example 1:

Input: "owoztneoer"

Output: "012"

Example 2:

Input: "fviefuro"

Output: "45"

【中文翻译】
给定一个非空字符串，包含乱序的英文数字 0-9 的字母表示，按升序输出数字。

注意：
    输入仅包含小写英文字母。
    输入保证有效，可以转换为原始数字。不允许 "abc" 或 "zerone" 等无效输入。
    输入长度小于 50,000。

示例 1：
    输入："owoztneoer"
    输出："012"

示例 2：
    输入："fviefuro"
    输出："45"
"""

from typing import List, Optional


class Solution:
    def originalDigits(self, s: str) -> str:
        # Count each letter
        from collections import Counter
        count = Counter(s)

        # Digits with unique letters:
        # zero -> z, two -> w, four -> u, six -> x, eight -> g
        digits = [0] * 10

        digits[0] = count["z"]                                  # zero
        digits[2] = count["w"]                                  # two
        digits[4] = count["u"]                                  # four
        digits[6] = count["x"]                                  # six
        digits[8] = count["g"]                                  # eight

        # Remaining digits derived from letters not in above:
        digits[3] = count["h"] - digits[8]                      # three (h is in eight and three)
        digits[5] = count["f"] - digits[4]                      # five (f is in four and five)
        digits[7] = count["s"] - digits[6]                      # seven (s is in six and seven)

        # Further derivations:
        digits[1] = count["o"] - digits[0] - digits[2] - digits[4]  # one
        digits[9] = count["i"] - digits[5] - digits[6] - digits[8]  # nine

        result = []
        for d in range(10):
            result.append(str(d) * digits[d])

        return "".join(result)


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 利用每个数字英文单词中的唯一字母来逐步推导。
#
# 第一阶段——使用唯一标识字母直接确定数量：
#   zero 由 z 唯一标识   → digits[0]
#   two  由 w 唯一标识   → digits[2]
#   four 由 u 唯一标识   → digits[4]
#   six  由 x 唯一标识   → digits[6]
#   eight 由 g 唯一标识  → digits[8]
#
# 第二阶段——利用已有数字推导：
#   three = h总数 - eight（h 只有 eight 和 three 有）
#   five  = f总数 - four（f 只有 four 和 five 有）
#   seven = s总数 - six（s 只有 six 和 seven 有）
#
# 第三阶段——进一步推导：
#   one   = o总数 - zero - two - four
#   nine  = i总数 - five - six - eight
#
# 最后按 0-9 的顺序拼接结果。
#
# 时间复杂度: O(N) — 遍历字符串统计 + 常数时间计算
# 空间复杂度: O(1) — 计数器和结果数组都是固定大小
#
# 关键点:
# - 利用每个数字单词中的"唯一字母"作为识别指纹
# - 按正确的依赖顺序处理数字（先处理有唯一字母的，再推导其他的）
# - z(0), w(2), u(4), x(6), g(8) 是第一阶段唯一标识
