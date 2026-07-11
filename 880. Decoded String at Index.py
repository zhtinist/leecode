"""
LeetCode #880 - Decoded String at Index
中文题名：索引处的解码字符串
https://leetcode.com/problems/decoded-string-at-index/

An encoded string `S` is given.  To find and write the decoded
string to a tape, the encoded string is read one character at a time and
the following steps are taken:

If the character read is a letter, that letter is written onto the tape.

If the character read is a digit (say `d`), the entire current tape is
repeatedly written `d-1` more times in total.

Now for some encoded string `S`, and an index `K`, find and return the
`K`-th letter (1 indexed) in the decoded string.

Example 1:

Input: S = "leet2code3", K = 10
Output: "o"
Explanation:
The decoded string is "leetleetcodeleetleetcodeleetleetcode".
The 10th letter in the string is "o".

Example 2:

Input: S = "ha22", K = 5
Output: "h"
Explanation:
The decoded string is "hahahaha".  The 5th letter is "h".

Example 3:

Input: S = "a2345678999999999999999", K = 1
Output: "a"
Explanation:
The decoded string is "a" repeated 8301530446056247680 times.  The 1st letter is "a".

Note:

`2 <= S.length <= 100`

`S` will only contain lowercase letters and digits
`2`
through `9`.

`S` starts with a letter.

`1 <= K <= 10^9`

The decoded string is guaranteed to have less than `2^63`
letters.

【中文翻译】
给定一个编码字符串 S。为了找出解码字符串并写入磁带，从编码字符串中每次读取一个字符，
并采取以下步骤：如果所读的字符是字母，则将该字母写在磁带上；如果所读的字符是数字 d，
则将整个当前磁带总共重复写入 d-1 次。现在，对于给定的编码字符串 S 和索引 K，
查找并返回解码字符串中的第 K 个字母（索引从 1 开始）。

"""

from typing import List, Optional


class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        # 第一遍：计算解码后的总长度
        total_len = 0
        for ch in s:
            if ch.isdigit():
                total_len *= int(ch)
            else:
                total_len += 1

        # 第二遍：从后往前反向推导第 K 个字符
        for ch in reversed(s):
            k %= total_len  # 将 K 映射到当前段的对应位置
            if ch.isdigit():
                # 当前段被重复了 d 次，缩小 total_len
                total_len //= int(ch)
            else:
                # 当前段是一个字母
                if k == 0:
                    return ch
                total_len -= 1

        return ""  # 不应到达这里



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 不能直接构造解码字符串，因为字符串可能非常长（K 可达 10^9，总长度可达 2^63）。
# 采用反向推导法：
# 1. 先正向扫描 S，计算解码后字符串的总长度 total_len（遇到字母 +1，遇到数字 *d）。
# 2. 从后往前反向扫描 S。对于每个字符：
#    - 先将 K 对 total_len 取模：K = K % total_len。这是因为重复段中每个位置在模意义下等价。
#    - 如果当前字符是数字 d，说明当前 total_len 是重复 d 次后的结果，需要还原：
#      total_len //= d。
#    - 如果当前字符是字母，检查 K == 0（即模运算后 K 指向该字母）：
#      如果 K 为 0，说明这就是答案；否则 total_len -= 1（去掉该字母）。
#
# 时间复杂度: O(N)，其中 N 是编码字符串 S 的长度（<= 100）
# 空间复杂度: O(1)
#
# 关键点:
# - 不能构造完整的解码字符串（会爆内存）
# - 反向推导：从编码字符串末尾向前工作，逐步缩小 K 和长度
# - K % total_len 将 K 映射到当前重复单位的对应位置
# - 当 k == 0 且遇到字母时，该字母就是答案
