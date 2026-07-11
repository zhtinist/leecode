"""
LeetCode #1679 - Max Number of K-Sum Pairs
中文题名：K和数对的最大数目
https://leetcode.com/problems/max-number-of-k-sum-pairs/

You are given an integer array `nums` and an integer `k`.

In one operation, you can pick two numbers from the array whose sum equals
`k` and remove them from the array.

Return the maximum number of operations you can perform on the array.

Example 1:

Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.

Example 2:

Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.

Constraints:

`1 <= nums.length <= 105`

`1 <= nums[i] <= 109`

`1 <= k <= 109`

【中文翻译】
给定一个整数数组nums和一个整数k。

在一次操作中，你可以从数组中选出两个和为k的数并将它们从数组中移除。

返回你可以对数组执行的最大操作次数。

示例1：

输入：nums = [1,2,3,4], k = 5
输出：2
解释：从nums=[1,2,3,4]开始：
- 移除数字1和4，得到nums=[2,3]
- 移除数字2和3，得到nums=[]
没有更多的和为5的数对，因此总共2次操作。

示例2：

输入：nums = [3,1,3,4,3], k = 6
输出：1
解释：从nums=[3,1,3,4,3]开始：
- 移除前两个3，得到nums=[1,4,3]
没有更多的和为6的数对，因此总共1次操作。

约束条件：

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
1 <= k <= 10^9

"""

from typing import List, Optional


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        from collections import Counter
        freq = Counter(nums)
        ans = 0
        for num in freq:
            complement = k - num
            if complement in freq:
                if num == complement:
                    # 同一元素配对，如 x + x = k
                    ans += freq[num] // 2
                elif num < complement:
                    # 不同元素配对，取两者频次的较小值
                    ans += min(freq[num], freq[complement])
        return ans










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用哈希表统计频率。对于每个数num，查找其补数complement = k - num：
# - 如果num == complement（如x+x=k），可以匹配freq[num] // 2对
# - 如果num < complement（避免重复计数），每对消耗min(freq[num], freq[complement])个元素
# 另一种解法：排序+双指针，时间复杂度O(nlogn)。
#
# 时间复杂度: O(n)
# 空间复杂度: O(n)
#
# 关键点:
# - 哈希表统计频率，O(n)时间
# - 处理num == complement的情况（同一元素配对）
# - 使用num < complement条件避免重复计数
# - 也可以用双指针法
