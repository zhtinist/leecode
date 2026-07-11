"""
LeetCode #881 - Boats to Save People
中文题名：救生艇
https://leetcode.com/problems/boats-to-save-people/

The `i`-th person has weight `people[i]`, and each boat can carry a
maximum weight of `limit`.

Each boat carries at most 2 people at the same time, provided the sum of the weight of
those people is at most `limit`.

Return the minimum number of boats to carry every given person.  (It is guaranteed each
person can be carried by a boat.)

Example 1:

Input: people = [1,2], limit = 3
Output: 1
Explanation: 1 boat (1, 2)

Example 2:

Input: people = [3,2,2,1], limit = 3
Output: 3
Explanation: 3 boats (1, 2), (2) and (3)

Example 3:

Input: people = [3,5,3,4], limit = 5
Output: 4
Explanation: 4 boats (3), (3), (4), (5)

Note:

`1 <= people.length <= 50000`

`1 <= people[i] <= limit <= 30000`

【中文翻译】

第 `i` 个人的体重为 `people[i]`，每艘船最大载重量为 `limit`。

每艘船最多同时搭载 2 人，前提是这些人的体重之和不超过 `limit`。

返回搭载所有人所需的最少船只数量。（保证每个人都能被船搭载。）

"""

from typing import List, Optional


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left, right = 0, len(people) - 1
        boats = 0

        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1  # 最轻的和最重的一起乘船
            right -= 1  # 最重的必定乘船
            boats += 1

        return boats



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 贪心 + 双指针。首先对体重数组排序。
# 使用左右双指针：最轻的人(left)和最重的人(right)尝试配对。
# 如果两人体重之和 <= limit，则两人同乘一条船，left 右移；
# 否则最重的人只能独自乘船。无论哪种情况，right 都左移。
# 每步都需要一艘船，boast计数+1。
# 当 left > right 时结束。
#
# 时间复杂度: O(N log N) — 排序占主导
# 空间复杂度: O(1) — 仅使用常数额外空间（或 O(N) 取决于排序实现）
#
# 关键点:
# - 每条船最多载2人，这是贪心策略正确的关键
# - 排序后最轻的和最重的配对是最优的
# - 如果最轻+最重 > limit，最重的无法和任何人配对
