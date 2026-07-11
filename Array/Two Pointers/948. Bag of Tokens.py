"""
LeetCode #948 - Bag of Tokens
中文题名：令牌放置
https://leetcode.com/problems/bag-of-tokens/

You have an initial power `P`, an initial score of `0` points, and a
bag of tokens.

Each token can be used at most once, has a value `token[i]`, and has potentially
two ways to use it.

If we have at least `token[i]` power, we may play the token face up, losing
`token[i]` power, and gaining `1` point.

If we have at least `1` point, we may play the token face down, gaining
`token[i]` power, and losing `1` point.

Return the largest number of points we can have after playing any number of tokens.

Example 1:

Input: tokens = [100], P = 50
Output: 0

Example 2:

Input: tokens = [100,200], P = 150
Output: 1

Example 3:

Input: tokens = [100,200,300,400], P = 200
Output: 2

Note:

`tokens.length <= 1000`

`0 <= tokens[i] < 10000`

`0 <= P < 10000`

【中文翻译】
你拥有初始能量 P，初始分数为 0 分，以及一包令牌。

每个令牌最多只能使用一次，具有值 token[i]，并且有两种使用方式：

- 如果当前能量至少为 token[i]，则可以正面朝上使用该令牌，失去 token[i] 能量，获得 1 分。
- 如果当前分数至少为 1 分，则可以反面朝上使用该令牌，获得 token[i] 能量，失去 1 分。

返回在使用了任意数量的令牌后可以拥有的最大分数。

"""

from typing import List, Optional


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        left, right = 0, len(tokens) - 1
        score = 0
        max_score = 0

        while left <= right:
            if power >= tokens[left]:
                # Play face up: spend small token to gain score
                power -= tokens[left]
                score += 1
                left += 1
                max_score = max(max_score, score)
            elif score > 0:
                # Play face down: spend score to gain power from large token
                power += tokens[right]
                score -= 1
                right -= 1
            else:
                break

        return max_score



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 1. 排序令牌：将令牌升序排序，以便用双指针从两端取用。
# 2. 双指针贪心：
#    - 左指针指向最小令牌（最适合正面朝上赚分）
#    - 右指针指向最大令牌（最适合反面朝上换能量）
# 3. 循环策略：
#    - 如果当前能量 >= 最小令牌值：正面朝上使用它（失去能量，获得 1 分）
#    - 否则如果当前分数 > 0：反面朝上使用最大令牌（失去 1 分，获得能量）
#    - 否则无法继续，退出循环
# 4. 过程中持续更新最大分数记录。
#
# 时间复杂度: O(N * log N) — 排序的开销，双指针遍历为 O(N)。
# 空间复杂度: O(1) — 如果忽略排序的额外空间。
#
# 关键点:
# - 贪心策略：用最小令牌赚分，用最大令牌换能量
# - 分数可以"兑换"能量来继续游戏，从而获得更高的总分数
# - 双指针分别从两端取令牌确保全局最优
