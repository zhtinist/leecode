"""
LeetCode #985 - Sum of Even Numbers After Queries
中文题名：查询后的偶数和
https://leetcode.com/problems/sum-of-even-numbers-after-queries/

有一个整数数组 A 和一个查询数组 queries。

对于第 i 次查询 val = queries[i][0], index = queries[i][1]，我们会把 val 加到 A[index] 上。然后，第 i 次查询的答案是 A 中所有偶数值的和。

（这里给定的 index = queries[i][1] 是从 0 开始的索引，每次查询都会永久修改数组 A。）

返回所有查询的答案。你的回答数组 answer 中 answer[i] 为第 i 次查询的答案。

示例 1：

输入：A = [1,2,3,4], queries = [[1,0],[-3,1],[-4,0],[2,3]]
输出：[8,6,2,4]
解释：
开始时，数组为 [1,2,3,4]。
将 1 加到 A[0] 上之后，数组为 [2,2,3,4]，偶数值之和为 2 + 2 + 4 = 8。
将 -3 加到 A[1] 上之后，数组为 [2,-1,3,4]，偶数值之和为 2 + 4 = 6。
将 -4 加到 A[0] 上之后，数组为 [-2,-1,3,4]，偶数值之和为 -2 + 4 = 2。
将 2 加到 A[3] 上之后，数组为 [-2,-1,3,6]，偶数值之和为 -2 + 6 = 4。

注意：

1 <= A.length <= 10000
-10000 <= A[i] <= 10000
1 <= queries.length <= 10000
-10000 <= queries[i][0] <= 10000
0 <= queries[i][1] < A.length

【中文翻译】
给定一个整数数组 A 和一系列查询，每次查询将指定值加到一个指定索引位置，然后求修改后数组中所有偶数元素的总和。需要返回每次查询后的偶数和结果。

"""

from typing import List, Optional


class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        # Calculate initial sum of even numbers
        even_sum = sum(x for x in nums if x % 2 == 0)
        result = []
        for val, idx in queries:
            old_val = nums[idx]
            # Remove old_val from sum if it was even
            if old_val % 2 == 0:
                even_sum -= old_val
            # Apply query
            nums[idx] = old_val + val
            # Add new value to sum if it is even
            if nums[idx] % 2 == 0:
                even_sum += nums[idx]
            result.append(even_sum)
        return result



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 维护当前偶数和：
# 1. 预先计算数组 A 中所有偶数的总和 even_sum。
# 2. 遍历每个查询 (val, idx)：
#    - 记录 A[idx] 的旧值 old_val。
#    - 如果 old_val 是偶数，从 even_sum 中减去它（因为即将被修改）。
#    - 更新 A[idx] = old_val + val。
#    - 如果新的 A[idx] 是偶数，将其加入 even_sum。
#    - 将当前 even_sum 加入结果数组。
# 3. 这样每次查询只需 O(1) 时间更新偶数和，避免了每次重新扫描整个数组。
#
# 时间复杂度: O(N + Q)，N 为数组长度（初始计算偶数和），Q 为查询数（每个查询 O(1)）
# 空间复杂度: O(1)，除了输出数组外只使用常量额外空间
#
# 关键点:
# - 维护一个 running sum 的偶数和，避免每次查询都重新遍历数组
# - 每次查询只影响一个位置的值，只需检查该位置的奇偶性变化
# - 分两步：先移除旧值（如果是偶数），再加回新值（如果是偶数）
# - 注意负数也可以是偶数（-2 % 2 == 0）
