"""
LeetCode #2023 - Number of Pairs of Strings With Concatenation Equal to Target
连接后等于目标字符串的字符串对
https://leetcode.cn/problems/number-of-pairs-of-strings-with-concatenation-equal-to-target/

给你一个 数字 字符串数组 `nums` 和一个 数字 字符串 `target` ，请你返回 `nums[i] + nums[j]` （两个字符串连接）结果等于 `target` 的下标 `(i, j)` （需满足 `i != j`）的数目。

示例 1：
输入：nums = ["777","7","77","77"], target = "7777" 输出：4 解释：符合要求的下标对包括： - (0, 1)："777" + "7" - (1, 0)："7" + "777" - (2, 3)："77" + "77" - (3, 2)："77" + "77"
示例 2：
输入：nums = ["123","4","12","34"], target = "1234" 输出：2 解释：符合要求的下标对包括 - (0, 1)："123" + "4" - (2, 3)："12" + "34"
示例 3：
输入：nums = ["1","1","1"], target = "11" 输出：6 解释：符合要求的下标对包括 - (0, 1)："1" + "1" - (1, 0)："1" + "1" - (0, 2)："1" + "1" - (2, 0)："1" + "1" - (1, 2)："1" + "1" - (2, 1)："1" + "1"

提示：
`2 <= nums.length <= 100`
`1 <= nums[i].length <= 100`
`2 <= target.length <= 100`
`nums[i]` 和 `target` 只包含数字。
`nums[i]` 和 `target` 不含有任何前导 0 。
"""

from typing import List, Optional


class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        from collections import Counter

        count = Counter(nums)
        result = 0
        for num in nums:
            # Check if num is a prefix of target
            if target.startswith(num):
                suffix = target[len(num):]
                if suffix in count:
                    result += count[suffix]
                    # If suffix == num, we counted pairing with itself, subtract 1
                    if suffix == num:
                        result -= 1
        return result



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Hash Table, String, Counting
#
# 解题思路:
# 使用哈希表统计每个字符串的出现次数。遍历每个字符串num，检查它是否是target的前缀。
# 如果是，则target的后缀部分如果在哈希表中存在，就可以和num配对。
# 注意当后缀等于num自身时，需要减去自己配对自己的那一次。
#
# 时间复杂度: O(n * L) 其中L是字符串长度
# 空间复杂度: O(n)
#
# 关键点:
# - 哈希表统计频率
# - 检查前缀-后缀配对
# - 注意避免自己配对自己（i!=j条件）
