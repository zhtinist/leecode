"""
LeetCode #3611 - Find Overbooked Employees
查找超预订员工
https://leetcode.cn/problems/find-overbooked-employees/

表：`employees`
+---------------+---------+ | Column Name   | Type    | +---------------+---------+ | employee_id   | int     | | employee_name | varchar | | department    | varchar | +---------------+---------+ employee_id 是这张表的唯一主键。 每一行包含一个员工和他们部门的信息。
表：`meetings`
+---------------+---------+ | Column Name   | Type    | +---------------+---------+ | meeting_id    | int     | | employee_id   | int     | | meeting_date  | date    | | meeting_type  | varchar | | duration_hours| decimal | +---------------+---------+ meeting_id 是这张表的唯一主键。 每一行表示一位员工参加的会议。meeting_type 可以是 'Team'，'Client' 或 'Training'。
编写一个解决方案来查找会议密集型的员工 -  在任何给定周内，花费超过 `50%` 工作时间在会议上的员工。
假定一个标准工作周是 `40` 小时
计算每位员工 每周（周一至周日）的 总会议小时数
员工如果每周会议时间超过 `20` 小时（`40` 小时工作时间的 `50%`），则被视为会议密集型。
统计每位员工有多少周是会议密集周
仅查找 至少 `2` 周会议密集的员工
返回结果表按会议密集周的数量降序排列，然后按员工姓名升序排列。结果格式如下所示。

示例：

Input:
employees 表：
+-------------+----------------+-------------+ | employee_id | employee_name  | department  | +-------------+----------------+-------------+ | 1           | Alice Johnson  | Engineering | | 2           | Bob Smith      | Marketing   | | 3           | Carol Davis    | Sales       | | 4           | David Wilson   | Engineering | | 5           | Emma Brown     | HR          | +-------------+----------------+-------------+
meetings 表：
+------------+-------------+--------------+--------------+----------------+ | meeting_id | employee_id | meeting_date | meeting_type | duration_hours | +------------+-------------+--------------+--------------+----------------+ | 1          | 1           | 2023-06-05   | Team         | 8.0            | | 2          | 1           | 2023-06-06   | Client       | 6.0            | | 3          | 1           | 2023-06-07   | Training     | 7.0            | | 4          | 1           | 2023-06-12   | Team         | 12.0           | | 5          | 1           | 2023-06-13   | Client       | 9.0            | | 6          | 2           | 2023-06-05   | Team         | 15.0           | | 7          | 2           | 2023-06-06   | Client       | 8.0            | | 8          | 2           | 2023-06-12   | Training     | 10.0           | | 9          | 3           | 2023-06-05   | Team         | 4.0            | | 10         | 3           | 2023-06-06   | Client       | 3.0            | | 11         | 4           | 2023-06-05   | Team         | 25.0           | | 12         | 4           | 2023-06-19   | Client       | 22.0           | | 13         | 5           | 2023-06-05   | Training     | 2.0            | +------------+-------------+--------------+--------------+----------------+
输出：
+-------------+----------------+-------------+---------------------+ | employee_id | employee_name  | department  | meeting_heavy_weeks | +-------------+----------------+-------------+---------------------+ | 1           | Alice Johnson  | Engineering | 2                   | | 4           | David Wilson   | Engineering | 2                   | +-------------+----------------+-------------+---------------------+
解释：
Alice Johnson (employee_id = 1):
6 月 5 日至 11 日（2023-06-05 至 2023-06-11）：8.0 + 6.0 + 7.0 = 21.0 小时（> 20 小时）
6 月 12 日至 18 日（2023-06-12 至 2023-06-18）: 12.0 + 9.0 = 21.0 小时（> 20 小时）
2 周会议密集
David Wilson (employee_id = 4):
6 月 5 日至 11 日：25.0 小时（> 20 小时）
6 月 19 日至 25 日：22.0 小时（> 20 小时）
2 周会议密集
未包含的员工：
Bob Smith（employee_id = 2）：6 月 5 日至 11 日：15.0 + 8.0 = 23.0 小时（> 20），6 月 12 日至 18 日：10.0 小时（< 20）。只有 1 个会议密集周。
Carol Davis（employee_id = 3）：6 月 5 日至 11 日：4.0 + 3.0 = 7.0 小时（< 20）。没有会议密集周。
Emma Brown（employee_id = 5）：6 月 5 日至 11 日：2.0 小时（< 20）。没有会议密集周。
结果表按 meeting_heavy_weeks 降序排列，然后按员工姓名升序排列。
"""

from typing import List, Optional


class Solution:
    def findOverbookedEmployees(self, employees: List[dict], meetings: List[dict]) -> List[dict]:
        from datetime import datetime, timedelta
        from collections import defaultdict

        # Map employee_id -> (name, department)
        emp_info = {}
        for e in employees:
            emp_info[e['employee_id']] = (e['employee_name'], e['department'])

        # Group meetings by employee_id
        emp_meetings = defaultdict(list)
        for m in meetings:
            emp_meetings[m['employee_id']].append(m)

        results = []
        for emp_id, mtgs in emp_meetings.items():
            # Aggregate meeting hours per week (Monday-to-Sunday)
            week_hours = defaultdict(float)
            for m in mtgs:
                dt = datetime.strptime(str(m['meeting_date']), '%Y-%m-%d')
                # Monday of the current week
                monday = dt - timedelta(days=dt.weekday())
                week_key = monday.strftime('%Y-%m-%d')
                week_hours[week_key] += float(m['duration_hours'])

            # Count weeks where meeting hours > 20 (50% of 40-hour work week)
            heavy_weeks = sum(1 for hours in week_hours.values() if hours > 20)

            if heavy_weeks >= 2:
                name, dept = emp_info[emp_id]
                results.append({
                    'employee_id': emp_id,
                    'employee_name': name,
                    'department': dept,
                    'meeting_heavy_weeks': heavy_weeks,
                })

        # Sort: meeting_heavy_weeks DESC, employee_name ASC
        results.sort(key=lambda x: (-x['meeting_heavy_weeks'], x['employee_name']))
        return results










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: 数据库
#
# 解题思路:
# 1. 将 employees 表映射为字典，方便根据 employee_id 快速获取姓名和部门
# 2. 将 meetings 按 employee_id 分组
# 3. 对每位员工的会议按周聚合（周一至周日为一周，用该周一日期作为周标识）
#    - 使用 Python datetime 计算 meeting_date 所在周的周一
#    - 累加同一周内的 duration_hours
# 4. 统计会议密集型周数：每周会议小时数 > 20（40 小时的 50%）
# 5. 筛选至少有 2 个会议密集周的员工
# 6. 按 meeting_heavy_weeks 降序、employee_name 升序排序返回
#
# 时间复杂度: O(E + M * log M) — E: employees 数量, M: meetings 数量, 排序开销
# 空间复杂度: O(E + M) — 存储员工信息和会议分组
#
# 关键点:
# - 周的定义：周一至周日，用周一日期作为该周唯一标识
# - 阈值 20 小时 = 40 * 50%
# - 至少 2 周为会议密集型才入选
# - 降序按 heavy_weeks、升序按姓名排序
