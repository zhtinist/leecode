"""
LeetCode #3577 - Count the Number of Computer Unlocking Permutations
统计计算机解锁顺序排列数
https://leetcode.cn/problems/count-the-number-of-computer-unlocking-permutations/

给你一个长度为 `n` 的数组 `complexity`。
在房间里有 `n` 台 上锁的 计算机，这些计算机的编号为 0 到 `n - 1`，每台计算机都有一个 唯一 的密码。编号为 `i` 的计算机的密码复杂度为 `complexity[i]`。
编号为 0 的计算机密码已经 解锁 ，并作为根节点。其他所有计算机必须通过它或其他已经解锁的计算机来解锁，具体规则如下：
可以使用编号为 `j` 的计算机的密码解锁编号为 `i` 的计算机，其中 `j` 是任何小于 `i` 的整数，且满足 `complexity[j] < complexity[i]`（即 `j < i` 并且 `complexity[j] < complexity[i]`）。
要解锁编号为 `i` 的计算机，你需要事先解锁一个编号为 `j` 的计算机，满足 `j < i` 并且 `complexity[j] < complexity[i]`。
求共有多少种 `[0, 1, 2, ..., (n - 1)]` 的排列方式，能够表示从编号为 0 的计算机（唯一初始解锁的计算机）开始解锁所有计算机的有效顺序。
由于答案可能很大，返回结果需要对 10^9 + 7 取余数。
注意：编号为 0 的计算机的密码已解锁，而 不是 排列中第一个位置的计算机密码已解锁。
排列 是一个数组中所有元素的重新排列。

示例 1：

输入： complexity = [1,2,3]
输出： 2
解释：
有效的排列有：
[0, 1, 2]
首先使用根密码解锁计算机 0。
使用计算机 0 的密码解锁计算机 1，因为 `complexity[0] < complexity[1]`。
使用计算机 1 的密码解锁计算机 2，因为 `complexity[1] < complexity[2]`。
[0, 2, 1]
首先使用根密码解锁计算机 0。
使用计算机 0 的密码解锁计算机 2，因为 `complexity[0] < complexity[2]`。
使用计算机 0 的密码解锁计算机 1，因为 `complexity[0] < complexity[1]`。
示例 2：

输入： complexity = [3,3,3,4,4,4]
输出： 0
解释：
没有任何排列能够解锁所有计算机。

提示：
`2 <= complexity.length <= 10^5`
`1 <= complexity[i] <= 10^9`
"""

from typing import List, Optional

MOD = 10 ** 9 + 7


class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        n = len(complexity)

        # 计算机 0 是唯一初始解锁的。它可以在排列中的任何位置吗？
        # 注意题目说："编号为 0 的计算机的密码已解锁，而不是排列中第一个位置的计算机密码已解锁"
        # 但它是唯一初始解锁的，所以排列必须从 0 开始（否则第一个元素没有被解锁的来源）
        # 然而排列 [1, 0, 2] 是否可能？不行，因为计算机 1 初始未解锁。

        # 检查可行性：对于每个 i > 0，是否存在 j < i 且 complexity[j] < complexity[i]？
        # 由于只有计算机 0 初始解锁，计算机 0 必须能解锁所有其他计算机（直接或间接）。
        # 计算机 0 要解锁计算机 i，条件：0 < i 且 complexity[0] < complexity[i]。
        # 因此 complexity[0] 必须严格小于所有其他 complexity 值。
        # 否则，任何 complexity ≤ complexity[0] 的计算机都无法被解锁。

        for i in range(1, n):
            if complexity[i] <= complexity[0]:
                return 0

        # 若所有计算机都可被计算机 0 解锁，则排列的第一个位置必须是 0，
        # 其余 n-1 台计算机可以以任意顺序排列（每台都可以被 0 直接解锁）。
        # 因此有效排列数 = (n-1)!

        ans = 1
        for i in range(2, n):
            ans = (ans * i) % MOD
        return ans










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Brainteaser, Array, Math, Combinatorics
#
# 解题思路:
# 关键分析：
# 1. 计算机 0 是唯一初始解锁的计算机。
# 2. 要解锁计算机 i (>0)，需要存在已解锁的 j < i 满足 complexity[j] < complexity[i]。
# 3. 由于 0 < i 对所有 i > 0 成立，只要 complexity[0] < complexity[i]，
#    计算机 0 就可以直接解锁计算机 i。
# 4. 如果存在任何 i > 0 满足 complexity[i] ≤ complexity[0]，则该计算机永远无法被解锁，
#    因为没有比 complexity[0] 更小的 complexity 值可用于解锁它。
# 5. 当全部 n-1 台计算机都能被 0 直接解锁时，排列的有效性仅要求 0 在排列首位
#    （因为只有 0 是初始解锁的，第一个被解锁的必须是 0）。
# 6. 其余 n-1 台计算机可以任意排列，都能被 0（已在前面）解锁。
# 7. 因此答案 = (n-1)! mod (10^9+7)，或者 0（如果有无法解锁的计算机）。
#
# 时间复杂度: O(n)
# 空间复杂度: O(1)
#
# 关键点:
# - 唯一初始解锁的是计算机 0，必须排在首位
# - complexity[0] 必须是全局严格最小值
# - 确认 feasibility 后，答案为 (n-1)!
