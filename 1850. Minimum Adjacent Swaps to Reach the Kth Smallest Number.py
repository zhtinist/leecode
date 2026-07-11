"""
LeetCode #1850 - Minimum Adjacent Swaps to Reach the Kth Smallest Number
中文题名：达到第K个最小数的最少相邻交换次数
https://leetcode.com/problems/minimum-adjacent-swaps-to-reach-the-kth-smallest-number/

You are given a string `num`, representing a large integer, and an integer `k`.

We call some integer wonderful if it is a permutation of the digits in `num` and is greater in value than `num`. There can be many wonderful integers. However, we only care about the smallest-valued ones.

For example, when `num = "5489355142"`:

The 1st smallest wonderful integer is `"5489355214"`.

The 2nd smallest wonderful integer is `"5489355241"`.

The 3rd smallest wonderful integer is `"5489355412"`.

The 4th smallest wonderful integer is `"5489355421"`.

Return the minimum number of adjacent digit swaps that needs to be applied to `num` to reach the `kth` smallest wonderful integer.

The tests are generated in such a way that `kth` smallest wonderful integer exists.

Example 1:

Input: num = "5489355142", k = 4
Output: 2
Explanation: The 4th smallest wonderful number is "5489355421". To get this number:
- Swap index 7 with index 8: "5489355142" -> "5489355412"
- Swap index 8 with index 9: "5489355412" -> "5489355421"

Example 2:

Input: num = "11112", k = 4
Output: 4
Explanation: The 4th smallest wonderful number is "21111". To get this number:
- Swap index 3 with index 4: "11112" -> "11121"
- Swap index 2 with index 3: "11121" -> "11211"
- Swap index 1 with index 2: "11211" -> "12111"
- Swap index 0 with index 1: "12111" -> "21111"

Example 3:

Input: num = "00123", k = 1
Output: 1
Explanation: The 1st smallest wonderful number is "00132". To get this number:
- Swap index 3 with index 4: "00123" -> "00132"

Constraints:

`2 <= num.length <= 1000`

`1 <= k <= 1000`

`num` only consists of digits.

【中文翻译】

给定一个表示大整数的字符串 `num` 和一个整数 `k`。

如果一个整数是 `num` 中数字的排列且值大于 `num`，则称之为wonderful。在众多wonderful整数中，我们只关心最小的那些。

返回将 `num` 变为第k个最小的wonderful整数所需的最少相邻数字交换次数。测试数据保证第k个最小的wonderful整数存在。

示例：
输入：num = "5489355142", k = 4
输出：2
解释：第4小的wonderful数是"5489355421"。需要交换索引7和8，再交换8和9，共2次。

"""

from typing import List, Optional


class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        def next_permutation(s: list) -> None:
            i = len(s) - 2
            while i >= 0 and s[i] >= s[i + 1]:
                i -= 1

            if i >= 0:
                j = len(s) - 1
                while j > i and s[j] <= s[i]:
                    j -= 1
                s[i], s[j] = s[j], s[i]

            left, right = i + 1, len(s) - 1
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

        # 找到第k个下一个排列
        target = list(num)
        for _ in range(k):
            next_permutation(target)

        # 计算最少相邻交换次数
        original = list(num)
        swaps = 0
        for i in range(len(original)):
            if original[i] != target[i]:
                j = i
                while j < len(original) and original[j] != target[i]:
                    j += 1
                # 将匹配字符冒泡到位置i
                while j > i:
                    original[j], original[j - 1] = original[j - 1], original[j]
                    swaps += 1
                    j -= 1

        return swaps










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 分两步：1) 使用next_permutation算法k次，得到目标排列；
# 2) 使用贪心法计算从原始排列变为目标排列所需的最少相邻交换次数：
# 从左到右遍历，如果当前位置字符不匹配，在原始数组中找到匹配字符，
# 将其通过相邻交换（冒泡）移动到当前位置，累加交换次数。
#
# 时间复杂度: O(K * N + N^2)，K次排列每次O(N)，交换计数O(N^2)
# 空间复杂度: O(N)，存储目标排列和原始排列的字符数组
#
# 关键点:
# - next_permutation: 找右起第一个<s[i+1]的s[i]，交换，翻转后缀
# - 最少相邻交换：对每个位置找到目标字符并冒泡到该位置
# - 贪心移动不会增加后续的交换次数（局部最优等于全局最优）
