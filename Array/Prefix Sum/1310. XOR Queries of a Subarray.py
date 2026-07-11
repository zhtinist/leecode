"""
LeetCode #1310 - XOR Queries of a Subarray
中文题名：子数组异或查询
https://leetcode.com/problems/xor-queries-of-a-subarray/

Given the array `arr` of positive integers and the array
`queries` where `queries[i] = [Li, Ri]`, for
each query `i` compute the XOR of elements from `Li`
to `Ri` (that is, `arr[Li] xor
arr[Li+1] xor ... xor arr[Ri]`
). Return an array containing the result for the given `queries`.

Example 1:

Input: arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]
Output: [2,7,14,8]
Explanation:
The binary representation of the elements in the array are:
1 = 0001
3 = 0011
4 = 0100
8 = 1000
The XOR values for queries are:
[0,1] = 1 xor 3 = 2
[1,2] = 3 xor 4 = 7
[0,3] = 1 xor 3 xor 4 xor 8 = 14
[3,3] = 8

Example 2:

Input: arr = [4,8,2,10], queries = [[2,3],[1,3],[0,0],[0,3]]
Output: [8,0,4,4]

Constraints:

`1 <= arr.length <= 3 * 10^4`

`1 <= arr[i] <= 10^9`

`1 <= queries.length <= 3 * 10^4`

`queries[i].length == 2`

`0 <= queries[i][0] <= queries[i][1] < arr.length`

【中文翻译】
给定正整数数组 arr 和查询数组 queries，其中 queries[i] = [Li, Ri]。
对于每个查询 i，计算从 Li 到 Ri 的元素异或结果（即 arr[Li] xor arr[Li+1] xor ... xor arr[Ri]）。
返回一个包含所有查询结果的数组。

示例 1：
输入：arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]
输出：[2,7,14,8]
解释：
数组中元素的二进制表示：
1 = 0001
3 = 0011
4 = 0100
8 = 1000
查询的异或值：
[0,1] = 1 xor 3 = 2
[1,2] = 3 xor 4 = 7
[0,3] = 1 xor 3 xor 4 xor 8 = 14
[3,3] = 8

示例 2：
输入：arr = [4,8,2,10], queries = [[2,3],[1,3],[0,0],[0,3]]
输出：[8,0,4,4]

约束条件：
1 <= arr.length <= 3 * 10^4
1 <= arr[i] <= 10^9
1 <= queries.length <= 3 * 10^4
queries[i].length == 2
0 <= queries[i][0] <= queries[i][1] < arr.length
"""

from typing import List


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        # prefix[i] = XOR of arr[0..i-1], prefix[0] = 0
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] ^ arr[i]

        result = []
        for L, R in queries:
            # XOR[L..R] = prefix[R+1] ^ prefix[L]
            result.append(prefix[R + 1] ^ prefix[L])
        return result



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用前缀异或（Prefix XOR）技巧。
# 定义 prefix[i] = arr[0] ^ arr[1] ^ ... ^ arr[i-1]，即前 i 个元素的异或结果。
# 则任意区间 [L, R] 的异或结果为：
#   XOR(L..R) = prefix[R+1] ^ prefix[L]
# 这是因为：prefix[R+1] 包含了 arr[0..R] 的异或，
# 再异或上 prefix[L]（即 arr[0..L-1] 的异或），
# arr[0..L-1] 部分被异或两次抵消，剩下 arr[L..R] 的异或。
# 预处理前缀异或数组 O(N)，然后每个查询 O(1) 回答。
#
# 时间复杂度: O(N + Q)，N 为 arr 长度，Q 为 queries 数量。
#  构建前缀数组 O(N)，每个查询 O(1)。
# 空间复杂度: O(N)，存储前缀异或数组（结果数组不计入额外空间）。
#
# 关键点:
# - XOR 的逆运算就是 XOR 自身，即 a ^ b ^ b = a
# - 前缀 XOR 与前缀和的原理完全相同，只是将 "+" 换成 "^"
# - prefix[0] = 0 作为哨兵，方便处理从索引 0 开始的区间
# - 区间 [L, R] 对应 prefix[R+1] ^ prefix[L]
# - 异或满足结合律和交换律










