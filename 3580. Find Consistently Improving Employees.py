"""
LeetCode #3580 - Find Consistently Improving Employees
寻找持续进步的员工
https://leetcode.cn/problems/find-consistently-improving-employees/

表：`employees`
+-------------+---------+ | Column Name | Type    | +-------------+---------+ | employee_id | int     | | name        | varchar | +-------------+---------+ employee_id 是这张表的唯一主键。 每一行包含一名员工的信息。
表：`performance_reviews`
+-------------+------+ | Column Name | Type | +-------------+------+ | review_id   | int  | | employee_id | int  | | review_date | date | | rating      | int  | +-------------+------+ review_id 是这张表的唯一主键。 每一行表示一名员工的绩效评估。评分在 1-5 的范围内，5分代表优秀，1分代表较差。
编写一个解决方案，以找到在过去三次评估中持续提高绩效的员工。
员工 至少需要 `3` 次评估 才能被考虑
员工过去的 `3` 次评估，评分必须 严格递增（每次评价都比上一次好）
根据 `review_date` 为每位员工分析最近的 `3` 次评估
进步分数 为最后 `3` 次评估中最后一次评分与最早一次评分之间的差值
返回结果表以 进步分数 降序 排序，然后以 名字 升序 排序。
结果格式如下所示。

示例：

输入：
employees 表：
+-------------+----------------+ | employee_id | name           | +-------------+----------------+ | 1           | Alice Johnson  | | 2           | Bob Smith      | | 3           | Carol Davis    | | 4           | David Wilson   | | 5           | Emma Brown     | +-------------+----------------+
performance_reviews 表：
+-----------+-------------+-------------+--------+ | review_id | employee_id | review_date | rating | +-----------+-------------+-------------+--------+ | 1         | 1           | 2023-01-15  | 2      | | 2         | 1           | 2023-04-15  | 3      | | 3         | 1           | 2023-07-15  | 4      | | 4         | 1           | 2023-10-15  | 5      | | 5         | 2           | 2023-02-01  | 3      | | 6         | 2           | 2023-05-01  | 2      | | 7         | 2           | 2023-08-01  | 4      | | 8         | 2           | 2023-11-01  | 5      | | 9         | 3           | 2023-03-10  | 1      | | 10        | 3           | 2023-06-10  | 2      | | 11        | 3           | 2023-09-10  | 3      | | 12        | 3           | 2023-12-10  | 4      | | 13        | 4           | 2023-01-20  | 4      | | 14        | 4           | 2023-04-20  | 4      | | 15        | 4           | 2023-07-20  | 4      | | 16        | 5           | 2023-02-15  | 3      | | 17        | 5           | 2023-05-15  | 2      | +-----------+-------------+-------------+--------+
输出：
+-------------+----------------+-------------------+ | employee_id | name           | improvement_score | +-------------+----------------+-------------------+ | 2           | Bob Smith      | 3                 | | 1           | Alice Johnson  | 2                 | | 3           | Carol Davis    | 2                 | +-------------+----------------+-------------------+
解释：
Alice Johnson (employee_id = 1)：
有 4 次评估，分数：2, 3, 4, 5
最后 3 次评估（按日期）：2023-04-15 (3), 2023-07-15 (4), 2023-10-15 (5)
评分严格递增：3 → 4 → 5
进步分数：5 - 3 = 2
Carol Davis (employee_id = 3)：
有 4 次评估，分数：1, 2, 3, 4
最后 3 次评估（按日期）：2023-06-10 (2)，2023-09-10 (3)，2023-12-10 (4)
评分严格递增：2 → 3 → 4
进步分数：4 - 2 = 2
Bob Smith (employee_id = 2)：
有 4 次评估，分数：3，2，4，5
最后 3 次评估（按日期）：2023-05-01 (2)，2023-08-01 (4)，2023-11-01 (5)
评分严格递增：2 → 4 → 5
进步分数：5 - 2 = 3
未包含的员工：
David Wilson (employee_id = 4)：之前 3 次评估都是 4 分（没有进步）
Emma Brown (employee_id = 5)：只有 2 次评估（需要至少 3 次）
输出表以 improvement_score 降序排序，然后以 name 升序排序。
"""

from typing import List, Optional
import pandas as pd


class Solution:
    def findConsistentlyImprovingEmployees(
        self, employees: pd.DataFrame, performance_reviews: pd.DataFrame
    ) -> pd.DataFrame:
        """
        使用 pandas 模拟 SQL 逻辑：
        1. 按 employee_id 分组，每组按 review_date 降序取最近 3 条记录
        2. 按日期升序排列这 3 条记录，检查 rating 是否严格递增
        3. 计算进步分数 = 最近评分 - 最早评分（在最近 3 次中）
        4. 与 employees 表关联获取 name
        5. 按 improvement_score DESC, name ASC 排序
        """
        # 按 employee_id 分组，按 review_date 降序排名
        reviews = performance_reviews.copy()
        reviews['rn'] = reviews.groupby('employee_id')['review_date'].rank(
            ascending=False, method='first'
        )

        # 只保留每位员工最近 3 次评估
        recent3 = reviews[reviews['rn'] <= 3].copy()

        # 过滤掉评估次数不足 3 次的员工
        emp_review_counts = recent3.groupby('employee_id').size()
        valid_emps = emp_review_counts[emp_review_counts == 3].index
        recent3 = recent3[recent3['employee_id'].isin(valid_emps)]

        # 对每位员工的最近 3 次评估按日期升序排列
        recent3 = recent3.sort_values(['employee_id', 'review_date'])

        # 对于每位员工，检查 rating 是否严格递增
        # groupby 后取 rating 列表
        def check_improving(group):
            ratings = group['rating'].tolist()
            if len(ratings) < 3:
                return pd.Series({
                    'is_improving': False,
                    'improvement_score': 0
                })
            # 检查严格递增
            is_inc = ratings[0] < ratings[1] < ratings[2]
            score = ratings[2] - ratings[0] if is_inc else 0
            return pd.Series({
                'is_improving': is_inc,
                'improvement_score': score
            })

        result = recent3.groupby('employee_id').apply(check_improving).reset_index()

        # 只保留持续进步的员工
        result = result[result['is_improving']]

        # 关联 employees 表获取 name
        result = result.merge(employees, on='employee_id')

        # 选择输出列并排序
        result = result[['employee_id', 'name', 'improvement_score']]
        result = result.sort_values(
            ['improvement_score', 'name'],
            ascending=[False, True]
        )

        return result










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: 数据库
#
# 解题思路:
# 使用 pandas 模拟 SQL 窗口函数和分组逻辑：
# 1. 对 performance_reviews 按 employee_id 分组，使用 rank 函数按 review_date 降序排名，
#    筛选出每位员工最近（日期最新）的 3 条记录（rn ≤ 3）。
# 2. 过滤掉总评估次数不足 3 次的员工（groupby 后 count < 3 的分组）。
# 3. 对每位员工的 3 条记录按 review_date 升序排列后，检查 rating 是否严格递增
#    （即 rating[0] < rating[1] < rating[2]）。
# 4. 对于满足严格递增的员工，计算进步分数 = rating[2] - rating[0]。
# 5. 与 employees 表关联获取员工姓名，按 improvement_score 降序、name 升序排序输出。
#
# 时间复杂度: O(N log N) — 主要为排序和分组操作
# 空间复杂度: O(N)
#
# 关键点:
# - 取每位员工最近（按日期）的 3 次评估，而非任意 3 次
# - 评分必须严格递增（不能相等）
# - 进步分数 = 最后一次评分 - 第一次评分（在最近 3 次中）
# - 员工评估次数 < 3 的直接排除
