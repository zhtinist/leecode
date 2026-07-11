"""
LeetCode #2623 - Memoize
记忆函数
https://leetcode.cn/problems/memoize/

请你编写一个函数 `fn`，它接收另一个函数作为输入，并返回该函数的 记忆化 后的结果。
记忆函数 是一个对于相同的输入永远不会被调用两次的函数。相反，它将返回一个缓存值。
你可以假设有 3 个可能的输入函数：`sum` 、`fib` 和 `factorial` 。
`sum` 接收两个整型参数 `a` 和 `b` ，并返回 `a + b` 。假设如果参数 `(b, a)` 已经缓存了值，其中 `a != b`，它不能用于参数 `(a, b)`。例如，如果参数是 `(3, 2)` 和 `(2, 3)`，则应进行两个单独的调用。
`fib` 接收一个整型参数 `n` ，如果 `n <= 1` 则返回 `1`，否则返回 `fib (n - 1) + fib (n - 2)`。
`factorial` 接收一个整型参数 `n` ，如果 `n <= 1` 则返回  `1` ，否则返回 `factorial(n - 1) * n` 。

示例 1：
输入： fnName = "sum" actions = ["call","call","getCallCount","call","getCallCount"] values = [[2,2],[2,2],[],[1,2],[]] 输出：[4,4,1,3,2] 解释： const sum = (a, b) => a + b; const memoizedSum = memoize(sum); memoizedSum (2, 2);// "call" - 返回 4。sum() 被调用，因为之前没有使用参数 (2, 2) 调用过。 memoizedSum (2, 2);// "call" - 返回 4。没有调用 sum()，因为前面有相同的输入。 // "getCallCount" - 总调用数： 1 memoizedSum(1, 2);// "call" - 返回 3。sum() 被调用，因为之前没有使用参数 (1, 2) 调用过。 // "getCallCount" - 总调用数： 2
示例 2：
输入： fnName = "factorial" actions = ["call","call","call","getCallCount","call","getCallCount"] values = [[2],[3],[2],[],[3],[]] 输出：[2,6,2,2,6,2] 解释： const factorial = (n) => (n <= 1) ? 1 : (n * factorial(n - 1)); const memoFactorial = memoize(factorial); memoFactorial(2); // "call" - 返回 2。 memoFactorial(3); // "call" - 返回 6。 memoFactorial(2); // "call" - 返回 2。 没有调用 factorial()，因为前面有相同的输入。 // "getCallCount" -  总调用数：2 memoFactorial(3); // "call" - 返回 6。 没有调用 factorial()，因为前面有相同的输入。 // "getCallCount" -  总调用数：2
示例 3：
输入： fnName = "fib" actions = ["call","getCallCount"] values = [[5],[]] 输出：[8,1] 解释： fib(5) = 8 // "call" // "getCallCount" - 总调用数：1

提示：
`0 <= a, b <= 10^5`
`1 <= n <= 10`
`1 <= actions.length <= 10^5`
`actions.length === values.length`
`actions[i]` 为 "call" 和 "getCallCount" 中的一个
`fnName` 为 "sum", "factorial" 和 "fib" 中的一个
"""

from typing import List, Optional


from functools import wraps


class Solution:

    def memoize(self, fn):
        cache = {}
        call_count = [0]

        @wraps(fn)
        def memoized(*args):
            if args in cache:
                return cache[args]
            call_count[0] += 1
            result = fn(*args)
            cache[args] = result
            return result

        memoized.getCallCount = lambda: call_count[0]
        return memoized



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: 
#
# 解题思路:
# 使用Python装饰器模式实现记忆化。内部维护一个字典cache，以参数元组为键缓存结果。
# 如果参数已缓存则直接返回，否则调用原函数并缓存结果。同时维护调用计数器。
# 使用functools.wraps保留原函数的元数据。
#
# 时间复杂度: 每次调用O(1)均摊（字典查找）
# 空间复杂度: O(k) 其中k是不同参数组合的数量
#
# 关键点:
# - 使用*args将参数转为元组作为字典键
# - 需要维护getCallCount来跟踪实际调用次数
# - 记忆化对递归函数（如fib, factorial）效果显著
