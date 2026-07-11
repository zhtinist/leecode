"""
LeetCode #1237 - Find Positive Integer Solution for a Given Equation
中文题名：找出给定方程的正整数解
https://leetcode.com/problems/find-positive-integer-solution-for-a-given-equation/

Given a function  `f(x, y)` and a value `z`, return all
positive integer pairs `x` and `y` where `f(x,y) == z`.

The function is constantly increasing, i.e.:

`f(x, y) < f(x + 1, y)`

`f(x, y) < f(x, y + 1)`

The function interface is defined like this:

interface CustomFunction {
public:
// Returns positive integer f(x, y) for any given positive integer x and y.
int f(int x, int y);
};

For custom testing purposes you're given an integer `function_id` and a target
`z` as input, where `function_id` represent one function from an
secret internal list, on the examples you'll know only two functions from the list.

You may return the solutions in any order.

Example 1:

Input: function_id = 1, z = 5
Output: [[1,4],[2,3],[3,2],[4,1]]
Explanation: function_id = 1 means that f(x, y) = x + y

Example 2:

Input: function_id = 2, z = 5
Output: [[1,5],[5,1]]
Explanation: function_id = 2 means that f(x, y) = x * y

Constraints:

`1 <= function_id <= 9`

`1 <= z <= 100`

It's guaranteed that the solutions of `f(x, y) == z` will be on the range
`1 <= x, y <= 1000`

It's also guaranteed that `f(x, y)` will fit in 32 bit signed integer if
`1 <= x, y <= 1000`

【中文翻译】
给你一个函数 `f(x, y)` 和一个目标值 `z`，请你返回所有满足 `f(x, y) == z` 的正整数对 `x` 和 `y`。

函数是严格单调递增的，即：

`f(x, y) < f(x + 1, y)`

`f(x, y) < f(x, y + 1)`

函数接口定义如下：

interface CustomFunction {
public:
// 对于任意给定的正整数 x 和 y，返回正整数 f(x, y)。
int f(int x, int y);
};

为了自定义测试，你会得到一个整数 `function_id` 和一个目标值 `z` 作为输入，其中 `function_id` 代表一个内部秘密列表中的某个函数。从示例中你只会知道列表中的两个函数。

你可以按任意顺序返回解。

示例 1：

输入：function_id = 1, z = 5
输出：[[1,4],[2,3],[3,2],[4,1]]
解释：function_id = 1 表示 f(x, y) = x + y

示例 2：

输入：function_id = 2, z = 5
输出：[[1,5],[5,1]]
解释：function_id = 2 表示 f(x, y) = x * y

约束条件：

`1 <= function_id <= 9`

`1 <= z <= 100`

保证 `f(x, y) == z` 的解在范围 `1 <= x, y <= 1000` 内。

同时保证当 `1 <= x, y <= 1000` 时，`f(x, y)` 的值在 32 位有符号整数范围内。
"""

from typing import List, Optional


class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        res = []
        x, y = 1, 1000

        while x <= 1000 and y >= 1:
            val = customfunction.f(x, y)
            if val == z:
                res.append([x, y])
                x += 1
                y -= 1
            elif val < z:
                x += 1
            else:
                y -= 1

        return res










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 双指针法（类似于在有序矩阵中搜索）。
# 由于 f(x, y) 关于 x 和 y 都是严格单调递增的，可以：
# 1. 初始化 x = 1, y = 1000（右上角）。
# 2. 计算 val = f(x, y)：
#    - 如果 val == z，记录 [x, y]，然后 x++, y--（两方向都前进以找到所有解）。
#    - 如果 val < z，说明需要增大值，x++（向下走）。
#    - 如果 val > z，说明需要减小值，y--（向左走）。
# 3. 循环直到 x > 1000 或 y < 1。
#
# 时间复杂度: O(x + y) = O(2000) = O(1)，因为 x 和 y 的搜索范围固定为 [1, 1000]
# 空间复杂度: O(1)，不计结果数组
#
# 关键点:
# - 利用函数在两个维度上都单调递增的性质，使用双指针从右上角搜索
# - 类似于"在行列递增的矩阵中查找目标值"的经典问题
# - 当 val == z 时两个指针可以同时移动，因为继续在同行或同列不可能再找到解
# - x 和 y 的范围固定为 [1, 1000]，搜索空间有限
