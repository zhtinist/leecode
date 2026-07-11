"""
LeetCode #2526 - Find Consecutive Integers from a Data Stream
找到数据流中的连续整数
https://leetcode.cn/problems/find-consecutive-integers-from-a-data-stream/

给你一个整数数据流，请你实现一个数据结构，检查数据流中最后 `k` 个整数是否 等于 给定值 `value` 。
请你实现 DataStream 类：
`DataStream(int value, int k)` 用两个整数 `value` 和 `k` 初始化一个空的整数数据流。
`boolean consec(int num)` 将 `num` 添加到整数数据流。如果后 `k` 个整数都等于 `value` ，返回 `true` ，否则返回 `false` 。如果少于 `k` 个整数，条件不满足，所以也返回 `false` 。

示例 1：
输入： ["DataStream", "consec", "consec", "consec", "consec"] [[4, 3], [4], [4], [4], [3]] 输出： [null, false, false, true, false]  解释： DataStream dataStream = new DataStream(4, 3); // value = 4, k = 3  dataStream.consec(4); // 数据流中只有 1 个整数，所以返回 False 。 dataStream.consec(4); // 数据流中只有 2 个整数                       // 由于 2 小于 k ，返回 False 。 dataStream.consec(4); // 数据流最后 3 个整数都等于 value， 所以返回 True 。 dataStream.consec(3); // 最后 k 个整数分别是 [4,4,3] 。                       // 由于 3 不等于 value ，返回 False 。

提示：
`1 <= value, num <= 10^9`
`1 <= k <= 10^5`
至多调用 `consec` 次数为 `10^5` 次。
"""

from typing import List, Optional


class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.cnt = 0

    def consec(self, num: int) -> bool:
        if num == self.value:
            self.cnt += 1
        else:
            self.cnt = 0
        return self.cnt >= self.k



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Design, Queue, Hash Table, Counting, Data Stream
#
# 解题思路:
# 维护一个计数器记录当前连续等于value的元素个数。每次添加新数字时，
# 若等于value则计数+1，否则重置为0。当计数器>=k时返回True。
#
# 时间复杂度: O(1) 每次调用
# 空间复杂度: O(1)
#
# 关键点:
# - 不需要存储所有元素，只需维护连续匹配计数
# - 一旦遇到不匹配的值，计数器立即归零
# - 少于k个元素时cnt<k自动返回False
