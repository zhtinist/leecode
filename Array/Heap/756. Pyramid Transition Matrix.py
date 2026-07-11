"""
LeetCode #756 - Pyramid Transition Matrix
中文题名：金字塔转换矩阵
https://leetcode.com/problems/pyramid-transition-matrix/

We are stacking blocks to form a pyramid. Each block has a color which is a one letter
string.

We are allowed to place any color block `C` on top of two adjacent blocks of
colors `A` and `B`, if and only if `ABC` is an allowed
triple.

We start with a bottom row of `bottom`, represented as a single string. We also
start with a list of allowed triples `allowed`. Each allowed triple is
represented as a string of length 3.

Return true if we can build the pyramid all the way to the top, otherwise false.

Example 1:

Input: bottom = "BCD", allowed = ["BCG", "CDE", "GEA", "FFF"]
Output: true
Explanation:
We can stack the pyramid like this:
A
/ \
G   E
/ \ / \
B   C   D

We are allowed to place G on top of B and C because BCG is an allowed triple.  Similarly, we can place E on top of C and D, then A on top of G and E.

Example 2:

Input: bottom = "AABA", allowed = ["AAA", "AAB", "ABA", "ABB", "BAC"]
Output: false
Explanation:
We can't stack the pyramid to the top.
Note that there could be allowed triples (A, B, C) and (A, B, D) with C != D.

Note:

`bottom` will be a string with length in range `[2, 8]`.

`allowed` will have length in range `[0, 200]`.

Letters in all strings will be chosen from the set `{'A', 'B',
'C', 'D', 'E', 'F', 'G'}`.

【中文翻译】
现在，我们用一些方块来堆砌一个金字塔。每个方块用仅包含一个字母的字符串表示。

使用三元组表示金字塔的堆砌规则如下：

对于三元组 (A, B, C)，"C" 为顶层方块，方块 "A"、"B" 分别作为方块 "C" 下一层的左、右方块。当且仅当 (A, B, C) 是被允许的三元组，我们才可以将其堆砌上。

初始时，给定金字塔的基层 bottom，用一个字符串表示。我们还给出一个允许的三元组列表 allowed，每个允许的三元组用一个长度为 3 的字符串表示。

如果可以从基层一直堆到塔尖，则返回 true，否则返回 false。

示例 1：

输入：bottom = "BCD", allowed = ["BCG", "CDE", "GEA", "FFF"]
输出：true
解释：
可以堆砌成这样金字塔：
    A
   / \
  G   E
 / \ / \
B   C   D

因为 ('B', 'C', 'G') , ('C', 'D', 'E') 和 ('G', 'E', 'A') 三种规则都是允许的。

示例 2：

输入：bottom = "AABA", allowed = ["AAA", "AAB", "ABA", "ABB", "BAC"]
输出：false
解释：
无法一直堆到塔尖。
注意，允许存在 (A, B, C) 和 (A, B, D) 这样的三元组，其中 C != D。

注意：

bottom 的长度范围在 [2, 8]。

allowed 的长度范围在 [0, 200]。

所有字符串中的字母都选自集合 {'A', 'B', 'C', 'D', 'E', 'F', 'G'}。
"""

from typing import List, Optional


class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        from collections import defaultdict
        allow = defaultdict(list)
        for a, b, c in allowed:
            allow[a + b].append(c)

        memo = {}

        def dfs(cur: str) -> bool:
            if len(cur) == 1:
                return True
            if cur in memo:
                return memo[cur]

            def build_next(cur: str, pos: int, next_row: str) -> bool:
                if pos == len(cur) - 1:
                    return dfs(next_row)
                key = cur[pos:pos + 2]
                if key not in allow:
                    return False
                for c in allow[key]:
                    if build_next(cur, pos + 1, next_row + c):
                        return True
                return False

            memo[cur] = build_next(cur, 0, "")
            return memo[cur]

        return dfs(bottom)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# DFS + 记忆化搜索 + 回溯。
# 1. 预处理 allowed 列表：建立映射 allow[AB] = [C1, C2, ...]，表示底层为 AB 时可以放置哪些顶层字母。
# 2. 从 bottom 开始，逐层向上构建金字塔：
#    - 给定当前层 cur（长度为 L），尝试构建长度为 L-1 的上一层 next_row。
#    - 对于每个位置 pos，取其下方两个字母作为 key = cur[pos:pos+2]。
#    - 从 allow[key] 中依次尝试每个候选字母，递归构建剩余位置。
# 3. 当 cur 长度为 1（塔尖）时，返回 True。
# 4. 使用 memo 字典缓存每层的构建结果，避免重复计算。
#
# 时间复杂度: O(7^(N) * N * A) - N 为 bottom 长度 <= 8，字母集大小为 7，实际远小于此上限
# 空间复杂度: O(N^2) - 递归栈深度和记忆化缓存
#
# 关键点:
# - 预处理 allowed 为哈希表加速查找（key 是前两个字母，value 是候选第三个字母列表）
# - 记忆化搜索：同一层 cur 可能多次被尝试，缓存结果避免重复
# - 回溯思想：对于每个位置，尝试所有可能的字母，失败则回溯尝试下一个
# - 数据规模小（bottom <= 8, allowed <= 200），DFS 可行
