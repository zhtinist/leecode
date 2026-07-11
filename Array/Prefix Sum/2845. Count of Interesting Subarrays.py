"""
LeetCode #2845 - Count of Interesting Subarrays
统计趣味子数组的数目
https://leetcode.cn/problems/count-of-interesting-subarrays/

给你一个下标从 0 开始的整数数组 `nums` ，以及整数 `modulo` 和整数 `k` 。
请你找出并统计数组中 趣味子数组 的数目。
如果 子数组 `nums[l..r]` 满足下述条件，则称其为 趣味子数组 ：
在范围 `[l, r]` 内，设 `cnt` 为满足 `nums[i] % modulo == k` 的索引 `i` 的数量。并且 `cnt % modulo == k` 。
以整数形式表示并返回趣味子数组的数目。
注意：子数组是数组中的一个连续非空的元素序列。

示例 1：
输入：nums = [3,2,4], modulo = 2, k = 1 输出：3 解释：在这个示例中，趣味子数组分别是：  子数组 nums[0..0] ，也就是 [3] 。  - 在范围 [0, 0] 内，只存在 1 个下标 i = 0 满足 nums[i] % modulo == k 。 - 因此 cnt = 1 ，且 cnt % modulo == k 。 子数组 nums[0..1] ，也就是 [3,2] 。 - 在范围 [0, 1] 内，只存在 1 个下标 i = 0 满足 nums[i] % modulo == k 。 - 因此 cnt = 1 ，且 cnt % modulo == k 。 子数组 nums[0..2] ，也就是 [3,2,4] 。 - 在范围 [0, 2] 内，只存在 1 个下标 i = 0 满足 nums[i] % modulo == k 。 - 因此 cnt = 1 ，且 cnt % modulo == k 。 可以证明不存在其他趣味子数组。因此，答案为 3 。
示例 2：
输入：nums = [3,1,9,6], modulo = 3, k = 0 输出：2 解释：在这个示例中，趣味子数组分别是：  子数组 nums[0..3] ，也就是 [3,1,9,6] 。 - 在范围 [0, 3] 内，只存在 3 个下标 i = 0, 2, 3 满足 nums[i] % modulo == k 。 - 因此 cnt = 3 ，且 cnt % modulo == k 。 子数组 nums[1..1] ，也就是 [1] 。 - 在范围 [1, 1] 内，不存在下标满足 nums[i] % modulo == k 。 - 因此 cnt = 0 ，且 cnt % modulo == k 。 可以证明不存在其他趣味子数组，因此答案为 2 。

提示：
`1 <= nums.length <= 10^5 `
`1 <= nums[i] <= 10^9`
`1 <= modulo <= 10^9`
`0 <= k < modulo`
"""

from typing import List, Optional


class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        prefix = 0
        freq = {0: 1}
        ans = 0
        for x in nums:
            if x % modulo == k:
                prefix = (prefix + 1) % modulo
            # We need: (prefix - prev) % modulo == k
            # => prev % modulo == (prefix - k) % modulo
            target = (prefix - k) % modulo
            ans += freq.get(target, 0)
            freq[prefix] = freq.get(prefix, 0) + 1
        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Hash Table, Prefix Sum
#
# 解题思路:
# 将满足 nums[i] % modulo == k 的元素视为1，否则视为0。问题转化为求子数组和 % modulo == k 的个数。
# 使用前缀和与哈希表：维护前缀和（对 modulo 取模），对于当前位置的前缀和 prefix，
# 需要找之前出现过的 prev 使得 (prefix - prev) % modulo == k，即 prev % modulo == (prefix - k) % modulo。
#
# 时间复杂度: O(n)
# 空间复杂度: O(modulo) / O(n)
#
# 关键点:
# - 转化为前缀和对 modulo 取模的同余问题
# - prefix 只记录满足条件的元素计数 % modulo
# - 哈希表记录每种模值出现的次数，O(1) 查询 target 数量
