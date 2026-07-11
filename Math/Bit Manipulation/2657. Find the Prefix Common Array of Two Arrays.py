"""
LeetCode #2657 - Find the Prefix Common Array of Two Arrays
找到两个数组的前缀公共数组
https://leetcode.cn/problems/find-the-prefix-common-array-of-two-arrays/

给你两个下标从 0 开始长度为 `n` 的整数排列 `A` 和 `B` 。
`A` 和 `B` 的 前缀公共数组 定义为数组 `C` ，其中 `C[i]` 是数组 `A` 和 `B` 到下标为 `i` 之前公共元素的数目。
请你返回 `A` 和 `B` 的 前缀公共数组 。
如果一个长度为 `n` 的数组包含 `1` 到 `n` 的元素恰好一次，我们称这个数组是一个长度为 `n` 的 排列 。

示例 1：
输入：A = [1,3,2,4], B = [3,1,2,4] 输出：[0,2,3,4] 解释：i = 0：没有公共元素，所以 C[0] = 0 。 i = 1：1 和 3 是两个数组的前缀公共元素，所以 C[1] = 2 。 i = 2：1，2 和 3 是两个数组的前缀公共元素，所以 C[2] = 3 。 i = 3：1，2，3 和 4 是两个数组的前缀公共元素，所以 C[3] = 4 。
示例 2：
输入：A = [2,3,1], B = [3,1,2] 输出：[0,1,3] 解释：i = 0：没有公共元素，所以 C[0] = 0 。 i = 1：只有 3 是公共元素，所以 C[1] = 1 。 i = 2：1，2 和 3 是两个数组的前缀公共元素，所以 C[2] = 3 。

提示：
`1 <= A.length == B.length == n <= 50`
`1 <= A[i], B[i] <= n`
题目保证 `A` 和 `B` 两个数组都是 `n` 个元素的排列。
"""

from typing import List, Optional


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        ans = []
        seen_A = set()
        seen_B = set()
        for i in range(n):
            seen_A.add(A[i])
            seen_B.add(B[i])
            ans.append(len(seen_A & seen_B))
        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Bit Manipulation, Array, Hash Table
#
# 解题思路:
# 维护两个集合分别记录A和B中出现过的元素。对于每个位置i，将A[i]和B[i]分别加入对应集合，
# 然后计算两个集合的交集大小即为到i为止的公共元素数量。
# 由于A和B都是1到n的排列，两集合的并集大小最多为n。
#
# 时间复杂度: O(n^2)  (n<=50可接受) 或 O(n)使用频率计数
# 空间复杂度: O(n)
#
# 关键点:
# - 公共元素 = 在两个数组中都出现过的元素
# - 集合交集的大小就是公共元素数量
# - 也可用频率计数：当元素出现次数=2时公共数+1
