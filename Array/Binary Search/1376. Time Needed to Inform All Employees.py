"""
LeetCode #1376 - Time Needed to Inform All Employees
中文题名：通知所有员工所需的时间
https://leetcode.com/problems/time-needed-to-inform-all-employees/

A company has `n` employees with a unique ID for each employee from
`0` to `n - 1`. The head of the company has is the one with `headID`.

Each employee has one direct manager given in the `manager` array
where `manager[i]` is the direct manager of the `i-th`
employee, `manager[headID] = -1`. Also it's guaranteed that the
subordination relationships have a tree structure.

The head of the company wants to inform all the employees of the company of an urgent
piece of news. He will inform his direct subordinates and they will inform their
subordinates and so on until all employees know about the urgent news.

The `i-th` employee needs `informTime[i]` minutes to inform all
of his direct subordinates (i.e After informTime[i] minutes, all his direct
subordinates can start spreading the news).

Return the number of minutes needed to inform all the employees about the
urgent news.

Example 1:

Input: n = 1, headID = 0, manager = [-1], informTime = [0]
Output: 0
Explanation: The head of the company is the only employee in the company.

Example 2:

Input: n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0]
Output: 1
Explanation: The head of the company with id = 2 is the direct manager of all the employees in the company and needs 1 minute to inform them all.
The tree structure of the employees in the company is shown.

Example 3:

Input: n = 7, headID = 6, manager = [1,2,3,4,5,6,-1], informTime = [0,6,5,4,3,2,1]
Output: 21
Explanation: The head has id = 6. He will inform employee with id = 5 in 1 minute.
The employee with id = 5 will inform the employee with id = 4 in 2 minutes.
The employee with id = 4 will inform the employee with id = 3 in 3 minutes.
The employee with id = 3 will inform the employee with id = 2 in 4 minutes.
The employee with id = 2 will inform the employee with id = 1 in 5 minutes.
The employee with id = 1 will inform the employee with id = 0 in 6 minutes.
Needed time = 1 + 2 + 3 + 4 + 5 + 6 = 21.

Example 4:

Input: n = 15, headID = 0, manager = [-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6], informTime = [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]
Output: 3
Explanation: The first minute the head will inform employees 1 and 2.
The second minute they will inform employees 3, 4, 5 and 6.
The third minute they will inform the rest of employees.

Example 5:

Input: n = 4, headID = 2, manager = [3,3,-1,2], informTime = [0,0,162,914]
Output: 1076

Constraints:

`1 <= n <= 10^5`

`0 <= headID < n`

`manager.length == n`

`0 <= manager[i] < n`

`manager[headID] == -1`

`informTime.length == n`

`0 <= informTime[i] <= 1000`

`informTime[i] == 0` if employee `i` has no
subordinates.

It is guaranteed that all the employees can be informed.

【中文翻译】
公司有 `n` 名员工，每个员工的唯一 ID 从 `0` 到 `n - 1`。公司老板是 `headID`。

每个员工有一个直接经理，由 `manager` 数组给出，其中 `manager[i]` 是第 `i` 个员工的直接经理，`manager[headID] = -1`。保证从属关系呈树状结构。

公司老板希望向所有员工通知紧急消息。他将通知其直接下属，下属再通知他们的下属，直到所有员工都知悉该紧急消息。

第 `i` 个员工需要 `informTime[i]` 分钟来通知其所有直接下属（即在 `informTime[i]` 分钟后，其所有直接下属可以开始传播消息）。

返回通知所有员工所需的分钟数。

示例 1：
输入：n = 1, headID = 0, manager = [-1], informTime = [0]
输出：0
解释：公司老板是公司中唯一的员工。

示例 2：
输入：n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0]
输出：1
解释：id = 2 的老板是公司所有员工的直接经理，需要 1 分钟来通知所有员工。

示例 3：
输入：n = 7, headID = 6, manager = [1,2,3,4,5,6,-1], informTime = [0,6,5,4,3,2,1]
输出：21
解释：老板 id = 6，他将在 1 分钟内通知 id = 5 的员工。
id = 5 将在 2 分钟内通知 id = 4。
id = 4 将在 3 分钟内通知 id = 3。
id = 3 将在 4 分钟内通知 id = 2。
id = 2 将在 5 分钟内通知 id = 1。
id = 1 将在 6 分钟内通知 id = 0。
总时间 = 1 + 2 + 3 + 4 + 5 + 6 = 21。

示例 4：
输入：n = 15, headID = 0, manager = [-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6], informTime = [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]
输出：3
解释：第一分钟老板通知员工 1 和 2。
第二分钟他们通知员工 3、4、5 和 6。
第三分钟他们通知其余员工。

示例 5：
输入：n = 4, headID = 2, manager = [3,3,-1,2], informTime = [0,0,162,914]
输出：1076
"""

from typing import List
from collections import defaultdict, deque


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # 构建邻接表：manager -> subordinates
        graph = defaultdict(list)
        for emp_id, mgr in enumerate(manager):
            if mgr != -1:
                graph[mgr].append(emp_id)

        # DFS 计算到达每个员工的最大时间
        def dfs(node: int) -> int:
            if not graph[node]:
                return 0
            max_sub_time = 0
            for sub in graph[node]:
                max_sub_time = max(max_sub_time, dfs(sub))
            return informTime[node] + max_sub_time

        return dfs(headID)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 构建树形结构，从根节点（headID）DFS 计算到达每个叶子节点的最大时间。
# 1. 用 manager 数组构建邻接表（manager -> list of subordinates）。
# 2. 从 headID 开始 DFS：对于每个节点，递归计算其所有下属子树的通知时间，
#    取最大值加上当前节点的 informTime 作为当前节点子树的总通知时间。
# 3. 根节点的总通知时间即为答案（所有员工都被通知到的总时间）。
#
# 时间复杂度: O(N)，N 为员工数，每个员工访问一次
# 空间复杂度: O(N)，邻接表和递归栈
#
# 关键点:
# - 树形结构的 DFS：通知时间 = 当前节点 informTime + max(所有子树通知时间)
# - 下沉通知是并行的（同级下属同时被通知），所以取最大值而非求和
# - manager 数组反向构建邻接表便于从上往下遍历













