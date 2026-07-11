"""
LeetCode #1010 - Pairs of Songs With Total Durations Divisible by 60
中文题名：总持续时间可被60整除的歌曲
https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/

In a list of songs, the `i`-th song has a duration
of `time[i]` seconds.

Return the number of pairs of songs for which their total duration in seconds is
divisible by `60`.  Formally, we want the number of indices `i
< j` with `(time[i] + time[j]) % 60 == 0`.

Example 1:

Input: [30,20,150,100,40]
Output: 3
Explanation: Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60

Example 2:

Input: [60,60,60]
Output: 3
Explanation: All three pairs have a total duration of 120, which is divisible by 60.

【中文翻译】
在歌曲列表中，第 `i` 首歌曲的持续时间为 `time[i]` 秒。

返回其总持续时间（以秒为单位）可被 `60` 整除的歌曲对的数量。形式上，我们想要满足 `(time[i] + time[j]) % 60 == 0` 的下标对 `i < j` 的数量。

示例 1：

输入：[30,20,150,100,40]
输出：3
解释：三对歌曲的总持续时间可被 60 整除：
(time[0] = 30, time[2] = 150)：总持续时间 180
(time[1] = 20, time[3] = 100)：总持续时间 120
(time[1] = 20, time[4] = 40)：总持续时间 60

示例 2：

输入：[60,60,60]
输出：3
解释：所有三对歌曲的总持续时间都是 120，可被 60 整除。

"""

from typing import List, Optional


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        remainders = [0] * 60
        count = 0
        for t in time:
            rem = t % 60
            complement = (60 - rem) % 60
            count += remainders[complement]
            remainders[rem] += 1
        return count










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用哈希表统计余数的出现次数。(a + b) % 60 == 0 等价于 a % 60 + b % 60 是 0 或 60。
# 即对于余数 rem，需要找余数为 (60 - rem) % 60 的歌曲配对。
# 遍历数组，对于每首歌的持续时间 t：
# 1. 计算 rem = t % 60，complement = (60 - rem) % 60
# 2. 将之前出现的 complement 余数的歌曲数量累加到计数中
# 3. 将当前 rem 的出现次数加 1
# 这样保证每对只被计数一次（i < j）。
#
# 时间复杂度: O(n) - 遍历一次数组
# 空间复杂度: O(1) - 余数数组固定大小 60
#
# 关键点:
# - 对 60 取模，将问题转化为两余数之和为 60（或 0）
# - complement = (60 - rem) % 60 处理 rem=0 的情况（补数为 0 而非 60）
# - 先累加计数再更新余数，确保每对只统计一次（i < j）
