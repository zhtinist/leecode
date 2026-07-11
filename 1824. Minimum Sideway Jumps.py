"""
LeetCode #1824 - Minimum Sideway Jumps
中文题名：最少侧跳次数
https://leetcode.com/problems/minimum-sideway-jumps/

There is a 3 lane road of length `n` that consists of `n + 1` points labeled from `0` to `n`. A frog starts at point `0` in the second lane and wants to jump to point `n`. However, there could be obstacles along the way.

You are given an array `obstacles` of length `n + 1` where each `obstacles[i]` (ranging from 0 to 3) describes an obstacle on the lane `obstacles[i]` at point `i`. If `obstacles[i] == 0`, there are no obstacles at point `i`. There will be at most one obstacle in the 3 lanes at each point.

For example, if `obstacles[2] == 1`, then there is an obstacle on lane 1 at point 2.

The frog can only travel from point `i` to point `i + 1` on the same lane if there is not an obstacle on the lane at point `i + 1`. To avoid obstacles, the frog can also perform a side jump to jump to another lane (even if they are not adjacent) at the same point if there is no obstacle on the new lane.

For example, the frog can jump from lane 3 at point 3 to lane 1 at point 3.

Return the minimum number of side jumps the frog needs to reach any lane at point n starting from lane `2` at point 0.

Note: There will be no obstacles on points `0` and `n`.

Example 1:

Input: obstacles = [0,1,2,3,0]
Output: 2
Explanation: The optimal solution is shown by the arrows above. There are 2 side jumps (red arrows).
Note that the frog can jump over obstacles only when making side jumps (as shown at point 2).

Example 2:

Input: obstacles = [0,1,1,3,3,0]
Output: 0
Explanation: There are no obstacles on lane 2. No side jumps are required.

Example 3:

Input: obstacles = [0,2,1,0,3,0]
Output: 2
Explanation: The optimal solution is shown by the arrows above. There are 2 side jumps.

Constraints:

`obstacles.length == n + 1`

`1 <= n <= 5 * 105`

`0 <= obstacles[i] <= 3`

`obstacles[0] == obstacles[n] == 0`

【中文翻译】

有一条长度为n的3车道公路，包含从0到n标记的n+1个点。一只青蛙从点0的第二车道出发，想要跳到点n。沿途可能存在障碍物。

给定一个长度为n+1的数组 `obstacles`，`obstacles[i]`（范围0到3）描述了点i处车道上的障碍物。如果`obstacles[i]==0`，表示点i处没有障碍物。每个点最多有一个障碍物。

青蛙只能在同一条车道上从点i移动到点i+1（如果点i+1处该车道没有障碍物）。为了避开障碍物，青蛙还可以在同一位置进行侧跳跳到另一车道（即使不相邻），前提是新车道没有障碍物。

返回青蛙从点0的第二车道出发，到达点n任意车道所需的最少侧跳次数。

示例：
输入：obstacles = [0,1,2,3,0]
输出：2
解释：在点2从车道2跳到车道3，然后到点4，共2次侧跳。

"""

from typing import List, Optional


class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        n = len(obstacles) - 1
        # dp[lane]: 到达当前位置各车道的最少侧跳次数 (lane 0,1,2 = 车道 1,2,3)
        dp = [1, 0, 1]  # 起点在车道2(index=1)，跳到其他车道需要1次

        for i in range(1, n + 1):
            # 标记有障碍的车道为不可达
            if obstacles[i] > 0:
                dp[obstacles[i] - 1] = float('inf')

            # 更新每条车道：可以从前一位置同车道到达，或从其他车道侧跳到达
            for lane in range(3):
                if obstacles[i] != lane + 1:
                    dp[lane] = min(
                        dp[lane],
                        dp[(lane + 1) % 3] + 1,
                        dp[(lane + 2) % 3] + 1
                    )

        return min(dp)










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 动态规划。dp[lane]表示到达当前位置各车道的最少侧跳次数。
# 初始时dp[1]=0（起点在车道2），dp[0]=dp[2]=1（需要1次侧跳）。
# 遍历每个位置i：如果该位置某车道有障碍，将该车道设为inf。
# 然后对每条无障碍车道，可以从同车道直行（保持原值）或从其他车道侧跳到达。
# 最终答案为min(dp)。
#
# 时间复杂度: O(N)，N为障碍数组长度
# 空间复杂度: O(1)，只使用长度为3的dp数组
#
# 关键点:
# - 只有3条车道，dp数组长度为3
# - 每个位置先标记障碍再更新各车道
# - 侧跳可以在同一位置进行（不需要前进）
