"""
LeetCode #1471 - The k Strongest Values in an Array
中文题名：数组中最强的 k 个值
https://leetcode.com/problems/the-k-strongest-values-in-an-array/

Given an array of integers `arr` and an integer `k`.

A value `arr[i]` is said to be stronger than a value `arr[j]`
if `|arr[i] - m| > |arr[j] - m|` where `m` is the
median of the array.

If `|arr[i] - m| == |arr[j] - m|`, then `arr[i]` is said to be
stronger than `arr[j]` if `arr[i] > arr[j]`.

Return a list of the strongest `k` values in the array. return
the answer in any arbitrary order.

Median is the middle value in an ordered integer list. More
formally, if the length of the list is n, the median is the element in position
`((n - 1) / 2)` in the sorted list (0-indexed).

For `arr = [6, -3, 7, 2, 11]`, `n = 5` and the
median is obtained by sorting the array `arr = [-3, 2, 6, 7,
11]` and the median is `arr[m]` where `m = ((5 - 1) /
2) = 2`. The median is `6`.

For `arr = [-7, 22, 17, 3]`, `n = 4` and the
median is obtained by sorting the array `arr = [-7, 3, 17, 22]`
and the median is `arr[m]` where `m = ((4 - 1) / 2) = 1`.
The median is `3`.

Example 1:

Input: arr = [1,2,3,4,5], k = 2
Output: [5,1]
Explanation: Median is 3, the elements of the array sorted by the strongest are [5,1,4,2,3]. The strongest 2 elements are [5, 1]. [1, 5] is also accepted answer.
Please note that although |5 - 3| == |1 - 3| but 5 is stronger than 1 because 5 > 1.

Example 2:

Input: arr = [1,1,3,5,5], k = 2
Output: [5,5]
Explanation: Median is 3, the elements of the array sorted by the strongest are [5,5,1,1,3]. The strongest 2 elements are [5, 5].

Example 3:

Input: arr = [6,7,11,7,6,8], k = 5
Output: [11,8,6,6,7]
Explanation: Median is 7, the elements of the array sorted by the strongest are [11,8,6,6,7,7].
Any permutation of [11,8,6,6,7] is accepted.

Example 4:

Input: arr = [6,-3,7,2,11], k = 3
Output: [-3,11,2]

Example 5:

Input: arr = [-7,22,17,3], k = 2
Output: [22,17]

Constraints:

`1 <= arr.length <= 10^5`

`-10^5 <= arr[i] <= 10^5`

`1 <= k <= arr.length`

【中文翻译】

给定一个整数数组 `arr` 和一个整数 `k`。

一个值 `arr[i]` 被认为比 `arr[j]` 更强，如果 `|arr[i] - m| > |arr[j] - m|`，其中 `m` 是数组的中位数。
如果 `|arr[i] - m| == |arr[j] - m|`，那么当 `arr[i] > arr[j]` 时，`arr[i]` 比 `arr[j]` 更强。

返回数组中最强的 `k` 个值的列表。答案可以按任意顺序返回。

中位数是有序整数列表中的中间值。更正式地说，如果列表的长度为 n，则中位数是排序列表中位置 `((n - 1) / 2)` 的元素（0 索引）。

示例 1：
输入：arr = [1,2,3,4,5], k = 2
输出：[5,1]
解释：中位数为 3，按强度排序后的数组元素为 [5,1,4,2,3]。最强的 2 个元素是 [5, 1]。[1, 5] 也是可接受的答案。请注意，虽然 |5 - 3| == |1 - 3|，但 5 比 1 更强，因为 5 > 1。

示例 2：
输入：arr = [1,1,3,5,5], k = 2
输出：[5,5]
解释：中位数为 3，按强度排序后的数组元素为 [5,5,1,1,3]。最强的 2 个元素是 [5, 5]。

示例 3：
输入：arr = [6,7,11,7,6,8], k = 5
输出：[11,8,6,6,7]
解释：中位数为 7，按强度排序后的数组元素为 [11,8,6,6,7,7]。[11,8,6,6,7] 的任意排列均可接受。

示例 4：
输入：arr = [6,-3,7,2,11], k = 3
输出：[-3,11,2]

示例 5：
输入：arr = [-7,22,17,3], k = 2
输出：[22,17]

约束条件：
1 <= arr.length <= 10^5
-10^5 <= arr[i] <= 10^5
1 <= k <= arr.length

"""

from typing import List, Optional


class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        n = len(arr)
        median = arr[(n - 1) // 2]

        # Sort by (abs diff, value) descending
        arr.sort(key=lambda x: (abs(x - median), x), reverse=True)

        return arr[:k]



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 1. 首先对数组排序，计算中位数 m = arr[(n-1)//2]。
# 2. 然后按照强度定义排序：首要关键字为 |arr[i] - m|（降序），
#    次要关键字为 arr[i] 本身（降序）。
# 3. 取排序后的前 k 个元素即可。
# 4. 也可以使用双指针法：排序后使用左右指针向中间靠拢，
#    每次选择"更强"的值，共选 k 次。时间复杂度 O(N log N) 主要
#    来自排序。
#
# 时间复杂度: O(N log N)
# 空间复杂度: O(1) 或 O(N)（取决于排序算法）
#
# 关键点:
# - 中位数的定义：排序数组中索引 (n-1)//2 的元素
# - 强度比较规则：先比绝对差，再比元素值本身
# - 排序后直接取前 k 个即可










