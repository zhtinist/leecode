"""
LeetCode #842 - Split Array into Fibonacci Sequence
中文题名：将数组拆分成斐波那契数列
https://leetcode.com/problems/split-array-into-fibonacci-sequence/

Given a string `S` of digits, such as `S = "123456579"`,
we can split it into a Fibonacci-like sequence `[123, 456, 579].`

Formally, a Fibonacci-like sequence is a list `F` of non-negative integers
such that:

`0 <= F[i] <= 2^31 - 1`, (that is, each integer fits a 32-bit
signed integer type);

`F.length >= 3`;

and` F[i] + F[i+1] = F[i+2] `for all `0 <= i < F.length - 2`.

Also, note that when splitting the string into pieces, each piece must not have extra leading
zeroes, except if the piece is the number 0 itself.

Return any Fibonacci-like sequence split from `S`, or return `[]` if it
cannot be done.

Example 1:

Input: "123456579"
Output: [123,456,579]

Example 2:

Input: "11235813"
Output: [1,1,2,3,5,8,13]

Example 3:

Input: "112358130"
Output: []
Explanation: The task is impossible.

Example 4:

Input: "0123"
Output: []
Explanation: Leading zeroes are not allowed, so "01", "2", "3" is not valid.

Example 5:

Input: "1101111"
Output: [110, 1, 111]
Explanation: The output [11, 0, 11, 11] would also be accepted.

Note:

`1 <= S.length <= 200`

`S` contains only digits.

【中文翻译】
给定一个数字字符串 `S`，比如 `S = "123456579"`，我们可以将其拆分成斐波那契式的数列 `[123, 456, 579]`。

形式上，斐波那契式数列是一个非负整数列表 `F`，且满足：

`0 <= F[i] <= 2^31 - 1`（即每个整数都符合 32 位有符号整数类型）；

`F.length >= 3`；

对于所有的 `0 <= i < F.length - 2`，都有 `F[i] + F[i+1] = F[i+2]`。

另外，拆分字符串时，每个数字块不能包含前导零，除非这个数字块是数字 0 本身。

返回从 `S` 拆分出来的任意一组斐波那契式的数列，如果不能拆分则返回 `[]`。

示例 1：

输入："123456579"
输出：[123,456,579]

示例 2：

输入："11235813"
输出：[1,1,2,3,5,8,13]

示例 3：

输入："112358130"
输出：[]
解释：无法完成该任务。

示例 4：

输入："0123"
输出：[]
解释：不允许有前导零，因此 "01", "2", "3" 是无效的。

示例 5：

输入："1101111"
输出：[110, 1, 111]
解释：输出 [11, 0, 11, 11] 也会被接受。

注意：

`1 <= S.length <= 200`

`S` 只包含数字。

"""

from typing import List, Optional


class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        n = len(num)
        MAX_INT = 2**31 - 1

        def backtrack(start: int, seq: List[int]) -> List[int]:
            if start == n and len(seq) >= 3:
                return seq

            for end in range(start + 1, n + 1):
                # Leading zero check
                if num[start] == '0' and end > start + 1:
                    break

                val = int(num[start:end])
                if val > MAX_INT:
                    break

                if len(seq) < 2:
                    seq.append(val)
                    result = backtrack(end, seq)
                    if result:
                        return result
                    seq.pop()
                else:
                    expected = seq[-1] + seq[-2]
                    if val < expected:
                        continue
                    elif val > expected:
                        break  # values only increase
                    else:
                        seq.append(val)
                        result = backtrack(end, seq)
                        if result:
                            return result
                        seq.pop()
                        break  # exact match either works or doesn't

            return []

        return backtrack(0, [])



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 回溯法。由于只需要返回任意一组有效解，在找到第一组时就返回。
# 1. 先确定前两个数字（它们没有和的约束，只需满足32位整数范围和无前导零）。
# 2. 从第三个数字开始，每个数字必须等于前两个数字之和（Fibonacci 性质）。
# 3. 剪枝策略：
#    - 超过 2^31-1 的值直接跳过
#    - 前导零只能用于单独的数字 0
#    - 当前值 < 期望和：尝试更长的子串（continue）
#    - 当前值 = 期望和：进入下一层递归，之后 break（更长的一定更大）
#    - 当前值 > 期望和：break（数字只会越来越大）
# 4. 当处理完整个字符串且数列长度 >= 3，返回结果。
#
# 时间复杂度: O(N^2) — 回溯树大小有限，实际远小于最坏情况
# 空间复杂度: O(N) — 递归深度和存储数列
#
# 关键点:
# - 前两个数字的选择决定了整个数列（贪心验证即可）
# - 前导零规则：只有单独的 "0" 是合法的
# - Fibonacci 数列在 32 位范围内最多约 44 项，足够覆盖
# - 利用 val > expected 时 break 进行剪枝，因为数值单调递增
