"""
LeetCode #1497 - Check If Array Pairs Are Divisible by k
中文题名：检查数组对是否可以被 k 整除
https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/

Given an array of integers `arr` of even length `n` and an integer
`k`.

We want to divide the array into exactly `n / 2` pairs such that the sum
of each pair is divisible by `k`.

Return True If you can find a way to do that or False otherwise.

Example 1:

Input: arr = [1,2,3,4,5,10,6,7,8,9], k = 5
Output: true
Explanation: Pairs are (1,9),(2,8),(3,7),(4,6) and (5,10).

Example 2:

Input: arr = [1,2,3,4,5,6], k = 7
Output: true
Explanation: Pairs are (1,6),(2,5) and(3,4).

Example 3:

Input: arr = [1,2,3,4,5,6], k = 10
Output: false
Explanation: You can try all possible pairs to see that there is no way to divide arr into 3 pairs each with sum divisible by 10.

Example 4:

Input: arr = [-10,10], k = 2
Output: true

Example 5:

Input: arr = [-1,1,-2,2,-3,3,-4,4], k = 3
Output: true

Constraints:

`arr.length == n`

`1 <= n <= 10^5`

`n` is even.

`-10^9 <= arr[i] <= 10^9`

`1 <= k <= 10^5`

【中文翻译】

给定一个偶数长度 `n` 的整数数组 `arr` 和一个整数 `k`。

我们想将数组恰好分成 `n / 2` 对，使得每对的和都能被 `k` 整除。

如果能找到这样的分法，返回 True，否则返回 False。

示例 1：
输入：arr = [1,2,3,4,5,10,6,7,8,9], k = 5
输出：true
解释：对为 (1,9)、(2,8)、(3,7)、(4,6) 和 (5,10)。

示例 2：
输入：arr = [1,2,3,4,5,6], k = 7
输出：true
解释：对为 (1,6)、(2,5) 和 (3,4)。

示例 3：
输入：arr = [1,2,3,4,5,6], k = 10
输出：false
解释：可以尝试所有可能的配对，但没有办法将 arr 分成 3 对每对和都能被 10 整除。

示例 4：
输入：arr = [-10,10], k = 2
输出：true

示例 5：
输入：arr = [-1,1,-2,2,-3,3,-4,4], k = 3
输出：true

约束条件：
arr.length == n 且为偶数
1 <= n <= 10^5
-10^9 <= arr[i] <= 10^9
1 <= k <= 10^5

"""

from typing import List, Optional


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        from collections import Counter
        # Count remainder frequencies (handle negative numbers)
        rem = [0] * k
        for num in arr:
            r = num % k
            # Python's % on negative gives positive remainder
            rem[r] += 1

        # Check remainder 0: must be even
        if rem[0] % 2 != 0:
            return False

        # Check all other remainders
        for r in range(1, k // 2 + 1):
            if r == k - r:  # when k is even, middle remainder
                if rem[r] % 2 != 0:
                    return False
            elif rem[r] != rem[k - r]:
                return False

        return True



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 1. 两数之和能被 k 整除，等价于两数的余数之和能被 k 整除。
#    (a + b) % k == 0 等价于 (a % k + b % k) % k == 0。
# 2. 统计每个余数的出现频率（注意处理负数：Python 的 % 运算
#    对负数也返回非负余数）。
# 3. 配对规则：
#    - 余数为 0 的元素必须两两配对（因为 0+0=0 能被 k 整除），
#      所以 rem[0] 必须是偶数。
#    - 对于其他余数 r（1 <= r <= k//2），rem[r] 必须等于
#      rem[k-r]（因为 r + (k-r) = k 能被 k 整除）。
#    - 如果 k 是偶数，余数为 k/2 的元素也必须两两配对，
#      所以 rem[k/2] 必须是偶数。
# 4. 如果所有条件满足，返回 True，否则返回 False。
#
# 时间复杂度: O(N)
# 空间复杂度: O(K)
#
# 关键点:
# - 同余定理：(a+b)%k==0 等价于 a%k + b%k 为 0 或 k
# - Python 的 % 对负数得到非负余数，简化了处理
# - 处理 k 为偶数时中间余数的特殊情况
# - 余数为 0 的元素只能和同为余数 0 的配对










