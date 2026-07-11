"""
LeetCode #1442 - Count Triplets That Can Form Two Arrays of Equal XOR
中文题名：形成两个异或相等数组的三元组数目
https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/

Given an array of integers `arr`.

We want to select three indices `i`, `j` and `k`
where `(0 <= i < j <= k < arr.length)`.

Let's define `a` and `b` as follows:

`a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]`

`b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]`

Note that ^ denotes the bitwise-xor operation.

Return the number of triplets (`i`, `j` and
`k`) Where `a == b`.

Example 1:

Input: arr = [2,3,1,6,7]
Output: 4
Explanation: The triplets are (0,1,2), (0,2,2), (2,3,4) and (2,4,4)

Example 2:

Input: arr = [1,1,1,1,1]
Output: 10

Example 3:

Input: arr = [2,3]
Output: 0

Example 4:

Input: arr = [1,3,5,7,9]
Output: 3

Example 5:

Input: arr = [7,11,12,9,5,2,7,17,22]
Output: 8

Constraints:

`1 <= arr.length <= 300`

`1 <= arr[i] <= 10^8`

【中文翻译】
给定一个整数数组 `arr`。

我们想要选择三个下标 `i`、`j` 和 `k`，
其中 `(0 <= i < j <= k < arr.length)`。

定义 `a` 和 `b` 如下：

`a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]`

`b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]`

注意 ^ 表示按位异或操作。

返回满足 `a == b` 的三元组 (`i`, `j` 和 `k`) 的数量。

示例 1：

输入：arr = [2,3,1,6,7]
输出：4
解释：三元组为 (0,1,2), (0,2,2), (2,3,4) 和 (2,4,4)

示例 2：

输入：arr = [1,1,1,1,1]
输出：10

示例 3：

输入：arr = [2,3]
输出：0

示例 4：

输入：arr = [1,3,5,7,9]
输出：3

示例 5：

输入：arr = [7,11,12,9,5,2,7,17,22]
输出：8

约束条件：

`1 <= arr.length <= 300`

`1 <= arr[i] <= 10^8`
"""

from typing import List, Optional


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        ans = 0
        n = len(arr)
        for i in range(n):
            xor = 0
            for k in range(i, n):
                xor ^= arr[k]
                if xor == 0:
                    ans += (k - i)
        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 核心观察：a == b 等价于 a ^ b == 0，即 arr[i] ^ ... ^ arr[j-1] ^ arr[j] ^ ... ^ arr[k] == 0。
# 也就是说 arr[i..k] 整个区间的异或结果为 0。
# 对于每个起始位置 i，向后计算累计异或值。当异或变为 0 时，
# 对于任意 j (i < j <= k)，三元组 (i, j, k) 都满足条件，共有 (k-i) 个。
# 将所有这些 (k-i) 累加到答案中。
#
# 时间复杂度: O(N^2)  -- 两层循环遍历所有子数组
# 空间复杂度: O(1)  -- 仅用常数额外空间
#
# 关键点:
# - 利用异或的自我逆运算性质：a ^ a = 0
# - a == b 等价于整个 arr[i..k] 的异或为 0
# - 当区间 [i, k] 异或为 0 时，对于任意 j ∈ (i, k] 都有 a == b，贡献 k-i 个三元组









