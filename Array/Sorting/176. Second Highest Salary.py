"""
LeetCode #176 - Second Highest Salary
https://leetcode.com/problems/second-highest-salary/

Given salary values from the Employee table, return the second highest distinct
salary. If there is no second highest salary, return None.

Example 1:
    Input: salaries = [100, 200, 300]
    Output: 200

Example 2:
    Input: salaries = [100]
    Output: None

Example 3:
    Input: salaries = [100, 100, 200]
    Output: 100

Constraints:
    0 <= len(salaries) <= 10^4
    -10^6 <= salaries[i] <= 10^6
"""

from typing import List, Optional


class Solution:
    def secondHighestSalary(self, salaries: List[int]) -> Optional[int]:
        distinct = sorted(set(salaries), reverse=True)
        if len(distinct) < 2:
            return None
        return distinct[1]
