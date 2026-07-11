"""
LeetCode #2671 - Frequency Tracker
频率跟踪器
https://leetcode.cn/problems/frequency-tracker/

请你设计并实现一个能够对其中的值进行跟踪的数据结构，并支持对频率相关查询进行应答。
实现 `FrequencyTracker` 类：
`FrequencyTracker()`：使用一个空数组初始化 `FrequencyTracker` 对象。
`void add(int number)`：添加一个 `number` 到数据结构中。
`void deleteOne(int number)`：从数据结构中删除一个 `number` 。数据结构 可能不包含 `number` ，在这种情况下不删除任何内容。
`bool hasFrequency(int frequency)`: 如果数据结构中存在出现 `frequency` 次的数字，则返回 `true`，否则返回 `false`。

示例 1：
输入 ["FrequencyTracker", "add", "add", "hasFrequency"] [[], [3], [3], [2]] 输出 [null, null, null, true]  解释 FrequencyTracker frequencyTracker = new FrequencyTracker(); frequencyTracker.add(3); // 数据结构现在包含 [3] frequencyTracker.add(3); // 数据结构现在包含 [3, 3] frequencyTracker.hasFrequency(2); // 返回 true ，因为 3 出现 2 次
示例 2：
输入 ["FrequencyTracker", "add", "deleteOne", "hasFrequency"] [[], [1], [1], [1]] 输出 [null, null, null, false]  解释 FrequencyTracker frequencyTracker = new FrequencyTracker(); frequencyTracker.add(1); // 数据结构现在包含 [1] frequencyTracker.deleteOne(1); // 数据结构现在为空 [] frequencyTracker.hasFrequency(1); // 返回 false ，因为数据结构为空
示例 3：
输入 ["FrequencyTracker", "hasFrequency", "add", "hasFrequency"] [[], [2], [3], [1]] 输出 [null, false, null, true]  解释 FrequencyTracker frequencyTracker = new FrequencyTracker(); frequencyTracker.hasFrequency(2); // 返回 false ，因为数据结构为空 frequencyTracker.add(3); // 数据结构现在包含 [3] frequencyTracker.hasFrequency(1); // 返回 true ，因为 3 出现 1 次

提示：
`1 <= number <= 10^5`
`1 <= frequency <= 10^5`
最多调用 `add`、`deleteOne` 和 `hasFrequency` 共计 `2 * 10^5` 次
"""

from typing import List, Optional


class FrequencyTracker:

    def __init__(self):
        self.num_freq = {}  # number -> frequency
        self.freq_count = {}  # frequency -> count of numbers with that frequency

    def add(self, number: int) -> None:
        old_freq = self.num_freq.get(number, 0)
        new_freq = old_freq + 1
        self.num_freq[number] = new_freq

        if old_freq > 0:
            self.freq_count[old_freq] = self.freq_count.get(old_freq, 0) - 1
            if self.freq_count[old_freq] == 0:
                del self.freq_count[old_freq]

        self.freq_count[new_freq] = self.freq_count.get(new_freq, 0) + 1

    def deleteOne(self, number: int) -> None:
        if number not in self.num_freq:
            return
        old_freq = self.num_freq[number]
        new_freq = old_freq - 1

        self.freq_count[old_freq] = self.freq_count.get(old_freq, 0) - 1
        if self.freq_count[old_freq] == 0:
            del self.freq_count[old_freq]

        if new_freq == 0:
            del self.num_freq[number]
        else:
            self.num_freq[number] = new_freq
            self.freq_count[new_freq] = self.freq_count.get(new_freq, 0) + 1

    def hasFrequency(self, frequency: int) -> bool:
        return frequency in self.freq_count and self.freq_count[frequency] > 0


# Test harness calls FrequencyTracker directly — no Solution wrapper needed



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Design, Hash Table
#
# 解题思路:
# 使用两个哈希表：num_freq记录每个数字的出现次数，freq_count记录每个频率有多少个数字。
# add时更新数字频率并同步更新频率计数。deleteOne时减少频率。hasFrequency只需O(1)查freq_count。
# 通过双向维护确保所有操作O(1)。
#
# 时间复杂度: O(1) 每次操作
# 空间复杂度: O(n) 其中n是不同数字的数量
#
# 关键点:
# - 双哈希表设计：数字->频率，频率->数字个数
# - 每次更新频率时同时更新两个表
# - 删除频率为0的条目保持表清洁
