"""
LeetCode #2721 - Execute Asynchronous Functions in Parallel
并行执行异步函数
https://leetcode.cn/problems/execute-asynchronous-functions-in-parallel/

给定一个异步函数数组 `functions`，返回一个新的 promise 对象 `promise`。数组中的每个函数都不接受参数并返回一个 promise。所有的 promise 都应该并行执行。
`promise` resolve 条件：
当所有从 `functions` 返回的 promise 都成功的并行解析时。`promise` 的解析值应该是一个按照它们在 `functions` 中的顺序排列的 promise 的解析值数组。`promise` 应该在数组中的所有异步函数并行执行完成时解析。
`promise` reject 条件：
当任何从 `functions` 返回的 promise 被拒绝时。`promise` 也会被拒绝，并返回第一个拒绝的原因。
请在不使用内置的 `Promise.all` 函数的情况下解决。

示例 1：
输入：functions = [   () => new Promise(resolve => setTimeout(() => resolve(5), 200)) ] 输出：{"t": 200, "resolved": [5]} 解释： promiseAll(functions).then(console.log); // [5]  单个函数在 200 毫秒后以值 5 成功解析。
示例 2：
输入：functions = [     () => new Promise(resolve => setTimeout(() => resolve(1), 200)),      () => new Promise((resolve, reject) => setTimeout(() => reject("Error"), 100)) ] 输出：{"t": 100, "rejected": "Error"} 解释：由于其中一个 promise 被拒绝，返回的 promise 也在同一时间被拒绝并返回相同的错误。
示例 3：
输入：functions = [     () => new Promise(resolve => setTimeout(() => resolve(4), 50)),      () => new Promise(resolve => setTimeout(() => resolve(10), 150)),      () => new Promise(resolve => setTimeout(() => resolve(16), 100)) ] 输出：{"t": 150, "resolved": [4, 10, 16]} 解释：所有的 promise 都成功执行。当最后一个 promise 被解析时，返回的 promise 也被解析了。

提示：
函数 `functions` 是一个返回 promise 的函数数组
`1 <= functions.length <= 10`
"""

from typing import List, Optional


class Solution:
    def promiseAll(self, functions: List) -> List:
        """
        Python equivalent: execute all functions in parallel and return results in order.
        Since LeetCode JS problems use a custom runner, here we implement the logic
        using asyncio for Python, or simulate with a simple parallel execution pattern.
        """
        import concurrent.futures
        results = [None] * len(functions)
        errors = [None]

        def worker(idx, fn):
            try:
                results[idx] = fn()
            except Exception as e:
                if errors[0] is None:
                    errors[0] = (idx, e)

        with concurrent.futures.ThreadPoolExecutor(max_workers=len(functions)) as executor:
            futures = [executor.submit(worker, i, fn) for i, fn in enumerate(functions)]
            concurrent.futures.wait(futures)

        if errors[0] is not None:
            raise errors[0][1]

        return results



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: 
#
# 解题思路:
# 原题为 JavaScript 的 Promise.all 手动实现。Python 中使用线程池并行执行所有函数。
# 维护结果数组保持原始顺序。一旦任何函数抛出异常，记录第一个错误并最终抛出。
# 所有函数并行提交到线程池，等待全部完成后返回结果数组。
#
# 时间复杂度: O(T) 其中 T 是所有函数中最长的执行时间（并行执行）
# 空间复杂度: O(n) 用于存储结果数组
#
# 关键点:
# - 并行执行：使用线程池同时启动所有函数
# - 保持顺序：每个 worker 将结果写入对应索引位置
# - 错误处理：只记录第一个错误，在全部完成后抛出
# - LeetCode JS 环境使用自定义测试框架，Python 实现为等效逻辑
