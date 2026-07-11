"""
LeetCode #1985 - Find the Kth Largest Integer in the Array
找出数组中的第 K 大整数
https://leetcode.cn/problems/find-the-kth-largest-integer-in-the-array/

给你一个字符串数组 `nums` 和一个整数 `k` 。`nums` 中的每个字符串都表示一个不含前导零的整数。
返回 `nums` 中表示第 `k` 大整数的字符串。
注意：重复的数字在统计时会视为不同元素考虑。例如，如果 `nums` 是 `["1","2","2"]`，那么 `"2"` 是最大的整数，`"2"` 是第二大的整数，`"1"` 是第三大的整数。

示例 1：
输入：nums = ["3","6","7","10"], k = 4 输出："3" 解释： nums 中的数字按非递减顺序排列为 ["3","6","7","10"] 其中第 4 大整数是 "3"
示例 2：
输入：nums = ["2","21","12","1"], k = 3 输出："2" 解释： nums 中的数字按非递减顺序排列为 ["1","2","12","21"] 其中第 3 大整数是 "2"
示例 3：
输入：nums = ["0","0"], k = 2 输出："0" 解释： nums 中的数字按非递减顺序排列为 ["0","0"] 其中第 2 大整数是 "0"

提示：
`1 <= k <= nums.length <= 10^4`
`1 <= nums[i].length <= 100`
`nums[i]` 仅由数字组成
`nums[i]` 不含任何前导零
"""

from typing import List, Optional


class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        """
        Sort by custom comparator: first by length, then lexicographically.
        Since string numbers can be up to 100 digits, we compare by length
        first (longer = larger), then lexicographically for same length.
        """
        nums.sort(key=lambda x: (len(x), x), reverse=True)
        return nums[k - 1]



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, String, Divide and Conquer, Quickselect, Sorting, Heap (Priority Queue)
#
# 解题思路:
# 字符串数字可能长达 100 位，无法转为整数比较。
# 自定义排序：先按长度排序（位数多的更大），长度相同时按字典序排序。
# 排序后取第 k 个最大（索引 k-1）。
# 也可以使用堆维护前 k 大元素，但排序 O(N log N) 对于 N <= 10^4 完全可行。
#
# 时间复杂度: O(N log N * L)，N 为数组长度，L 为字符串比较开销
# 空间复杂度: O(N)，排序所需
#
# 关键点:
# - 大数字不能直接转 int（100 位超出范围）
# - 排序键：(长度, 字典序)
# - 第 k 大对应排序后索引 k-1
