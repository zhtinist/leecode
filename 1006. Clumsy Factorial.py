"""
LeetCode #1006 - Clumsy Factorial
中文题名：笨阶乘
https://leetcode.com/problems/clumsy-factorial/

Normally, the factorial of a positive integer `n` is the product of all
positive integers less than or equal to `n`.  For example, `factorial(10)
= 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1`.

We instead make a clumsy factorial: using the integers in decreasing order, we swap
out the multiply operations for a fixed rotation of operations: multiply (*), divide
(/), add (+) and subtract (-) in this order.

For example, `clumsy(10) = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1`.  However,
these operations are still applied using the usual order of operations of arithmetic: we do
all multiplication and division steps before any addition or subtraction steps, and
multiplication and division steps are processed left to right.

Additionally, the division that we use is floor division such that `10
* 9 / 8` equals `11`.  This guarantees the result is an
integer.

`Implement the clumsy` function as
defined above: given an integer `N`, it returns the clumsy factorial of
`N`.

Example 1:

Input: 4
Output: 7
Explanation: 7 = 4 * 3 / 2 + 1

Example 2:

Input: 10
Output: 12
Explanation: 12 = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1

Note:

`1 <= N <= 10000`

`-2^31 <= answer <= 2^31 - 1`  (The answer is guaranteed to fit
within a 32-bit integer.)

【中文翻译】
通常，正整数 `n` 的阶乘是所有小于或等于 `n` 的正整数的乘积。例如，`factorial(10) = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1`。

相反，我们设计了一个笨阶乘：在递减的整数序列中，我们使用固定顺序的操作符来代替乘法操作符：乘（*）、除（/）、加（+）和减（-），按此顺序循环。

例如，`clumsy(10) = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1`。然而，这些运算仍然使用通常的算术运算顺序：我们在任何加法或减法步骤之前执行所有乘法和除法步骤，并且乘法和除法步骤从左到右处理。

此外，我们使用的除法是地板除法，因此 `10 * 9 / 8` 等于 `11`。这保证结果是一个整数。

实现如上定义的 `clumsy` 函数：给定一个整数 `N`，它返回 `N` 的笨阶乘。

示例 1：

输入：4
输出：7
解释：7 = 4 * 3 / 2 + 1

示例 2：

输入：10
输出：12
解释：12 = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1

注意：

`1 <= N <= 10000`

`-2^31 <= answer <= 2^31 - 1`（答案保证在 32 位整数范围内。）

"""

from typing import List, Optional


class Solution:
    def clumsy(self, N: int) -> int:
        if N == 1:
            return 1
        stack = [N]
        ops = ['*', '/', '+', '-']
        op_idx = 0
        for i in range(N - 1, 0, -1):
            op = ops[op_idx % 4]
            if op == '*':
                stack[-1] *= i
            elif op == '/':
                stack[-1] = int(stack[-1] / i)
            elif op == '+':
                stack.append(i)
            elif op == '-':
                stack.append(-i)
            op_idx += 1
        return sum(stack)










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用栈来模拟运算过程，遵循乘除优先于加减的规则。
# 操作符按 *, /, +, - 循环。将 N 作为初始值压入栈，然后从 N-1 递减到 1：
# - 遇到 *：栈顶元素乘以当前数字，结果存回栈顶。
# - 遇到 /：栈顶元素整除以当前数字（地板除法 int(a/b) 向零取整），结果存回栈顶。
# - 遇到 +：将当前数字压入栈（正数）。
# - 遇到 -：将当前数字的相反数压入栈（负数）。
# 最后将栈中所有元素求和，栈中符号已正确表示加减。
# 这种处理方式自动保证了乘除优先于加减。
#
# 时间复杂度: O(n) - 从 N 到 1 遍历一次
# 空间复杂度: O(n) - 栈最多存储约 n/4 个元素
#
# 关键点:
# - 栈顶操作保证乘除优先：遇到 * 或 / 时直接修改栈顶
# - 加减通过压入正/负数实现，最后 sum 统一处理
# - 除法使用 int(a/b) 进行向零取整（Python 中正数除法就是地板除法）
