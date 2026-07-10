"""
LeetCode #299 - Bulls and Cows
中文题名：猜数字游戏
https://leetcode.com/problems/bulls-and-cows/

You are playing the following Bulls and Cows game with your friend:
You write down a number and ask your friend to guess what the number is. Each time your
friend makes a guess, you provide a hint that indicates how many digits in said guess match
your secret number exactly in both digit and position (called "bulls") and how
many digits match the secret number but locate in the wrong position (called "cows").
Your friend will use successive guesses and hints to eventually derive the secret number.

Write a function to return a hint according to the secret number and friend's guess, use
`A` to indicate the bulls and `B` to indicate the cows.

Please note that both secret number and friend's guess may contain duplicate digits.

Example 1:

Input: secret = "1807", guess = "7810"

Output: "1A3B"

Explanation: `1` bull and `3` cows. The bull is `8`, the cows are `0`, `1` and `7.`

Example 2:

Input: secret = "1123", guess = "0111"

Output: "1A1B"

Explanation: The 1st `1 `in friend's guess is a bull, the 2nd or 3rd `1` is a cow.

Note: You may assume that the secret number and your friend's guess only
contain digits, and their lengths are always equal.

【中文翻译】
你正在和你的朋友玩 Bulls and Cows（猜数字）游戏。你写出一个数字，让你的朋友猜。每次朋友猜测时，你会给出一个提示，告诉朋友猜测的数字中有多少位数字和位置都完全匹配（称为「Bulls，公牛」），有多少位数字匹配但位置错误（称为「Cows，母牛」）。朋友会根据连续的猜测和提示最终猜出秘密数字。

编写一个函数，根据秘密数字和朋友的猜测，返回提示。用 `A` 表示 Bulls，用 `B` 表示 Cows。

请注意，秘密数字和朋友的猜测都可能包含重复数字。

示例 1：

输入：secret = "1807", guess = "7810"

输出："1A3B"

解释：`1` 个 Bulls 和 `3` 个 Cows。Bulls 是 `8`，Cows 是 `0`、`1` 和 `7`。

示例 2：

输入：secret = "1123", guess = "0111"

输出："1A1B"

解释：朋友猜测中第 1 个 `1` 是 Bulls，第 2 个或第 3 个 `1` 是 Cows。

注意：你可以假设秘密数字和朋友的猜测只包含数字，且长度始终相等。
"""

from typing import List, Optional


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        """Return hint in the format "xAyB" where x = bulls, y = cows.

        Bulls: same digit at same position.
        Cows: same digit at different position (not already counted as bulls).

        Two-pass approach:
        Pass 1: Count bulls and record unmatched digits.
        Pass 2 (or combined): Count cows from unmatched digits.
        """
        bulls = 0
        cows = 0
        # Count occurrences of digits 0-9 in unmatched positions
        secret_count = [0] * 10
        guess_count = [0] * 10

        for s_ch, g_ch in zip(secret, guess):
            if s_ch == g_ch:
                bulls += 1
            else:
                secret_count[int(s_ch)] += 1
                guess_count[int(g_ch)] += 1

        # Cows = sum of min(secret_count[i], guess_count[i]) for each digit
        for i in range(10):
            cows += min(secret_count[i], guess_count[i])

        return f"{bulls}A{cows}B"


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 两遍扫描法。
# 第一遍：扫描所有位置，如果同一位置字符相同，则是一个 bull (A)。
# 如果不相同，则将 secret 和 guess 中该位置的字符分别计数。
# 第二遍：对于 0-9 的每个数字，其在 cows 中的贡献是
# min(secret_count[i], guess_count[i])，即两者中都出现的次数
# （但不包括已经匹配为 bull 的位置）。
# 最终返回格式 "xAyB"。
#
# 时间复杂度: O(N) - 一次遍历
# 空间复杂度: O(1) - 两个大小为 10 的数组
#
# 关键点:
# - Bulls 优先：同一位置相同字符
# - 排除 bulls 后再统计 cows
# - Cows 的计算：对每个数字取 secret 和 guess 中出现的较小值
# - 因为数字只有 0-9，用大小为 10 的数组比哈希表更高效
