"""
LeetCode #826 - Most Profit Assigning Work
中文题名：安排工作以达到最大收益
https://leetcode.com/problems/most-profit-assigning-work/

We have jobs: `difficulty[i]` is the difficulty of the `i`th
job, and `profit[i]` is the profit of the `i`th job.

Now we have some workers. `worker[i]` is the ability of
the `i`th worker, which means that this worker can only complete a job with
difficulty at most `worker[i]`.

Every worker can be assigned at most one job, but one job can be completed multiple
times.

For example, if 3 people attempt the same job that pays $1, then the total profit will be $3.
If a worker cannot complete any job, his profit is $0.

What is the most profit we can make?

Example 1:

Input: difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]
Output: 100
Explanation: Workers are assigned jobs of difficulty [4,4,6,6] and they get profit of [20,20,30,30] seperately.

Notes:

`1 <= difficulty.length = profit.length <= 10000`

`1 <= worker.length <= 10000`

`difficulty[i], profit[i], worker[i]`  are in range `[1,
10^5]`

【中文翻译】
有一些工作：`difficulty[i]` 表示第 i 个工作的难度，`profit[i]` 表示第 i 个工作的收益。

现在我们有一些工人：`worker[i]` 是第 i 个工人的能力，这意味着该工人只能完成难度不超过 `worker[i]` 的工作。

每个工人最多只能安排一个工作，但一个工作可以被多个工人完成。

例如，如果有 3 个人都尝试完成同一个支付 1 美元的工作，那么总收益就是 3 美元。如果一个工人不能完成任何工作，他的收益为 0。

请问我们能获得的最大收益是多少？

示例 1：

输入：difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]
输出：100
解释：工人被分配难度为 [4,4,6,6] 的工作，他们分别获得 [20,20,30,30] 的收益。

注意：

`1 <= difficulty.length = profit.length <= 10000`

`1 <= worker.length <= 10000`

`difficulty[i], profit[i], worker[i]` 的范围是 `[1, 10^5]`

"""

from typing import List, Optional


class Solution:
    def maxProfitAssignment(
        self, difficulty: List[int], profit: List[int], worker: List[int]
    ) -> int:
        # Pair and sort jobs by difficulty
        jobs = sorted(zip(difficulty, profit))
        # Precompute best profit up to each difficulty level
        best_profit = []
        max_profit = 0
        for d, p in jobs:
            max_profit = max(max_profit, p)
            best_profit.append((d, max_profit))

        # Sort workers by ability
        worker.sort()

        total = 0
        j = 0
        n = len(best_profit)
        for ability in worker:
            # Move pointer to the hardest job this worker can do
            while j < n and best_profit[j][0] <= ability:
                j += 1
            if j > 0:
                total += best_profit[j - 1][1]

        return total



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 贪心 + 排序 + 双指针。
# 1. 将工作按难度排序，并维护到当前难度为止的最大收益（因为高难度工作不一定高收益）。
# 2. 将工人按能力排序。
# 3. 使用双指针：对每个工人，移动指针找到他能完成的最难工作，
#    取对应的最大收益（已预处理为前缀最大值）。
# 每个工人都选择自己能完成的工作中收益最高的那个。
#
# 时间复杂度: O(n log n + m log m) — n 为工作数，m 为工人数，主要时间在排序
# 空间复杂度: O(n) — 存储排序后的工作列表
#
# 关键点:
# - 工作可以重复完成，所以每个工人都应选择自己能完成的最高收益工作
# - 预处理前缀最大收益：难度更高的工作收益不一定更高，需要取 max
# - 双指针避免对每个工人都从头扫描工作列表
