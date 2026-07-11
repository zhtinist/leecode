"""
LeetCode #2024 - Maximize the Confusion of an Exam
考试的最大困扰度
https://leetcode.cn/problems/maximize-the-confusion-of-an-exam/

一位老师正在出一场由 `n` 道判断题构成的考试，每道题的答案为 true （用 `'T'` 表示）或者 false （用 `'F'` 表示）。老师想增加学生对自己做出答案的不确定性，方法是 最大化 有 连续相同 结果的题数。（也就是连续出现 true 或者连续出现 false）。
给你一个字符串 `answerKey` ，其中 `answerKey[i]` 是第 `i` 个问题的正确结果。除此以外，还给你一个整数 `k` ，表示你能进行以下操作的最多次数：
每次操作中，将问题的正确答案改为 `'T'` 或者 `'F'` （也就是将 `answerKey[i]` 改为 `'T'` 或者 `'F'` ）。
请你返回在不超过 `k` 次操作的情况下，最大 连续 `'T'` 或者 `'F'` 的数目。

示例 1：
输入：answerKey = "TTFF", k = 2 输出：4 解释：我们可以将两个 'F' 都变为 'T' ，得到 answerKey = "TTTT" 。 总共有四个连续的 'T' 。
示例 2：
输入：answerKey = "TFFT", k = 1 输出：3 解释：我们可以将最前面的 'T' 换成 'F' ，得到 answerKey = "FFFT" 。 或者，我们可以将第二个 'T' 换成 'F' ，得到 answerKey = "TFFF" 。 两种情况下，都有三个连续的 'F' 。
示例 3：
输入：answerKey = "TTFTTFTT", k = 1 输出：5 解释：我们可以将第一个 'F' 换成 'T' ，得到 answerKey = "TTTTTFTT" 。 或者我们可以将第二个 'F' 换成 'T' ，得到 answerKey = "TTFTTTTT" 。 两种情况下，都有五个连续的 'T' 。

提示：
`n == answerKey.length`
`1 <= n <= 5 * 10^4`
`answerKey[i]` 要么是 `'T'` ，要么是 `'F'`
`1 <= k <= n`
"""

from typing import List, Optional


class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n = len(answerKey)

        def max_consecutive(ch: str) -> int:
            left = 0
            flips = 0
            max_len = 0
            for right in range(n):
                if answerKey[right] != ch:
                    flips += 1
                while flips > k:
                    if answerKey[left] != ch:
                        flips -= 1
                    left += 1
                max_len = max(max_len, right - left + 1)
            return max_len

        return max(max_consecutive('T'), max_consecutive('F'))



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: String, Binary Search, Prefix Sum, Sliding Window
#
# 解题思路:
# 滑动窗口。分别计算将窗口内字符变成全'T'和全'F'的最大长度。
# 对于每种目标字符，维护一个窗口，记录需要翻转的次数。
# 当翻转次数超过k时，收缩左边界。最终取两种情况的最大值。
#
# 时间复杂度: O(n)
# 空间复杂度: O(1)
#
# 关键点:
# - 分别计算转换为T和F的情况
# - 滑动窗口维护翻转次数
# - 窗口内翻转次数 = 窗口长度 - 目标字符出现次数
