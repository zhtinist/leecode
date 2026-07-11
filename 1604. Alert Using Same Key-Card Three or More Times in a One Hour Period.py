"""
LeetCode #1604 - Alert Using Same Key-Card Three or More Times in a One Hour Period
中文题名：警告一小时内使用相同员工卡大于等于三次的人
https://leetcode.com/problems/alert-using-same-key-card-three-or-more-times-in-a-one-hour-period/

Leetcode company workers use key-cards to unlock office doors. Each time a worker
uses their key-card, the security system saves the worker's name and the time when it
was used. The system emits an alert if any worker uses the key-card
three or more times in a one-hour period.

You are given a list of strings `keyName` and `keyTime` where
`[keyName[i], keyTime[i]]` corresponds to a person's name and the time
when their key-card was used in a single day.

Access times are given in the 24-hour time format "HH:MM", such as
`"23:51"` and `"09:49"`.

Return a list of unique worker names who received an alert for frequent keycard
use. Sort the names in ascending order alphabetically.

Notice that `"10:00"` - `"11:00"` is considered to be within a
one-hour period, while `"23:51"` - `"00:10"` is not considered
to be within a one-hour period.

Example 1:

Input: keyName = ["daniel","daniel","daniel","luis","luis","luis","luis"], keyTime = ["10:00","10:40","11:00","09:00","11:00","13:00","15:00"]
Output: ["daniel"]
Explanation: "daniel" used the keycard 3 times in a one-hour period ("10:00","10:40", "11:00").

Example 2:

Input: keyName = ["alice","alice","alice","bob","bob","bob","bob"], keyTime = ["12:01","12:00","18:00","21:00","21:20","21:30","23:00"]
Output: ["bob"]
Explanation: "bob" used the keycard 3 times in a one-hour period ("21:00","21:20", "21:30").

Example 3:

Input: keyName = ["john","john","john"], keyTime = ["23:58","23:59","00:01"]
Output: []

Example 4:

Input: keyName = ["leslie","leslie","leslie","clare","clare","clare","clare"], keyTime = ["13:00","13:20","14:00","18:00","18:51","19:30","19:49"]
Output: ["clare","leslie"]

Constraints:

`1 <= keyName.length, keyTime.length <= 105`

`keyName.length == keyTime.length`

`keyTime` are in the format "HH:MM".

`[keyName[i], keyTime[i]]` is unique.

`1 <= keyName[i].length <= 10`

`keyName[i] contains only lowercase English letters.`

【中文翻译】
给定员工姓名列表 keyName 和时间列表 keyTime，每个员工每次刷卡系统会记录姓名和时间（24小时制 "HH:MM"）。
如果任何员工在一小时内使用员工卡三次或以上，系统会发出警报。返回所有收到警报的员工姓名，按字母升序排列。
注意 "10:00"-"11:00" 被视为一小时内，但跨天的 "23:51"-"00:10" 不算。

示例 1：
输入: keyName = ["daniel","daniel","daniel","luis","luis","luis","luis"], keyTime = ["10:00","10:40","11:00","09:00","11:00","13:00","15:00"]
输出: ["daniel"]
解释: "daniel" 在一小时内使用了三次卡 ("10:00","10:40","11:00")。

示例 2：
输入: keyName = ["alice","alice","alice","bob","bob","bob","bob"], keyTime = ["12:01","12:00","18:00","21:00","21:20","21:30","23:00"]
输出: ["bob"]
解释: "bob" 在一小时内使用了三次卡 ("21:00","21:20","21:30")。

示例 3：
输入: keyName = ["john","john","john"], keyTime = ["23:58","23:59","00:01"]
输出: [] (跨天不算一小时内)

示例 4：
输入: keyName = ["leslie","leslie","leslie","clare","clare","clare","clare"], keyTime = ["13:00","13:20","14:00","18:00","18:51","19:30","19:49"]
输出: ["clare","leslie"]
"""

from typing import List, Optional
from collections import defaultdict


class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        def to_minutes(t: str) -> int:
            h, m = t.split(":")
            return int(h) * 60 + int(m)

        # 按员工分组，记录所有刷卡时间（转换为分钟）
        records = defaultdict(list)
        for name, time in zip(keyName, keyTime):
            records[name].append(to_minutes(time))

        alert_list = []
        for name in sorted(records):
            times = sorted(records[name])
            # 滑动窗口：检查是否存在三个时间在60分钟内
            for i in range(len(times) - 2):
                if times[i + 2] - times[i] <= 60:
                    alert_list.append(name)
                    break
        return alert_list



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 1. 将每个员工的时间转换为分钟数（便于比较），按员工名分组存储
# 2. 对每个员工的时间排序后使用滑动窗口：检查是否存在三个连续时间差 <= 60 分钟
# 3. 满足条件则该员工触发警报，加入结果集
# 4. 返回按字母序升序排序的结果
#
# 时间复杂度: O(N log N) — 每个员工的时间排序，N为总刷卡次数；最坏情况所有刷卡属于同一员工
# 空间复杂度: O(N) — 存储所有刷卡记录的分组字典
#
# 关键点:
# - 将 HH:MM 转换为分钟数统一比较
# - 滑动窗口只需检查 i 和 i+2 的差值（中间那个自然也在范围内）
# - 跨天的不算一小时内：无需特殊处理，时间按同一天计算
