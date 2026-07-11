"""
LeetCode #974 - Subarray Sums Divisible by K
中文题名：和可被 K 整除的子数组
https://leetcode.com/problems/subarray-sums-divisible-by-k/

给定一个整数数组 A，返回其中元素之和可被 K 整除的（连续、非空）子数组的数目。

示例 1：

输入：A = [4,5,0,-2,-3,1], K = 5
输出：7
解释：有 7 个子数组的元素之和可以被 K = 5 整除：
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]

注意：

1 <= A.length <= 30000
-10000 <= A[i] <= 10000
2 <= K <= 10000

【中文翻译】
给定一个整数数组 A，求元素之和能被 K 整除的连续子数组的个数。注意数组元素可能为负数，K 可能大于数组长度。

"""

from typing import List, Optional
from collections import defaultdict


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # prefix sum modulo frequency
        mod_count = defaultdict(int)
        mod_count[0] = 1  # empty prefix sum is divisible
        prefix_sum = 0
        result = 0
        for num in nums:
            prefix_sum += num
            mod = prefix_sum % k
            result += mod_count[mod]
            mod_count[mod] += 1
        return result



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 前缀和 + 同余定理 + 哈希表：
# 1. 子数组和能被 K 整除，等价于前缀和对 K 取模的余数相同。
#    - 设 prefix[i] = A[0] + ... + A[i-1]（前 i 个元素的和）
#    - 子数组 A[i..j] 的和 = prefix[j+1] - prefix[i]
#    - 若 (prefix[j+1] - prefix[i]) % K == 0，则 prefix[j+1] % K == prefix[i] % K
# 2. 遍历数组，计算累积前缀和对 K 取模的余数。
# 3. 使用哈希表记录每个余数出现的次数。
# 4. 对于当前余数 mod，已有 count[mod] 个之前的前缀和与当前前缀和对 K 同余，
#    意味着有 count[mod] 个子数组的和可被 K 整除，累加到结果中。
# 5. 初始化 count[0] = 1，表示空前缀（和为 0）可以被任何 K 整除。
#
# 时间复杂度: O(N)，遍历一次数组
# 空间复杂度: O(min(N, K))，哈希表最多存储 min(N, K) 个不同的余数。实际上最多 K 个
#
# 关键点:
# - 同余定理：(a - b) % K == 0 <=> a % K == b % K
# - Python 中负数取模结果自动为非负（符合数学定义），无需特殊处理
# - 前缀和模 K 相等的两个位置之间构成一个符合条件的子数组
# - 初始化 count[0] = 1 处理从数组开头开始的子数组
