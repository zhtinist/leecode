"""
LeetCode #271 - Encode and Decode Strings
https://leetcode.com/problems/encode-and-decode-strings/

Design an algorithm to encode a list of strings to a string. The encoded string
is then sent over the network and is decoded back to the original list of strings.

Machine 1 (sender) has the function:

string encode(vector<string> strs) {
// ... your code
return encoded_string;
}

Machine 2 (receiver) has the function:

vector<string> decode(string s) {
//... your code
return strs;
}

So Machine 1 does:

string encoded_string = encode(strs);

and Machine 2 does:

vector<string> strs2 = decode(encoded_string);

`strs2` in Machine 2 should be the same as `strs` in Machine 1.

Implement the `encode` and `decode` methods.

Note:

The string may contain any possible characters out of 256 valid ascii characters. Your
algorithm should be generalized enough to work on any possible characters.

Do not use class member/global/static variables to store states. Your encode and decode
algorithms should be stateless.

Do not rely on any library method such as `eval` or serialize methods. You
should implement your own encode/decode algorithm.
"""

from typing import List, Optional


class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.

        Uses length-prefix encoding: each string is prefixed with its length
        followed by a delimiter '#', then the string itself.
        Example: ["hello", "world"] -> "5#hello5#world"
        """
        encoded = []
        for s in strs:
            encoded.append(f"{len(s)}#{s}")
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string back to a list of strings."""
        decoded = []
        i = 0
        while i < len(s):
            # Find the delimiter '#' to read the length
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            # Extract the string of that length
            decoded.append(s[j + 1:j + 1 + length])
            i = j + 1 + length
        return decoded


class Solution:
    """
    This problem uses a Codec class, not Solution.
    The Codec implementation above is the complete solution.
    """
    pass


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: Yes
#
# 解题思路:
# 使用长度前缀编码（Length-Prefix Encoding）。对于每个字符串，先编码为
# "长度#字符串"的格式，例如 "hello" 编码为 "5#hello"。解码时从左到右扫描：
# 找到第一个 '#'，其前面的数字即为接下来要读取的字符串长度，然后跳过 '#'
# 读取该长度的字符串即可。这种编码方式可以处理包含任意字符（包括 '#' 和数字）
# 的字符串，因为长度信息位于字符串内容之前。
#
# 时间复杂度: O(N) - 编码和解码各需要遍历所有字符一次，N为所有字符串总长度
# 空间复杂度: O(N) - 编码后的字符串需要存储所有原始字符串内容
#
# 关键点:
# - 长度前缀编码能处理包含任意字符的字符串
# - 解码时通过 '#' 分隔符定位长度信息
# - 不使用任何全局/静态变量，编解码器完全无状态
