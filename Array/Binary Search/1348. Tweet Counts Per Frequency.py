"""
LeetCode #1348 - Tweet Counts Per Frequency
中文题名：推文计数
https://leetcode.com/problems/tweet-counts-per-frequency/

Implement the class `TweetCounts` that supports two methods:

1.` recordTweet(string tweetName, int time)`

Stores the `tweetName` at the recorded `time` (in seconds).

2.` getTweetCountsPerFrequency(string freq, string tweetName, int startTime, int
endTime)`

Returns the total number of occurrences for the given `tweetName` per
minute, hour, or day
(depending on `freq`) starting from the `startTime` (in
seconds) and ending at the `endTime` (in seconds).

`freq` is always
minute, hour or
day, representing the time interval to get the total
number of occurrences for the given `tweetName`.

The first time interval always starts from the `startTime`, so the
time intervals are `[startTime, startTime + delta*1>,  [startTime +
delta*1, startTime + delta*2>, [startTime + delta*2, startTime + delta*3>,
... , [startTime + delta*i, min(startTime + delta*(i+1),
endTime + 1)>` for some non-negative number `i` and
`delta` (which depends on `freq`).

Example:

Input
["TweetCounts","recordTweet","recordTweet","recordTweet","getTweetCountsPerFrequency","getTweetCountsPerFrequency","recordTweet","getTweetCountsPerFrequency"]
[[],["tweet3",0],["tweet3",60],["tweet3",10],["minute","tweet3",0,59],["minute","tweet3",0,60],["tweet3",120],["hour","tweet3",0,210]]

Output
[null,null,null,null,[2],[2,1],null,[4]]

Explanation
TweetCounts tweetCounts = new TweetCounts();
tweetCounts.recordTweet("tweet3", 0);
tweetCounts.recordTweet("tweet3", 60);
tweetCounts.recordTweet("tweet3", 10);                             // All tweets correspond to "tweet3" with recorded times at 0, 10 and 60.
tweetCounts.getTweetCountsPerFrequency("minute", "tweet3", 0, 59); // return [2]. The frequency is per minute (60 seconds), so there is one interval of time: 1) [0, 60> - > 2 tweets.
tweetCounts.getTweetCountsPerFrequency("minute", "tweet3", 0, 60); // return [2, 1]. The frequency is per minute (60 seconds), so there are two intervals of time: 1) [0, 60> - > 2 tweets, and 2) [60,61> - > 1 tweet.
tweetCounts.recordTweet("tweet3", 120);                            // All tweets correspond to "tweet3" with recorded times at 0, 10, 60 and 120.
tweetCounts.getTweetCountsPerFrequency("hour", "tweet3", 0, 210);  // return [4]. The frequency is per hour (3600 seconds), so there is one interval of time: 1) [0, 211> - > 4 tweets.

Constraints:

There will be at most `10000` operations considering both `recordTweet`
and `getTweetCountsPerFrequency`.

`0 <= time, startTime, endTime <= 10^9`

`0 <= endTime - startTime <= 10^4`

【中文翻译】
实现 `TweetCounts` 类，支持两种方法：

1. `recordTweet(string tweetName, int time)`：在给定的 `time`（以秒为单位）记录推文名称 `tweetName`。

2. `getTweetCountsPerFrequency(string freq, string tweetName, int startTime, int endTime)`：返回从 `startTime` 开始到 `endTime` 结束的每个分钟、小时或日（取决于 `freq`）中给定 `tweetName` 的出现次数。`freq` 始终为 `"minute"`、`"hour"` 或 `"day"`，表示获取给定 `tweetName` 出现次数的时间间隔。

第一个时间间隔始终从 `startTime` 开始，时间间隔为 `[startTime, startTime + delta*1>, [startTime + delta*1, startTime + delta*2>, ...`，对于某个非负整数 `i` 和 `delta`（取决于 `freq`）。

示例：
输入
["TweetCounts","recordTweet","recordTweet","recordTweet","getTweetCountsPerFrequency","getTweetCountsPerFrequency","recordTweet","getTweetCountsPerFrequency"]
[[],["tweet3",0],["tweet3",60],["tweet3",10],["minute","tweet3",0,59],["minute","tweet3",0,60],["tweet3",120],["hour","tweet3",0,210]]

输出
[null,null,null,null,[2],[2,1],null,[4]]

解释
TweetCounts tweetCounts = new TweetCounts();
tweetCounts.recordTweet("tweet3", 0);
tweetCounts.recordTweet("tweet3", 60);
tweetCounts.recordTweet("tweet3", 10);                             // 所有推文对应 "tweet3"，记录时间为 0, 10 和 60。
tweetCounts.getTweetCountsPerFrequency("minute", "tweet3", 0, 59); // 返回 [2]。频率为每分钟（60 秒），所以有一个时间间隔：1) [0, 60> -> 2 条推文。
tweetCounts.getTweetCountsPerFrequency("minute", "tweet3", 0, 60); // 返回 [2, 1]。频率为每分钟（60 秒），所以有两个时间间隔：1) [0, 60> -> 2 条推文，和 2) [60,61> -> 1 条推文。
tweetCounts.recordTweet("tweet3", 120);                            // 所有推文对应 "tweet3"，记录时间为 0, 10, 60 和 120。
tweetCounts.getTweetCountsPerFrequency("hour", "tweet3", 0, 210);  // 返回 [4]。频率为每小时（3600 秒），所以有一个时间间隔：1) [0, 211> -> 4 条推文。
"""

from typing import List
from collections import defaultdict
import bisect


class TweetCounts:

    def __init__(self):
        self.tweets = defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        bisect.insort(self.tweets[tweetName], time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        delta = {"minute": 60, "hour": 3600, "day": 86400}[freq]
        times = self.tweets.get(tweetName, [])
        result = []
        t = startTime
        while t <= endTime:
            interval_end = min(t + delta, endTime + 1)
            left = bisect.bisect_left(times, t)
            right = bisect.bisect_left(times, interval_end)
            result.append(right - left)
            t += delta
        return result



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用字典存储每个推文名称对应的时间戳列表，通过二分查找保持有序。
# recordTweet: 使用 bisect.insort 将时间戳按顺序插入列表，O(log N) 查找插入位置 + O(N) 移动元素。
# getTweetCountsPerFrequency: 根据频率确定时间间隔 delta（minute=60, hour=3600, day=86400），
# 然后从 startTime 开始，每次增加 delta，使用二分查找统计当前时间间隔内的推文数量。
#
# 时间复杂度: recordTweet O(N)（列表插入移动），getTweetCountsPerFrequency O(Q * log N)，其中 Q 为时间间隔数量
# 空间复杂度: O(N)，N 为所有推文记录总数
#
# 关键点:
# - 使用 bisect.insort 保持时间戳有序
# - 二分查找左右边界快速统计区间内推文数
# - delta 根据频率选择：minute=60, hour=3600, day=86400













