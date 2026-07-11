"""
LeetCode #1817 - Finding the Users Active Minutes
中文题名：查找用户的活跃分钟数
https://leetcode.com/problems/finding-the-users-active-minutes/

You are given the logs for users' actions on LeetCode, and an integer `k`. The logs are represented by a 2D integer array `logs` where each `logs[i] = [IDi, timei]` indicates that the user with `IDi` performed an action at the minute `timei`.

Multiple users can perform actions simultaneously, and a single user can perform multiple actions in the same minute.

The user active minutes (UAM) for a given user is defined as the number of unique minutes in which the user performed an action on LeetCode. A minute can only be counted once, even if multiple actions occur during it.

You are to calculate a 1-indexed array `answer` of size `k` such that, for each `j` (`1 <= j <= k`), `answer[j]` is the number of users whose UAM equals `j`.

Return the array `answer` as described above.

Example 1:

Input: logs = [[0,5],[1,2],[0,2],[0,5],[1,3]], k = 5
Output: [0,2,0,0,0]
Explanation:
The user with ID=0 performed actions at minutes 5, 2, and 5 again. Hence, they have a UAM of 2 (minute 5 is only counted once).
The user with ID=1 performed actions at minutes 2 and 3. Hence, they have a UAM of 2.
Since both users have a UAM of 2, answer[2] is 2, and the remaining answer[j] values are 0.

Example 2:

Input: logs = [[1,1],[2,2],[2,3]], k = 4
Output: [1,1,0,0]
Explanation:
The user with ID=1 performed a single action at minute 1. Hence, they have a UAM of 1.
The user with ID=2 performed actions at minutes 2 and 3. Hence, they have a UAM of 2.
There is one user with a UAM of 1 and one with a UAM of 2.
Hence, answer[1] = 1, answer[2] = 1, and the remaining values are 0.

Constraints:

`1 <= logs.length <= 104`

`0 <= IDi <= 109`

`1 <= timei <= 105`

`k` is in the range `[The maximum UAM for a user, 105]`.

【中文翻译】

给定用户在LeetCode上的操作日志 `logs`（二维整数数组，`logs[i] = [IDi, timei]` 表示用户IDi在分钟timei执行了操作）和一个整数k。

一个用户的活跃分钟数(UAM)定义为该用户在LeetCode上执行操作的不重复分钟数。同一分钟内的多次操作只计为一次。

计算一个大小为k的1索引数组 `answer`，使得对于每个 j（1 <= j <= k），`answer[j]` 是UAM等于j的用户数量。

示例：
输入：logs = [[0,5],[1,2],[0,2],[0,5],[1,3]], k = 5
输出：[0,2,0,0,0]
解释：ID=0的用户在分钟5、2、5执行了操作，UAM=2；ID=1的用户在分钟2、3执行了操作，UAM=2。两位用户UAM都是2，所以answer[2]=2。

"""

from typing import List, Optional


class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        from collections import defaultdict
        user_minutes = defaultdict(set)
        for user_id, minute in logs:
            user_minutes[user_id].add(minute)

        answer = [0] * k
        for minutes in user_minutes.values():
            uam = len(minutes)
            if 1 <= uam <= k:
                answer[uam - 1] += 1
        return answer










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用哈希表记录每个用户的唯一活跃分钟数（set去重）。遍历logs，将每个用户的
# 活跃分钟加入其对应的set。然后统计每个UAM值对应的用户数量，填充答案数组。
#
# 时间复杂度: O(N + K)，其中N是logs的长度，K是k的值
# 空间复杂度: O(N + K)，哈希表存储用户和其唯一分钟数
#
# 关键点:
# - 使用defaultdict(set)自动为每个用户创建set
# - UAM是唯一分钟数，需要去重
# - answer数组是1索引，UAM为j的计数存在answer[j-1]位置
