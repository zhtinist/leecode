"""
LeetCode #2649 - Nested Array Generator
嵌套数组生成器
https://leetcode.cn/problems/nested-array-generator/

现给定一个整数的 多维数组 ，请你返回一个生成器对象，按照 中序遍历 的顺序逐个生成整数。
多维数组 是一个递归数据结构，包含整数和其他 多维数组。
中序遍历 是从左到右遍历每个数组，在遇到任何整数时生成它，遇到任何数组时递归应用 中序遍历 。

示例 1：
输入：arr = [[[6]],[1,3],[]] 输出：[6,1,3] 解释： const generator = inorderTraversal(arr); generator.next().value; // 6 generator.next().value; // 1 generator.next().value; // 3 generator.next().done; // true
示例 2：
输入：arr = [] 输出：[] 解释：输入的多维数组没有任何参数，所以生成器不需要生成任何值。

提示：
`0 <= arr.flat().length <= 10^5`
`0 <= arr.flat()[i] <= 10^5`
`maxNestingDepth <= 10^5`
"""

from typing import List, Optional


class Solution:

    def inorderTraversal(self, arr: List):
        """Generator that yields integers from nested array in-order."""
        for item in arr:
            if isinstance(item, list):
                yield from self.inorderTraversal(item)
            else:
                yield item



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: 
#
# 解题思路:
# 使用Python生成器(yield)实现嵌套数组的中序遍历。遍历数组的每个元素：
# 如果是整数则直接yield，如果是列表则递归调用生成器并用yield from展开。
# 这与JavaScript的生成器函数语义等价。
#
# 时间复杂度: O(N) 每个元素访问一次
# 空间复杂度: O(D) 递归深度
#
# 关键点:
# - Python的yield实现生成器，与JS的生成器语义一致
# - yield from用于委托给子生成器，等价于递归展开
# - isinstance(item, list)区分整数和嵌套列表
