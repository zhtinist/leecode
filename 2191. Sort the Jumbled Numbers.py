"""
LeetCode #2191 - Sort the Jumbled Numbers
将杂乱无章的数字排序
https://leetcode.cn/problems/sort-the-jumbled-numbers/

给你一个下标从 0 开始的整数数组 `mapping` ，它表示一个十进制数的映射规则，`mapping[i] = j` 表示这个规则下将数位 `i` 映射为数位 `j` 。
一个整数 映射后的值 为将原数字每一个数位 `i` （`0 <= i <= 9`）映射为 `mapping[i]` 。
另外给你一个整数数组 `nums` ，请你将数组 `nums` 中每个数按照它们映射后对应数字非递减顺序排序后返回。
注意：
如果两个数字映射后对应的数字大小相同，则将它们按照输入中的 相对顺序 排序。
`nums` 中的元素只有在排序的时候需要按照映射后的值进行比较，返回的值应该是输入的元素本身。

示例 1：
输入：mapping = [8,9,4,0,2,1,3,5,7,6], nums = [991,338,38] 输出：[338,38,991] 解释： 将数字 991 按照如下规则映射： 1. mapping[9] = 6 ，所有数位 9 都会变成 6 。 2. mapping[1] = 9 ，所有数位 1 都会变成 9 。 所以，991 映射的值为 669 。 338 映射为 007 ，去掉前导 0 后得到 7 。 38 映射为 07 ，去掉前导 0 后得到 7 。 由于 338 和 38 映射后的值相同，所以它们的前后顺序保留原数组中的相对位置关系，338 在 38 的前面。 所以，排序后的数组为 [338,38,991] 。
示例 2：
输入：mapping = [0,1,2,3,4,5,6,7,8,9], nums = [789,456,123] 输出：[123,456,789] 解释：789 映射为 789 ，456 映射为 456 ，123 映射为 123 。所以排序后数组为 [123,456,789] 。

提示：
`mapping.length == 10`
`0 <= mapping[i] <= 9`
`mapping[i]` 的值 互不相同 。
`1 <= nums.length <= 3 * 10^4`
`0 <= nums[i] < 10^9`
"""

from typing import List, Optional


class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        """
        自定义排序：将 nums 中的每个数字按 mapping 映射规则转换，
        得到映射值，然后按映射值进行稳定排序。
        Python 的 sorted 默认是稳定排序，相同映射值的元素保持原相对顺序。
        """
        def get_mapped(num: int) -> int:
            """返回 num 按 mapping 映射后的整数值"""
            if num == 0:
                return mapping[0]
            res = 0
            for ch in str(num):
                res = res * 10 + mapping[int(ch)]
            return res

        # 按映射值排序（稳定排序，保持相同值的相对顺序）
        return sorted(nums, key=get_mapped)


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Sorting
#
# 解题思路:
# 1. 定义一个辅助函数 get_mapped(num)，将 num 的每一位数字按 mapping 映射，
#    生成新的整数值（注意：num = 0 需特殊处理，映射后为 mapping[0]）。
# 2. 使用 Python 内置的 sorted() 函数，以 get_mapped 作为排序的 key。
# 3. Python 的 sorted 是稳定排序（Timsort），因此映射值相同的元素会保持
#    在原数组中的相对顺序，满足题目要求。
# 4. 返回排序后的结果列表。
#
# 时间复杂度: O(N * D * log N)
# - N = len(nums)，D 为每个数字的平均位数（最多 10 位）。
# - 排序 O(N log N) 次比较，每次比较调用 get_mapped 需要 O(D)。
#
# 空间复杂度: O(N)
# - 排序过程中需要 O(N) 额外空间（Timsort）。
#
# 关键点:
# - num = 0 需要单独处理，映射后直接返回 mapping[0]。
# - 使用 Python 稳定排序保证相同映射值时保持原顺序。
# - 通过字符串转换简化逐位映射的实现。
