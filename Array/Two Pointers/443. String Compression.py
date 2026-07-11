"""
LeetCode #443 - String Compression
中文题名：压缩字符串
https://leetcode.com/problems/string-compression/

Given an array of characters, compress it in-place.

The length after compression must always be smaller than or equal to the original array.

Every element of the array should be a character (not int) of length 1.

After you are done modifying the input array in-place,
return the new length of the array.

Follow up:

Could you solve it using only O(1) extra space?

Example 1:

Input:
["a","a","b","b","c","c","c"]

Output:
Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]

Explanation:
"aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".

Example 2:

Input:
["a"]

Output:
Return 1, and the first 1 characters of the input array should be: ["a"]

Explanation:
Nothing is replaced.

Example 3:

Input:
["a","b","b","b","b","b","b","b","b","b","b","b","b"]

Output:
Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].

Explanation:
Since the character "a" does not repeat, it is not compressed. "bbbbbbbbbbbb" is replaced by "b12".
Notice each digit has it's own entry in the array.

Note:

All characters have an ASCII value in `[35, 126]`.

`1 <= len(chars) <= 1000`.

【中文翻译】
给定一个字符数组，原地压缩它。压缩后的长度必须始终小于或等于原数组。
数组的每个元素应为单个字符（非整数）。原地修改输入数组后，返回数组的新长度。

进阶：能否用 O(1) 额外空间解决？

示例 1：
    输入：["a","a","b","b","c","c","c"]
    输出：返回 6，输入数组前 6 个字符为 ["a","2","b","2","c","3"]
    解释："aa" 替换为 "a2"，"bb" 替换为 "b2"，"ccc" 替换为 "c3"

示例 2：
    输入：["a"]
    输出：返回 1，输入数组前 1 个字符为 ["a"]

示例 3：
    输入：["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    输出：返回 4，输入数组前 4 个字符为 ["a","b","1","2"]
    解释：字符 "a" 未重复不压缩，"bbbbbbbbbbbb" 替换为 "b12"（每个数字占一个元素）

注意：
    所有字符的 ASCII 值在 [35, 126] 范围内。
    1 <= len(chars) <= 1000。
"""

from typing import List, Optional


class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0
        read = 0
        n = len(chars)

        while read < n:
            ch = chars[read]
            count = 0

            # Count consecutive repeating characters
            while read < n and chars[read] == ch:
                read += 1
                count += 1

            # Write the character
            chars[write] = ch
            write += 1

            # Write the count if > 1
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        return write


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 双指针原地压缩。使用 read 指针读取字符，write 指针写入压缩结果。
#
# 1. read 遍历数组，对于每个字符组：
#    a. 记录当前字符 ch
#    b. 统计连续相同字符的数量 count（read 指针同时前移）
#    c. 在 write 位置写入字符 ch，write++
#    d. 如果 count > 1，将 count 的每个数字字符依序写入 write 位置
# 2. 返回 write（即压缩后的长度）
#
# 例如 ["a","a","b","b","c","c","c"]：
# - read=0: ch='a', count=2, write="a","2"
# - read=2: ch='b', count=2, write="b","2"
# - read=4: ch='c', count=3, write="c","3"
# - 返回 write=6
#
# 时间复杂度: O(N) — 每个字符遍历一次
# 空间复杂度: O(1) — 只使用常数变量
#
# 关键点:
# - read 和 write 双指针，read 在前读取，write 在后写入
# - write 永远不会超过 read，保证不会覆盖未读数据
# - count > 1 时才写入数字，单个字符不写计数
# - 多位数（如 12）需要逐位写入
