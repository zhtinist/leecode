"""
LeetCode #781 - Rabbits in Forest
中文题名：森林中的兔子
https://leetcode.com/problems/rabbits-in-forest/

In a forest, each rabbit has some color. Some subset of rabbits (possibly all of them) tell
you how many other rabbits have the same color as them. Those `answers` are
placed in an array.

Return the minimum number of rabbits that could be in the forest.

Examples:
Input: answers = [1, 1, 2]
Output: 5
Explanation:
The two rabbits that answered "1" could both be the same color, say red.
The rabbit than answered "2" can't be red or the answers would be inconsistent.
Say the rabbit that answered "2" was blue.
Then there should be 2 other blue rabbits in the forest that didn't answer into the array.
The smallest possible number of rabbits in the forest is therefore 5: 3 that answered plus 2 that didn't.

Input: answers = [10, 10, 10]
Output: 11

Input: answers = []
Output: 0

Note:

`answers` will have length at most `1000`.

Each `answers[i]` will be an integer in the range `[0, 999]`.

【中文翻译】
在森林中，每只兔子都有某种颜色。一部分兔子（可能是全部）告诉你与它们颜色相同的其他兔子有多少只。这些 `answers` 被放在一个数组中。

返回森林中兔子的最少数量。

示例：
输入：answers = [1, 1, 2]
输出：5
解释：
回答 "1" 的两只兔子可能都是同一种颜色，比如红色。
回答 "2" 的兔子不能是红色，否则答案会不一致。
假设回答 "2" 的兔子是蓝色。
那么森林中应该有另外 2 只没有回答的蓝色兔子。
因此森林中兔子的最少数量是 5：3 只回答的加上 2 只未回答的。

输入：answers = [10, 10, 10]
输出：11

输入：answers = []
输出：0

注意：

`answers` 的长度最多为 `1000`。

每个 `answers[i]` 是范围在 `[0, 999]` 内的整数。
"""

from typing import List, Optional


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        from collections import Counter
        cnt = Counter(answers)
        total = 0
        for x, freq in cnt.items():
            group_size = x + 1
            # ceil(freq / group_size) groups of this color
            groups = (freq + group_size - 1) // group_size
            total += groups * group_size
        return total



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 分组计数。
# 如果一只兔子回答 x，表示还有 x 只和它同色的兔子。因此这种颜色共有 x+1 只兔子。
# 如果有 freq 只兔子回答 x，需要 ceil(freq / (x+1)) 组（即这么多组不同颜色的兔子）。
# 每组有 x+1 只兔子。最少总兔子数 = sum(ceil(freq / (x+1)) * (x+1))。
# 例如：answers = [1,1,2]：
# - x=1, freq=2: ceil(2/2)*2 = 2 只（1 组红色）
# - x=2, freq=1: ceil(1/3)*3 = 3 只（1 组蓝色）
# - 总计 5 只。
#
# 时间复杂度: O(N) - Counter 遍历一次，再遍历不同答案
# 空间复杂度: O(N) - Counter 存储不同答案的计数
#
# 关键点:
# - 回答 x 表示该颜色族共有 x+1 只兔子
# - ceil(freq / (x+1)) 计算最少需要多少组颜色
# - 每组完整计算 x+1 只（包括未回答的）
# - 向上取整技巧：(freq + group_size - 1) // group_size
