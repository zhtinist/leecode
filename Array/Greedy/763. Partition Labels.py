"""
LeetCode #763 - Partition Labels
中文题名：划分字母区间
https://leetcode.com/problems/partition-labels/

A string `S` of lowercase letters is given. We want to partition this string into
as many parts as possible so that each letter appears in at most one part, and return a list
of integers representing the size of these parts.

Example 1:

Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.

Note:

`S` will have length in range `[1, 500]`.

`S` will consist of lowercase letters (`'a'` to `'z'`)
only.

【中文翻译】
字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一个字母只会出现在其中的一个片段。返回一个表示每个字符串片段的长度的列表。

示例 1：

输入：S = "ababcbacadefegdehijhklij"
输出：[9,7,8]
解释：
划分结果为 "ababcbaca", "defegde", "hijhklij"。
每个字母最多出现在一个片段中。
像 "ababcbacadefegde", "hijhklij" 的划分是错误的，因为划分的片段数较少。

注意：

S 的长度在 [1, 500] 之间。

S 只包含小写字母 'a' 到 'z'。
"""

from typing import List, Optional


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {c: i for i, c in enumerate(s)}
        result = []
        start = end = 0
        for i, c in enumerate(s):
            end = max(end, last[c])
            if i == end:
                result.append(end - start + 1)
                start = i + 1
        return result



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 贪心算法 + 哈希表。
# 1. 第一遍遍历字符串，用哈希表 last 记录每个字符最后一次出现的位置。
# 2. 第二遍遍历字符串，维护当前片段的起始位置 start 和结束位置 end：
#    - 对于当前字符 c，end = max(end, last[c])（扩展当前片段的右边界）。
#    - 当遍历到位置 i == end 时，说明当前片段的边界已经确定，
#      片段的长度为 end - start + 1，将其加入结果列表，
#      然后 start = i + 1 开始新的片断。
# 3. 这保证每个字符只出现在一个片段中，且片段数尽可能多。
#
# 时间复杂度: O(N) - 两次遍历字符串，N <= 500
# 空间复杂度: O(1) - 哈希表最多存 26 个小写字母
#
# 关键点:
# - 贪心策略：每次都取最小的满足条件的片段（尽可能多分）
# - 核心约束：一个字符的所有出现必须在同一片段内，所以片段右边界 = max(片段内所有字符的最右出现)
# - 当 i == end 时确定一个片段，贪心地立即分割
# - 类似"合并区间"的思想
