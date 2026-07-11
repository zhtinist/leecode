"""
LeetCode #1186 - Maximum Subarray Sum with One Deletion
中文题名：删除一次得到子数组最大和
https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/

Given an array of integers, return the maximum sum for a non-empty subarray
(contiguous elements) with at most one element deletion. In other words, you want to
choose a subarray and optionally delete one element from it so that there is still at least
one element left and the sum of the remaining elements is maximum possible.

Note that the subarray needs to be non-empty after deleting one element.

Example 1:

Input: arr = [1,-2,0,3]
Output: 4
Explanation: Because we can choose [1, -2, 0, 3] and drop -2, thus the subarray [1, 0, 3] becomes the maximum value.

Example 2:

Input: arr = [1,-2,-2,3]
Output: 3
Explanation: We just choose [3] and it's the maximum sum.

Example 3:

Input: arr = [-1,-1,-1,-1]
Output: -1
Explanation: The final subarray needs to be non-empty. You can't choose [-1] and delete -1 from it, then get an empty subarray to make the sum equals to 0.

Constraints:

`1 <= arr.length <= 10^5`

`-10^4 <= arr[i] <= 10^4`

【中文翻译】
给你一个整数数组 arr，返回它的某个非空子数组（连续元素）在执行一次可选的删除操作后，所能得到的最大元素总和。换句话说，你可以从数组中选出一个子数组并从中删除至多一个元素（也可以不删除），使得剩余元素的总和最大。

注意：删除一个元素后，子数组必须非空。

示例 1：

输入：arr = [1,-2,0,3]
输出：4
解释：我们可以选择 [1, -2, 0, 3]，然后删除 -2，剩余元素 [1, 0, 3] 的和为最大值。

示例 2：

输入：arr = [1,-2,-2,3]
输出：3
解释：我们直接选出 [3]，它的和是最大值。

示例 3：

输入：arr = [-1,-1,-1,-1]
输出：-1
解释：最终子数组必须非空。不能选择 [-1] 并删除 -1，得到一个空子数组使和为 0。

约束条件：

1 <= arr.length <= 10^5
-10^4 <= arr[i] <= 10^4

"""

from typing import List, Optional


class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        # noDelete: 以当前元素结尾、未删除任何元素的最大子数组和
        # oneDelete: 以当前元素结尾、已删除一个元素的最大子数组和
        noDelete = arr[0]
        oneDelete = 0  # 至少需要两个元素才能删除一个
        res = arr[0]

        for i in range(1, n):
            # 若从未删除，则要么延续前面的子数组，要么从当前元素重新开始
            # 若已删除一个，则要么删除当前元素（延续前面的 noDelete），要么在前面已删除的基础上加当前元素
            oneDelete = max(noDelete, oneDelete + arr[i])
            noDelete = max(noDelete + arr[i], arr[i])
            res = max(res, noDelete, oneDelete)

        return res










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用动态规划，维护两个状态：
# - noDelete: 以当前元素结尾、未删除任何元素的最大子数组和（即标准 Kadane 算法）
# - oneDelete: 以当前元素结尾、已删除一个元素的最大子数组和
#
# 状态转移：
# - noDelete[i] = max(noDelete[i-1] + arr[i], arr[i])
#   要么延续前面的子数组，要么从当前元素重新开始（不删除任何元素）
# - oneDelete[i] = max(noDelete[i-1], oneDelete[i-1] + arr[i])
#   要么删除当前元素（此时当前元素不计入，子数组和为 noDelete[i-1]），
#   要么在前面已删除一个的基础上加上当前元素
#
# 注意：oneDelete 初始化为 0，因为至少需要两个元素才能有一个被删除。
# 最终结果取所有状态中的最大值。
#
# 时间复杂度: O(n) - 单次遍历数组
# 空间复杂度: O(1) - 只使用常数个变量
#
# 关键点:
# - 两个 DP 状态分别表示"未删除"和"已删除一次"的情况
# - oneDelete 的转移：删除当前元素（延续 noDelete[i-1]）或保留当前元素（延续 oneDelete[i-1]）
# - 初始时 oneDelete = 0，因为单独一个元素不能"已删除"
# - 结果是遍历过程中所有 noDelete 和 oneDelete 的最大值，而非最后一个元素的值
