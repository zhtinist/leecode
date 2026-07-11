"""
LeetCode #848 - Shifting Letters
中文题名：字母移位
https://leetcode.com/problems/shifting-letters/

We have a string `S` of lowercase letters, and an integer array
`shifts`.

Call the shift of a letter, the next letter in the alphabet, (wrapping around so
that `'z'` becomes `'a'`).

For example, `shift('a') = 'b'`, `shift('t') = 'u'`,
and `shift('z') = 'a'`.

Now for each `shifts[i] = x`, we want to shift the first `i+1` letters
of `S`, `x` times.

Return the final string after all such shifts to `S` are applied.

Example 1:

Input: S = "abc", shifts = [3,5,9]
Output: "rpl"
Explanation:
We start with "abc".
After shifting the first 1 letters of S by 3, we have "dbc".
After shifting the first 2 letters of S by 5, we have "igc".
After shifting the first 3 letters of S by 9, we have "rpl", the answer.

Note:

`1 <= S.length = shifts.length <= 20000`

`0 <= shifts[i] <= 10 ^ 9`

【中文翻译】
有一个由小写字母组成的字符串 `S`，和一个整数数组 `shifts`。

我们将字母的"移位"定义为字母表中的下一个字母（循环移位，即 `'z'` 变为 `'a'`）。

例如，`shift('a') = 'b'`，`shift('t') = 'u'`，`shift('z') = 'a'`。

现在对于每个 `shifts[i] = x`，我们将 `S` 中的前 `i+1` 个字母移位 `x` 次。

返回将所有这些移位应用到 `S` 之后的最终字符串。

示例 1：

输入：S = "abc", shifts = [3,5,9]
输出："rpl"
解释：
我们从 "abc" 开始。
将 S 中的前 1 个字母移位 3 次后，得到 "dbc"。
将 S 中的前 2 个字母移位 5 次后，得到 "igc"。
将 S 中的前 3 个字母移位 9 次后，得到 "rpl"，即答案。

注意：

`1 <= S.length = shifts.length <= 20000`

`0 <= shifts[i] <= 10 ^ 9`

"""

from typing import List, Optional


class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        n = len(s)
        # Calculate suffix sum of shifts
        total_shifts = [0] * n
        suffix = 0
        for i in range(n - 1, -1, -1):
            suffix = (suffix + shifts[i]) % 26
            total_shifts[i] = suffix

        # Apply shifts to each character
        result = []
        for i, ch in enumerate(s):
            new_char = chr((ord(ch) - ord('a') + total_shifts[i]) % 26 + ord('a'))
            result.append(new_char)

        return ''.join(result)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 后缀和（逆向思维）。
# shifts[i] 会影响 S[0] 到 S[i]（前 i+1 个字母）。
# 等价于：S[0] 受到 shifts[0] + shifts[1] + ... + shifts[n-1] 次移位，
#        S[1] 受到 shifts[1] + ... + shifts[n-1] 次移位，
#        S[i] 受到 shifts[i] + ... + shifts[n-1] 次移位。
# 因此，从后向前计算后缀和：
#   1. suffix = (suffix + shifts[i]) % 26
#   2. S[i] 的新字符 = (S[i] - 'a' + suffix) % 26
# 由于移位次数可能非常大（10^9），需要对 26 取模。
#
# 时间复杂度: O(n) — 两次线性扫描
# 空间复杂度: O(n) — 存储 total_shifts 数组或直接使用后缀累加
#
# 关键点:
# - 每位字母的总移位次数 = 从该位置开始的所有 shifts 之和
# - 使用后缀和比逐个模拟每个操作高效得多
# - 对 26 取模避免大数溢出和不必要的完整轮转
# - 可以优化为一次遍历：从后向前计算后缀和并直接构建结果
