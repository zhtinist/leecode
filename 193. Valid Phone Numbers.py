"""
LeetCode #193 - Valid Phone Numbers
https://leetcode.com/problems/valid-phone-numbers/

Given a text file `file.txt` that contains list of phone numbers (one per line),
write a one liner bash script to print all valid phone numbers.

You may assume that a valid phone number must appear in one of the following two formats:
(xxx) xxx-xxxx or xxx-xxx-xxxx. (x means a digit)

You may also assume each line in the text file must not contain leading or trailing white
spaces.

Example:

Assume that `file.txt` has the following content:

987-123-4567
123 456 7890
(123) 456-7890

Your script should output the following valid phone numbers:

987-123-4567
(123) 456-7890
"""

from typing import List, Optional


class Solution:
    def validPhoneNumbers(self) -> str:
        return """grep -E '^([0-9]{3}-|\\([0-9]{3}\\) )[0-9]{3}-[0-9]{4}$' file.txt"""


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Easy
# Paid Only: No
#
# 解题思路:
# 使用 grep -E（扩展正则表达式）匹配两种有效电话号码格式：
# 格式一：xxx-xxx-xxxx（如 987-123-4567）
# 格式二：(xxx) xxx-xxxx（如 (123) 456-7890）
#
# 正则表达式解析：
# ^ — 行首
# ([0-9]{3}-|\([0-9]{3}\) ) — 匹配 "三个数字-" 或 "(三个数字) "
# [0-9]{3}-[0-9]{4} — 匹配 "三个数字-四个数字"
# $ — 行尾
#
# 时间复杂度: O(N) — 逐行扫描
# 空间复杂度: O(1) — 流式处理
#
# 关键点:
# - grep -E 支持扩展正则（+、|、() 等）
# - ^ 和 $ 确保完整匹配整行
# - | 实现"或"逻辑匹配两种格式
# - 注意格式二中括号后有空格
