"""
LeetCode #355 - Design Twitter
中文题名：设计推特
https://leetcode.com/problems/design-twitter/

Design a simplified version of Twitter where users can post tweets, follow/unfollow another
user and is able to see the 10 most recent tweets in the user's news feed. Your design
should support the following methods:

postTweet(userId, tweetId): Compose a new tweet.

getNewsFeed(userId): Retrieve the 10 most recent tweet ids in the user's news
feed. Each item in the news feed must be posted by users who the user followed or by the
user herself. Tweets must be ordered from most recent to least recent.

follow(followerId, followeeId): Follower follows a followee.

unfollow(followerId, followeeId): Follower unfollows a followee.

Example:

Twitter twitter = new Twitter();

// User 1 posts a new tweet (id = 5).
twitter.postTweet(1, 5);

// User 1's news feed should return a list with 1 tweet id -> [5].
twitter.getNewsFeed(1);

// User 1 follows user 2.
twitter.follow(1, 2);

// User 2 posts a new tweet (id = 6).
twitter.postTweet(2, 6);

// User 1's news feed should return a list with 2 tweet ids -> [6, 5].
// Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.getNewsFeed(1);

// User 1 unfollows user 2.
twitter.unfollow(1, 2);

// User 1's news feed should return a list with 1 tweet id -> [5],
// since user 1 is no longer following user 2.
twitter.getNewsFeed(1);

【中文翻译】
设计一个简化版的推特(Twitter)，可以让用户实现发送推文，关注/取消关注其他用户，能够看见关注人（包括自己）的最近十条推文。你的设计需要支持以下的几个功能：

postTweet(userId, tweetId): 创建一条新的推文。

getNewsFeed(userId): 检索最近的十条推文。每个推文都必须是由此用户关注的人或者是用户自己发出的。推文必须按照时间顺序由最近的开始排序。

follow(followerId, followeeId): 关注一个用户。

unfollow(followerId, followeeId): 取消关注一个用户。

示例：

Twitter twitter = new Twitter();

// 用户 1 发送了一条新推文 (id = 5)。
twitter.postTweet(1, 5);

// 用户 1 的获取推文应当返回一个列表，其中包含一个 id 为 5 的推文。
twitter.getNewsFeed(1);

// 用户 1 关注了用户 2。
twitter.follow(1, 2);

// 用户 2 发送了一个新推文 (id = 6)。
twitter.postTweet(2, 6);

// 用户 1 的获取推文应当返回一个列表，其中包含两个推文，id 分别为 -> [6, 5]。
// 推文 id 6 应当在推文 id 5 之前，因为它是在 5 之后发送的。
twitter.getNewsFeed(1);

// 用户 1 取消关注了用户 2。
twitter.unfollow(1, 2);

// 用户 1 的获取推文应当返回一个列表 [5]，
// 因为用户 1 已经不再关注用户 2。
twitter.getNewsFeed(1);
"""

from typing import List, Optional
from collections import defaultdict


class Twitter:

    def __init__(self):
        self.timestamp = 0
        # userId -> list of (timestamp, tweetId)，按时间顺序追加
        self.tweets = defaultdict(list)
        # followerId -> set of followeeId
        self.followees = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        """发布推文，时间戳递增保证全局有序"""
        self.tweets[userId].append((self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        """获取最新的 10 条推文，使用多路归并（K 路合并）"""
        import heapq
        # 需要检索的用户：自己 + 所有关注的人
        users = set([userId]) | self.followees[userId]
        heap = []
        # 将每个用户的最新一条推文加入堆
        for uid in users:
            if self.tweets[uid]:
                idx = len(self.tweets[uid]) - 1
                ts, tid = self.tweets[uid][idx]
                # 用负数实现大顶堆（Python 只有小顶堆）
                heapq.heappush(heap, (-ts, tid, uid, idx))
        res = []
        while heap and len(res) < 10:
            neg_ts, tid, uid, idx = heapq.heappop(heap)
            res.append(tid)
            # 如果该用户还有更早的推文，将下一条加入堆
            if idx > 0:
                ts, tid = self.tweets[uid][idx - 1]
                heapq.heappush(heap, (-ts, tid, uid, idx - 1))
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        """关注操作，不能自己关注自己"""
        if followerId != followeeId:
            self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """取消关注"""
        self.followees[followerId].discard(followeeId)










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 这是一道设计题，核心在于 getNewsFeed 的实现——需要从多个用户的推文列表中取出最新的 10 条。
# 数据结构设计：
# 1. tweets: defaultdict(list) - 为每个用户维护一个推文列表，每条推文为 (timestamp, tweetId) 元组。
#    使用全局递增的 timestamp 保证所有推文全局有序。
# 2. followees: defaultdict(set) - 为每个用户维护其关注的用户集合。
# getNewsFeed 使用 K 路归并算法：
# - 收集自身 + 所有关注用户的推文列表
# - 将每个用户列表的最后一条（最新）推文加入大顶堆（用负数时间戳模拟）
# - 每次弹出堆顶（最新推文），并将其所属用户的下一条推文加入堆
# - 取 10 条后返回
# postTweet: O(1) 追加到用户列表
# follow/unfollow: O(1) 集合操作
#
# 时间复杂度:
#   postTweet: O(1)
#   getNewsFeed: O(K log K + 10 log K) ≈ O(K log K)，K 为用户关注的用户数
#   follow: O(1)
#   unfollow: O(1)
# 空间复杂度: O(T + F)，T 为总推文数，F 为总关注关系数
#
# 关键点:
# - 全局时间戳保证推文全局有序，无需存储真实时间
# - 多路归并（K-way merge）是获取 top-K 最新推文的标准做法
# - heapq 在 Python 中是小顶堆，用负数模拟大顶堆
# - 不能自己关注自己（follow 时需判断）
# - unfollow 使用 discard 避免 KeyError
