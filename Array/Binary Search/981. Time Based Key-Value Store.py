"""
LeetCode #981 - Time Based Key-Value Store
中文题名：基于时间的键值存储
https://leetcode.com/problems/time-based-key-value-store/

创建一个基于时间的键值存储类 TimeMap，它支持以下两个操作：

1. set(string key, string value, int timestamp)
   存储键 key 和值 value，以及给定的时间戳 timestamp。

2. get(string key, int timestamp)
   返回一个值，该值之前由 set(key, value, timestamp_prev) 调用设置，且满足 timestamp_prev <= timestamp。
   如果有多个这样的值，则返回 timestamp_prev 最大的那个。
   如果没有值，则返回空字符串（""）。

示例 1：

输入：inputs = ["TimeMap","set","get","get","set","get","get"], inputs = [[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]
输出：[null,null,"bar","bar",null,"bar2","bar2"]
解释：
TimeMap kv;
kv.set("foo", "bar", 1); // 存储键 "foo" 和值 "bar"，时间戳 = 1
kv.get("foo", 1);  // 输出 "bar"
kv.get("foo", 3); // 输出 "bar"，因为在时间戳 3 和 2 处没有对应 foo 的值，唯一的值在时间戳 1，即 "bar"
kv.set("foo", "bar2", 4);
kv.get("foo", 4); // 输出 "bar2"
kv.get("foo", 5); // 输出 "bar2"

示例 2：

输入：inputs = ["TimeMap","set","set","get","get","get","get","get"], inputs = [[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]
输出：[null,null,null,"","high","high","low","low"]

【中文翻译】
设计一个基于时间戳的键值存储，支持 set（存储带时间戳的值）和 get（获取小于等于给定时间戳的最新值）两个操作。由于 set 的时间戳是严格递增的，可以利用二分查找加速 get 操作。

"""

from typing import List, Optional
from collections import defaultdict
import bisect


class TimeMap:

    def __init__(self):
        # key -> list of (timestamp, value)
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        values = self.store[key]
        # Binary search for the largest timestamp <= given timestamp
        idx = bisect.bisect_right(values, (timestamp, chr(127)))
        if idx == 0:
            return ""
        return values[idx - 1][1]



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 哈希表 + 二分查找：
# 1. 使用 defaultdict(list) 存储每个 key 对应的 (timestamp, value) 列表。
# 2. set 操作：题目保证同一 key 的 timestamp 严格递增，因此直接追加到列表末尾即可。
# 3. get 操作：对于给定的 key 和 timestamp，需要找到 timestamp_prev <= timestamp 的最大 timestamp_prev。
#    - 使用 bisect.bisect_right 二分查找第一个大于 timestamp 的位置。
#    - 如果 idx == 0，说明所有时间戳都大于给定值，返回 ""。
#    - 否则返回 idx - 1 位置的值。
# 4. 使用 chr(127) 作为值的上限，确保二分查找只比较时间戳部分。
#
# 时间复杂度:
#   - set: O(1)，追加到列表末尾
#   - get: O(log M)，M 为该 key 对应的 (timestamp, value) 数量，二分查找
# 空间复杂度: O(N)，N 为总的 set 调用次数，存储所有键值对
#
# 关键点:
# - 题目特性：每个 key 的 timestamp 是严格递增的（set 调用顺序），无需排序
# - get 操作使用二分查找（bisect_right）定位最大满足条件的时间戳
# - 元组比较 (timestamp, chr(127)) 确保不匹配到相同的 timestamp 但更大的 value
# - 边界处理：idx == 0 时没有满足条件的值
