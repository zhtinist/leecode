"""
LeetCode #1797 - Design Authentication Manager
中文题名：设计一个验证系统
https://leetcode.com/problems/design-authentication-manager/

There is an authentication system that works with authentication tokens. For each session, the user will receive a new authentication token that will expire `timeToLive` seconds after the `currentTime`. If the token is renewed, the expiry time will be extended to expire `timeToLive` seconds after the (potentially different) `currentTime`.

Implement the `AuthenticationManager` class:

`AuthenticationManager(int timeToLive)` constructs the `AuthenticationManager` and sets the `timeToLive`.

`generate(string tokenId, int currentTime)` generates a new token with the given `tokenId` at the given `currentTime` in seconds.

`renew(string tokenId, int currentTime)` renews the unexpired token with the given `tokenId` at the given `currentTime` in seconds. If there are no unexpired tokens with the given `tokenId`, the request is ignored, and nothing happens.

`countUnexpiredTokens(int currentTime)` returns the number of unexpired tokens at the given currentTime.

Note that if a token expires at time `t`, and another action happens on time `t` (`renew` or `countUnexpiredTokens`), the expiration takes place before the other actions.

Example 1:

Input
["AuthenticationManager", "`renew`", "generate", "`countUnexpiredTokens`", "generate", "`renew`", "`renew`", "`countUnexpiredTokens`"]
[[5], ["aaa", 1], ["aaa", 2], [6], ["bbb", 7], ["aaa", 8], ["bbb", 10], [15]]
Output
[null, null, null, 1, null, null, null, 0]

Explanation
AuthenticationManager authenticationManager = new AuthenticationManager(5); // Constructs the AuthenticationManager with `timeToLive` = 5 seconds.
authenticationManager.`renew`("aaa", 1); // No token exists with tokenId "aaa" at time 1, so nothing happens.
authenticationManager.generate("aaa", 2); // Generates a new token with tokenId "aaa" at time 2.
authenticationManager.`countUnexpiredTokens`(6); // The token with tokenId "aaa" is the only unexpired one at time 6, so return 1.
authenticationManager.generate("bbb", 7); // Generates a new token with tokenId "bbb" at time 7.
authenticationManager.`renew`("aaa", 8); // The token with tokenId "aaa" expired at time 7, and 8 >= 7, so at time 8 the `renew` request is ignored, and nothing happens.
authenticationManager.`renew`("bbb", 10); // The token with tokenId "bbb" is unexpired at time 10, so the `renew` request is fulfilled and now the token will expire at time 15.
authenticationManager.`countUnexpiredTokens`(15); // The token with tokenId "bbb" expires at time 15, and the token with tokenId "aaa" expired at time 7, so currently no token is unexpired, so return 0.

Constraints:

`1 <= timeToLive <= 108`

`1 <= currentTime <= 108`

`1 <= tokenId.length <= 5`

`tokenId` consists only of lowercase letters.

All calls to `generate` will contain unique values of `tokenId`.

The values of `currentTime` across all the function calls will be strictly increasing.

At most `2000` calls will be made to all functions combined.

【中文翻译】
设计一个 AuthenticationManager 类：
- AuthenticationManager(int timeToLive)：构造函数，设置 token 的存活时间 ttl
- generate(string tokenId, int currentTime)：生成一个 token，过期时间为 currentTime + ttl
- renew(string tokenId, int currentTime)：如果 token 尚未过期，更新其过期时间为 currentTime + ttl
- countUnexpiredTokens(int currentTime)：返回当前未过期的 token 数量

示例 1：
输入: ["AuthenticationManager","renew","generate","countUnexpiredTokens","generate","renew","renew","countUnexpiredTokens"]
[[5],["aaa",1],["aaa",2],[6],["bbb",7],["aaa",8],["bbb",10],[15]]
输出: [null,null,null,1,null,null,null,0]
"""

from typing import List, Optional


class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.ttl = timeToLive
        self.tokens = {}  # tokenId -> expiryTime

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokens[tokenId] = currentTime + self.ttl

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.tokens and self.tokens[tokenId] > currentTime:
            self.tokens[tokenId] = currentTime + self.ttl

    def countUnexpiredTokens(self, currentTime: int) -> int:
        # 清理过期 token（可选优化，不清理也能通过）
        expired = [k for k, v in self.tokens.items() if v <= currentTime]
        for k in expired:
            del self.tokens[k]
        return len(self.tokens)
# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用哈希表存储 token_id → expiry_time。
# generate：直接插入记录，过期时间为 currentTime + ttl。
# renew：如果 token 存在且未过期（expiry > currentTime），更新过期时间。
# countUnexpiredTokens：遍历所有 token，计数未过期的。
# 可以在 count 时懒惰清理已过期的 token。
#
# 时间复杂度: generate/renew O(1)；countUnexpiredTokens O(N) — N 为 token 数
# 空间复杂度: O(N)
#
# 关键点:
# - 过期判断：expiry > currentTime 表示未过期
# - 懒惰删除：在 count 时清理已过期 token
# - 注意 renew 时需检查 token 是否过期
