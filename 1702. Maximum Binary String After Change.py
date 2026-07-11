"""
LeetCode #1702 - Maximum Binary String After Change
中文题名：改变后的最大二进制字符串
https://leetcode.com/problems/maximum-binary-string-after-change/

You are given a binary string `binary` consisting of only `0`'s
or `1`'s. You can apply each of the following operations any number of times:

Operation 1: If the number contains the substring `"00"`, you can
replace it with `"10"`.

For example, `"00010" -> "10010`"

Operation 2: If the number contains the substring `"10"`, you can
replace it with `"01"`.

For example, `"00010" -> "00001"`

Return the maximum binary string you can obtain after any number
of operations. Binary string `x` is greater than binary string
`y` if `x`'s decimal representation is greater than
`y`'s decimal representation.

Example 1:

Input: binary = "000110"
Output: "111011"
Explanation: A valid transformation sequence can be:
"000110" -> "000101"
"000101" -> "100101"
"100101" -> "110101"
"110101" -> "110011"
"110011" -> "111011"

Example 2:

Input: binary = "01"
Output: "01"
Explanation: "01" cannot be transformed any further.

Constraints:

`1 <= binary.length <= 105`

`binary` consist of `'0'` and `'1'`.

【中文翻译】
给定一个仅由 `'0'` 和 `'1'` 组成的二进制字符串 `binary`。
你可以无限次应用以下两种操作：

操作 1：如果字符串包含子串 `"00"`，可以将其替换为 `"10"`。
例如 `"00010" -> "10010"`

操作 2：如果字符串包含子串 `"10"`，可以将其替换为 `"01"`。
例如 `"00010" -> "00001"`

返回经过任意次操作后能得到的最大的二进制字符串。
二进制字符串 `x` 大于 `y`，如果 `x` 的十进制表示大于 `y` 的十进制表示。

示例 1：

输入: binary = "000110"
输出: "111011"
解释: 一种有效的变换序列：
"000110" -> "000101" -> "100101" -> "110101" -> "110011" -> "111011"

示例 2：

输入: binary = "01"
输出: "01"
解释: "01" 无法再变换

约束条件：

`1 <= binary.length <= 10^5`
`binary` 仅由 '0' 和 '1' 组成
"""

from typing import List, Optional


class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        """
        操作 2 ("10" -> "01") 相当于将 1 向右移动一位，而 0 向左移动一位。
        操作 1 ("00" -> "10") 将两个相邻的 0 变成一个 1 和一个 0。

        策略：将所有 1 尽量移到右边，所有 0 集中到左边变成一个 0。
        最终结果形如：一堆 1，然后一个 0，然后剩余的 1。

        具体构造：
        - 如果零的数量 <= 1，返回原字符串（无法或无需变换）
        - 否则，找到第一个 0 的位置 first_zero
        - 结果中 1 的数量 = first_zero + (zeros - 1)
        - 然后放一个 0
        - 然后放剩余的 1（即总长度 len - 前面的数量 - 1）
        """
        zeros = binary.count('0')
        n = len(binary)
        if zeros <= 1:
            return binary

        first_zero = binary.index('0')
        ones_first_part = first_zero + zeros - 1
        ones_second_part = n - ones_first_part - 1
        return '1' * ones_first_part + '0' + '1' * ones_second_part










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 分析两种操作的实质效果：
# - 操作 1: "00" -> "10"，用 1 替换了第一个 0（两个零变成一个一和一个零）
# - 操作 2: "10" -> "01"，将 1 向右移动一位（等同于 0 向左移动一位）
#
# 核心策略：
# 通过操作 2，可以把所有 1 推到右边（将左边的 0 换到右边变成 1 的前面）。
# 通过操作 1，可以把两个相邻的 0 变为 "10"，即消除一个 0。
#
# 因此，如果原始字符串有 k 个 0（k >= 2），我们可以利用操作 1 将其中 k-1 个 0
# 变为 1（每个 "00" -> "10" 消除一个 0），只剩下一个 0。
# 然后用操作 2 将这个唯一的 0 移动到尽量靠后的位置。
#
# 具体位置：0 会出现在 first_zero + (zeros - 1) 处。
# 因为第一个 0 前面有 first_zero 个 1，我们用另外 zeros-1 个（由 0 变来的）1
# 排在它前面，然后放那个唯一的 0，最后放剩下的 1。
#
# 如果 zeros <= 1，无法或不需要变换，直接返回原字符串。
#
# 时间复杂度: O(n)，需要统计 0 的个数和构造结果字符串
# 空间复杂度: O(n)，构造结果字符串
#
# 关键点:
# - 操作 2 ("10"->"01") 实际上是把 1 往右推，0 往左移
# - 最终结果只有一个 0 在中间，其余全是 1
# - 0 的位置 = first_zero + zeros - 1（first_zero 是原字符串中第一个 0 的位置）
# - 特判 zeros <= 1 的情况
