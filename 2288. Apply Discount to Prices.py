"""
LeetCode #2288 - Apply Discount to Prices
价格减免
https://leetcode.cn/problems/apply-discount-to-prices/

句子 是由若干个单词组成的字符串，单词之间用单个空格分隔，其中每个单词可以包含数字、小写字母、和美元符号 `'$'` 。如果单词的形式为美元符号后跟着一个非负实数，那么这个单词就表示一个 价格 。
例如 `"$100"`、`"$23"` 和 `"$6"` 表示价格，而 `"100"`、`"$"` 和 `"$1e5` 不是。
给你一个字符串 `sentence` 表示一个句子和一个整数 `discount` 。对于每个表示价格的单词，都在价格的基础上减免 `discount%` ，并 更新 该单词到句子中。所有更新后的价格应该表示为一个 恰好保留小数点后两位 的数字。
返回表示修改后句子的字符串。
注意：所有价格 最多 为 `10` 位数字。

示例 1：
输入：sentence = "there are $1 $2 and 5$ candies in the shop", discount = 50 输出："there are $0.50 $1.00 and 5$ candies in the shop" 解释： 表示价格的单词是 "$1" 和 "$2" 。  - "$1" 减免 50% 为 "$0.50" ，所以 "$1" 替换为 "$0.50" 。 - "$2" 减免 50% 为 "$1" ，所以 "$2" 替换为 "$1.00" 。
示例 2：
输入：sentence = "1 2 $3 4 $5 $6 7 8$ $9 $10$", discount = 100 输出："1 2 $0.00 4 $0.00 $0.00 7 8$ $0.00 $10$" 解释： 任何价格减免 100% 都会得到 0 。 表示价格的单词分别是 "$3"、"$5"、"$6" 和 "$9"。 每个单词都替换为 "$0.00"。

提示：
`1 <= sentence.length <= 10^5`
`sentence` 由小写英文字母、数字、`' '` 和 `'$'` 组成
`sentence` 不含前导和尾随空格
`sentence` 的所有单词都用单个空格分隔
所有价格都是 正 整数且不含前导零
所有价格 最多 为  `10` 位数字
`0 <= discount <= 100`
"""

from typing import List, Optional


class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        """
        Parse each word in the sentence. If a word is a valid price (starts
        with '$' followed by digits only), apply the discount and reformat
        to two decimal places. Otherwise keep the word unchanged.
        """
        words = sentence.split(' ')
        factor = (100 - discount) / 100

        for i, word in enumerate(words):
            if self._is_price(word):
                price = int(word[1:])  # all prices are positive integers
                discounted = price * factor
                words[i] = f"${discounted:.2f}"

        return ' '.join(words)

    def _is_price(self, word: str) -> bool:
        """Check if word is a valid price: starts with '$' followed by digits."""
        if len(word) < 2 or word[0] != '$':
            return False
        # All remaining characters must be digits
        return word[1:].isdigit()


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: String
#
# 解题思路:
# 1. 将句子按空格分割成单词列表。
# 2. 遍历每个单词，检查是否为有效价格：以 '$' 开头，且后续字符全为数字。
# 3. 对有效价格应用折扣：discounted = original * (100 - discount) / 100。
# 4. 使用 f"${discounted:.2f}" 格式化输出，保留两位小数。
# 5. 对非价格单词保持原样。最后用空格连接所有单词返回。
#
# 时间复杂度: O(N)，N 为句子长度。分割 O(N)，遍历检查 O(N)
# 空间复杂度: O(N)，用于存储分割后的单词列表
#
# 关键点:
# - 有效价格的判断：必须以 '$' 开头，后续全是数字（isdigit()），避免 "$"、"$1e5"、"5$" 等情况
# - 格式化输出：使用 f"${value:.2f}" 确保恰好两位小数
# - 所有价格都是正整数，所以可以用 int() 转换后计算
