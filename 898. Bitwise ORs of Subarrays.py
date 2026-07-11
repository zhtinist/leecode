"""
LeetCode #898 - Bitwise ORs of Subarrays
中文题名：子数组按位或操作
https://leetcode.com/problems/bitwise-ors-of-subarrays/

We have an array `A` of non-negative integers.

For every (contiguous) subarray `B = [A[i], A[i+1], ..., A[j]]` (with `i
<= j`), we take the bitwise OR of all the elements in `B`, obtaining a
result `A[i] | A[i+1] | ... | A[j]`.

Return the number of possible results.  (Results that occur more than once are only
counted once in the final answer.)

Example 1:

Input: [0]
Output: 1
Explanation:
There is only one possible result: 0.

Example 2:

Input: [1,1,2]
Output: 3
Explanation:
The possible subarrays are [1], [1], [2], [1, 1], [1, 2], [1, 1, 2].
These yield the results 1, 1, 2, 1, 3, 3.
There are 3 unique values, so the answer is 3.

Example 3:

Input: [1,2,4]
Output: 6
Explanation:
The possible results are 1, 2, 3, 4, 6, and 7.

【中文翻译】
给定一个非负整数数组 `A`，对于每个（连续）子数组 `B = [A[i], A[i+1], ..., A[j]]`（其中 `i <= j`），我们对 `B` 中的所有元素进行按位或操作，得到结果 `A[i] | A[i+1] | ... | A[j]`。

返回可能结果的数量。（多次出现的结果只在最终答案中计数一次。）

示例 1：

输入：[0]
输出：1
解释：只有一种可能的结果：0。

示例 2：

输入：[1,1,2]
输出：3
解释：可能的子数组为 [1], [1], [2], [1,1], [1,2], [1,1,2]。
得到的结果为 1, 1, 2, 1, 3, 3。
有 3 个唯一值，所以答案是 3。

示例 3：

输入：[1,2,4]
输出：6
解释：可能的结果为 1, 2, 3, 4, 6 和 7。

"""

from typing import List, Optional


class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        res = set()          # 所有可能的 OR 结果
        cur = set()          # 以当前位置结尾的所有子数组的 OR 结果

        for num in arr:
            cur = {num} | {num | val for val in cur}
            res |= cur

        return len(res)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 核心观察：对于以位置 i 结尾的所有子数组，它们的 OR 值种类最多约 30 种
# （因为按位或操作只增加二进制位，而数字 <= 10^9 最多有 30 位）。
# 因此只需维护"以前一个位置结尾的所有子数组的 OR 值集合"cur，遍历当前数字 num：
#   cur = {num} | {num | val for val in cur}
# 即将所有已有结果 OR 上当前值。用全局集合 res 收集所有出现过的值。
# 最终返回 res 的大小。
#
# 时间复杂度: O(N * log(max_A)) — 每步集合大小上限约 30（即 O(1)），总体 O(N)
# 空间复杂度: O(N * log(max_A)) — res 最多收集所有可能的 OR 值，上限 O(30N) = O(N)
#
# 关键点:
# - OR 操作单调递增（只增不减位数），限制了每个位置结尾的 OR 值种类数
# - 使用集合推导式高效更新 cur
# - 不是暴力的 O(N^2)，而是利用 OR 的性质将每次迭代限制为 O(30)
