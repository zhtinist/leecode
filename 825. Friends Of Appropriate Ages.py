"""
LeetCode #825 - Friends Of Appropriate Ages
中文题名：适龄的朋友
https://leetcode.com/problems/friends-of-appropriate-ages/

Some people will make friend requests. The list of their ages is given and `ages[i]` is
the age of the ith person.

Person A will NOT friend request person B (B != A) if any of the following conditions are
true:

`age[B] <= 0.5 * age[A] + 7`

`age[B] > age[A]`

`age[B] > 100 && age[A] < 100`

Otherwise, A will friend request B.

Note that if A requests B, B does not necessarily request A.  Also, people will not
friend request themselves.

How many total friend requests are made?

Example 1:

Input: [16,16]
Output: 2
Explanation: 2 people friend request each other.

Example 2:

Input: [16,17,18]
Output: 2
Explanation: Friend requests are made 17 -> 16, 18 -> 17.

Example 3:

Input: [20,30,100,110,120]
Output:
Explanation: Friend requests are made 110 -> 100, 120 -> 110, 120 -> 100.

Notes:

`1 <= ages.length <= 20000`.

`1 <= ages[i] <= 120`.

【中文翻译】
有一些人会发送好友请求。给定一个数组 `ages`，其中 `ages[i]` 表示第 i 个人的年龄。

当以下任一条件成立时，A 不会向 B（B != A）发送好友请求：

`age[B] <= 0.5 * age[A] + 7`

`age[B] > age[A]`

`age[B] > 100 && age[A] < 100`

否则，A 会向 B 发送好友请求。

注意，如果 A 向 B 发送请求，B 不一定向 A 发送请求。同时，人不会向自己发送好友请求。

请问总共会发送多少个好友请求？

示例 1：

输入：[16,16]
输出：2
解释：两个人互相发送好友请求。

示例 2：

输入：[16,17,18]
输出：2
解释：好友请求为 17 -> 16，18 -> 17。

示例 3：

输入：[20,30,100,110,120]
输出：3
解释：好友请求为 110 -> 100，120 -> 110，120 -> 100。

注意：

`1 <= ages.length <= 20000`

`1 <= ages[i] <= 120`

"""

from typing import List, Optional


class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        # Count how many people of each age (age range 1-120)
        count = [0] * 121
        for age in ages:
            count[age] += 1

        requests = 0
        # For each age A, check which ages B can receive requests from A
        for ageA in range(1, 121):
            countA = count[ageA]
            if countA == 0:
                continue
            for ageB in range(1, 121):
                countB = count[ageB]
                if countB == 0:
                    continue
                # Condition: ageB <= 0.5 * ageA + 7 -> NOT friend
                if ageB <= 0.5 * ageA + 7:
                    continue
                # Condition: ageB > ageA -> NOT friend
                if ageB > ageA:
                    continue
                # Age same: A requests B but not self
                if ageA == ageB:
                    requests += countA * (countA - 1)
                else:
                    requests += countA * countB

        return requests



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 由于年龄范围只有 1-120，可以使用计数排序的思想。
# 先统计每个年龄的人数 count[age]。
# 然后对于每一对年龄 (ageA, ageB)，如果满足好友条件（即不触发任何阻止条件），
# 则 ageA 的人会向 ageB 的所有人发请求。
# 阻止条件：
#   1. ageB <= 0.5 * ageA + 7（年龄太小不请求）
#   2. ageB > ageA（不向年长者发请求）
# 当 ageA == ageB 时，不能向自己发请求，所以是 countA * (countA - 1)。
# 第三个条件 "ageB > 100 && ageA < 100" 实际上被前两个条件覆盖了，
# 因为当 ageA < 100 且 ageB > 100 时，ageB > ageA 已经成立，会被条件2阻止。
#
# 时间复杂度: O(120^2 + n) = O(n) — 其中 n 是 ages 长度，常量级年龄范围配对
# 空间复杂度: O(121) = O(1) — 只需固定大小计数数组
#
# 关键点:
# - 年龄范围很小(1-120)，用计数代替排序，避免 O(n log n)
# - 注意 ageA == ageB 时减去自身(countA - 1)
# - 条件3 (ageB > 100 && ageA < 100) 被前两个条件覆盖，可简化判断
