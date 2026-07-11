"""
LeetCode #3601 - Find Drivers with Improved Fuel Efficiency
寻找燃油效率提升的驾驶员
https://leetcode.cn/problems/find-drivers-with-improved-fuel-efficiency/

表：`drivers`
+-------------+---------+ | Column Name | Type    | +-------------+---------+ | driver_id   | int     | | driver_name | varchar | +-------------+---------+ driver_id 是这张表的唯一主键。 每一行都包含一个司机的信息。
表：`trips`
+---------------+---------+ | Column Name   | Type    | +---------------+---------+ | trip_id       | int     | | driver_id     | int     | | trip_date     | date    | | distance_km   | decimal | | fuel_consumed | decimal | +---------------+---------+ trip_id 是这张表的唯一主键。 每一行表示一名司机完成的一次行程，包括该次行程行驶的距离和消耗的燃油量。
编写一个解决方案，通过 比较 司机在 上半年 和 下半年 的 平均燃油效率 来找出 燃油效率有所提高 的司机。
通过 `distance_km / fuel_consumed` 计算 每次 行程的 燃油效率。
上半年：一月到六月，下半年：七月到十二月
只包含在上半年和下半年都有行程的司机
通过（`second_half_avg - first_half_avg`）计算 提升效率。
将所有结果 四舍五入 到小数点后 `2` 位
返回结果表按提升效率 降序 排列，然后按司机姓名 升序 排列。
结果格式如下所示。

示例：

输入：
drivers 表：
+-----------+---------------+ | driver_id | driver_name   | +-----------+---------------+ | 1         | Alice Johnson | | 2         | Bob Smith     | | 3         | Carol Davis   | | 4         | David Wilson  | | 5         | Emma Brown    | +-----------+---------------+
trips 表：
+---------+-----------+------------+-------------+---------------+ | trip_id | driver_id | trip_date  | distance_km | fuel_consumed | +---------+-----------+------------+-------------+---------------+ | 1       | 1         | 2023-02-15 | 120.5       | 10.2          | | 2       | 1         | 2023-03-20 | 200.0       | 16.5          | | 3       | 1         | 2023-08-10 | 150.0       | 11.0          | | 4       | 1         | 2023-09-25 | 180.0       | 12.5          | | 5       | 2         | 2023-01-10 | 100.0       | 9.0           | | 6       | 2         | 2023-04-15 | 250.0       | 22.0          | | 7       | 2         | 2023-10-05 | 200.0       | 15.0          | | 8       | 3         | 2023-03-12 | 80.0        | 8.5           | | 9       | 3         | 2023-05-18 | 90.0        | 9.2           | | 10      | 4         | 2023-07-22 | 160.0       | 12.8          | | 11      | 4         | 2023-11-30 | 140.0       | 11.0          | | 12      | 5         | 2023-02-28 | 110.0       | 11.5          | +---------+-----------+------------+-------------+---------------+
输出：
+-----------+---------------+------------------+-------------------+------------------------+ | driver_id | driver_name   | first_half_avg   | second_half_avg   | efficiency_improvement | +-----------+---------------+------------------+-------------------+------------------------+ | 2         | Bob Smith     | 11.24            | 13.33             | 2.10                   | | 1         | Alice Johnson | 11.97            | 14.02             | 2.05                   | +-----------+---------------+------------------+-------------------+------------------------+
解释：
Alice Johnson (driver_id = 1):
上半年行程（一月到六月）：Feb 15 (120.5/10.2 = 11.81), Mar 20 (200.0/16.5 = 12.12)
上半年平均效率：(11.81 + 12.12) / 2 = 11.97
下半年行程（七月到十二月）：Aug 10 (150.0/11.0 = 13.64), Sep 25 (180.0/12.5 = 14.40)
下半年平均效率：(13.64 + 14.40) / 2 = 14.02
效率提升：14.02 - 11.97 = 2.05
Bob Smith (driver_id = 2):
上半年行程：Jan 10 (100.0/9.0 = 11.11), Apr 15 (250.0/22.0 = 11.36)
上半年平均效率：(11.11 + 11.36) / 2 = 11.24
下半年行程：Oct 5 (200.0/15.0 = 13.33)
下半年平均效率：13.33
效率提升：13.33 - 11.24 = 2.10（舍入到 2 位小数）
未包含的司机：
Carol Davis (driver_id = 3)：只有上半年的行程（三月，五月）
David Wilson (driver_id = 4)：只有下半年的行程（七月，十一月）
Emma Brown (driver_id = 5)：只有上半年的行程（二月）
输出表按提升效率降序排列，然后按司机名字升序排列。
"""

from typing import List, Optional


class Solution:
    def findDriversWithImprovedEfficiency(
        self, drivers: List[List], trips: List[List]
    ) -> List[List]:
        """
        drivers: list of [driver_id, driver_name]
        trips: list of [trip_id, driver_id, trip_date, distance_km, fuel_consumed]
        Returns: list of [driver_id, driver_name, first_half_avg,
                          second_half_avg, efficiency_improvement]
        """
        from collections import defaultdict

        # Group trips by driver
        driver_trips = defaultdict(list)
        for trip in trips:
            _, did, date, dist, fuel = trip
            driver_trips[did].append((date, float(dist), float(fuel)))

        # Driver lookup
        driver_info = {}
        for d in drivers:
            did, name = d
            driver_info[did] = name

        results = []
        for did, trip_list in driver_trips.items():
            first_half_effs = []
            second_half_effs = []

            for date, dist, fuel in trip_list:
                # Extract month from date string "YYYY-MM-DD"
                month = int(date.split('-')[1])
                efficiency = dist / fuel
                if 1 <= month <= 6:
                    first_half_effs.append(efficiency)
                elif 7 <= month <= 12:
                    second_half_effs.append(efficiency)

            # Only include drivers with trips in both halves
            if not first_half_effs or not second_half_effs:
                continue

            first_avg = sum(first_half_effs) / len(first_half_effs)
            second_avg = sum(second_half_effs) / len(second_half_effs)

            # Only include if efficiency improved
            improvement = second_avg - first_avg
            if improvement <= 0:
                continue

            results.append([
                did,
                driver_info[did],
                round(first_avg, 2),
                round(second_avg, 2),
                round(improvement, 2),
            ])

        # Sort by efficiency_improvement DESC, then driver_name ASC
        results.sort(key=lambda x: (-x[4], x[1]))
        return results











# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: 数据库
#
# 解题思路:
# 此题是 SQL 题，用 Python 模拟数据库查询逻辑。
# 1. 按 driver_id 分组所有行程记录。
# 2. 对每组行程：
#    a. 根据月份将行程分为上半年（1-6月）和下半年（7-12月）。
#    b. 分别计算两个半年的平均燃油效率（distance_km / fuel_consumed）。
#    c. 只保留在上半年和下半年都有行程的司机。
# 3. 计算效率提升：second_half_avg - first_half_avg。
#    只保留提升为正数的司机（效率真正提高了的）。
# 4. 将所有平均值和提升值四舍五入保留 2 位小数。
# 5. 按 efficiency_improvement 降序、driver_name 升序排序返回。
#
# 时间复杂度: O(T + D log D)，其中 T 是行程数，D 是符合条件的司机数（用于排序）
# 空间复杂度: O(T + D)，存储分组后的行程数据
#
# 关键点:
# - 燃油效率 = distance_km / fuel_consumed（不是反过来）
# - 使用原始平均值计算提升值，然后再四舍五入（而非用舍入后的值相减）
# - 只包含两个半年都有行程的司机
# - 效率提升必须为正数（second_half > first_half）
