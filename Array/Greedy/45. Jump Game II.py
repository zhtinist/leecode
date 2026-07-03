"""
LeetCode #45 - Jump Game II
https://leetcode.com/problems/jump-game-ii/

You are given a 0-indexed array of integers nums of length n. You are initially
positioned at nums[0].

Each element nums[i] represents the maximum jump length from index i. In other
words, if you are at nums[i], you can jump to any nums[i + j] where:

    0 <= j <= nums[i] and
    i + j < n

Return the minimum number of jumps to reach nums[n - 1]. The test cases are
generated such that you can reach nums[n - 1].

Example 1:
    Input: nums = [2,3,1,1,4]
    Output: 2
    Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 from index 0 to 1, then 3 steps to the last index.

Example 2:
    Input: nums = [2,3,0,1,4]
    Output: 2

Constraints:
    1 <= nums.length <= 10^4
    0 <= nums[i] <= 1000
    It's guaranteed that you can reach nums[n - 1].
"""

from collections import deque
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        queue = deque([0])
        visited = {0}
        steps = 0

        while queue:
            steps += 1
            for _ in range(len(queue)):
                i = queue.popleft()
                for j in range(i + 1, min(i + nums[i] + 1, n)):
                    if j in visited:
                        continue
                    if j == n - 1:
                        return steps
                    visited.add(j)
                    queue.append(j)

        return steps
