"""
LeetCode #3152 - Special Array II
特殊数组 II
https://leetcode.cn/problems/special-array-ii/

如果数组的每一对相邻元素都是两个奇偶性不同的数字，则该数组被认为是一个 特殊数组 。
你有一个整数数组 `nums` 和一个二维整数矩阵 `queries`，对于 `queries[i] = [from_i, to_i]`，请你帮助你检查 子数组 `nums[from_i..to_i]` 是不是一个 特殊数组 。
返回布尔数组 `answer`，如果 `nums[from_i..to_i]` 是特殊数组，则 `answer[i]` 为 `true` ，否则，`answer[i]` 为 `false` 。

示例 1：

输入：nums = [3,4,1,2,6], queries = [[0,4]]
输出：[false]
解释：
子数组是 `[3,4,1,2,6]`。2 和 6 都是偶数。
示例 2：

输入：nums = [4,3,1,6], queries = [[0,2],[2,3]]
输出：[false,true]
解释：
子数组是 `[4,3,1]`。3 和 1 都是奇数。因此这个查询的答案是 `false`。
子数组是 `[1,6]`。只有一对：`(1,6)`，且包含了奇偶性不同的数字。因此这个查询的答案是 `true`。

提示：
`1 <= nums.length <= 10^5`
`1 <= nums[i] <= 10^5`
`1 <= queries.length <= 10^5`
`queries[i].length == 2`
`0 <= queries[i][0] <= queries[i][1] <= nums.length - 1`
"""

from typing import List, Optional


class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        # violation[i] = 1 如果 nums[i] 和 nums[i+1] 奇偶性相同
        violation = [0] * (n - 1)
        for i in range(n - 1):
            if nums[i] % 2 == nums[i + 1] % 2:
                violation[i] = 1

        # 前缀和
        pref = [0] * n
        for i in range(n - 1):
            pref[i + 1] = pref[i] + violation[i]

        ans = []
        for l, r in queries:
            # 区间 [l, r] 内相邻配对数 = r - l 对
            # 检查是否有违规
            if l == r or pref[r] - pref[l] == 0:
                ans.append(True)
            else:
                ans.append(False)
        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Binary Search, Prefix Sum
#
# 解题思路:
# 特殊数组要求相邻元素奇偶性不同。预处理违规标记数组violation，
# 其中violation[i]=1表示nums[i]和nums[i+1]奇偶性相同。
# 构建前缀和pref，对于查询[l,r]，区间内需要检查r-l对相邻关系，
# 即pref[r] - pref[l]是否为0（无违规）。等于0则为特殊数组。
#
# 时间复杂度: O(n + q)
# 空间复杂度: O(n)
#
# 关键点:
# - 奇偶性检查：nums[i]%2 == nums[i+1]%2
# - 前缀和快速判断区间内是否有违规
# - l==r时长度1，必定是特殊数组
