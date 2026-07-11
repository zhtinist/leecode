"""
LeetCode #1024 - Video Stitching
中文题名：视频拼接
https://leetcode.com/problems/video-stitching/

You are given a series of video clips from a sporting event that lasted `T`
seconds.  These video clips can be overlapping with each other and have varied
lengths.

Each video clip `clips[i]` is an interval: it starts at time `clips[i][0]`
and ends at time `clips[i][1]`.  We can cut these clips into segments
freely: for example, a clip `[0, 7]` can be cut into segments `[0, 1] + [1,
3] + [3, 7]`.

Return the minimum number of clips needed so that we can cut the clips into segments that
cover the entire sporting event (`[0, T]`).  If the task is impossible,
return `-1`.

Example 1:

Input: clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], T = 10
Output: 3
Explanation:
We take the clips [0,2], [8,10], [1,9]; a total of 3 clips.
Then, we can reconstruct the sporting event as follows:
We cut [1,9] into segments [1,2] + [2,8] + [8,9].
Now we have segments [0,2] + [2,8] + [8,10] which cover the sporting event [0, 10].

Example 2:

Input: clips = [[0,1],[1,2]], T = 5
Output: -1
Explanation:
We can't cover [0,5] with only [0,1] and [0,2].

Example 3:

Input: clips = [[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]], T = 9
Output: 3
Explanation:
We can take clips [0,4], [4,7], and [6,9].

Example 4:

Input: clips = [[0,4],[2,8]], T = 5
Output: 2
Explanation:
Notice you can have extra video after the event ends.

Note:

`1 <= clips.length <= 100`

`0 <= clips[i][0], clips[i][1] <= 100`

`0 <= T <= 100`

【中文翻译】
你会得到一系列来自持续 `T` 秒的体育赛事的视频片段。这些视频片段可以相互重叠，也可以有不同的长度。

每个视频片段 `clips[i]` 是一个区间：它开始于时间 `clips[i][0]`，结束于时间 `clips[i][1]`。我们可以自由地将这些片段切成段：例如，片段 `[0, 7]` 可以被切成段 `[0, 1] + [1, 3] + [3, 7]`。

返回所需的最少片段数，以便我们可以将片段切成段来覆盖整个体育赛事（`[0, T]`）。如果无法完成任务，返回 `-1`。

示例 1：

输入：clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], T = 10
输出：3
解释：
我们取片段 [0,2], [8,10], [1,9]；共 3 个片段。
然后，我们可以按如下方式重建体育赛事：
我们将 [1,9] 切成段 [1,2] + [2,8] + [8,9]。
现在我们有了覆盖体育赛事 [0, 10] 的段 [0,2] + [2,8] + [8,10]。

示例 2：

输入：clips = [[0,1],[1,2]], T = 5
输出：-1
解释：
我们无法仅用 [0,1] 和 [0,2] 覆盖 [0,5]。

示例 3：

输入：clips = [[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]], T = 9
输出：3
解释：
我们可以取片段 [0,4], [4,7] 和 [6,9]。

示例 4：

输入：clips = [[0,4],[2,8]], T = 5
输出：2
解释：
注意，你可以在赛事结束后有多余的视频。

注意：

`1 <= clips.length <= 100`

`0 <= clips[i][0], clips[i][1] <= 100`

`0 <= T <= 100`

"""

from typing import List, Optional


class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        clips.sort(key=lambda x: (x[0], -x[1]))

        count = 0
        i = 0
        cur_end = 0
        next_end = 0

        while i < len(clips) and cur_end < T:
            while i < len(clips) and clips[i][0] <= cur_end:
                next_end = max(next_end, clips[i][1])
                i += 1
            if next_end <= cur_end:
                return -1
            cur_end = next_end
            count += 1

        return count if cur_end >= T else -1










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用贪心算法，类似"跳跃游戏 II"的思路。先按片段的开始时间排序（开始时间相同按结束时间降序）。
# 维护两个变量：cur_end（当前能覆盖到的最远位置）和 next_end（下一轮能扩展到的更远位置）。
# 遍历排序后的片段列表：
# - 对于所有开始时间 <= cur_end 的片段，更新 next_end = max(next_end, clips[i][1])。
# - 如果 next_end <= cur_end，说明无法继续扩展，返回 -1。
# - 否则 cur_end = next_end，片段计数加 1。
# - 当 cur_end >= T 时停止。
# 最终如果 cur_end >= T 返回片段计数，否则返回 -1。
#
# 时间复杂度: O(n log n) - 排序占主导
# 空间复杂度: O(1) - 使用常数额外空间（不考虑排序的栈空间）
#
# 关键点:
# - 贪心选择：每次选择能扩展最远的片段（类似跳跃游戏 II）
# - 排序规则：按开始时间升序，开始时间相同时按结束时间降序
# - 当 next_end <= cur_end 时无法前进，说明存在无法覆盖的间隙
