"""
LeetCode #969 - Pancake Sorting
中文题名：煎饼排序
https://leetcode.com/problems/pancake-sorting/

Given an array `A`, we can perform a pancake flip: We choose
some positive integer `k <= A.length`, then reverse the
order of the first k elements of `A`.  We want to perform
zero or more pancake flips (doing them one after another in succession) to sort the array
`A`.

Return the k-values corresponding to a sequence of pancake flips that sort `A`.
Any valid answer that sorts the array within `10 * A.length` flips will be
judged as correct.

Example 1:

Input: [3,2,4,1]
Output: [4,2,4,3]
Explanation:
We perform 4 pancake flips, with k values 4, 2, 4, and 3.
Starting state: A = [3, 2, 4, 1]
After 1st flip (k=4): A = [1, 4, 2, 3]
After 2nd flip (k=2): A = [4, 1, 2, 3]
After 3rd flip (k=4): A = [3, 2, 1, 4]
After 4th flip (k=3): A = [1, 2, 3, 4], which is sorted.

Example 2:

Input: [1,2,3]
Output: []
Explanation: The input is already sorted, so there is no need to flip anything.
Note that other answers, such as [3, 3], would also be accepted.

【中文翻译】
给定一个数组 `A`，我们可以执行煎饼翻转：选择一个正整数 `k <= A.length`，
然后反转 `A` 的前 k 个元素的顺序。我们要执行零次或多次煎饼翻转（依次进行）来对数组 `A` 排序。
返回对 `A` 排序的一系列煎饼翻转对应的 k 值。
任何在 `10 * A.length` 次翻转内完成排序的有效答案都将被判为正确。

"""

from typing import List, Optional


class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        result = []

        def flip(k: int) -> None:
            """反转前 k 个元素"""
            arr[:k] = arr[:k][::-1]

        for target in range(n, 1, -1):
            # 找到当前最大值 target 的位置
            idx = arr.index(target)

            if idx == target - 1:
                # 已经在正确位置
                continue

            # 如果不在第一位，先翻转到第一位
            if idx != 0:
                result.append(idx + 1)
                flip(idx + 1)

            # 再从第一位翻转到正确位置
            result.append(target)
            flip(target)

        return result



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 贪心策略：从大到小依次将每个元素放到正确位置。
# 对于当前要放置的最大值 target（从 n 到 2）：
# 1. 找到 target 在数组中的位置 idx
# 2. 如果已在正确位置（idx == target - 1），跳过
# 3. 如果不在第一位（idx != 0），执行一次翻转将 target 移到第一位
# 4. 再执行一次翻转将 target 移到位置 target - 1（数组末尾的对应位置）
# 每次翻转最多 2 次操作，总共最多 2N 次翻转，远小于题目要求的 10N。
#
# 时间复杂度: O(N^2) — 每次 index() 和翻转都是 O(N)
# 空间复杂度: O(N) — 存储结果列表（不计输入数组修改）
#
# 关键点:
# - 贪心策略：从大到小放置元素
# - 每轮最多两次翻转：先翻到首位，再翻到目标位置
# - 使用 Python 切片反转实现翻转操作
# - 最多 2N 次翻转确保满足题目约束
