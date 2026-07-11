"""
LeetCode #3388 - Count Beautiful Splits in an Array
统计数组中的美丽分割
https://leetcode.cn/problems/count-beautiful-splits-in-an-array/

给你一个整数数组 `nums` 。
如果数组 `nums` 的一个分割满足以下条件，我们称它是一个 美丽 分割：
数组 `nums` 分为三段 非空子数组：`nums1` ，`nums2` 和 `nums3` ，三个数组 `nums1` ，`nums2` 和 `nums3` 按顺序连接可以得到 `nums` 。
子数组 `nums1` 是子数组 `nums2` 的 前缀 或者 `nums2` 是 `nums3` 的 前缀。
请你返回满足以上条件的分割 数目 。
子数组 指的是一个数组里一段连续 非空 的元素。
前缀 指的是一个数组从头开始到中间某个元素结束的子数组。

示例 1：

输入：nums = [1,1,2,1]
输出：2
解释：
美丽分割如下：
`nums1 = [1]` ，`nums2 = [1,2]` ，`nums3 = [1]` 。
`nums1 = [1]` ，`nums2 = [1]` ，`nums3 = [2,1]` 。
示例 2：

输入：nums = [1,2,3,4]
输出：0
解释：
没有美丽分割。

提示：
`1 <= nums.length <= 5000`
`0 <= nums[i] <= 50`
"""

from typing import List, Optional


class Solution:
    def beautifulSplits(self, nums: List[int]) -> int:
        n = len(nums)
        MOD = 10 ** 9 + 7
        BASE = 101
        powers = [1] * (n + 1)
        hashes = [0] * (n + 1)
        for i in range(n):
            powers[i + 1] = (powers[i] * BASE) % MOD
            hashes[i + 1] = (hashes[i] * BASE + nums[i] + 1) % MOD

        def get_hash(l: int, r: int) -> int:
            return (hashes[r] - hashes[l] * powers[r - l]) % MOD

        def is_prefix(a: int, b: int, len_check: int) -> bool:
            return get_hash(a, a + len_check) == get_hash(b, b + len_check)

        ans = 0
        for i in range(1, n - 1):       # end of nums1
            len1 = i
            for j in range(i + 1, n):   # end of nums2
                len2 = j - i
                len3 = n - j
                if (len1 <= len2 and is_prefix(0, i, len1)) or \
                   (len2 <= len3 and is_prefix(i, j, len2)):
                    ans += 1
        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Dynamic Programming
#
# 解题思路:
# 枚举所有分割点(i,j)（i<j<n），检查nums1是否为nums2的前缀或nums2是否为nums3的前缀。
# 使用滚动哈希(Rolling Hash)在O(1)时间内比较任意子数组是否相等。
# n<=5000，枚举所有O(n^2)对分割点，每对O(1)哈希比较，总计约1250万次操作。
#
# 时间复杂度: O(n^2)
# 空间复杂度: O(n)
#
# 关键点:
# - 滚动哈希实现O(1)子数组比较
# - 两个条件满足其一即可
