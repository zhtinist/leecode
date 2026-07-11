"""
LeetCode #2622 - Cache With Time Limit
有时间限制的缓存
https://leetcode.cn/problems/cache-with-time-limit/

编写一个类，它允许获取和设置键-值对，并且每个键都有一个 过期时间 。
该类有三个公共方法：
`set(key, value, duration)` ：接收参数为整型键 `key` 、整型值 `value` 和以毫秒为单位的持续时间 `duration` 。一旦 `duration` 到期后，这个键就无法访问。如果相同的未过期键已经存在，该方法将返回 `true` ，否则返回 `false` 。如果该键已经存在，则它的值和持续时间都应该被覆盖。
`get(key)` ：如果存在一个未过期的键，它应该返回这个键相关的值。否则返回 `-1` 。
`count()` ：返回未过期键的总数。

示例 1：
输入：  actions = ["TimeLimitedCache", "set", "get", "count", "get"] values = [[], [1, 42, 100], [1], [], [1]] timeDelays = [0, 0, 50, 50, 150] 输出： [null, false, 42, 1, -1] 解释： 在 t=0 时，缓存被构造。 在 t=0 时，添加一个键值对 (1: 42) ，过期时间为 100ms 。因为该值不存在，因此返回false。 在 t=50 时，请求 key=1 并返回值 42。 在 t=50 时，调用 count() ，缓存中有一个未过期的键。 在 t=100 时，key=1 到期。 在 t=150 时，调用 get(1) ，返回 -1，因为缓存是空的。
示例 2：
输入： actions = ["TimeLimitedCache", "set", "set", "get", "get", "get", "count"] values = [[], [1, 42, 50], [1, 50, 100], [1], [1], [1], []] timeDelays = [0, 0, 40, 50, 120, 200, 250] 输出： [null, false, true, 50, 50, -1] 解释： 在 t=0 时，缓存被构造。 在 t=0 时，添加一个键值对 (1: 42) ，过期时间为 50ms。因为该值不存在，因此返回false。 当 t=40 时，添加一个键值对 (1: 50) ，过期时间为 100ms。因为一个未过期的键已经存在，返回 true 并覆盖这个键的旧值。 在 t=50 时，调用 get(1) ，返回 50。 在 t=120 时，调用 get(1) ，返回 50。 在 t=140 时，key=1 过期。 在 t=200 时，调用 get(1) ，但缓存为空，因此返回 -1。 在 t=250 时，count() 返回0 ，因为缓存是空的，没有未过期的键。

提示：
`0 <= key, value <= 10^9`
`0 <= duration <= 1000`
`1 <= actions.length <= 100`
`actions.length === values.length`
`actions.length === timeDelays.length`
`0 <= timeDelays[i] <= 1450`
`actions[i]` 是 "TimeLimitedCache"、"set"、"get" 和 "count" 中的一个。
第一个操作始终是 "TimeLimitedCache" 而且一定会以 0 毫秒的延迟立即执行
"""

from typing import List, Optional


import time


class TimeLimitedCache:

    def __init__(self):
        self.cache = {}  # key -> (value, expiry_time_ms)

    def set(self, key: int, value: int, duration: int) -> bool:
        now = time.time() * 1000
        existed = key in self.cache and self.cache[key][1] > now
        self.cache[key] = (value, now + duration)
        return existed

    def get(self, key: int) -> int:
        now = time.time() * 1000
        if key in self.cache and self.cache[key][1] > now:
            return self.cache[key][0]
        return -1

    def count(self) -> int:
        now = time.time() * 1000
        expired = [k for k, (v, exp) in self.cache.items() if exp <= now]
        for k in expired:
            del self.cache[k]
        return len(self.cache)


# Test harness calls TimeLimitedCache directly — no Solution wrapper needed



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: 
#
# 解题思路:
# 维护字典存储key到(value, expiry_timestamp_ms)的映射。set时检查key是否存在且未过期作为返回值，
# 然后覆盖值。get时检查时间戳是否过期，count时先清理过期键再返回数量。
# 使用time.time()*1000获取毫秒级当前时间来判断过期。
#
# 时间复杂度: set/get O(1), count O(n)
# 空间复杂度: O(n)
#
# 关键点:
# - 过期判断基于时间戳比较，每次操作获取当前时间
# - set总是覆盖已存在的键并返回之前是否存在未过期的值
# - count需要清理过期键以保持数据准确
