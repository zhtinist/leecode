"""
LeetCode #470 - Implement Rand10() Using Rand7()
中文题名：用 Rand7() 实现 Rand10()
https://leetcode.com/problems/implement-rand10-using-rand7/

Given a function `rand7` which generates a uniform random integer in the range 1
to 7, write a function `rand10` which generates a uniform random integer in
the range 1 to 10.

Do NOT use system's `Math.random()`.

Example 1:

Input: 1
Output: [7]

Example 2:

Input: 2
Output: [8,4]

Example 3:

Input: 3
Output: [8,1,10]

Note:

`rand7` is predefined.

Each testcase has one argument: `n`, the number of times
that `rand10`
is called.

Follow up:

What is the expected
value for the number of calls to `rand7()` function?

Could you minimize the number of calls to `rand7()`?

【中文翻译】
给定一个生成 1 到 7 范围内均匀随机整数的函数 `rand7`，编写一个函数 `rand10`
生成 1 到 10 范围内均匀随机整数。不要使用系统的 `Math.random()`。

注意：`rand7` 已预定义。每个测试用例有一个参数 `n`，表示调用 `rand10` 的次数。

进阶：
- `rand10()` 调用 `rand7()` 的期望次数是多少？
- 能否尽量减少 `rand7()` 的调用次数？

示例 1：
    输入：1
    输出：[7]

示例 2：
    输入：2
    输出：[8,4]

示例 3：
    输入：3
    输出：[8,1,10]
"""

from typing import List, Optional


# rand7() is predefined by LeetCode
# def rand7() -> int:
#     ...

class Solution:
    def rand10(self) -> int:
        """
        Rejection sampling: use two rand7() calls to generate a number
        in [1, 49] uniformly, reject values > 40, and map the rest to [1, 10].
        """
        while True:
            # (rand7()-1)*7 + rand7() generates 1..49 uniformly
            row = rand7() - 1      # 0..6
            col = rand7()          # 1..7
            val = row * 7 + col    # 1..49
            if val <= 40:
                return val % 10 + 1  # 1..10



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用拒绝采样 (Rejection Sampling)。核心公式：(rand7() - 1) * 7 + rand7() 可以
# 均匀生成 [1, 49] 范围的整数。若结果 ≤ 40，则取 val % 10 + 1 映射到 [1, 10]，
# 否则拒绝并重新采样。因为 49 个数中前 40 个被均匀映射到 1-10（每个数字恰好映射 4 次），
# 所以结果是均匀的。
#
# 期望调用次数：rand7() 每次采样调用 2 次，接受概率 40/49 ≈ 0.816，故期望调用
# 次数约为 2 * 49/40 = 2.45 次。
#
# 时间复杂度: O(1) 期望（最坏可能无限，但概率极低）
# 空间复杂度: O(1)
#
# 关键点:
# - (rand7() - 1) * 7 + rand7() 是经典的"用低维随机数生成高维随机数"技巧
# - 拒绝采样保证均匀性
# - 接受率 40/49 ≈ 81.6%，效率很高
# - 进阶优化：利用被拒绝的 [41, 49] 的 9 个值也可进一步回收利用减少调用次数
