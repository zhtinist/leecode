"""
LeetCode #535 - Encode and Decode TinyURL
中文题名：TinyURL 的编码与解码
https://leetcode.com/problems/encode-and-decode-tinyurl/

Note: This is a companion problem to the System
Design problem: Design TinyURL.

TinyURL is a URL shortening service where you enter a URL such as `https://leetcode.com/problems/design-tinyurl`
and it returns a short URL such as `http://tinyurl.com/4e9iAk`.

Design the `encode` and `decode` methods for the TinyURL service. There
is no restriction on how your encode/decode algorithm should work. You just need to ensure
that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.

【中文翻译】
设计 TinyURL 的编码和解码方法。TinyURL 是一个短链接服务，输入一个长 URL（如 https://leetcode.com/problems/design-tinyurl），
返回一个短 URL（如 http://tinyurl.com/4e9iAk）。需实现 encode 方法将长 URL 编码为短 URL，
以及 decode 方法将短 URL 解码回原始 URL。编码和解码算法的实现方式不限，只需保证能正确编码和解码即可。
"""

import hashlib
from typing import List, Optional


class Codec:
    def __init__(self):
        self.url_to_code = {}
        self.code_to_url = {}
        self.base_url = "http://tinyurl.com/"
        self.counter = 0

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL."""
        if longUrl in self.url_to_code:
            return self.base_url + self.url_to_code[longUrl]
        code = hashlib.md5(longUrl.encode() + str(self.counter).encode()).hexdigest()[:6]
        self.counter += 1
        self.url_to_code[longUrl] = code
        self.code_to_url[code] = longUrl
        return self.base_url + code

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL."""
        code = shortUrl.split("/")[-1]
        return self.code_to_url.get(code, "")


class Solution:
    pass



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用哈希表建立长短 URL 的双向映射。encode 时：检查该长 URL 是否已编码过，
# 若已存在则直接返回；否则用 MD5 哈希 + 计数器生成一个 6 位短码，存入两个映射表中。
# decode 时：从短 URL 末尾提取短码，在映射表中查找原始 URL 返回即可。
#
# 时间复杂度: O(1) — 每次编码和解码都是字典 O(1) 操作
# 空间复杂度: O(N) — N 为编码的不同 URL 数量，需要存储映射关系
#
# 关键点:
# - 使用双向映射（长→短，短→长）保证 O(1) 编解码
# - 用哈希 + 计数器避免碰撞
# - 实际面试中本题考察系统设计思维，代码实现相对简单
# - 注意：虽然定义了 Solution 类（兼容框架），但实际实现的是 Codec 类
