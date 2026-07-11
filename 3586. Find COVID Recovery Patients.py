"""
LeetCode #3586 - Find COVID Recovery Patients
寻找 COVID 康复患者
https://leetcode.cn/problems/find-covid-recovery-patients/

表：`patients`
+-------------+---------+ | Column Name | Type    | +-------------+---------+ | patient_id  | int     | | patient_name| varchar | | age         | int     | +-------------+---------+ patient_id 是这张表的唯一主键。 每一行表示一个患者的信息。
表：`covid_tests`
+-------------+---------+ | Column Name | Type    | +-------------+---------+ | test_id     | int     | | patient_id  | int     | | test_date   | date    | | result      | varchar | +-------------+---------+ test_id 是这张表的唯一主键。 每一行代表一个 COVID 检测结果。结果可以是阳性、阴性或不确定。
编写一个解决方案以找到从 COVID 中康复的患者——那些曾经检测呈阳性但后来检测呈阴性的患者。
患者如果 至少有一次阳性 检测结果后，在 之后的日期 至少有一次 阴性 检测结果，则被认为已康复。
计算从 首次阳性检测 结果到 该阳性检测 后的 首次阴性检测结果 之间的 康复时间（以天为单位）
仅包括 同时具有阳性及阴性检测结果的患者
返回结果表以 `recovery_time` 升序 排序，然后以 `patient_name` 升序 排序。
结果格式如下所示。

示例：

输入：
patients 表：
+------------+--------------+-----+ | patient_id | patient_name | age | +------------+--------------+-----+ | 1          | Alice Smith  | 28  | | 2          | Bob Johnson  | 35  | | 3          | Carol Davis  | 42  | | 4          | David Wilson | 31  | | 5          | Emma Brown   | 29  | +------------+--------------+-----+
covid_tests 表：
+---------+------------+------------+--------------+ | test_id | patient_id | test_date  | result       | +---------+------------+------------+--------------+ | 1       | 1          | 2023-01-15 | Positive     | | 2       | 1          | 2023-01-25 | Negative     | | 3       | 2          | 2023-02-01 | Positive     | | 4       | 2          | 2023-02-05 | Inconclusive | | 5       | 2          | 2023-02-12 | Negative     | | 6       | 3          | 2023-01-20 | Negative     | | 7       | 3          | 2023-02-10 | Positive     | | 8       | 3          | 2023-02-20 | Negative     | | 9       | 4          | 2023-01-10 | Positive     | | 10      | 4          | 2023-01-18 | Positive     | | 11      | 5          | 2023-02-15 | Negative     | | 12      | 5          | 2023-02-20 | Negative     | +---------+------------+------------+--------------+
输出：
+------------+--------------+-----+---------------+ | patient_id | patient_name | age | recovery_time | +------------+--------------+-----+---------------+ | 1          | Alice Smith  | 28  | 10            | | 3          | Carol Davis  | 42  | 10            | | 2          | Bob Johnson  | 35  | 11            | +------------+--------------+-----+---------------+
解释：
Alice Smith (patient_id = 1):
首次阳性检测：2023-01-15
阳性检测后的首次阴性检测：2023-01-25
康复时间：25 - 15 = 10 天
Bob Johnson (patient_id = 2):
首次阳性检测：2023-02-01
测试结果不明确：2023-02-05（忽略计算康复时间）
阳性检测后的首次阴性检测：2023-02-12
康复时间：12 - 1 = 11 天
Carol Davis (patient_id = 3):
检测呈阴性：2023-01-20（在阳性检测前）
首次阳性检测：2023-02-10
阳性检测后的首次阴性检测：2023-02-20
康复时间：20 - 10 = 10 天
没有包含的患者：
David Wilson（patient_id = 4）：只有阳性检测，之后没有阴性检测。
Emma Brown（patient_id = 5）：只有阴性检测，从未有阳性检测。
输出表以 recovery_time 升序排序，然后以 patient_name 升序排序。
"""

from typing import List, Optional


class Solution:
    def findCovidRecoveryPatients(
        self, patients: List[List], covid_tests: List[List]
    ) -> List[List]:
        """
        patients: list of [patient_id, patient_name, age]
        covid_tests: list of [test_id, patient_id, test_date, result]
        Returns: list of [patient_id, patient_name, age, recovery_time]
        """
        from collections import defaultdict

        # Group tests by patient
        patient_tests = defaultdict(list)
        for test in covid_tests:
            _, pid, date, result = test
            patient_tests[pid].append((date, result))

        # Patient lookup
        patient_info = {}
        for p in patients:
            pid, name, age = p
            patient_info[pid] = (name, age)

        results = []
        for pid, tests in patient_tests.items():
            # Sort by date
            tests.sort(key=lambda x: x[0])

            first_positive_date = None
            recovered = False
            recovery_time = None

            for date, result in tests:
                if result == "Positive" and first_positive_date is None:
                    first_positive_date = date
                elif result == "Negative" and first_positive_date is not None:
                    # Found first negative after first positive
                    from datetime import date as dt
                    d1 = dt.fromisoformat(first_positive_date)
                    d2 = dt.fromisoformat(date)
                    recovery_time = (d2 - d1).days
                    recovered = True
                    break

            if recovered and recovery_time is not None:
                name, age = patient_info[pid]
                results.append([pid, name, age, recovery_time])

        # Sort by recovery_time ASC, then patient_name ASC
        results.sort(key=lambda x: (x[3], x[1]))
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
# 1. 按 patient_id 分组每个患者的所有检测记录，并按日期排序。
# 2. 对每组记录：
#    a. 找到第一个阳性检测日期 (first_positive_date)。
#    b. 在第一个阳性日期之后，寻找第一个阴性检测日期。
#    c. 如果找到，计算两者的天数差作为 recovery_time。
# 3. 只包含同时有阳性和（之后）阴性检测的患者。
# 4. 按 recovery_time 升序、patient_name 升序排序返回结果。
# 注意：需忽略中间结果中的 "Inconclusive"（不确定），只看阳性和阴性。
#
# 时间复杂度: O(T log T + P)，其中 T 是检测记录数 (排序)，P 是患者数
# 空间复杂度: O(T + P)，存储分组后的检测记录和患者信息
#
# 关键点:
# - 必须先有阳性，之后再有阴性的才算康复
# - 康复时间是从第一个阳性到该阳性之后的第一个阴性
# - 不确定(Inconclusive)的检测结果不影响康复判断，直接忽略
# - 只包含有完整康复路径的患者
