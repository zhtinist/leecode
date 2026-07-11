"""
LeetCode #1343 - Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
中文题名：大小为 K 且平均值大于等于阈值的子数组数目
https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/

Given an array of integers `arr` and two integers `k` and
`threshold`.

Return the number of sub-arrays of size `k` and average greater
than or equal to `threshold`.

Example 1:

Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
Output: 3
Explanation: Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6 respectively. All other sub-arrays of size 3 have averages less than 4 (the threshold).

Example 2:

Input: arr = [1,1,1,1,1], k = 1, threshold = 0
Output: 5

Example 3:

Input: arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5
Output: 6
Explanation: The first 6 sub-arrays of size 3 have averages greater than 5. Note that averages are not integers.

Example 4:

Input: arr = [7,7,7,7,7,7,7], k = 7, threshold = 7
Output: 1

Example 5:

Input: arr = [4,4,4,4], k = 4, threshold = 1
Output: 1

Constraints:

`1 <= arr.length <= 10^5`

`1 <= arr[i] <= 10^4`

`1 <= k <= arr.length`

`0 <= threshold <= 10^4`

【中文翻译】
给定一个整数数组 `arr` 和两个整数 `k` 和 `threshold`。

返回大小为 `k` 且平均值大于等于 `threshold` 的子数组的数量。

示例 1：

输入: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
输出: 3
解释: 子数组 [2,5,5]、[5,5,5] 和 [5,5,8] 的平均值分别为 4、5 和 6。
其他长度为 3 的子数组的平均值都小于 4（阈值）。

示例 2：

输入: arr = [1,1,1,1,1], k = 1, threshold = 0
输出: 5
解释: 任一长度为 1 的子数组平均值都是 1 >= 0，共 5 个。

示例 3：

输入: arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5
输出: 6
解释: 前 6 个长度为 3 的子数组的平均值都大于 5。注意平均值不一定是整数。

示例 4：

输入: arr = [7,7,7,7,7,7,7], k = 7, threshold = 7
输出: 1
解释: 唯一的长度为 7 的子数组是整个数组，其平均值为 7 >= 7。

示例 5：

输入: arr = [4,4,4,4], k = 4, threshold = 1
输出: 1

约束条件：

`1 <= arr.length <= 10^5`

`1 <= arr[i] <= 10^4`

`1 <= k <= arr.length`

`0 <= threshold <= 10^4`
"""

from typing import List, Optional


class Solution:
    def numOfSubarrays(
        self, arr: List[int], k: int, threshold: int
    ) -> int:
        # 平均值 >= threshold 等价于 总和 >= threshold * k
        target_sum = threshold * k
        window_sum = sum(arr[:k])
        count = 0

        if window_sum >= target_sum:
            count += 1

        # 滑动窗口：移除左边元素，加入右边元素
        for i in range(k, len(arr)):
            window_sum += arr[i] - arr[i - k]
            if window_sum >= target_sum:
                count += 1

        return count



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 1. 关键化简：子数组平均值 >= threshold 等价于子数组元素总和 >= threshold * k。
#    这样就避免了浮点数运算，全程使用整数比较。
# 2. 使用固定大小的滑动窗口技术：
#    - 先计算前 k 个元素的和作为初始窗口和。
#    - 然后每次将窗口向右滑动一位：窗口和 = 窗口和 + 新进入元素 - 移出元素。
#    - 每次检查 window_sum >= target_sum，若满足则计数器加 1。
# 3. 返回计数器值。
#
# 时间复杂度: O(N) — 遍历数组一次
# 空间复杂度: O(1) — 只使用常数个变量
#
# 关键点:
# - 将平均值比较转化为总和比较，避免浮点数精度问题
# - 滑动窗口：window_sum += arr[i] - arr[i - k] 高效更新
# - 注意初始窗口也要检查










