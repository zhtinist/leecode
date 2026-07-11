"""
LeetCode #553 - Optimal Division
中文题名：最优除法
https://leetcode.com/problems/optimal-division/

Given a list of positive integers, the adjacent integers will perform the float
division. For example, [2,3,4] -> 2 / 3 / 4.

However, you can add any number of parenthesis at any position to change the priority of
operations. You should find out how to add parenthesis to get the maximum result, and
return the corresponding expression in string format. Your expression should NOT contain
redundant parenthesis.

Example:

Input: [1000,100,10,2]
Output: "1000/(100/10/2)"
Explanation:
1000/(100/10/2) = 1000/((100/10)/2) = 200
However, the bold parenthesis in "1000/((100/10)/2)" are redundant,
since they don't influence the operation priority. So you should return "1000/(100/10/2)".

Other cases:
1000/(100/10)/2 = 50
1000/(100/(10/2)) = 50
1000/100/10/2 = 0.5
1000/100/(10/2) = 2

Note:

The length of the input array is [1, 10].

Elements in the given array will be in range [2, 1000].

There is only one optimal division for each test case.

【中文翻译】
给定一个正整数列表，相邻整数将执行浮点除法。例如，[2,3,4] -> 2 / 3 / 4。

你可以在任意位置添加任意数量的括号来改变运算优先级。你需要找出如何添加括号来获得最大结果，
并以字符串格式返回相应的表达式。你的表达式不应包含多余括号。

示例：
    输入：[1000,100,10,2]
    输出："1000/(100/10/2)"
    解释：
    1000/(100/10/2) = 1000/((100/10)/2) = 200
    然而，"1000/((100/10)/2)" 中的粗体括号是多余的，因为它们不影响运算优先级。
    所以你应该返回 "1000/(100/10/2)"。

    其他情况：
    1000/(100/10)/2 = 50
    1000/(100/(10/2)) = 50
    1000/100/10/2 = 0.5
    1000/100/(10/2) = 2

注意：
    输入数组的长度范围是 [1, 10]。
    数组中的元素范围是 [2, 1000]。
    每个测试用例只有一个最优除法。
"""

from typing import List, Optional


class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        n = len(nums)
        if n == 1:
            return str(nums[0])
        if n == 2:
            return f"{nums[0]}/{nums[1]}"
        # n >= 3: 最大化 a/(b/c/d/...) 即第一个数为分子，其余全部放入分母
        return f"{nums[0]}/({'/'.join(str(x) for x in nums[1:])})"



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 数学推导题。要使 a/b/c/d 结果最大，需要让分子尽量大、分母尽量小。
# 所有数都是 >=2 的正整数，连续除法会让分母越来越大。所以将第一个数作为分子，
# 其余全部除式作为分母（即将分母包裹在一个括号中变成连除），可以得到最大结果。
# 当 n=1 时直接返回该数，n=2 时返回 "a/b"，n>=3 时返回 "a/(b/c/d/...)"。
#
# 时间复杂度: O(N) — 遍历一次数组构建字符串
# 空间复杂度: O(N) — 输出字符串的大小
#
# 关键点:
# - 本质上是要把从第二个数开始的所有数放进分母的连除中
# - 对于 n>=3，a/(b/c/d) = a*c*d/b 是最大值
# - 括号只在 n>=3 时需要，且只需一对
