"""
LeetCode #2456 - Most Popular Video Creator
最流行的视频创作者
https://leetcode.cn/problems/most-popular-video-creator/

给你两个字符串数组 `creators` 和 `ids` ，和一个整数数组 `views` ，所有数组的长度都是 `n` 。平台上第 `i` 个视频者是 `creator[i]` ，视频分配的 id 是 `ids[i]` ，且播放量为 `views[i]` 。
视频创作者的 流行度 是该创作者的 所有 视频的播放量的 总和 。请找出流行度 最高 创作者以及该创作者播放量 最大 的视频的 id 。
如果存在多个创作者流行度都最高，则需要找出所有符合条件的创作者。
如果某个创作者存在多个播放量最高的视频，则只需要找出字典序最小的 `id` 。
返回一个二维字符串数组 `answer` ，其中 `answer[i] = [creator_i, id_i]` 表示 `creator_i` 的流行度 最高 且其最流行的视频 id 是 `id_i` ，可以按任何顺序返回该结果。

示例 1：
输入：creators = ["alice","bob","alice","chris"], ids = ["one","two","three","four"], views = [5,10,5,4] 输出：[["alice","one"],["bob","two"]] 解释： alice 的流行度是 5 + 5 = 10 。 bob 的流行度是 10 。 chris 的流行度是 4 。 alice 和 bob 是流行度最高的创作者。 bob 播放量最高的视频 id 为 "two" 。 alice 播放量最高的视频 id 是 "one" 和 "three" 。由于 "one" 的字典序比 "three" 更小，所以结果中返回的 id 是 "one" 。
示例 2：
输入：creators = ["alice","alice","alice"], ids = ["a","b","c"], views = [1,2,2] 输出：[["alice","b"]] 解释： id 为 "b" 和 "c" 的视频都满足播放量最高的条件。 由于 "b" 的字典序比 "c" 更小，所以结果中返回的 id 是 "b" 。

提示：
`n == creators.length == ids.length == views.length`
`1 <= n <= 10^5`
`1 <= creators[i].length, ids[i].length <= 5`
`creators[i]` 和 `ids[i]` 仅由小写英文字母组成
`0 <= views[i] <= 10^5`
"""

from typing import List, Optional


class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        total_views = {}
        best_video = {}  # creator -> (max_views, best_id)

        for creator, vid, v in zip(creators, ids, views):
            # Update total views
            total_views[creator] = total_views.get(creator, 0) + v

            # Update best video for this creator
            if creator not in best_video:
                best_video[creator] = (v, vid)
            else:
                max_v, best_id = best_video[creator]
                if v > max_v or (v == max_v and vid < best_id):
                    best_video[creator] = (v, vid)

        # Find max total views
        max_total = max(total_views.values())

        # Collect all creators with max total views
        result = []
        for creator, total in total_views.items():
            if total == max_total:
                result.append([creator, best_video[creator][1]])

        return result


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Hash Table, String, Sorting, Heap (Priority Queue)
#
# 解题思路:
# 使用两个哈希表：一个记录每个创作者的总播放量，另一个记录每个创作者的最佳视频（最大播放量和对应 id）。
# 遍历所有视频：更新总播放量；更新最佳视频（播放量更高则替换，播放量相同但 id 字典序更小则替换）。
# 找到最大的总播放量 max_total，然后收集所有总播放量等于 max_total 的创作者及其最佳视频 id。
#
# 时间复杂度: O(n)
# 空间复杂度: O(n)
#
# 关键点:
# - 双哈希表：一个存总播放量，一个存最佳视频信息
# - 最佳视频更新规则：播放量优先，播放量相同时取字典序更小的 id
# - 返回所有流行度最高（并列）的创作者
