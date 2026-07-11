"""
LeetCode #690 - Employee Importance
中文题名：员工的重要性
https://leetcode.com/problems/employee-importance/

You are given a data structure of employee information, which includes the employee's unique
id, his importance value and his direct subordinates' id.

For example, employee 1 is the leader of employee 2, and employee 2 is the leader of employee
3. They have importance value 15, 10 and 5, respectively. Then employee 1 has a data
structure like [1, 15, [2]], and employee 2 has [2, 10, [3]], and employee 3 has [3, 5, []].
Note that although employee 3 is also a subordinate of employee 1, the relationship is not
direct.

Now given the employee information of a company, and an employee id, you need to return the
total importance value of this employee and all his subordinates.

Example 1:

Input: [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1
Output: 11
Explanation:
Employee 1 has importance value 5, and he has two direct subordinates: employee 2 and employee 3. They both have importance value 3. So the total importance value of employee 1 is 5 + 3 + 3 = 11.

Note:

One employee has at most one direct leader and may have several subordinates.

The maximum number of employees won't exceed 2000.

【中文翻译】
给定一个员工信息的数据结构，包含员工的唯一 ID、他的重要性值和他的直接下属的 ID。

例如，员工 1 是员工 2 的上级，员工 2 是员工 3 的上级。他们的重要性值分别为 15、10 和 5。那么员工 1 的数据结构为 [1, 15, [2]]，员工 2 的数据结构为 [2, 10, [3]]，员工 3 的数据结构为 [3, 5, []]。注意虽然员工 3 也是员工 1 的下属，但不是直接下属关系。

现在给定一家公司的员工信息，以及一个员工 ID，你需要返回该员工及其所有下属的重要性值之和。

示例 1：

输入: [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1
输出: 11
解释:
员工 1 的重要性值为 5，他有两个直接下属：员工 2 和员工 3。他们的重要性值都是 3。因此员工 1 的总重要性值为 5 + 3 + 3 = 11。

注意：

一个员工最多有一个直接上级，但可以有多个下属。

员工数量最多不超过 2000。
"""

from typing import List, Optional


class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        emp_map = {e.id: e for e in employees}

        def dfs(eid: int) -> int:
            emp = emp_map[eid]
            total = emp.importance
            for sub_id in emp.subordinates:
                total += dfs(sub_id)
            return total

        return dfs(id)









# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 先构建 id -> Employee 的哈希映射以支持 O(1) 查找。
# 使用 DFS 从目标员工开始递归向下计算：
# - 当前员工的总重要性 = 自身重要性 + 所有直接下属的总重要性（递归）。
# - 由于员工关系形成树结构（一个员工最多一个上级），无需担心循环。
# 也可以用 BFS（队列）实现。
#
# 时间复杂度: O(N) - 每个员工访问一次
# 空间复杂度: O(N) - 存储 id 映射和递归栈（最坏退化为链表）
#
# 关键点:
# - 预处理：哈希表映射 id -> Employee 对象
# - DFS 递归累加下属的重要性
# - 树形结构保证无环
