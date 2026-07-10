"""
LeetCode #202 - Happy Number
中文题名：快乐数
https://leetcode.com/problems/happy-number/

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive
integer, replace the number by the sum of the squares of its digits, and repeat the process
until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does
not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example:

Input: 19
Output: true
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

【中文翻译】
编写一个算法来判断一个数是否为「快乐数」。

「快乐数」定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，重复这个过程直到这个数变为 1，或是无限循环但始终变不到 1。如果可以变为 1，那么这个数就是「快乐数」。

示例：

输入：19
输出：true
解释：
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
"""

from typing import List, Optional


class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(num: int) -> int:
            total = 0
            while num > 0:
                digit = num % 10
                total += digit * digit
                num //= 10
            return total

        slow = n
        fast = get_next(n)

        while fast != 1 and slow != fast:
            slow = get_next(slow)
            fast = get_next(get_next(fast))

        return fast == 1


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Easy
# Paid Only: No
#
# 解题思路:
# 使用 Floyd 快慢指针检测循环。将"求各位数字平方和"的操作视为链表上的"下一步"。
# 如果数字是快乐的，最终会到达 1（链表末尾）。
# 如果不是快乐的，会进入一个不包含 1 的循环（链表中存在环）。
#
# 使用快慢指针：
# - slow 每次走一步（调用一次 get_next）
# - fast 每次走两步（调用两次 get_next）
# - 如果 fast 到达 1，返回 True
# - 如果 slow 和 fast 相遇（且不为 1），说明有环，返回 False
#
# 时间复杂度: O(log N) — 数字每次减小的速度很快
# 空间复杂度: O(1) — 只使用两个变量
#
# 关键点:
# - 快慢指针是检测循环的经典方法，O(1) 空间
# - 也可用哈希集合记录访问过的数字，但需要 O(N) 空间
# - 已知唯一的不快乐循环：4 → 16 → 37 → 58 → 89 → 145 → 42 → 20 → 4
