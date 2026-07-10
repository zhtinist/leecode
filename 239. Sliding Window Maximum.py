"""
LeetCode #239 - Sliding Window Maximum
https://leetcode.com/problems/sliding-window-maximum/

Given an array *nums*, there is a sliding window of size *k* which is moving
from the very left of the array to the very right. You can only see the *k* numbers
in the window. Each time the sliding window moves right by one position. Return the max
sliding window.

Example:

Input: *nums* = `[1,3,-1,-3,5,3,6,7]`, and *k* = 3
Output: `[3,3,5,5,6,7]
Explanation:
`
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
1 [3  -1  -3] 5  3  6  7       3
1  3 [-1  -3  5] 3  6  7       5
1  3  -1 [-3  5  3] 6  7       5
1  3  -1  -3 [5  3  6] 7       6
1  3  -1  -3  5 [3  6  7]      7

Note:

You may assume *k* is always valid, 1 <= k <= input array's size for
non-empty array.

Follow up:

Could you solve it in linear time?
"""

from typing import List, Optional


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        q = deque()
        res = []

        for i, num in enumerate(nums):
            while q and nums[q[-1]] < num:
                q.pop()
            q.append(i)

            if q[0] <= i - k:
                q.popleft()

            if i >= k - 1:
                res.append(nums[q[0]])

        return res










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Hard
# Paid Only: No
#
# 解题思路:
# 使用单调递减双端队列(Monotonic Deque)在线性时间内解决滑动窗口最大值问题。
# 队列中存储的是元素的下标(而非值)，且保持队列中下标对应的元素值严格递减。
# 遍历数组中的每个元素 nums[i]：
# 1. 维护单调递减性：从队列尾部开始，移除所有值小于等于当前元素的下标。
#    因为这些元素在窗口包含当前元素时不可能成为最大值。
# 2. 将当前下标 i 加入队列尾部。
# 3. 移除过期元素：若队首下标 <= i - k，说明该元素已滑出窗口，从队首移除。
# 4. 记录结果：当 i >= k - 1 时(窗口已形成)，队首下标对应的元素即为当前窗口的最大值。
# 每个元素最多入队一次、出队一次，确保 O(n) 总时间复杂度。
#
# 时间复杂度: O(n) - 每个元素入队出队各一次，共 2n 次操作
# 空间复杂度: O(k) - 双端队列最多存储 k+1 个下标
#
# 关键点:
# - 队列保持单调递减，队首永远是当前窗口的最大值
# - 存储下标而非值：既可用于值比较，又可用于判断是否过期(滑出窗口)
# - 移除队尾时用 while(小于"等于"也要移除，因为要保留最靠后的)
# - 移除队首时用 if(因为每次最多移除一个过期元素，窗口一次只滑动一步)
