"""
LeetCode #177 - Nth Highest Salary
https://leetcode.com/problems/nth-highest-salary/

Given salary values from the Employee table and an integer n, return the nth
highest distinct salary. If there are fewer than n distinct salaries, return
None.

Example 1:
    Input: salaries = [100, 200, 300], n = 2
    Output: 200

Example 2:
    Input: salaries = [100], n = 2
    Output: None

Example 3:
    Input: salaries = [100, 100, 200, 300], n = 3
    Output: 100

Constraints:
    0 <= len(salaries) <= 10^4
    -10^6 <= salaries[i] <= 10^6
    1 <= n <= 10^4
"""

from typing import List, Optional


class Solution:
    def getNthHighestSalary(self, salaries: List[int], n: int) -> Optional[int]:
        pass
