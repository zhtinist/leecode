"""
LeetCode #1282 - Group the People Given the Group Size They Belong To
中文题名：用户分组
https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/

There are `n` people whose IDs go from `0` to
`n - 1` and each person belongs exactly to one group.
Given the array `groupSizes` of length `n` telling the group
size each person belongs to, return the groups there are and the people's IDs
each group includes.

You can return any solution in any order and the same applies for IDs. Also, it is
guaranteed that there exists at least one solution.

Example 1:

Input: groupSizes = [3,3,3,3,3,1,3]
Output: [[5],[0,1,2],[3,4,6]]
Explanation:
Other possible solutions are [[2,1,6],[5],[0,4,3]] and [[5],[0,6,2],[4,3,1]].

Example 2:

Input: groupSizes = [2,1,3,3,3,2]
Output: [[1],[0,5],[2,3,4]]

Constraints:

`groupSizes.length == n`

`1 <= n <= 500`

`1 <= groupSizes[i] <= n`

【中文翻译】
有 n 个人，他们的 ID 从 0 到 n - 1，每个人恰好属于一个组。给定一个长度为 n 的数组 groupSizes，表示每个人所属组的大小。返回存在的组以及每个组包含的人的 ID。

你可以以任意顺序返回任意解，ID 也是如此。同时，保证至少存在一个解。

示例 1：

输入：groupSizes = [3,3,3,3,3,1,3]
输出：[[5],[0,1,2],[3,4,6]]
解释：
其他可能的解包括 [[2,1,6],[5],[0,4,3]] 和 [[5],[0,6,2],[4,3,1]]。

示例 2：

输入：groupSizes = [2,1,3,3,3,2]
输出：[[1],[0,5],[2,3,4]]

约束条件：

groupSizes.length == n
1 <= n <= 500
1 <= groupSizes[i] <= n
"""

from typing import List, Optional


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        from collections import defaultdict
        size_to_people = defaultdict(list)
        result = []

        for person_id, size in enumerate(groupSizes):
            size_to_people[size].append(person_id)
            if len(size_to_people[size]) == size:
                result.append(size_to_people[size])
                size_to_people[size] = []

        return result










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用哈希表将人按其组大小分组。
# 遍历每个人，将其 ID 添加到对应组大小的列表中。
# 当某个组大小的列表长度达到该组大小时，说明这组人已满，
# 将其加入结果列表并清空该列表，以便重新收集下一组。
# 由于保证有解，每个组大小的人数必然是该大小的整数倍，
# 因此这种贪心策略一定成功。
#
# 时间复杂度: O(n) - 遍历每个人一次，每次操作 O(1)
# 空间复杂度: O(n) - 哈希表存储所有人员 ID
#
# 关键点:
# - 使用字典将 groupSizes[i] 作为键，人员 ID 列表作为值
# - 列表长度达到 groupSize 时立即输出一组，保证不遗漏
# - 题目保证有解，不需验证输入合法性
