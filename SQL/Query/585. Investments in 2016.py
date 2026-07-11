"""
LeetCode #585 - Investments in 2016
中文题名：2016年的投资
https://leetcode.com/problems/investments-in-2016/

Write a query to print the sum of all total investment values in 2016 (TIV_2016), to a
scale of 2 decimal places, for all policy holders who meet the following criteria:

Have the same TIV_2015 value as one or more other policyholders.

Are not located in the same city as any other policyholder (i.e.: the (latitude,
longitude) attribute pairs must be unique).

Input Format:

The insurance table is described as follows:

| Column Name | Type          |
|-------------|---------------|
| PID         | INTEGER(11)   |
| TIV_2015    | NUMERIC(15,2) |
| TIV_2016    | NUMERIC(15,2) |
| LAT         | NUMERIC(5,2)  |
| LON         | NUMERIC(5,2)  |

where PID is the policyholder's policy ID, TIV_2015 is the total investment
value in 2015, TIV_2016 is the total investment value in 2016, LAT is the
latitude of the policy holder's city, and LON is the longitude of the policy
holder's city.

Sample Input

| PID | TIV_2015 | TIV_2016 | LAT | LON |
|-----|----------|----------|-----|-----|
| 1   | 10       | 5        | 10  | 10  |
| 2   | 20       | 20       | 20  | 20  |
| 3   | 10       | 30       | 20  | 20  |
| 4   | 10       | 40       | 40  | 40  |

Sample Output

| TIV_2016 |
|----------|
| 45.00    |

Explanation

The first record in the table, like the last record, meets both of the two criteria.
The TIV_2015 value '10' is as the same as the third and forth record, and its location unique.

The second record does not meet any of the two criteria. Its TIV_2015 is not like any other policyholders.

And its location is the same with the third record, which makes the third record fail, too.

So, the result is the sum of TIV_2016 of the first and last record, which is 45.

【中文翻译】
编写一个查询，计算 2016 年所有满足以下条件的投保人的总投资价值 (TIV_2016) 之和，保留两位小数：

1. 与一个或多个其他投保人具有相同的 TIV_2015 值。
2. 不与其他投保人位于同一城市（即 (LAT, LON) 属性对必须唯一）。

`insurance` 表结构：

| Column Name | Type          |
|-------------|---------------|
| PID         | INTEGER(11)   |
| TIV_2015    | NUMERIC(15,2) |
| TIV_2016    | NUMERIC(15,2) |
| LAT         | NUMERIC(5,2)  |
| LON         | NUMERIC(5,2)  |

其中 PID 是投保人的保单 ID，TIV_2015 是 2015 年总投资价值，TIV_2016 是 2016 年总投资价值，
LAT 是投保人所在城市的纬度，LON 是经度。

示例输入：

| PID | TIV_2015 | TIV_2016 | LAT | LON |
|-----|----------|----------|-----|-----|
| 1   | 10       | 5        | 10  | 10  |
| 2   | 20       | 20       | 20  | 20  |
| 3   | 10       | 30       | 20  | 20  |
| 4   | 10       | 40       | 40  | 40  |

输出：

| TIV_2016 |
|----------|
| 45.00    |

解释：
第一条记录（PID=1）和最后一条记录（PID=4）都满足两个条件：
- TIV_2015 值 '10' 与第三条和第四条记录相同（满足条件1）
- 位置唯一（满足条件2）

第二条记录不满足任何条件：其 TIV_2015 与其他人都不同。
第三条记录虽然 TIV_2015 与他人相同，但其位置与第二条记录相同，因此被排除。

最终结果为第一条和最后一条记录的 TIV_2016 之和：5 + 40 = 45。
"""

from typing import List, Optional


class Solution:
    def investmentsIn2016(self, insurances: List[dict]) -> Optional[float]:
        """
        SQL Solution:
            SELECT ROUND(SUM(TIV_2016), 2) AS TIV_2016
            FROM insurance
            WHERE TIV_2015 IN (
                SELECT TIV_2015
                FROM insurance
                GROUP BY TIV_2015
                HAVING COUNT(*) > 1
            )
            AND (LAT, LON) IN (
                SELECT LAT, LON
                FROM insurance
                GROUP BY LAT, LON
                HAVING COUNT(*) = 1
            );
        """
        pass



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 需要同时满足两个条件，使用 WHERE 子句分别用子查询筛选：
# 1. TIV_2015 值在表中出现超过一次（GROUP BY TIV_2015 HAVING COUNT(*) > 1）；
# 2. (LAT, LON) 位置对在表中唯一（GROUP BY LAT, LON HAVING COUNT(*) = 1）。
# 两条子查询用 AND 连接，对符合条件行的 TIV_2016 求和并用 ROUND 保留两位小数。
#
# 时间复杂度: O(N)
# 空间复杂度: O(N)（子查询临时结果集）
#
# 关键点:
# - 使用元组 (LAT, LON) 联合判断地理位置唯一性
# - TIV_2015 需要出现至少2次（> 1 而非 >= 2，效果相同）
# - 两个条件用 AND 连接，必须同时满足
# - ROUND(SUM(...), 2) 确保输出两位小数
