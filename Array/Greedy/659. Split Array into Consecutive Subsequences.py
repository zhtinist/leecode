"""
LeetCode #659 - Split Array into Consecutive Subsequences
中文题名：分割数组为连续子序列
https://leetcode.com/problems/split-array-into-consecutive-subsequences/

Given an array `nums` sorted in ascending order, return `true` if
and only if you can split it into 1 or more subsequences such that each subsequence consists
of consecutive integers and has length at least 3.

Example 1:

Input: [1,2,3,3,4,5]
Output: True
Explanation:
You can split them into two consecutive subsequences :
1, 2, 3
3, 4, 5

Example 2:

Input: [1,2,3,3,4,4,5,5]
Output: True
Explanation:
You can split them into two consecutive subsequences :
1, 2, 3, 4, 5
3, 4, 5

Example 3:

Input: [1,2,3,4,4,5]
Output: False

Constraints:

`1 <= nums.length <= 10000`

【中文翻译】
给定一个按升序排序的数组 `nums`，当且仅当你可以将其分割为 1 个或多个子序列，使得每个子序列由连续的整数组成且长度至少为 3 时，返回 `true`。

示例 1：

输入：[1,2,3,3,4,5]
输出：True
解释：
你可以将它们分成两个连续子序列：
1, 2, 3
3, 4, 5

示例 2：

输入：[1,2,3,3,4,4,5,5]
输出：True
解释：
你可以将它们分成两个连续子序列：
1, 2, 3, 4, 5
3, 4, 5

示例 3：

输入：[1,2,3,4,4,5]
输出：False

约束条件：

`1 <= nums.length <= 10000`
"""

from collections import Counter
from typing import List, Optional


class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        freq = Counter(nums)
        need: dict[int, int] = {}

        for num in nums:
            if freq[num] == 0:
                continue

            if need.get(num, 0) > 0:
                need[num] -= 1
                need[num + 1] = need.get(num + 1, 0) + 1
                freq[num] -= 1
            elif freq.get(num + 1, 0) > 0 and freq.get(num + 2, 0) > 0:
                freq[num] -= 1
                freq[num + 1] -= 1
                freq[num + 2] -= 1
                need[num + 3] = need.get(num + 3, 0) + 1
            else:
                return False

        return True











# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用贪心算法，维护两个哈希表：
# - freq：记录每个数字的剩余出现次数
# - need：记录需要接在当前数字后面的序列数量（即期望某个数字出现的次数）
#
# 遍历数组中的每个数字 num：
# 1. 如果 freq[num] == 0，已被使用完，跳过
# 2. 如果 need[num] > 0，说明存在等待 num 接续的序列：
#    - 将 num 附加到其中一个序列末尾
#    - need[num] 减 1，need[num+1] 加 1（期待下一个数字）
# 3. 否则，以 num 为起点开启一个新序列（需要 num, num+1, num+2）：
#    - 如果 freq[num+1] > 0 且 freq[num+2] > 0，消耗这三个数字
#    - need[num+3] 加 1（期待下一个数字续上）
# 4. 如果以上都不满足，返回 False
#
# 时间复杂度: O(n) - 每个元素处理一次
# 空间复杂度: O(n) - freq 和 need 哈希表
#
# 关键点:
# - 贪心策略的核心：优先将数字附加到已有序列末尾，再尝试开启新序列
# - need 哈希表巧妙地记录了"缺口"：需要在哪个数字处接续
# - 要么延长旧序列，要么开启长度为 3 的新序列——保证每个子序列长度 >= 3
# - 类似生活中的"接龙"问题，贪心保证最优解
