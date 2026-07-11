"""
LeetCode #910 - Smallest Range II
中文题名：最小差值 II
https://leetcode.com/problems/smallest-range-ii/

Given an array `A` of integers, for each integer `A[i]` we need to
choose either `x = -K` or `x = K`, and add
`x` to `A[i] (only once)`.

After this process, we have some array `B`.

Return the smallest possible difference between the maximum value of `B` and
the minimum value of `B`.

Example 1:

Input: A = [1], K = 0
Output: 0
Explanation: B = [1]

Example 2:

Input: A = [0,10], K = 2
Output: 6
Explanation: B = [2,8]

Example 3:

Input: A = [1,3,6], K = 3
Output: 3
Explanation: B = [4,6,3]

Note:

`1 <= A.length <= 10000`

`0 <= A[i] <= 10000`

`0 <= K <= 10000`

【中文翻译】
给定一个整数数组 `A`，对于每个整数 `A[i]`，我们必须选择 `x = -K` 或 `x = K`，并将 `x` 加到 `A[i]`（仅加一次）。

经过此过程后，我们得到某个数组 `B`。

返回 `B` 的最大值和 `B` 的最小值之间可能的最小差值。

示例 1：

输入：A = [1], K = 0
输出：0
解释：B = [1]

示例 2：

输入：A = [0,10], K = 2
输出：6
解释：B = [2,8]

示例 3：

输入：A = [1,3,6], K = 3
输出：3
解释：B = [4,6,3]

"""

from typing import List, Optional


class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)

        # 最坏情况：全部加 K 或全部减 K
        ans = nums[-1] - nums[0]

        # 尝试在位置 i 处分割：A[0..i] 都 +K, A[i+1..n-1] 都 -K
        for i in range(n - 1):
            high = max(nums[i] + k, nums[-1] - k)
            low = min(nums[0] + k, nums[i + 1] - k)
            ans = min(ans, high - low)

        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 贪心策略 + 排序。首先将数组排序。
# 直觉：要想最小化极差（max - min），应该让较小的数 +K（变大），较大的数 -K（变小）。
# 因此最优策略一定是：存在一个分割点 i，使得 A[0..i] 都 +K，A[i+1..n-1] 都 -K
# （反证：如果某个 +K 的数比某个 -K 的数还大，交换它们的操作不会使结果更差）。
#
# 分割后：
# - 最大值 = max(A[i] + K, A[n-1] - K)   // 前半段最大的 +K 或 后半段最大的 -K
# - 最小值 = min(A[0] + K, A[i+1] - K)    // 前半段最小的 +K 或 后半段最小的 -K
# - 极差 = 最大值 - 最小值
#
# 遍历所有分割点 i ∈ [0, n-2]，取最小极差。
# 基线情况 ans 初始化为 A[-1] - A[0]（全部 +K 或全部 -K）。
#
# 时间复杂度: O(N log N) — 排序主导
# 空间复杂度: O(1) — 或不考虑排序栈空间的 O(log N)
#
# 关键点:
# - 排序后确定分割点是核心思想
# - max 和 min 的计算要考虑前后两段
# - 基线情况 ans = A[-1] - A[0] 等价于全部加/减（不分段）
# - 与 Smallest Range I（#908）的区别：I 可以选 [-K, K] 任意值，只需返回 max(0, diff - 2K)
