"""
LeetCode #2202 - Maximize the Topmost Element After K Moves
K 次操作后最大化顶端元素
https://leetcode.cn/problems/maximize-the-topmost-element-after-k-moves/

给你一个下标从 0 开始的整数数组 `nums` ，它表示一个 堆 ，其中 `nums[0]` 是堆顶的元素。
每一次操作中，你可以执行以下操作 之一 ：
如果堆非空，那么 删除 堆顶端的元素。
如果存在 1 个或者多个被删除的元素，你可以从它们中选择任何一个，添加 回堆顶，这个元素成为新的堆顶元素。
同时给你一个整数 `k` ，它表示你总共需要执行操作的次数。
请你返回 恰好 执行 `k` 次操作以后，堆顶元素的 最大值 。如果执行完 `k` 次操作以后，堆一定为空，请你返回 `-1` 。

示例 1：
输入：nums = [5,2,2,4,0,6], k = 4 输出：5 解释： 4 次操作后，堆顶元素为 5 的方法之一为： - 第 1 次操作：删除堆顶元素 5 ，堆变为 [2,2,4,0,6] 。 - 第 2 次操作：删除堆顶元素 2 ，堆变为 [2,4,0,6] 。 - 第 3 次操作：删除堆顶元素 2 ，堆变为 [4,0,6] 。 - 第 4 次操作：将 5 添加回堆顶，堆变为 [5,4,0,6] 。 注意，这不是最后堆顶元素为 5 的唯一方式。但可以证明，4 次操作以后 5 是能得到的最大堆顶元素。
示例 2：
输入：nums = [2], k = 1 输出：-1 解释： 第 1 次操作中，我们唯一的选择是将堆顶元素弹出堆。 由于 1 次操作后无法得到一个非空的堆，所以我们返回 -1 。

提示：
`1 <= nums.length <= 10^5`
`0 <= nums[i], k <= 10^9`
"""

from typing import List, Optional


class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # No operations: top is nums[0]
        if k == 0:
            return nums[0]

        # Only one element: alternating push/pop
        # Odd k -> stack empty; even k -> original element on top
        if n == 1:
            return -1 if k % 2 == 1 else nums[0]

        # Case 1: max among the first (k-1) elements that can be pushed back
        # We can pop up to min(k-1, n) elements and push the max one back
        max_first = max(nums[:min(k - 1, n)]) if k - 1 > 0 else -1

        # Case 2: pop exactly k times to expose nums[k] (if k < n)
        max_expose = nums[k] if k < n else -1

        return max(max_first, max_expose)


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Array
#
# 解题思路:
# 1. 特殊情况处理：
#    - k == 0：没有操作，堆顶即为 nums[0]。
#    - n == 1：只有一个元素时，奇数次操作必然使堆为空返回 -1，
#      偶数次操作可以通过交替弹出和推回来保持原元素在顶部。
# 2. 一般情况（n > 1）：经过恰好 k 次操作后，堆顶元素只有两种可能的来源：
#    a) 从前 k-1 个元素中选一个最大值"推回"堆顶：
#       具体做法是弹出前面若干个元素（使目标元素被弹出），然后将它推回堆顶，
#       剩余操作次数可以通过反复弹出-推回来消耗（必须为偶数次）。
#       实际操作中，我们只需取 nums[0:min(k-1, n)] 的最大值即可。
#    b) 前 k 个元素全部弹出来暴露 nums[k]（前提是 k < n）：
#       恰好 k 次弹出后，nums[k] 成为新的堆顶元素。
# 3. 取这两种情况的最大值即可。
#
# 时间复杂度: O(min(k, n))，需要扫描前 min(k-1, n) 个元素求最大值。
# 空间复杂度: O(1)，只使用常数额外空间（切片创建了新列表，若严格 O(1) 可改用循环）。
#
# 关键点:
# - 理解操作的本质：弹出等同于"消耗"，推回等同于"从已删元素中选择一个放到顶部"。
# - 当 k > n 时，可以弹出所有元素，然后推回任意一个（实际上是全部元素的最大值）。
# - 边界情况 n==1 和 k==0 需要仔细处理。
# - 若 k-1 ≤ 0（即 k==1 且 n>1），只能通过弹出一次来暴露 nums[1]。
