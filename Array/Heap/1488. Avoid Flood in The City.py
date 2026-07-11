"""
LeetCode #1488 - Avoid Flood in The City
中文题名：避免洪水泛滥
https://leetcode.com/problems/avoid-flood-in-the-city/

Your country has an infinite number of lakes. Initially, all the lakes are empty,
but when it rains over the `nth` lake, the `nth` lake becomes full
of water. If it rains over a lake which is full of water, there will be
a flood. Your goal is to avoid the flood in any lake.

Given an integer array `rains` where:

`rains[i] > 0` means there will be rains over the
`rains[i]` lake.

`rains[i] == 0` means there are no rains this day and you can choose
one lake this day and dry it.

Return an array `ans` where:

`ans.length == rains.length`

`ans[i] == -1` if `rains[i] > 0`.

`ans[i]` is the lake you choose to dry in the `ith` day if
`rains[i] == 0`.

If there are multiple valid answers return any of them. If it is
impossible to avoid flood return an empty array.

Notice that if you chose to dry a full lake, it becomes empty, but if you chose to
dry an empty lake, nothing changes. (see example 4)

Example 1:

Input: rains = [1,2,3,4]
Output: [-1,-1,-1,-1]
Explanation: After the first day full lakes are [1]
After the second day full lakes are [1,2]
After the third day full lakes are [1,2,3]
After the fourth day full lakes are [1,2,3,4]
There's no day to dry any lake and there is no flood in any lake.

Example 2:

Input: rains = [1,2,0,0,2,1]
Output: [-1,-1,2,1,-1,-1]
Explanation: After the first day full lakes are [1]
After the second day full lakes are [1,2]
After the third day, we dry lake 2. Full lakes are [1]
After the fourth day, we dry lake 1. There is no full lakes.
After the fifth day, full lakes are [2].
After the sixth day, full lakes are [1,2].
It is easy that this scenario is flood-free. [-1,-1,1,2,-1,-1] is another acceptable scenario.

Example 3:

Input: rains = [1,2,0,1,2]
Output: []
Explanation: After the second day, full lakes are  [1,2]. We have to dry one lake in the third day.
After that, it will rain over lakes [1,2]. It's easy to prove that no matter which lake you choose to dry in the 3rd day, the other one will flood.

Example 4:

Input: rains = [69,0,0,0,69]
Output: [-1,69,1,1,-1]
Explanation: Any solution on one of the forms [-1,69,x,y,-1], [-1,x,69,y,-1] or [-1,x,y,69,-1] is acceptable where 1 <= x,y <= 10^9

Example 5:

Input: rains = [10,20,20]
Output: []
Explanation: It will rain over lake 20 two consecutive days. There is no chance to dry any lake.

Constraints:

`1 <= rains.length <= 10^5`

`0 <= rains[i] <= 10^9`

【中文翻译】

你的国家有无限数量的湖泊。最初，所有湖泊都是空的，但当第 `n` 个湖泊下雨时，第 `n` 个湖泊就会充满水。如果对一个已经充满水的湖泊下雨，就会发生洪水。你的目标是避免任何湖泊发生洪水。

给定一个整数数组 `rains`，其中：
- `rains[i] > 0` 表示第 `i` 天将在第 `rains[i]` 个湖泊下雨。
- `rains[i] == 0` 表示第 `i` 天没有雨，你可以选择这天将一个湖泊抽干。

返回一个数组 `ans`，其中：
- `ans.length == rains.length`
- 如果 `rains[i] > 0`，则 `ans[i] == -1`。
- 如果 `rains[i] == 0`，则 `ans[i]` 是你选择在第 `i` 天抽干的湖泊。

如果有多个有效答案，返回其中任意一个。如果无法避免洪水，返回空数组。

请注意，如果你选择抽干一个满的湖泊，它会变空，但如果你选择抽干一个空的湖泊，不会发生任何变化（见示例 4）。

示例 1：
输入：rains = [1,2,3,4]
输出：[-1,-1,-1,-1]
解释：第一天后满的湖泊是 [1]；第二天后是 [1,2]；第三天后是 [1,2,3]；第四天后是 [1,2,3,4]。没有可以抽干任何湖泊的日子，也没有任何湖泊发生洪水。

示例 2：
输入：rains = [1,2,0,0,2,1]
输出：[-1,-1,2,1,-1,-1]
解释：第一天后满的湖泊是 [1]；第二天后是 [1,2]；第三天我们抽干湖泊 2，满的湖泊是 [1]；第四天我们抽干湖泊 1，没有满的湖泊；第五天后满的湖泊是 [2]；第六天后满的湖泊是 [1,2]。显然这种方案是无洪水的。[-1,-1,1,2,-1,-1] 是另一种可接受的方案。

示例 3：
输入：rains = [1,2,0,1,2]
输出：[]
解释：第二天后满的湖泊是 [1,2]。我们必须在第三天抽干一个湖泊。之后将在湖泊 [1,2] 下雨。容易证明无论第三天选择抽干哪个湖泊，另一个都会发生洪水。

示例 4：
输入：rains = [69,0,0,0,69]
输出：[-1,69,1,1,-1]
解释：任何形式为 [-1,69,x,y,-1]、[-1,x,69,y,-1] 或 [-1,x,y,69,-1] 的答案都是可接受的，其中 1 <= x,y <= 10^9。

示例 5：
输入：rains = [10,20,20]
输出：[]
解释：湖泊 20 连续两天下雨，没有机会抽干任何湖泊。

约束条件：
1 <= rains.length <= 10^5
0 <= rains[i] <= 10^9

"""

from typing import List, Optional


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        from heapq import heappush, heappop

        n = len(rains)
        ans = [-1] * n

        # Pre-process: for each lake, record all days it rains
        rain_days = {}
        for i, lake in enumerate(rains):
            if lake > 0:
                if lake not in rain_days:
                    rain_days[lake] = []
                rain_days[lake].append(i)

        # Track which index (in rain_days[lake]) we are at for each lake
        next_idx = {lake: 0 for lake in rain_days}

        # Min-heap of (next_rain_day, lake) for lakes that are full
        # and will rain again in the future
        heap = []
        full = set()

        for i, lake in enumerate(rains):
            if lake > 0:
                if lake in full:
                    return []  # flood

                full.add(lake)
                next_idx[lake] += 1

                # If this lake will rain again, add to heap
                idx = next_idx[lake]
                if idx < len(rain_days[lake]):
                    heappush(heap, (rain_days[lake][idx], lake))
            else:
                # Sunny day: dry the lake that will rain earliest
                if heap:
                    next_day, lake_to_dry = heappop(heap)
                    ans[i] = lake_to_dry
                    full.remove(lake_to_dry)
                else:
                    ans[i] = 1  # any lake is fine

        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 1. 预处理：记录每个湖泊下雨的所有日期。
# 2. 维护一个集合 full 记录当前已满的湖泊。
# 3. 维护一个最小堆 heap，存储 (下一次下雨日期, 湖泊编号)，
#    用于追踪哪些已满的湖泊将来还会下雨。
# 4. 遍历每天：
#    - 下雨天（rains[i] > 0）：
#      如果该湖泊已满，直接返回空数组（洪水）。
#      将该湖泊标记为满，并检查它将来是否还会下雨：
#      如果会，将 (下次下雨日期, 湖泊) 加入堆中。
#    - 晴天（rains[i] == 0）：
#      从堆中弹出下次下雨最早的湖泊，抽干它（贪心策略）。
#      如果堆为空，可以任意选择一个湖泊抽干（如湖泊 1）。
# 5. 贪心策略正确性：在晴天时，优先抽干最快会再次下雨的湖泊，
#    这样能给其他湖泊留出更多的抽干机会。这等价于在 sorted set
#    中查找"上次下雨后最早的晴天"的二分查找策略。
#
# 时间复杂度: O(N log N)
# 空间复杂度: O(N)
#
# 关键点:
# - 贪心策略：优先抽干最早会再次下雨的湖泊
# - 使用最小堆实现 O(log N) 的插入和弹出
# - 预处理每个湖泊的所有下雨日期，便于追踪下次下雨时间
# - 需要处理湖泊不会再下雨的情况（不加入堆）










