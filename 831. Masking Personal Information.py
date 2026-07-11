"""
LeetCode #831 - Masking Personal Information
中文题名：隐藏个人信息
https://leetcode.com/problems/masking-personal-information/

We are given a personal information string `S`, which may represent either
an email address or a phone number.

We would like to mask this personal information according to the following
rules:

1. Email address:

We define a name to be a string of `length >= 2`
consisting of only lowercase letters `a-z` or uppercase letters `A-Z`.

An email address starts with a name, followed by the symbol `'@'`,
followed by a name, followed by the dot `'.'` and followed
by a name.

All email addresses are guaranteed to be valid and in the format of `"name1@name2.name3".`

To mask an email, all names must be converted to lowercase and all
letters between the first and last letter of the first name must be replaced by 5
asterisks `'*'`.

2. Phone number:

A phone number is a string consisting of only the digits `0-9` or the
characters from the set `{'+', '-', '(', ')', ' '}.` You
may assume a phone number contains 10 to 13 digits.

The last 10 digits make up the local number, while the digits before those make up the
country code. Note that the country code is optional. We want to expose only the last 4
digits and mask all other digits.

The local number should be formatted and masked as `"***-***-1111", `where
`1` represents the exposed digits.

To mask a phone number with country code like `"+111 111 111 1111"`, we
write it in the form `"+***-***-***-1111".`  The
`'+'` sign and the first `'-'` sign before
the local number should only exist if there is a country code.  For example, a 12 digit
phone number mask should start with `"+**-"`.

Note that extraneous characters like `"(", ")", " "`,
as well as extra dashes or plus signs not part of the above formatting scheme should be
removed.

Return the correct "mask" of the information provided.

Example 1:

Input: "LeetCode@LeetCode.com"
Output: "l*****e@leetcode.com"
Explanation: All names are converted to lowercase, and the letters between the
first and last letter of the first name is replaced by 5 asterisks.
Therefore, "leetcode" -> "l*****e".

Example 2:

Input: "AB@qq.com"
Output: "a*****b@qq.com"
Explanation: There must be 5 asterisks between the first and last letter
of the first name "ab". Therefore, "ab" -> "a*****b".

Example 3:

Input: "1(234)567-890"
Output: "***-***-7890"
Explanation: 10 digits in the phone number, which means all digits make up the local number.

Example 4:

Input: "86-(10)12345678"
Output: "+**-***-***-5678"
Explanation: 12 digits, 2 digits for country code and 10 digits for local number.

Notes:

`S.length <= 40`.

Emails have length at least 8.

Phone numbers have length at least 10.

【中文翻译】
给你一个个人信息字符串 `S`，它可能是一个邮箱地址，也可能是一个电话号码。

我们将按照以下规则隐藏这些个人信息：

1. 电子邮件地址：

定义一个"名称"为长度 >= 2，且只包含小写字母 `a-z` 或大写字母 `A-Z` 的字符串。

一个电子邮件地址以一个名称开头，后跟 `'@'` 符号，再跟一个名称，后跟一个 `'.'`，再跟一个名称。

所有电子邮件地址保证有效且格式为 `"名称1@名称2.名称3"`。

要隐藏电子邮件，必须将所有名称转为小写，并将第一个名称的首尾字母之间的所有字母替换为 5 个星号 `'*'`。

2. 电话号码：

电话号码是一串只包含数字 `0-9` 或字符 `{'+', '-', '(', ')', ' '}` 的字符串。你可以假设电话号码包含 10 到 13 位数字。

最后 10 位数字组成本地号码，其余数字组成国家代码。注意国家代码是可选的。我们只想暴露最后 4 位数字，并隐藏所有其他数字。

本地号码应格式化为 `"***-***-1111"`，其中 `1` 代表暴露的数字。

要隐藏带有国家代码的电话号码如 `"+111 111 111 1111"`，我们写成 `"+***-***-***-1111"`。`'+'` 和本地号码前的第一个 `'-'` 只有在有国家代码时才存在。例如，12 位数字的电话号码掩码应以 `"+**-"` 开头。

注意，多余的字符如 `"("`、`")"`、`" "` 以及不属于上述格式的破折号或加号都应去除。

返回所提供信息的正确"掩码"。

示例 1：

输入："LeetCode@LeetCode.com"
输出："l*****e@leetcode.com"
解释：所有名称转为小写，第一个名称的首尾字母之间的字母替换为 5 个星号。因此，"leetcode" -> "l*****e"。

示例 2：

输入："AB@qq.com"
输出："a*****b@qq.com"
解释：第一个名称 "ab" 的首尾字母之间必须有 5 个星号。因此，"ab" -> "a*****b"。

示例 3：

输入："1(234)567-890"
输出："***-***-7890"
解释：电话号码中有 10 位数字，全部组成本地号码。

示例 4：

输入："86-(10)12345678"
输出："+**-***-***-5678"
解释：12 位数字，2 位为国家代码，10 位为本地号码。

注意：

`S.length <= 40`

电子邮件地址长度至少为 8。

电话号码长度至少为 10。

"""

from typing import List, Optional


class Solution:
    def maskPII(self, s: str) -> str:
        if '@' in s:
            # Email case
            s = s.lower()
            name, domain = s.split('@')
            return name[0] + '*****' + name[-1] + '@' + domain
        else:
            # Phone case
            digits = [c for c in s if c.isdigit()]
            local = ''.join(digits[-10:])
            country_len = len(digits) - 10

            masked_local = '***-***-' + local[-4:]

            if country_len == 0:
                return masked_local
            elif country_len == 1:
                return '+*-' + masked_local
            elif country_len == 2:
                return '+**-' + masked_local
            else:  # country_len == 3
                return '+***-' + masked_local



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 根据输入是否包含 '@' 来区分邮箱和电话号码。
#
# 邮箱处理：
#   1. 全部转为小写
#   2. 按 '@' 分割，取第一个名称
#   3. 用 name[0] + '*****' + name[-1] 替换第一个名称
#
# 电话号码处理：
#   1. 提取所有数字字符
#   2. 后 10 位是本地号码，前面的位数为国家代码位数
#   3. 本地号码格式化为 '***-***-' + 后四位
#   4. 根据国家代码位数（0/1/2/3）在前面加上相应格式
#
# 时间复杂度: O(n) — 其中 n 是字符串长度
# 空间复杂度: O(n) — 需要存储提取的数字
#
# 关键点:
# - 通过 '@' 符号区分邮箱和电话号码
# - 电话号码只提取数字，忽略所有分隔符
# - 国家代码位数可能为 0、1、2 或 3（10-13 位总数）
# - 邮箱名称长度 >= 2，首尾字母之间替换为恰好 5 个 '*'
