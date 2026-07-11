"""
LeetCode #1674 - Minimum Moves to Make Array Complementary
中文题名：使数组互补的最少操作次数
https://leetcode.com/problems/minimum-moves-to-make-array-complementary/

You are given an integer array `nums` of even length
`n` and an integer `limit`. In one move, you can replace any
integer from `nums` with another integer between `1` and `limit`,
inclusive.

The array `nums` is complementary if for all indices
`i` (0-indexed), `nums[i] + nums[n - 1 - i]`
equals the same number. For example, the array `[1,2,3,4]` is
complementary because for all indices `i`, `nums[i] + nums[n - 1 -
i] = 5`.

Return the minimum number of moves required to make `nums`
complementary.

Example 1:

Input: nums = [1,2,4,3], limit = 4
Output: 1
Explanation: In 1 move, you can change nums to [1,2,2,3] (underlined elements are changed).
nums[0] + nums[3] = 1 + 3 = 4.
nums[1] + nums[2] = 2 + 2 = 4.
nums[2] + nums[1] = 2 + 2 = 4.
nums[3] + nums[0] = 3 + 1 = 4.
Therefore, nums[i] + nums[n-1-i] = 4 for every i, so nums is complementary.

Example 2:

Input: nums = [1,2,2,1], limit = 2
Output: 2
Explanation: In 2 moves, you can change nums to [2,2,2,2]. You cannot change any number to 3 since 3 > limit.

Example 3:

Input: nums = [1,2,1,2], limit = 2
Output: 0
Explanation: nums is already complementary.

Constraints:

`n == nums.length`

`2 <= n <= 105`

`1 <= nums[i] <= limit <= 105`

`n` is even.

【中文翻译】
给定一个长度为偶数n的整数数组nums和一个整数limit。在一步操作中，你可以将nums中的任意整数替换为另一个在1到limit之间（含两端）的整数。

如果对于所有索引i（从0开始），nums[i]+nums[n-1-i]都等于同一个数，则数组nums是互补的。例如，数组[1,2,3,4]是互补的，因为对于所有i，nums[i]+nums[n-1-i]=5。

返回使nums成为互补数组所需的最少操作次数。

示例1：

输入：nums = [1,2,4,3], limit = 4
输出：1
解释：一步操作可以将nums变为[1,2,2,3]（下划线标注的元素已更改）。
nums[0]+nums[3]=1+3=4。
nums[1]+nums[2]=2+2=4。
所以所有对称位置的和都是4，数组是互补的。

示例2：

输入：nums = [1,2,2,1], limit = 2
输出：2
解释：两步操作可以将nums变为[2,2,2,2]。不能把任何数改为3，因为3>limit。

示例3：

输入：nums = [1,2,1,2], limit = 2
输出：0
解释：nums已经是互补的。

约束条件：

n == nums.length
2 <= n <= 10^5
1 <= nums[i] <= limit <= 10^5
n是偶数。

"""

from typing import List, Optional


class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        # 差分数组，范围是 [2, 2*limit]
        diff = [0] * (2 * limit + 2)

        for i in range(n // 2):
            a, b = nums[i], nums[n - 1 - i]
            # 当前配对和
            cur_sum = a + b
            # 只改一个数能达到的最小和：min(a,b) + 1
            min_sum_one = min(a, b) + 1
            # 只改一个数能达到的最大和：max(a,b) + limit
            max_sum_one = max(a, b) + limit

            # 对于所有 T 在 [2, 2*limit] 范围内：
            # 默认需要2次修改
            diff[2] += 2
            diff[2 * limit + 1] -= 2

            # T 在 [min_sum_one, max_sum_one] 范围内只需要1次修改
            diff[min_sum_one] -= 1
            diff[max_sum_one + 1] += 1

            # T == cur_sum 时不需要修改
            diff[cur_sum] -= 1
            diff[cur_sum + 1] += 1

        # 扫描差分数组得到最小操作次数
        ans = n  # 最多 n 次修改
        cur = 0
        for T in range(2, 2 * limit + 1):
            cur += diff[T]
            ans = min(ans, cur)

        return ans










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 差分数组/扫描线。对于每对对称元素(a,b)，设目标和为T：
# - 如果T == a+b，不需要修改（0次操作）
# - 如果T在[min(a,b)+1, max(a,b)+limit]范围内，修改1个元素即可（1次操作）
# - 否则需要修改2个元素（2次操作）
# 遍历所有配对，用差分数组记录不同T需要的操作次数，最后扫描差分数组找到最小值。
# T的取值范围是[2, 2*limit]。
#
# 时间复杂度: O(n + limit)
# 空间复杂度: O(limit)
#
# 关键点:
# - 差分数组技巧高效处理区间更新
# - 对于配对(a,b)，分析需要0/1/2次操作的目标和T范围
# - 只改一个数时，最小值是min(a,b)+1（把小的改成1），最大值是max(a,b)+limit（把大的改成limit）
# - 最后扫描所有可能的T值（2到2*limit），取最小操作次数
