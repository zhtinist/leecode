"""
LeetCode #1306 - Jump Game III
中文题名：跳跃游戏 III
https://leetcode.com/problems/jump-game-iii/

Given an array of non-negative integers `arr`, you are initially
positioned at `start` index of the array. When you are at index
`i`, you can jump to `i + arr[i]` or `i - arr[i]`,
check if you can reach to any index with value 0.

Notice that you can not jump outside of the array at any time.

Example 1:

Input: arr = [4,2,3,0,3,1,2], start = 5
Output: true
Explanation:
All possible ways to reach at index 3 with value 0 are:
index 5 -> index 4 -> index 1 -> index 3
index 5 -> index 6 -> index 4 -> index 1 -> index 3

Example 2:

Input: arr = [4,2,3,0,3,1,2], start = 0
Output: true
Explanation:
One possible way to reach at index 3 with value 0 is:
index 0 -> index 4 -> index 1 -> index 3

Example 3:

Input: arr = [3,0,2,1,2], start = 2
Output: false
Explanation: There is no way to reach at index 1 with value 0.

Constraints:

`1 <= arr.length <= 5 * 10^4`

`0 <= arr[i] < arr.length`

`0 <= start < arr.length`

【中文翻译】
给定一个非负整数数组 arr，你最初位于数组的 start 索引处。
当你位于索引 i 时，你可以跳到 i + arr[i] 或 i - arr[i]。
请判断你是否能够到达任意值为 0 的索引。

注意，任何时候你都不能跳到数组范围之外。

示例 1：
输入：arr = [4,2,3,0,3,1,2], start = 5
输出：true
解释：
到达值为 0 的索引 3 的所有可能路径为：
索引 5 -> 索引 4 -> 索引 1 -> 索引 3
索引 5 -> 索引 6 -> 索引 4 -> 索引 1 -> 索引 3

示例 2：
输入：arr = [4,2,3,0,3,1,2], start = 0
输出：true
解释：
到达值为 0 的索引 3 的一种可能路径为：
索引 0 -> 索引 4 -> 索引 1 -> 索引 3

示例 3：
输入：arr = [3,0,2,1,2], start = 2
输出：false
解释：无法到达值为 0 的索引 1。

约束条件：
1 <= arr.length <= 5 * 10^4
0 <= arr[i] < arr.length
0 <= start < arr.length
"""

from typing import List
from collections import deque


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        visited = [False] * n
        queue = deque([start])
        visited[start] = True

        while queue:
            idx = queue.popleft()
            if arr[idx] == 0:
                return True
            # Jump forward: i + arr[i]
            forward = idx + arr[idx]
            if forward < n and not visited[forward]:
                visited[forward] = True
                queue.append(forward)
            # Jump backward: i - arr[i]
            backward = idx - arr[idx]
            if backward >= 0 and not visited[backward]:
                visited[backward] = True
                queue.append(backward)

        return False



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 将问题建模为图的遍历问题：每个索引是一个节点，
# 从索引 i 可以跳到 i+arr[i] 和 i-arr[i]（如果在数组范围内）。
# 使用 BFS（或 DFS）从 start 出发遍历所有可达的索引，
# 同时使用 visited 数组记录已访问的索引以避免无限循环。
# 如果在遍历过程中遇到值为 0 的索引，返回 True；
# 如果遍历完所有可达位置都没找到 0，返回 False。
#
# 时间复杂度: O(N)，每个索引最多入队一次
# 空间复杂度: O(N)，visited 数组和队列各 O(N)
#
# 关键点:
# - 每个索引可以看作图中的节点，跳跃规则定义了有向边
# - 使用 visited 集合避免重复访问和无限循环
# - arr[i] >= 0 保证不会原地踏步（除非 arr[i]=0，此时直接返回 True）
# - 也可以使用 DFS（递归/栈），但 BFS 在处理层级问题时更自然
# - 等价于判断从 start 出发能否到达值为 0 的节点










