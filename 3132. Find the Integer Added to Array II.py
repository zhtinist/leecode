"""
LeetCode #3132 - Find the Integer Added to Array II
找出与数组相加的整数 II
https://leetcode.cn/problems/find-the-integer-added-to-array-ii/

给你两个整数数组 `nums1` 和 `nums2`。
从 `nums1` 中移除两个元素，并且所有其他元素都与变量 `x` 所表示的整数相加。如果 `x` 为负数，则表现为元素值的减少。
执行上述操作后，`nums1` 和 `nums2` 相等 。当两个数组中包含相同的整数，并且这些整数出现的频次相同时，两个数组 相等 。
返回能够实现数组相等的 最小 整数 `x` 。

示例 1:

输入：nums1 = [4,20,16,12,8], nums2 = [14,18,10]
输出：-2
解释：
移除 `nums1` 中下标为 `[0,4]` 的两个元素，并且每个元素与 `-2` 相加后，`nums1` 变为 `[18,14,10]` ，与 `nums2` 相等。
示例 2:

输入：nums1 = [3,5,5,3], nums2 = [7,7]
输出：2
解释：
移除 `nums1` 中下标为 `[0,3]` 的两个元素，并且每个元素与 `2` 相加后，`nums1` 变为 `[7,7]` ，与 `nums2` 相等。

提示：
`3 <= nums1.length <= 200`
`nums2.length == nums1.length - 2`
`0 <= nums1[i], nums2[i] <= 1000`
测试用例以这样的方式生成：存在一个整数 `x`，`nums1` 中的每个元素都与 `x` 相加后，再移除两个元素，`nums1` 可以与 `nums2` 相等。
"""

from typing import List, Optional


class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        ans = float('inf')

        # nums2[0]必定匹配nums1前三个元素之一（最多删2个）
        for i in range(3):
            x = nums2[0] - nums1[i]
            j = 0  # nums2的指针
            skip = 0  # nums1中跳过的元素数
            for k in range(len(nums1)):
                if j < len(nums2) and nums1[k] + x == nums2[j]:
                    j += 1
                else:
                    skip += 1
                if skip > 2:
                    break
            if j == len(nums2) and skip <= 2:
                ans = min(ans, x)

        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Two Pointers, Enumeration, Sorting
#
# 解题思路:
# 排序两个数组。nums2的最小值必定对应nums1排序后前三个元素之一（删除2个最多遗漏最小的2个）。
# 枚举i=0,1,2，设x=nums2[0]-nums1[i]，用双指针验证：遍历nums1，
# 若nums1[k]+x匹配nums2[j]则前进j，否则记为跳过。若跳过数<=2且nums2全部匹配则x有效。
# 返回最小有效的x。
#
# 时间复杂度: O(n log n)
# 空间复杂度: O(1)
#
# 关键点:
# - 排序后nums2[0]仅可能匹配nums1的前三个元素
# - 双指针贪心匹配
# - 跳过计数不超过2
