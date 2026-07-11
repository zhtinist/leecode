"""
LeetCode #2693 - Call Function with Custom Context
使用自定义上下文调用函数
https://leetcode.cn/problems/call-function-with-custom-context/

增强所有函数，使其具有 `callPolyfill` 方法。该方法接受一个对象 `obj` 作为第一个参数，以及任意数量的附加参数。`obj` 成为函数的 `this` 上下文。附加参数将传递给该函数（即 `callPolyfill` 方法所属的函数）。
例如，如果有以下函数：
function tax(price, taxRate) {   const totalCost = price * (1 + taxRate);   console.log(`The cost of ${this.item} is ${totalCost}`); }
调用 `tax(10, 0.1)` 将输出 `"The cost of undefined is 11"` 。这是因为 `this` 上下文未定义。
然而，调用 `tax.callPolyfill({item: "salad"}, 10, 0.1)` 将输出 `"The cost of salad is 11"` 。`this` 上下文被正确设置，函数输出了适当的结果。
请在不使用内置的 `Function.call` 方法的情况下解决这个问题。

示例 1：
输入： fn = function add(b) {   return this.a + b; } args = [{"a": 5}, 7] 输出：12 解释： fn.callPolyfill({"a": 5}, 7); // 12 `callPolyfill `将 "this" 上下文设置为 `{"a": 5} `，并将 7 作为参数传递。
示例 2：
输入： fn = function tax(price, taxRate) {   return `The cost of the ${this.item} is ${price * taxRate}`;  } args = [{"item": "burger"}, 10, 1,1] 输出："The cost of the burger is 11" 解释：`callPolyfill `将 "this" 上下文设置为 `{"item": "burger"} `，并将 10 和 1.1 作为附加参数传递。

提示：
`typeof args[0] == 'object' and args[0] != null`
`1 <= args.length <= 100`
`2 <= JSON.stringify(args[0]).length <= 10^5`
"""

from typing import List, Optional


class Solution:

    def callPolyfill(self, fn, obj, *args):
        """Simulate JavaScript's Function.call by passing obj as 'this' context.
        In Python, the function expects the context object as its first argument,
        analogous to how 'self' works in methods."""
        return fn(obj, *args)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: 
#
# 解题思路:
# Python中等价实现JS的call：将上下文对象obj作为函数的第一个参数传递。
# 在JS中，this是隐式绑定；在Python中，上下文对象需要显式传递。
# 这模拟了JS函数调用时this的设置效果——obj成为函数内部的"this"上下文。
#
# 时间复杂度: O(1)
# 空间复杂度: O(1)
#
# 关键点:
# - JS的this在Python中等价于显式传递上下文参数
# - 将obj作为函数第一个参数传递即可实现相同效果
# - fn(obj, *args)等价于JS的fn.call(obj, ...args)
