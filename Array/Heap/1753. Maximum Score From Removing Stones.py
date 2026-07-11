"""
LeetCode #1753 - Maximum Score From Removing Stones
中文题名：移除石子的最大得分
https://leetcode.com/problems/maximum-score-from-removing-stones/

You are playing a solitaire game with three piles of stones of sizes `a`​​​​​​, `b`,​​​​​​ and `c`​​​​​​ respectively. Each turn you choose two different non-empty piles, take one stone from each, and add `1` point to your score. The game stops when there are fewer than two non-empty piles (meaning there are no more available moves).

Given three integers `a`​​​​​, `b`,​​​​​ and `c`​​​​​, return the maximum score you can get.

Example 1:

Input: a = 2, b = 4, c = 6
Output: 6
Explanation: The starting state is (2, 4, 6). One optimal set of moves is:
- Take from 1st and 3rd piles, state is now (1, 4, 5)
- Take from 1st and 3rd piles, state is now (0, 4, 4)
- Take from 2nd and 3rd piles, state is now (0, 3, 3)
- Take from 2nd and 3rd piles, state is now (0, 2, 2)
- Take from 2nd and 3rd piles, state is now (0, 1, 1)
- Take from 2nd and 3rd piles, state is now (0, 0, 0)
There are fewer than two non-empty piles, so the game ends. Total: 6 points.

Example 2:

Input: a = 4, b = 4, c = 6
Output: 7
Explanation: The starting state is (4, 4, 6). One optimal set of moves is:
- Take from 1st and 2nd piles, state is now (3, 3, 6)
- Take from 1st and 3rd piles, state is now (2, 3, 5)
- Take from 1st and 3rd piles, state is now (1, 3, 4)
- Take from 1st and 3rd piles, state is now (0, 3, 3)
- Take from 2nd and 3rd piles, state is now (0, 2, 2)
- Take from 2nd and 3rd piles, state is now (0, 1, 1)
- Take from 2nd and 3rd piles, state is now (0, 0, 0)
There are fewer than two non-empty piles, so the game ends. Total: 7 points.

Example 3:

Input: a = 1, b = 8, c = 8
Output: 8
Explanation: One optimal set of moves is to take from the 2nd and 3rd piles for 8 turns until they are empty.
After that, there are fewer than two non-empty piles, so the game ends.

Constraints:

`1 <= a, b, c <= 105`

【中文翻译】
有三堆石子 a、b、c。每次可以从两堆不同的石子中各移除一个石子，得1分。
当有两堆为空时游戏结束。求可以获得的最大分数。

示例 1：
输入: a = 2, b = 4, c = 6
输出: 6
解释: 每次都从最大的两堆取（(4,6)→(3,5)→(2,4)→(1,3)→(0,2)→(0,1)→结束），得6分。

示例 2：
输入: a = 4, b = 4, c = 6
输出: 7
解释: 从(4,6)取→(3,5)→(2,4)→(1,3)→(0,2)→这时a=0,b=2,c=4→从b,c取→(0,0)→得分=7。
"""

from typing import List, Optional


class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        arr = sorted([a, b, c])
        # 如果最小的两个之和 <= 最大的，答案 = 最小的两个之和
        if arr[0] + arr[1] <= arr[2]:
            return arr[0] + arr[1]
        # 否则 answer = (a + b + c) // 2
        return (a + b + c) // 2
# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 数学推导。总是从最大的两堆取石子。
# 排序后设 arr[0] <= arr[1] <= arr[2]。
# 情况1：arr[0] + arr[1] <= arr[2]，可以一直用前两堆和第三堆配对，答案为 arr[0] + arr[1]。
# 情况2：arr[0] + arr[1] > arr[2]，可以让三堆都剩下不超过1个，答案为 (a+b+c)//2。
# 贪心正确性：每次从最大的两堆取可以最大化操作次数。
#
# 时间复杂度: O(1) — 排序3个元素
# 空间复杂度: O(1)
#
# 关键点:
# - 贪心策略：总是从最大的两堆取
# - 两种情况直接计算，无需模拟
# - 情况2用整数除法直接得到结果
