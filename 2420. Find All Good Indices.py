"""
LeetCode #2420 - Find All Good Indices
找到所有好下标
https://leetcode.cn/problems/find-all-good-indices/

给你一个大小为 `n` 下标从 0 开始的整数数组 `nums` 和一个正整数 `k` 。
对于 `k <= i < n - k` 之间的一个下标 `i` ，如果它满足以下条件，我们就称它为一个 好 下标：
下标 `i` 之前 的 `k` 个元素是 非递增的 。
下标 `i` 之后 的 `k` 个元素是 非递减的 。
按 升序 返回所有好下标。

示例 1：
输入：nums = [2,1,1,1,3,4,1], k = 2 输出：[2,3] 解释：数组中有两个好下标： - 下标 2 。子数组 [2,1] 是非递增的，子数组 [1,3] 是非递减的。 - 下标 3 。子数组 [1,1] 是非递增的，子数组 [3,4] 是非递减的。 注意，下标 4 不是好下标，因为 [4,1] 不是非递减的。
示例 2：
输入：nums = [2,1,1,2], k = 2 输出：[] 解释：数组中没有好下标。

提示：
`n == nums.length`
`3 <= n <= 10^5`
`1 <= nums[i] <= 10^6`
`1 <= k <= n / 2`
"""

from typing import List, Optional


class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        # dec[i]: length of non-increasing consecutive run ending at i
        dec = [1] * n
        for i in range(1, n):
            if nums[i - 1] >= nums[i]:
                dec[i] = dec[i - 1] + 1

        # inc[i]: length of non-decreasing consecutive run starting at i
        inc = [1] * n
        for i in range(n - 2, -1, -1):
            if nums[i] <= nums[i + 1]:
                inc[i] = inc[i + 1] + 1

        # i is good if the k elements before i are non-increasing
        # (dec[i-1] >= k) and k elements after i are non-decreasing
        # (inc[i+1] >= k)
        res = []
        for i in range(k, n - k):
            if dec[i - 1] >= k and inc[i + 1] >= k:
                res.append(i)
        return res



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Dynamic Programming, Prefix Sum
#
# 解题思路:
# 构建两个辅助数组 dec 和 inc：
# - dec[i] 表示以 i 结尾的最长非递增连续子数组的长度
# - inc[i] 表示以 i 开头的最长非递减连续子数组的长度
# 对于下标 i（k <= i < n-k），如果 dec[i-1] >= k 说明 i 之前的 k 个
# 元素是非递增的；如果 inc[i+1] >= k 说明 i 之后的 k 个元素是非递减的。
# 满足两个条件即为好下标，收集所有满足条件的 i。
#
# 时间复杂度: O(n) — 三次线性遍历
# 空间复杂度: O(n) — 两个辅助数组 dec 和 inc
#
# 关键点:
# - 使用前缀/后缀思想预计算连续非递增和非递减的长度
# - 判断 i 是否好下标时只需 O(1) 查表
# - 注意检查索引边界：i 的范围是 [k, n-k)
