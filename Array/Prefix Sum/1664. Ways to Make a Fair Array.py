"""
LeetCode #1664 - Ways to Make a Fair Array
中文题名：生成平衡数组的方案数
https://leetcode.com/problems/ways-to-make-a-fair-array/

You are given an integer array `nums`. You can choose exactly
one index (0-indexed) and remove the element. Notice that the
index of the elements may change after the removal.

For example, if `nums = [6,1,7,4,1]`:

Choosing to remove index `1` results in `nums = [6,7,4,1]`.

Choosing to remove index `2` results in `nums = [6,1,4,1]`.

Choosing to remove index `4` results in `nums = [6,1,7,4]`.

An array is fair if the sum of the odd-indexed values equals the sum
of the even-indexed values.

Return the number of indices that you could choose such that
after the removal, `nums` is fair.

Example 1:

Input: nums = [2,1,6,4]
Output: 1
Explanation:
Remove index 0: [1,6,4] -> Even sum: 1 + 4 = 5. Odd sum: 6. Not fair.
Remove index 1: [2,6,4] -> Even sum: 2 + 4 = 6. Odd sum: 6. Fair.
Remove index 2: [2,1,4] -> Even sum: 2 + 4 = 6. Odd sum: 1. Not fair.
Remove index 3: [2,1,6] -> Even sum: 2 + 6 = 8. Odd sum: 1. Not fair.
There is 1 index that you can remove to make nums fair.

Example 2:

Input: nums = [1,1,1]
Output: 3
Explanation: You can remove any index and the remaining array is fair.

Example 3:

Input: nums = [1,2,3]
Output: 0
Explanation: You cannot make a fair array after removing any index.

Constraints:

`1 <= nums.length <= 105`

`1 <= nums[i] <= 104`

【中文翻译】
给定一个整数数组nums。你可以选择恰好一个索引（从0开始）并移除该位置的元素。注意移除后元素的下标可能会发生改变。

例如，如果nums=[6,1,7,4,1]：
- 选择移除索引1，得到nums=[6,7,4,1]
- 选择移除索引2，得到nums=[6,1,4,1]
- 选择移除索引4，得到nums=[6,1,7,4]

如果一个数组中奇数下标元素之和等于偶数下标元素之和，则该数组是平衡的。

返回你可以移除后使得nums变成平衡数组的索引的数量。

示例1：

输入：nums = [2,1,6,4]
输出：1
解释：
移除索引0：[1,6,4] -> 偶数下标之和：1+4=5，奇数下标之和：6，不平衡。
移除索引1：[2,6,4] -> 偶数下标之和：2+4=6，奇数下标之和：6，平衡。
移除索引2：[2,1,4] -> 偶数下标之和：2+4=6，奇数下标之和：1，不平衡。
移除索引3：[2,1,6] -> 偶数下标之和：2+6=8，奇数下标之和：1，不平衡。
有1个索引可以在移除后使nums变成平衡数组。

示例2：

输入：nums = [1,1,1]
输出：3
解释：你可以移除任意索引，剩余数组都是平衡的。

示例3：

输入：nums = [1,2,3]
输出：0
解释：无论移除哪个索引，都无法使数组平衡。

约束条件：

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^4

"""

from typing import List, Optional


class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums)
        # prefix_even[i] = 前i个元素中偶数下标元素之和 (i excluded)
        # prefix_odd[i]  = 前i个元素中奇数下标元素之和 (i excluded)
        prefix_even = [0] * (n + 1)
        prefix_odd = [0] * (n + 1)
        for i in range(n):
            prefix_even[i + 1] = prefix_even[i]
            prefix_odd[i + 1] = prefix_odd[i]
            if i % 2 == 0:
                prefix_even[i + 1] += nums[i]
            else:
                prefix_odd[i + 1] += nums[i]

        total_even = prefix_even[n]
        total_odd = prefix_odd[n]
        ans = 0

        for i in range(n):
            # 移除 nums[i] 后：
            # 左侧原偶数下标还是偶数下标，左侧原奇数下标还是奇数下标
            left_even = prefix_even[i]
            left_odd = prefix_odd[i]
            # 右侧元素的下标奇偶性全部翻转（原来偶数变奇数，原来奇数变偶数）
            right_even = total_odd - prefix_odd[i + 1]
            right_odd = total_even - prefix_even[i + 1]

            new_even = left_even + right_even
            new_odd = left_odd + right_odd
            if new_even == new_odd:
                ans += 1

        return ans










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 前缀和。移除索引i后，i左侧的所有元素下标奇偶性不变，i右侧的所有元素下标奇偶性翻转
# （原偶数下标变奇数，原奇数下标变偶数）。
# 预处理偶数下标和奇数下标的前缀和。对于每个位置i：
# - 新的偶数下标和 = i左侧的偶数下标和 + i右侧的奇数下标和
# - 新的奇数下标和 = i左侧的奇数下标和 + i右侧的偶数下标和
# 判断两者是否相等即可。
#
# 时间复杂度: O(n)
# 空间复杂度: O(n)，可以优化为O(1)但前缀数组更清晰
#
# 关键点:
# - 移除元素后，右侧元素的奇偶下标翻转
# - 用前缀和预处理偶数和奇数下标和
# - 对于位置i，注意prefix[i]不包含i，prefix[i+1]包含i
